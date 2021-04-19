# Import relevant libraries
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
import time

# Load dataframe to extract competitor ids
df_19 = pd.read_csv('./data/2019_opens_clean.csv')

# Set the amount of ID's to scrape from web &
# define the output csv-file
amount=1000
competitor_list = df_19[:amount].competitorid.to_list()
file_csv = './data/2019_opens_bs_10.csv'
print(f"Writing, {amount} ID's to file {file_csv}")

# create column names for benchmark stats dataframe
bs_cols = [
    'fullname', 'countryoforigin', 'competitorid', 'division', 'age', 'height', 'weight', 'affiliate', \
    'bs_backsquat', 'bs_cleanandjerk', 'bs_snatch', 'bs_deadlift', 'bs_fightgonebad', 'bs_maxpull_ups', \
    'bs_fran', 'bs_grace', 'bs_helen', 'bs_filthy50', 'bs_sprint400m', 'bs_run5k'
]

# Initiate writing to csv file
with open(file_csv, mode='w', newline='') as csv_file:
    
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(bs_cols)

    # With for-loop go through all declared competitor id's
    count = 1
    for competitor in competitor_list:

        # Get the url
        url_profile="https://games.crossfit.com/athlete/{}".format(competitor)

        # Get the data from the page
        response=requests.get(url_profile)
        soup = bs(response.content,features='html.parser')

        # Select the data in the infobar (details on the athlete)
        infobar=soup.find("ul", {"class": "infobar"})

        # information in the infobar
        if not infobar is None:

            # Set empty list for actual competitor
            competitor_i = []

            # Get name
            name=soup.find("h3",{"class":"c-heading-page-cover"})
            firstname=name.find("small").text
            lastname=name.text.replace(firstname,"").replace("\n","").replace(" ","")
            competitor_i.append(firstname+' '+lastname)

            # Get the different columns
            for i in infobar.find_all("li"):
                field=i.find("div",{"class": "item-label"}).text.replace("\n","").replace(" ","").lower()
                value=i.find("div",{"class": "text"}).text.replace("\n","").replace(" ","")
                competitor_i.append(value)
            
            # Get benchmark exercice
            stats=soup.find("ul",{"class": "stats-container"})
            for i in stats.find_all("tr"):
                exercise="bs_"+i.find("th",{"class": "stats-header"}).text.replace("\n","").replace(" ","").lower()
                value=i.find("td").text.replace("\n","").replace(" ","")
                competitor_i.append(value)
            
            # Add new observation to benchmark stats csv
            csv_writer.writerow(competitor_i)

        count=count+1

        # Status report
        print("*** Status: ", round(100*count/amount,2),"% done ***", end = "\r")

        time.sleep(0.5)


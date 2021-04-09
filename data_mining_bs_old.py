import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

df_19 = pd.read_csv('./data/2019_opens_clean.csv')

amount=50
file_csv = './data/2019_opens_bs_test.csv'
competitor_list = df_19[:amount].competitorid.to_list()

# create column names for benchmark stats dataframe
bs_cols = [
    'fullname', 'countryoforigin', 'competitorid', 'division', 'age', 'height', 'weight', 'affiliate', \
    'bs_backsquat', 'bs_cleanandjerk', 'bs_snatch', 'bs_deadlift', 'bs_fightgonebad', 'bs_maxpull_ups', \
    'bs_fran', 'bs_grace', 'bs_helen', 'bs_filthy50', 'bs_sprint400m', 'bs_run5k'
]

# create empty dataframe with above declared columns
df_bs = pd.DataFrame(columns=bs_cols)
df_bs.to_csv(file_csv)

print(f"Writing, {amount} ID's to file {file_csv}")

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
        
        #Get name
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
            
        # Add new observation to benchmark stats dataframe
        df_bs = df_bs.append(pd.Series(competitor_i, index=bs_cols), ignore_index=True)
        df_bs.to_csv(file_csv)

        count=count+1
        print("Status: ", round(100*count/amount,2),"% done", end = "\r")


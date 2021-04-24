# project-crossfit-data
Data-Driven Insights from CrossFit Competition

![CFM](./images/CFM.png)

<span>Photo from CFM Crossfit Mitte in Berlin on <a href="https://urbansportsclub.com/de/venues/cfm-crossfit-mitte-berlin">Urban Sports Club</a></span>

---

This repository was created in the course of my final project in neuefische Data Science Bootcamp.

### CrossFit

CrossFit incorporates elements of olympic weightlifting, gymnastics, high-intensity intervall training and many more. There is a wide range equipment used, like barbells, kettlebells, rowing machines, jump ropes, pull-up bars, plyo boxes etc. A typical workout in CrossFit (called Workout of the Day - "WOD") is a bootcamp-like circuit training. The goal is to perform repetitions of various exercises with maximum weight as fast as you can. The annual CrossFit Open is a five-week-long international competition with one workout each week. Everybody in the world can participate and the amount of competitors is still growing, e.g. around 350k in 2019.

I really like it, because it is versatile, measurable and you can track all your improvements.

### Dataset

The project deals with data from Reebok Crossfit Open 2019 and contains already provided Open Athlete's and Open Score datasets from [kaggle.com](https://www.kaggle.com/jeanmidev/crossfit-games) as well as self-employed benchmark statistics from [crossfit.com](https://games.crossfit.com) via webscraping:
* Athlete's statistics like height, weight, age, country of origin, etc.
* Open workout results like time or repetitions of each competition
* Athlete's benchmark statistics like 1RM (maximum weight of one repetition) of olympic lifts, best scores of specific benchmark workouts or personal records in bodyweight exercises

### Purpose of Data-driven Insights

Possible insights from competition data could help:
* both CrossFit beginners and elite athletes to evaluate their own performance
* Coaches to give reasonable advice
* Organizers to improve their events

### Guiding Questions

In this project I am oriented towards following questions/tasks:
* Are the workouts in the CrossFit Open 2019 well-balanced regarding gender and/or level of performance?
* Which exercises are weak points in competitor's performance?
* What has the most significant impact on my ranking?
* Is it possible to predict workout scores? - Classifying the ability to perform or not perform:
  - one strict Handstand Push-Up
  - one Bar Muscle-Up

### File Content:
1. [Data Mining](https://github.com/malefiz1988/project-crossfit-data/blob/main/1_Data_Mining.py)
2. [Raw Data Description](https://github.com/malefiz1988/project-crossfit-data/blob/main/2_Raw_Data_Description.ipynb)
3. Data Cleaning of [Benchmark Statistics](https://github.com/malefiz1988/project-crossfit-data/blob/main/3_Data_Cleaning_bs.ipynb) and [full Dataset](https://github.com/malefiz1988/project-crossfit-data/blob/main/3_Data_Cleaning_19.ipynb)
4. EDA [Notebook](https://github.com/malefiz1988/project-crossfit-data/blob/main/4_EDA.ipynb) and [Script](https://github.com/malefiz1988/project-crossfit-data/blob/main/EDA_plots.py) with plot-functions
5. [Missing Data Analysis](https://github.com/malefiz1988/project-crossfit-data/blob/main/5_Missing_Data_Analysis.ipynb)
6. [Data Preparation](https://github.com/malefiz1988/project-crossfit-data/blob/main/6_Data_Preparation.ipynb)
7. Regression Model and Sensitivity Analysis [Notebook](https://github.com/malefiz1988/project-crossfit-data/blob/main/7_Regression_and_Sensitivity_Analysis.ipynb)
8. Classification Model

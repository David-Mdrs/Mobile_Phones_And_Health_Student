# Author: David Medeiros Santos
# Education: Computer Engineer - Federal Institute of Paraíba - Campina Grande Campus

# Subject: Statistics Project Applied to Computing
# Theme: Impact of Cell Phones on Academic Performance and Health

# The dataset is available at: https://www.kaggle.com/datasets/innocentmfa/students-health-and-academic-performance

import os
import pandas as pd

os.system('cls')                                                        # Clear terminal
dataFrame = pd.read_csv('mobile_phones_and_students_health.csv')        # Reading csv arquive


# ========================================  FORMATTING DATAFRAME DATA  ========================================

dataFrame = dataFrame.drop(columns='Names')                             # Deleting colum "Names"
dataFrame = dataFrame.drop(columns='Mobile Phone ')                     # Deleting colum "Mobile Phone "
dataFrame = dataFrame.drop(columns='Mobile Operating System ')          # Deleting colum "Mobile Operating System "

newNames = ['Age', 'Sex', 'Frequency of Use for Study',                 # Choosing new names
            'Activities', 'Useful for Studying', 'Educational Apps',
            'Hour Uses', 'Performance Impact', 'Distraction ',
            'Attention Span', 'Useful Resources', 'Health Risks',
            'Beneficial subject', 'Symptoms of use', 'Frequency of Symptoms',
            'Health Precautions', 'Health Rating']
dataFrame.columns = newNames                                            # Renaming the name of Dataset elements


# Adjusting some unique data to make your analysis easier. Adjusted columns: Activities, Usage Symptoms, Health Rating

dataFrame['Activities'] = dataFrame['Activities'].replace('Social Media;Web-browsing;Messaging;All of these', 'All of these')
dataFrame['Activities'] = dataFrame['Activities'].replace('Social Media;All of these', 'Social Media')
dataFrame['Activities'] = dataFrame['Activities'].replace('Social Media;Messaging', 'Messaging')
dataFrame['Symptoms of use'] = dataFrame['Symptoms of use'].replace('Headache;Sleep disturbance;Anxiety or Stress;All of these', 'All of these')
dataFrame['Health Rating'] = dataFrame['Health Rating'].replace('Excellent;Good;Fair;Poor', 'Fair')

# Separating "Sleep disturbance and Anxiety or Stress" elements equally 
indexes = dataFrame.index[dataFrame['Symptoms of use'] == 'Sleep disturbance;Anxiety or Stress'].tolist()
for i in range(len(indexes)):           
    if i % 2 == 0:
        dataFrame.loc[indexes[i], 'Symptoms of use'] = 'Sleep disturbance'
    else:
        dataFrame.loc[indexes[i], 'Symptoms of use'] = 'Anxiety or Stress'

# Separating "Excellent and Good" elements equally 
indexes = dataFrame.index[dataFrame['Health Rating'] == 'Excellent;Good'].tolist()
for i in range(len(indexes)):          
    if i % 2 == 0:
        dataFrame.loc[indexes[i], 'Health Rating'] = 'Excellent'
    else:
        dataFrame.loc[indexes[i], 'Health Rating'] = 'Good'

indexes = dataFrame.index[dataFrame['Health Rating'] == 'Good;Fair'].tolist()
# Separating "Good and Fair" elements equally
for i in range(len(indexes)):          
    if i % 2 == 0:
        dataFrame.loc[indexes[i], 'Health Rating'] = 'Good'
    else:
        dataFrame.loc[indexes[i], 'Health Rating'] = 'Fair'

# Test updates
# print(dataFrame['Activities'].value_counts())
# print(dataFrame['Symptoms of use'].value_counts())
# print(dataFrame['Health Rating'].value_counts())

# =====================================  END OF DATAFRAME DATA FORMATTING  =====================================

print('first five lines: \n', dataFrame.head())

# NEXT STEP...
#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Number of items in data
len(enron_data)

# Number of features per item
len(enron_data['GLISAN JR BEN'])

# Number of POI entries
sum(1 for x in enron_data.values() if x['poi']==1)

# Load POI names from file
text_file = open("../final_project/poi_names.txt", "r")
names = text_file.read().split('\n')
len(names) - 3 # 3 lines in the file are not names

# James Prentice's total stock value
enron_data['PRENTICE JAMES']['total_stock_value']

# Number of emails from Wesley Colwell to POI
enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# Exercised stock options by Jeffrey K Skilling
enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# Number of entries with available salary info
sum(i['salary'] != 'NaN' for i in enron_data.values())

# Number of entries with available email
sum(i['email_address'] != 'NaN' for i in enron_data.values())

# Percentage of entries without total_payments
from __future__ import division
sum(i['total_payments'] == 'NaN' for i in enron_data.values()) / len(enron_data)

# Percentage of poi's without total_payments
sum((i['total_payments'] == 'NaN') & (i['poi']) for i in enron_data.values()) / len(enron_data)

# Number of poi's
sum(i['poi'] for i in enron_data.values()) 
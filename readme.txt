1. All the imports are required:
from flask import Flask, render_template, request, url_for, flash, redirect
from flask import Flask
import pickle
import numpy
import csv
import pandas as pd
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

Once you have the imports and files set in place you can run main.py and you will be given a url which when you paste it in your web browser you can play around with the website. When you submit a post or you update your temperature, the data will be stored in site.db

# this is not required but if site.db doesn't work follow these steps:
To create the site.db file and its contents
- the user must go to the terminal directory where the coding lab folder is
- type in python3
- from main import db
- db.drop_all()
- db.create_all()
exit()

After that you are all set to go
###################################################

In data.csv file the values 1, -1, 0 refer to the extent or seriousness of the health issue they are facing. 1 for example might be very difficult to breath
All that is defined in my code

BLOG POSTS AND TEMPERATURE CHECKS ARE SENT TO DATABASE AND THEN CAN BE GIVEN TO GOVERNMENT AGENCIES SO THEY CAN SEE ANY TEMPERAUTRE FLUCTUATIONS OR  IF THE USER MIGHT HAVE COVID. MAKES JOB FOR GOVERNMENT AGENCIES MUCH EASIER


The website can be run only when the main.py file is still running.


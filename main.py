import requests as r
import time as t
from datetime import datetime
import json
import os
import boto3
import sys
from dotenv import load_dotenv

from bike_point_extract import extract
from bike_point_load import load

url = 'https://api.tfl.gov.uk/BikePoint'

extract(url)
load()
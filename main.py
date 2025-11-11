from bike_point_extract import extract
from bike_point_load import load

url = 'https://api.tfl.gov.uk/BikePoint'

extract(url)
load()
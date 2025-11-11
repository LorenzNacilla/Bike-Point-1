import json
import time
from datetime import datetime
import requests

url = 'https://api.tfl.gov.uk/BikePoint'

def extract(url):
    response = requests.get(url, timeout = 10)
    retry_codes = [249,500]

    count = 0
    max_tries = 3

    while count < max_tries:
        if response.status_code == 200:
            try: # if api call is successful, ensure the status is 200
                data = response.json() # getting the data in json format if connected successfully 
            except Exception as e:
                print(e) # print error message and break the loop
                break
                
            extract_timestamp = datetime.now()
            for bp in data:
                bp["extract_timestamp"] = str(extract_timestamp) # getting the current timestamp as a key

            filepath = 'data/' + extract_timestamp.strftime('%Y-%m-%dT%H-%M-%S') + '.json'
            with open(filepath, 'w') as file: # saving the json data file with the timestamp of running the script
                json.dump(data, file)
            break

        elif response.status_code in retry_codes: # giving it time to reconnect again based on codes set earlier if it returns that
            time.sleep(20)
            print(response.reason())
            count += 1

        else:
            print(response.reason()) # there may be another error occuring instead and print that
            break
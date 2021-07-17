import os
import googlemaps
from  pathlib import Path
from dotenv import load_dotenv
import time
from excel import Excel
'''
Configurations
_ _ _ _ _ _ _ _

'''
# Use the Google maps api 
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
API_KEY = os.environ['API_KEY']

'''
A class that is used to get the response from the places api

'''
class ApiResponse:
    map_client = googlemaps.Client(API_KEY)
    def __init__(self,category):
        self.category = category

    def scrape_data(self):
        nextPageToken = None
        while True:
            # only sleep after the 1st page has passed
            if nextPageToken:
                # stagger the api calls to prevent an invalid request from the google maps api
                time.sleep(3)
            response = ApiResponse.map_client.places(query=self.category,page_token=nextPageToken)

            # Get the next Page token from the maps api
            try:
                nextPageToken = response['next_page_token']
            except KeyError:
                break

            # iterate thorugh all the places in the page
            excel = Excel()
            for places in response['results']:
                NOT_FOUND = 'Details Cannot Be Found From Google'

                # get the address contact name,rating,website for all the store
                place_id = places['place_id']
                name = places['name']
                # take the case where the
                try:
                    address = places['formatted_address']
                except KeyError:
                    address = NOT_FOUND
                place_details = ApiResponse.map_client.place(place_id=place_id)
                try:
                    contact = place_details['result']['formatted_phone_number']
                except KeyError:
                    contact =NOT_FOUND
                try:
                    website = place_details['result']['website']
                except KeyError:
                    website =NOT_FOUND
                
                excel.append_excel(contact,name,website,address)




                
            # Continue until there is no more results from the google api


            
            




    






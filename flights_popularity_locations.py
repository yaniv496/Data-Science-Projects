# -*- coding: utf-8 -*-
"""Copy of flights_popularity_locations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hPBZH7RnyicEW5doXAEfeogEutuxmo94
"""

import requests
import pandas as pd
from datetime import datetime

# Constants
BASE_URL = 'http://api.aviationstack.com/v1'
API_KEY = 'cb4bdcd201136fd91a2c0d656e817e79'

def load_airport_data():
    return pd.read_csv('airports.csv')

def get_flight_info(dep_iata, arr_iata, flight_date):
    params = {
        'access_key': API_KEY,
        'dep_iata': dep_iata,
        'arr_iata': arr_iata,
        'flight_date': flight_date
    }
    response = requests.get(f"{BASE_URL}/flights", params=params)
    data = response.json()
    return data

def main():

  # List of airports
  airports = [
      # Europe
      {"airport": "Charles de Gaulle Airport", "city": "Paris", "iata": "CDG"},
      {"airport": "Frankfurt Airport", "city": "Frankfurt", "iata": "FRA"},
      {"airport": "Amsterdam Airport Schiphol", "city": "Amsterdam", "iata": "AMS"},
      {"airport": "Madrid-Barajas Airport", "city": "Madrid", "iata": "MAD"},
      {"airport": "Heathrow Airport", "city": "London", "iata": "LHR"},
      {"airport": "Munich Airport", "city": "Munich", "iata": "MUC"},
      {"airport": "Leonardo da Vinci–Fiumicino Airport", "city": "Rome", "iata": "FCO"},
      {"airport": "Zurich Airport", "city": "Zurich", "iata": "ZRH"},
      {"airport": "Barcelona-El Prat Airport", "city": "Barcelona", "iata": "BCN"},
      {"airport": "Vienna International Airport", "city": "Vienna", "iata": "VIE"},

      # USA
      {"airport": "Hartsfield-Jackson Atlanta International Airport", "city": "Atlanta", "iata": "ATL"},
      {"airport": "Los Angeles International Airport", "city": "Los Angeles", "iata": "LAX"},
      {"airport": "O'Hare International Airport", "city": "Chicago", "iata": "ORD"},
      {"airport": "Dallas/Fort Worth International Airport", "city": "Dallas", "iata": "DFW"},
      {"airport": "Denver International Airport", "city": "Denver", "iata": "DEN"},
      {"airport": "John F. Kennedy International Airport", "city": "New York", "iata": "JFK"},
      {"airport": "San Francisco International Airport", "city": "San Francisco", "iata": "SFO"},
      {"airport": "Seattle-Tacoma International Airport", "city": "Seattle", "iata": "SEA"},
      {"airport": "McCarran International Airport", "city": "Las Vegas", "iata": "LAS"},
      {"airport": "Orlando International Airport", "city": "Orlando", "iata": "MCO"},

      # Israel
      {"airport": "Ben Gurion Airport", "city": "Tel Aviv", "iata": "TLV"}
  ]

  # Create a DataFrame
  df = pd.DataFrame(airports)

  # Save to CSV
  df.to_csv('airports.csv', index=False)

  print("CSV file 'airports.csv' has been created.")


  


    key_input = ''
    while key_input != 'q':
        #load csv data
        airport_data = load_airport_data()
        ita_list =[]
        print("Select Reference Airport to compare:") # Departure
        for idx, row in airport_data.iterrows():
            print(f"{idx}. {row['airport']} ({row['iata']}) - {row['city']}")
            ita_list.append(row['iata'])

        print (ita_list)
        ref_index1 = st.text_input("\nEnter the number of the Reference airport: ", '')
        ref_index = int(input("\nEnter the number of the Reference airport: "))
        ref_iata = airport_data.iloc[ref_index]['iata']

        flight_date = input("\nEnter the flight date (YYYY-MM-DD): ")
        try:
            datetime.strptime(flight_date, '%Y-%m-%d')
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")
            return
        # print("\nSelect Arrival Airport:")
        # for idx, row in airport_data.iterrows():
        #     print(f"{idx}. {row['airport']} ({row['iata']}) - {row['city']}")
        ref_iata_to_ita = {}
        uta_to_ref_iata = {}
        print('Ref to all locations List: \n')
        max_flights = 0
        flight_detail =''
        for ita in ita_list:
            if ita != ref_iata:
                flight_data_all = get_flight_info(ref_iata, ita,flight_date)
                flight_count = len(flight_data_all['data'])
                if flight_count > max_flights:
                    max_flights = flight_count
                    flight_detail = ref_iata + ' to ' + ita

                print('flight_counts -  ' + ref_iata + ' to ' + ita + ' :  ' + str(flight_count))


        print('\n all locations to Ref List: \n')
        for ita in ita_list:
            if ita != ref_iata:
                flight_data_all = get_flight_info(ita,ref_iata,flight_date)
                flight_count = len(flight_data_all['data'])
                if flight_count > max_flights:
                    max_flights = flight_count
                    flight_detail = ita + ' to ' + ref_iata
                print('flight_counts -  ' + ita + ' to ' + ref_iata + ' :  ' + str(flight_count))

        arr_index = int(input("\nFor flights details Enter the number of airports from the list : "))
        arr_iata = airport_data.iloc[arr_index]['iata']


        flight_data = get_flight_info(ref_iata, arr_iata, flight_date)
        flight_count = len(flight_data['data'])
        print('flight_counts -  ' + ref_iata + ' to ' + arr_iata + ' :  ' + str(flight_count))
        if 'error' in flight_data:
            print(f"Error: {flight_data['error']['info']}")
        else:
            print("\nFlight Information:")
            for flight in flight_data['data']:
                print(f"Flight: {flight['flight']['iata']}, Airline: {flight['airline']['name']}, Status: {flight['flight_status']}")
                print(f"Departure: {flight['departure']['airport']} at {flight['departure']['scheduled']}")
                print(f"Arrival: {flight['arrival']['airport']} at {flight['arrival']['scheduled']}")
                print("-----")

        flight_data2 = get_flight_info(arr_iata,ref_iata, flight_date)
        flight_count2 = len(flight_data2['data'])
        print('flight_counts -  ' + arr_iata + ' to ' + ref_iata     + ' :  ' + str(flight_count2))
        if 'error' in flight_data:
            print(f"Error: {flight_data['error']['info']}")
        else:
            print("\nFlight Information:")
            for flight in flight_data2['data']:
                print(f"Flight: {flight['flight']['iata']}, Airline: {flight['airline']['name']}, Status: {flight['flight_status']}")
                print(f"Departure: {flight['departure']['airport']} at {flight['departure']['scheduled']}")
                print(f"Arrival: {flight['arrival']['airport']} at {flight['arrival']['scheduled']}")
                print("-----")

        print('The Most poplar flight root path  for ' + str(flight_date) + ' is: ' + flight_detail + ' with '  + str(max_flights) + ' flights' )
        print( '\nHave a good flight')

        key_input = input("\n Stop searching flights - > press q else press Enter ")
        
if __name__ == '__main__':
    main()
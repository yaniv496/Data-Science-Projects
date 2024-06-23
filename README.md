# Data-Science-Projects
Data Science Projects - Bar Ilan University
python flight project:
	Number of Flight per days: compare amount of flights in both directions between two locations
	1. set 1 reference airport location 
	2. set list of airports locations 
	3. Read the amount of flights between reference to each location in the list
	4. Read the amount of flights in the opposite direction: between each location in the list to the reference location 
	5. Can print all the flights detailed for each pair of locations

use aviationstack.com API WEB and API_KEY value is update in code 
BASE_URL = 'http://api.aviationstack.com/v1'


Explanations:




results of running script:

example  of running:

Select Reference Airport to compare:
0. Charles de Gaulle Airport (CDG) - Paris
1. Frankfurt Airport (FRA) - Frankfurt
2. Amsterdam Airport Schiphol (AMS) - Amsterdam
3. Madrid-Barajas Airport (MAD) - Madrid
4. Heathrow Airport (LHR) - London
5. Munich Airport (MUC) - Munich
6. Leonardo da Vinci–Fiumicino Airport (FCO) - Rome
7. Zurich Airport (ZRH) - Zurich
8. Barcelona-El Prat Airport (BCN) - Barcelona
9. Vienna International Airport (VIE) - Vienna
10. Hartsfield-Jackson Atlanta International Airport (ATL) - Atlanta
11. Los Angeles International Airport (LAX) - Los Angeles
12. O'Hare International Airport (ORD) - Chicago
13. Dallas/Fort Worth International Airport (DFW) - Dallas
14. Denver International Airport (DEN) - Denver
15. John F. Kennedy International Airport (JFK) - New York
16. San Francisco International Airport (SFO) - San Francisco
17. Seattle-Tacoma International Airport (SEA) - Seattle
18. McCarran International Airport (LAS) - Las Vegas
19. Orlando International Airport (MCO) - Orlando
20. Ben Gurion Airport (TLV) - Tel Aviv
['CDG', 'FRA', 'AMS', 'MAD', 'LHR', 'MUC', 'FCO', 'ZRH', 'BCN', 'VIE', 'ATL', 'LAX', 'ORD', 'DFW', 'DEN', 'JFK', 'SFO', 'SEA', 'LAS', 'MCO', 'TLV']


Enter the number of the Reference airport: 12

Enter the flight date (YYYY-MM-DD): 2024-06-22
Ref to all locations List: 

flight_counts -  ORD to CDG :  15
flight_counts -  ORD to FRA :  17
flight_counts -  ORD to AMS :  8
flight_counts -  ORD to MAD :  6
flight_counts -  ORD to LHR :  63
flight_counts -  ORD to MUC :  9
flight_counts -  ORD to FCO :  13
flight_counts -  ORD to ZRH :  10
flight_counts -  ORD to BCN :  7
flight_counts -  ORD to VIE :  2
flight_counts -  ORD to ATL :  89
flight_counts -  ORD to LAX :  100
flight_counts -  ORD to ORD :  1
flight_counts -  ORD to DFW :  71
flight_counts -  ORD to DEN :  50
flight_counts -  ORD to JFK :  58
flight_counts -  ORD to SFO :  76
flight_counts -  ORD to SEA :  59
flight_counts -  ORD to LAS :  43
flight_counts -  ORD to MCO :  56
flight_counts -  ORD to TLV :  0

 all locations to Ref List: 

flight_counts -  CDG to ORD :  18
flight_counts -  FRA to ORD :  16
flight_counts -  AMS to ORD :  11
flight_counts -  MAD to ORD :  6
flight_counts -  LHR to ORD :  62
flight_counts -  MUC to ORD :  9
flight_counts -  FCO to ORD :  13
flight_counts -  ZRH to ORD :  10
flight_counts -  BCN to ORD :  7
flight_counts -  VIE to ORD :  2
flight_counts -  ATL to ORD :  74
flight_counts -  LAX to ORD :  100
flight_counts -  ORD to ORD :  1
flight_counts -  DFW to ORD :  79
flight_counts -  DEN to ORD :  54
flight_counts -  JFK to ORD :  48
flight_counts -  SFO to ORD :  75
flight_counts -  SEA to ORD :  59
flight_counts -  LAS to ORD :  44
flight_counts -  MCO to ORD :  55
flight_counts -  TLV to ORD :  0
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:11:54 2018

@author: marco
"""

import csv
from data import *

def lines(text): return text.strip().splitlines()

def Coordinate_map(lines, delimiter=' ', lat_col=1, long_col=2, lat_scale=69, long_scale=-48):
    """Make a set of Cities from an iterable of lines of text.
    Specify the column delimiter, and the zero-based column number of lat and long.
    Treat long/lat as a square x/y grid, scaled by long_scale and lat_scale.
    Source can be a file object, or list of lines."""
    return frozenset(City(long_scale * float(row[long_col]),
                          lat_scale  * float(row[lat_col]))
                     for row in csv.reader(lines, delimiter=delimiter, skipinitialspace=True))


USA_map = Coordinate_map(lines("""
[TCL]  33.23   87.62  Tuscaloosa,AL
[FLG]  35.13  111.67  Flagstaff,AZ
[PHX]  33.43  112.02  Phoenix,AZ
[PGA]  36.93  111.45  Page,AZ
[TUS]  32.12  110.93  Tucson,AZ
[LIT]  35.22   92.38  Little Rock,AR
[SFO]  37.62  122.38  San Francisco,CA
[LAX]  33.93  118.40  Los Angeles,CA
[SAC]  38.52  121.50  Sacramento,CA
[SAN]  32.73  117.17  San Diego,CA
[SBP]  35.23  120.65  San Luis Obi,CA
[EKA]  41.33  124.28  Eureka,CA
[DEN]  39.75  104.87  Denver,CO
[DCA]  38.85   77.04  Washington/Natl,DC
[MIA]  25.82   80.28  Miami Intl,FL
[TPA]  27.97   82.53  Tampa Intl,FL
[JAX]  30.50   81.70  Jacksonville,FL
[TLH]  30.38   84.37  Tallahassee,FL
[ATL]  33.65   84.42  Atlanta,GA
[BOI]  43.57  116.22  Boise,ID
[CHI]  41.90   87.65  Chicago,IL
[IND]  39.73   86.27  Indianapolis,IN
[DSM]  41.53   93.65  Des Moines,IA
[SUX]  42.40   96.38  Sioux City,IA
[ICT]  37.65   97.43  Wichita,KS
[LEX]  38.05   85.00  Lexington,KY
[NEW]  30.03   90.03  New Orleans,LA
[BOS]  42.37   71.03  Boston,MA
[PWM]  43.65   70.32  Portland,ME
[BGR]  44.80   68.82  Bangor,ME
[CAR]  46.87   68.02  Caribou Mun,ME
[DET]  42.42   83.02  Detroit,MI
[STC]  45.55   94.07  St Cloud,MN
[DLH]  46.83   92.18  Duluth,MN
[STL]  38.75   90.37  St Louis,MO
[JAN]  32.32   90.08  Jackson,MS
[BIL]  45.80  108.53  Billings,MT
[BTM]  45.95  112.50  Butte,MT
[RDU]  35.87   78.78  Raleigh-Durh,NC
[INT]  36.13   80.23  Winston-Salem,NC
[OMA]  41.30   95.90  Omaha/Eppley,NE
[LAS]  36.08  115.17  Las Vegas,NV
[RNO]  39.50  119.78  Reno,NV
[AWH]  41.33  116.25  Wildhorse,NV
[EWR]  40.70   74.17  Newark Intl,NJ
[SAF]  35.62  106.08  Santa Fe,NM
[NYC]  40.77   73.98  New York,NY
[BUF]  42.93   78.73  Buffalo,NY
[ALB]  42.75   73.80  Albany,NY
[FAR]  46.90   96.80  Fargo,ND
[BIS]  46.77  100.75  Bismarck,ND
[CVG]  39.05   84.67  Cincinnati,OH
[CLE]  41.42   81.87  Cleveland,OH
[OKC]  35.40   97.60  Oklahoma Cty,OK
[PDX]  45.60  122.60  Portland,OR
[MFR]  42.37  122.87  Medford,OR
[AGC]  40.35   79.93  Pittsburgh,PA
[PVD]  41.73   71.43  Providence,RI
[CHS]  32.90   80.03  Charleston,SC
[RAP]  44.05  103.07  Rapid City,SD
[FSD]  43.58   96.73  Sioux Falls,SD
[MEM]  35.05   90.00  Memphis Intl,TN
[TYS]  35.82   83.98  Knoxville,TN
[CRP]  27.77   97.50  Corpus Chrst,TX
[DRT]  29.37  100.92  Del Rio,TX
[IAH]  29.97   95.35  Houston,TX
[SAT]  29.53   98.47  San Antonio,TX
[LGU]  41.78  111.85  Logan,UT
[SLC]  40.78  111.97  Salt Lake Ct,UT
[SGU]  37.08  113.60  Saint George,UT
[CNY]  38.77  109.75  Moab,UT
[MPV]  44.20   72.57  Montpelier,VT
[RIC]  37.50   77.33  Richmond,VA
[BLI]  48.80  122.53  Bellingham,WA
[SEA]  47.45  122.30  Seattle,WA
[ALW]  46.10  118.28  Walla Walla,WA
[GRB]  44.48   88.13  Green Bay,WI
[MKE]  42.95   87.90  Milwaukee,WI
[CYS]  41.15  104.82  Cheyenne,WY
[SHR]  44.77  106.97  Sheridan,WY
"""))



USA_landmarks_map = Coordinate_map(lines("""
Mount Rushmore National Memorial, South Dakota 244, Keystone, SD	43.879102	-103.459067
Toltec Mounds, Scott, AR	34.647037	-92.065143
Ashfall Fossil Bed, Royal, NE	42.425000	-98.158611
Maryland State House, 100 State Cir, Annapolis, MD 21401	38.978828	-76.490974
The Mark Twain House & Museum, Farmington Avenue, Hartford, CT	41.766759	-72.701173
Columbia River Gorge National Scenic Area, Oregon	45.711564	-121.519633
Mammoth Cave National Park, Mammoth Cave Pkwy, Mammoth Cave, KY	37.186998	-86.100528
Bryce Canyon National Park, Hwy 63, Bryce, UT	37.593038	-112.187089
USS Alabama, Battleship Parkway, Mobile, AL	30.681803	-88.014426
Graceland, Elvis Presley Boulevard, Memphis, TN	35.047691	-90.026049
Wright Brothers National Memorial Visitor Center, Manteo, NC	35.908226	-75.675730
Vicksburg National Military Park, Clay Street, Vicksburg, MS	32.346550	-90.849850
Statue of Liberty, Liberty Island, NYC, NY	40.689249	-74.044500
Mount Vernon, Fairfax County, Virginia	38.729314	-77.107386
Fort Union Trading Post National Historic Site, Williston, North Dakota 1804, ND	48.000160	-104.041483
San Andreas Fault, San Benito County, CA	36.576088	-120.987632
Chickasaw National Recreation Area, 1008 W 2nd St, Sulphur, OK 73086	34.457043	-97.012213
Hanford Site, Benton County, WA	46.550684	-119.488974
Spring Grove Cemetery, Spring Grove Avenue, Cincinnati, OH	39.174331	-84.524997
Craters of the Moon National Monument & Preserve, Arco, ID	43.416650	-113.516650
The Alamo, Alamo Plaza, San Antonio, TX	29.425967	-98.486142
New Castle Historic District, Delaware	38.910832	-75.527670
Gateway Arch, Washington Avenue, St Louis, MO	38.624647	-90.184992
West Baden Springs Hotel, West Baden Avenue, West Baden Springs, IN	38.566697	-86.617524
Carlsbad Caverns National Park, Carlsbad, NM	32.123169	-104.587450
Pikes Peak, Colorado	38.840871	-105.042260
Okefenokee Swamp Park, Okefenokee Swamp Park Road, Waycross, GA	31.056794	-82.272327
Cape Canaveral, FL	28.388333	-80.603611
Glacier National Park, West Glacier, MT	48.759613	-113.787023
Congress Hall, Congress Place, Cape May, NJ 08204	38.931843	-74.924184
Olympia Entertainment, Woodward Avenue, Detroit, MI	42.387579	-83.084943
Fort Snelling, Tower Avenue, Saint Paul, MN	44.892850	-93.180627
Hoover Dam, Boulder City, CO	36.012638	-114.742225
White House, Pennsylvania Avenue Northwest, Washington, DC	38.897676	-77.036530
USS Constitution, Boston, MA	42.372470	-71.056575
Omni Mount Washington Resort, Mount Washington Hotel Road, Bretton Woods, NH	44.258120	-71.441189
Grand Canyon National Park, Arizona	36.106965	-112.112997
The Breakers, Ochre Point Avenue, Newport, RI	41.469858	-71.298265
Fort Sumter National Monument, Sullivan's Island, SC	32.752348	-79.874692
Cable Car Museum, 94108, 1201 Mason St, San Francisco, CA 94108	37.794781	-122.411715
Yellowstone National Park, WY 82190	44.462085	-110.642441
French Quarter, New Orleans, LA	29.958443	-90.064411
C. W. Parker Carousel Museum, South Esplanade Street, Leavenworth, KS	39.317245	-94.909536
Shelburne Farms, Harbor Road, Shelburne, VT	44.408948	-73.247227
Taliesin, County Road C, Spring Green, Wisconsin	43.141031	-90.070467
Acadia National Park, Maine	44.338556	-68.273335
Liberty Bell, 6th Street, Philadelphia, PA	39.949610	-75.150282
Terrace Hill, Grand Avenue, Des Moines, IA	41.583218	-93.648542
Lincoln Home National Historic Site Visitor Center, 426 South 7th Street, Springfield, IL	39.797501	-89.646211
Lost World Caverns, Lewisburg, WV	37.801788	-80.445630
"""), delimiter='\t', long_scale=48)




def continental_USA(line):
    "Does line denote a city in the continental United States?"
    return line.startswith('[') and ',AK' not in line and ',HI' not in line

# USA_big_map = Coordinate_map(filter(continental_USA, open('latlong.htm')))

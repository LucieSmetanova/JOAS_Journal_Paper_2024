import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

lat_PM = [53.7803,54.1412,53.7094,53.6392,53.9650,53.6285,53.7671,53.5718,53.4031,53.1979,53.1276,53.0639,52.9967,52.7828,52.5544,53.1415,53.1713,53.0027,53.0494,52.8244,52.6228,53.420333,53.4225]
lon_PM = [-7.2946,-6.6511,-6.6053,-5.9592,-5.7421,-5.7659,-5.5,-5.6373,-5.9456,-5.6409,-5.5669,-5.5,-5.3775,-4.9925,-5.5,-5.8063,-6.3669,-6.6611,-7.2702,-6.9304,-6.6301,-6.2505,-6.29]

RT1_lat = [lat_PM[0],lat_PM[2],lat_PM[3],lat_PM[5],lat_PM[7]]
RT2_lat = [lat_PM[1],lat_PM[2],lat_PM[3],lat_PM[5],lat_PM[7]]
RT3_lat = [lat_PM[4],lat_PM[5],lat_PM[7]]
RT4_lat = [lat_PM[6],lat_PM[5],lat_PM[7]]
RT5_lat = [lat_PM[18],lat_PM[17],lat_PM[16],lat_PM[15],lat_PM[9]]
RT6_lat = [lat_PM[19],lat_PM[17],lat_PM[16],lat_PM[15],lat_PM[9]]
RT7_lat = [lat_PM[20],lat_PM[17],lat_PM[16],lat_PM[15],lat_PM[9]]
RT8_lat = [lat_PM[14],lat_PM[15],lat_PM[9]]
RT9_lat = [lat_PM[13],lat_PM[12],lat_PM[11],lat_PM[10],lat_PM[9]]
RT12_lat = [lat_PM[8],lat_PM[21],lat_PM[22]]

RT1_lon = [lon_PM[0],lon_PM[2],lon_PM[3],lon_PM[5],lon_PM[7]]
RT2_lon = [lon_PM[1],lon_PM[2],lon_PM[3],lon_PM[5],lon_PM[7]]
RT3_lon = [lon_PM[4],lon_PM[5],lon_PM[7]]
RT4_lon = [lon_PM[6],lon_PM[5],lon_PM[7]]
RT5_lon = [lon_PM[18],lon_PM[17],lon_PM[16],lon_PM[15],lon_PM[9]]
RT6_lon = [lon_PM[19],lon_PM[17],lon_PM[16],lon_PM[15],lon_PM[9]]
RT7_lon = [lon_PM[20],lon_PM[17],lon_PM[16],lon_PM[15],lon_PM[9]]
RT8_lon = [lon_PM[14],lon_PM[15],lon_PM[9]]
RT9_lon = [lon_PM[13],lon_PM[12],lon_PM[11],lon_PM[10],lon_PM[9]]
RT12_lon = [lon_PM[8],lon_PM[21],lon_PM[22]]

def dms2dd(as_string):
    degrees = int(as_string[:2])
    minutes = int(as_string[2:4])
    seconds = float(as_string[4:8])
    lat_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    degrees = -1*int(as_string[10:13])
    minutes = -1*int(as_string[13:15])
    seconds = -1*float(as_string[15:19])
    lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)

    return lat_dd, lon_dd

SIVNA_lat, SIVNA_lon = dms2dd("531152.3N 0053827.7W")
SIVNA_circle_center = Point(SIVNA_lon, SIVNA_lat)
KOGAX_lat, KOGAX_lon = dms2dd("533418.6N 0053814.1W")
KOGAX_circle_center = Point(KOGAX_lon, KOGAX_lat)
KUDOM_lat, KUDOM_lon = dms2dd("532925.8N 0053314.3W")
KUDOM_circle_center = Point(KUDOM_lon, KUDOM_lat)
DW814_lat, DW814_lon = dms2dd("532347.5N 0053141.1W")
DW814_circle_center = Point(DW814_lon, DW814_lat)
DW815_lat, DW815_lon = dms2dd("531812.9N 0053346.6W")
DW815_circle_center = Point(DW815_lon, DW815_lat)
DW816_lat, DW816_lon = dms2dd("531346.9N 0053844.4W")
DW816_circle_center = Point(DW816_lon, DW816_lat)
SUGAD_lat, SUGAD_lon = dms2dd("531722.5N 0053139.8W")
SUGAD_circle_center = Point(SUGAD_lon, SUGAD_lat)
DW704_lat, DW704_lon = dms2dd("532403.7N 0052910.1W")
DW704_circle_center = Point(DW704_lon, DW704_lat)
DW705_lat, DW705_lon = dms2dd("533046.6N 0053126.4W")
DW705_circle_center = Point(DW705_lon, DW705_lat)
DW706_lat, DW706_lon = dms2dd("533621.3N 0053806.9W")
DW706_circle_center = Point(DW706_lon, DW706_lat)
LAPMO_lat, LAPMO_lon = dms2dd("532411.0N 0055644.1W")

RT10_lat = [KOGAX_lat,KUDOM_lat,DW814_lat,DW815_lat,DW816_lat,LAPMO_lat]
RT11_lat = [SIVNA_lat,SUGAD_lat,DW704_lat,DW705_lat,DW706_lat,LAPMO_lat]
RT10_lon = [KOGAX_lon,KUDOM_lon,DW814_lon,DW815_lon,DW816_lon,LAPMO_lon]
RT11_lon = [SIVNA_lon,SUGAD_lon,DW704_lon,DW705_lon,DW706_lon,LAPMO_lon]


radius=0.05
rad = 'rad05'

flightsrwy2 = pd.DataFrame()
flights = pd.read_csv('PM_dataset.csv', 
header=None,
sep=' '
) 
list_col_names = ['x','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flights.columns = list_col_names
flightsrwy2 = pd.concat([flightsrwy2,flights])
flightsrwy = flights.copy()
flightsrwy = flightsrwy.drop("x", axis='columns')

err = ['220705RYR846Z','220705RYR8556','220713EIN74P','220710RYR21PU','220711EIN415','220701RYR7GK','220706THY98W','220701RYR4CA','220706EIN52X',
          '220702RYR7VN','220705BAW84W', '220719EIN605P', '220721RYR59BD', '220721RYR69QY','220721RYR863', '220721RYR92EW', '220721RYR9PT',
          '220716RYR671', '220717SWR48X', '220718EAI65BM', '220718RYR42XU','220719RYR3KU','220717RYR34BD','220721EIN63K','220717EIN545','220722CFE221',
          '220722EAI95LS', '220722EIN3LG','220722EIN69Y', '220722RYR94HQ', '220727EAI75BH', '220727EIN209', '220728EAB27MU','220714RYR3UN',
          '220722EIN799', '220724EIN545', '220725EAI57EU', '220725RYR171J','220724RYR56RB', '220726TOM239','220705RYR22EL','220706RYR1FL',
          '220715EIN122','220716EIN122','220717EIN960','220719AAL208','220719RYR84HD','220721AAL722','220721RYR4DP','220717RYR3JX','220720DAL154',
          '220721EAI87DM','220721EIN70V','220715EIN1MN','220721AFR95UF', '220721BLA2RA', '220721BLA4JU', '220721DLH982','220721EIN33W', '220721EIN4GJ',
          '220721EIN529','220721EIN737','220721EIN76HJ', '220721FIA711', '220721RYR12MC', '220721RYR1341','220721RYR1UP', '220721RYR2PV', '220721RYR323M',
          '220721RYR3WR','220721RYR3YW', '220721RYR47JE', '220721RYR673', '220721RYR69NK','220721RYR6MW', '220721RYR7149', '220721RYR717R', '220721RYR72',
          '220721RYR74TG', '220721RYR7EX', '220721RYR7ZZ', '220721RYR98KD','220721RYR9GF', '220721RYR9LK','220722EIN122', '220722EIN1MN', '220722EIN58R',
          '220722EIN5HL','220723AAL722', '220723AAL724', '220727EIN104', '220728EIN104','220728EIN122', '220728EIN13K', '220728RYR6678','220723EIN122',
          '220723EIN1MN', '220724EIN104', '220724EIN1TC','220727EIN11P','220722BLA3SX', '220722EIN17VT', '220722EIN38JC', '220722EIN497','220722RYR4AV',
          '220722TOM1487', '220722TOM2DT','220722RYR23FJ']

flightsrwy = flightsrwy[~flightsrwy['flightID'].isin(err)]

flightsrwy['time_in_final'] = flightsrwy.groupby(['flightID','endDate'])['timestamp'].transform('max')    
number_of_flights = flightsrwy['flightID'].nunique()
flightsrwy['time_to_final'] = (flightsrwy['time_in_final'] - flightsrwy['timestamp'])/60
flightsrwy['altitude_ft'] = flightsrwy['baroAltitude']*3.281/100
xx = flightsrwy.loc[(flightsrwy['flightID']=='220708EAI17NQ')]
nflights = flightsrwy['flightID'].nunique()
print('Number of flights in original PM: ',nflights)

flights_arcs = flightsrwy.loc[((flightsrwy['altitude_ft']>=67)&(flightsrwy['altitude_ft']<=73))|((flightsrwy['altitude_ft']>=77)&(flightsrwy['altitude_ft']<=83))]
level_flights = flights_arcs.groupby('flightID').size()
df = level_flights.reset_index()
df = df.rename(columns={0:'number'})
df['group'] = df['number'].round(decimals=-1)
occur = df.groupby('group').size().idxmax()
print('The number with highest occurence (threshold): ',occur)
level_flights = level_flights.loc[(level_flights)>=occur].reset_index()
mask = flightsrwy['flightID'].isin(level_flights['flightID'])
flights_PM_level = flightsrwy[mask]
nflights_level = flights_PM_level['flightID'].nunique()
print('Number of flights in filtered subset: ',nflights_level)
flights_PM_level.to_csv('PM_VP_dataset_'+rad+'.csv', sep=' ', encoding='utf-8', float_format='%.3f', index = False, header = False)

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# axes = plt.gca()
# axes.legend().set_visible(False)
xx.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='blue',lw=3)
ax.axhline(80, color="red", linestyle="--")
ax.axhline(70, color="orange", linestyle="--")
ax.set_xlim([0,40])                                                               #setting limits for axes
ax.set_ylim([0,300])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flights_PM_level.groupby(['flightID','endDate']):
    g.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# axes = plt.gca()
# axes.legend().set_visible(False)
xx.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='blue',lw=3)
ax.axhline(80, color="red", linestyle="--")
ax.axhline(70, color="orange", linestyle="--")
ax.set_xlim([0,40])                                                               #setting limits for axes
ax.set_ylim([0,300])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


fig, ax = plt.subplots(figsize=(9,9))
for i, g in flights_PM_level.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((KOGAX_lon,KOGAX_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((SIVNA_lon,SIVNA_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black')
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black')
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black')
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black')
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black')
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black')
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black')
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black')
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black')
plot11 = plt.plot(RT10_lon, RT10_lat,linewidth=1.5,color = 'black')
plot12 = plt.plot(RT11_lon, RT11_lat,linewidth=1.5,color = 'black')
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set(xlabel=None)
ax.set_xlim([-6.1,-5.43])                                                               #setting limits for axes
ax.set_ylim([53.08,53.75])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((KOGAX_lon,KOGAX_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((SIVNA_lon,SIVNA_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black')
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black')
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black')
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black')
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black')
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black')
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black')
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black')
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black')
plot11 = plt.plot(RT10_lon, RT10_lat,linewidth=1.5,color = 'black')
plot12 = plt.plot(RT11_lon, RT11_lat,linewidth=1.5,color = 'black')
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([-6.1,-5.43])                                                               #setting limits for axes
ax.set_ylim([53.08,53.75])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


fig, ax = plt.subplots(figsize=(9,9))
xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((KOGAX_lon,KOGAX_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((SIVNA_lon,SIVNA_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black')
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black')
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black')
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black')
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black')
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black')
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black')
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black')
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black')
plot11 = plt.plot(RT10_lon, RT10_lat,linewidth=1.5,color = 'black')
plot12 = plt.plot(RT11_lon, RT11_lat,linewidth=1.5,color = 'black')
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set(xlabel=None)
ax.set_xlim([-6.1,-5.43])                                                               #setting limits for axes
ax.set_ylim([53.08,53.75])
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


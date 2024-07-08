import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def dms2dd(as_string):
    degrees = int(as_string[:2])
    minutes = int(as_string[2:4])
    seconds = float(as_string[4:9])
    lat_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    degrees = int(as_string[10:14])
    minutes = int(as_string[14:16])
    seconds = float(as_string[16:21])
    lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)

    return lat_dd, lon_dd

BABKU_lat, BABKU_lon = dms2dd("513519.59N 0011916.23E")
NONVA_lat, NONVA_lon = dms2dd("513846.45N 0012144.31E")
ELMIV_lat, ELMIV_lon = dms2dd("512033.08N 0011533.36E")
GODLU_lat, GODLU_lon = dms2dd("510958.44N 0011704.26E")
LCE11_lat, LCE11_lon = dms2dd('512504.57N 0011834.81E')
LCE12_lat, LCE12_lon = dms2dd('512958.17N 0011906.68E')
LCE13_lat, LCE13_lon = dms2dd('513442.46N 0011704.79E')
RAVSA_lat, RAVSA_lon = dms2dd('512829.01N 0005513.72E')
GAPGI_lat, GAPGI_lon = dms2dd('512844.89N 0004820.99E')
JACKO_lat, JACKO_lon = dms2dd('514408.65N 0012536.00E')
LCE21_lat, LCE21_lon = dms2dd('513006.82N 0012130.07E')
LCE22_lat, LCE22_lon = dms2dd('512443.87N 0012054.73E')
LCE23_lat, LCE23_lon = dms2dd('511945.28N 0011734.94E')

RT1_lat = [GODLU_lat, ELMIV_lat, LCE11_lat, LCE12_lat, LCE13_lat, RAVSA_lat, GAPGI_lat]
RT2_lat = [JACKO_lat, NONVA_lat, BABKU_lat, LCE21_lat, LCE22_lat, LCE23_lat, RAVSA_lat, GAPGI_lat]

RT1_lon = [GODLU_lon, ELMIV_lon, LCE11_lon, LCE12_lon, LCE13_lon, RAVSA_lon, GAPGI_lon]
RT2_lon = [JACKO_lon, NONVA_lon, BABKU_lon, LCE21_lon, LCE22_lon, LCE23_lon, RAVSA_lon, GAPGI_lon]

radius=0.025
rad = 'rad025'

flightsrwy = pd.read_csv('Data'
sep=' '
) 
list_col_names = ['xx','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flightsrwy.columns = list_col_names
flightsrwy = flightsrwy.drop("xx", axis='columns')
flightsrwy['time_in_final'] = flightsrwy.groupby(['flightID','endDate'])['timestamp'].transform('max')    
number_of_flights = flightsrwy['flightID'].nunique()
flightsrwy['time_to_final'] = (flightsrwy['time_in_final'] - flightsrwy['timestamp'])/60
flightsrwy['altitude_ft'] = flightsrwy['baroAltitude']*3.281/100
xx = flightsrwy.loc[(flightsrwy['flightID']=='220602SWR442')]
nflights = flightsrwy['flightID'].nunique()
print('Number of flights in original PM: ',nflights)

flights_arcs = flightsrwy.loc[((flightsrwy['altitude_ft']>=87)&(flightsrwy['altitude_ft']<=93))|((flightsrwy['altitude_ft']>=97)&(flightsrwy['altitude_ft']<=103))]
level_flights = flights_arcs.groupby('flightID').size()
df = level_flights.reset_index()
df = df.rename(columns={0:'number'})
df['group'] = df['number'].round(decimals=-1)
occur = df.groupby('group').size().idxmax()
print('The number with highest occurence (threshold): ',occur)
level_flights = level_flights.loc[(level_flights)>=occur].reset_index()
mask = flightsrwy['flightID'].isin(level_flights['flightID'])
flights_PM_level = flightsrwy[mask]
flights_non_PM = flightsrwy[~mask]
nflights_level = flights_PM_level['flightID'].nunique()
nflights_nonPM = flights_non_PM['flightID'].nunique()
print('Number of flights in filtered subset: ',nflights_level)

flights_PM_level.to_csv('VP_data.csv', sep=' ', encoding='utf-8', float_format='%.3f', index = False, header = False)

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# axes = plt.gca()
# axes.legend().set_visible(False)
xx.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='blue',lw=3)
ax.axhline(90, color="red", linestyle="--")
ax.axhline(100, color="orange", linestyle="--")
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
ax.axhline(90, color="red", linestyle="--")
ax.axhline(100, color="orange", linestyle="--")
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
circle1  = plt.Circle((GODLU_lon, GODLU_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((ELMIV_lon, ELMIV_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((NONVA_lon, NONVA_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((BABKU_lon, BABKU_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([0.75,1.5])                                                               #setting limits for axes
ax.set_ylim([51.1,51.8])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


# fig, ax = plt.subplots(figsize=(9,9))
# xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# circle1  = plt.Circle((GODLU_lon, GODLU_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle1)
# circle2  = plt.Circle((ELMIV_lon, ELMIV_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle2)
# circle3  = plt.Circle((NONVA_lon, NONVA_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle3)
# circle4  = plt.Circle((BABKU_lon, BABKU_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
# ax.add_patch(circle4)
# plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
# plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
# # axes = plt.gca()
# # axes.legend().set_visible(False)
# ax.set_xlim([0.75,1.5])                                                               #setting limits for axes
# ax.set_ylim([51.1,51.8])
# ax.set(xlabel=None)
# ax.grid()
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flights_non_PM.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((GODLU_lon, GODLU_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((ELMIV_lon, ELMIV_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((NONVA_lon, NONVA_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((BABKU_lon, BABKU_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([0.75,1.5])                                                               #setting limits for axes
ax.set_ylim([51.1,51.8])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

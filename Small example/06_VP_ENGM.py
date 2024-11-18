import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

RT7_lat = [60.761417,60.724861,60.657833,60.567194,60.466111]
RT8_lat = [60.572944,60.6685,60.739528,60.771639,60.466111]
RT7_lon = [10.977667,10.778139,10.616583,10.510444,11.084444]
RT8_lon = [10.479722,10.590667,10.760528,10.9185,11.084444]

GM404_circle_center = Point(10.256944, 59.814444)
GM405_circle_center = Point(10.1785, 60.027056)
GM406_circle_center = Point(10.180472, 59.91725)
GM407_circle_center = Point(10.211389, 60.024306)
GM408_circle_center = Point(10.213278, 59.920528)
GM409_circle_center = Point(10.285444, 59.822778)
GM410_circle_center = Point(10.41975, 59.743583)
GM411_circle_center = Point(11.704639, 59.816194)
GM412_circle_center = Point(11.427306, 59.65125)
GM413_circle_center = Point(11.595222, 59.721278)
GM414_circle_center = Point(11.67475, 59.821861)
GM415_circle_center = Point(11.569167, 59.732583)
GM416_circle_center = Point(11.217, 59.630412)
GM417_circle_center = Point(11.410528, 59.665472)
GM418_circle_center = Point(11.7955, 60.651194)
GM419_circle_center = Point(11.930556, 60.570167)
GM420_circle_center = Point(12.001583, 60.471861)
GM421_circle_center = Point(12.000083, 60.368222)
GM423_circle_center = Point(12.03375, 60.36525)
GM424_circle_center = Point(12.03525, 60.474583)
GM425_circle_center = Point(11.9595, 60.578)
GM432_circle_center = Point(RT7_lon[0],RT7_lat[0])
GM433_circle_center = Point(RT7_lon[1],RT7_lat[1])
GM434_circle_center = Point(RT7_lon[2],RT7_lat[2])
GM435_circle_center = Point(RT7_lon[3],RT7_lat[3])
GM429_circle_center = Point(RT8_lon[0],RT8_lat[0])
GM430_circle_center = Point(RT8_lon[1],RT8_lat[1])
GM431_circle_center = Point(RT8_lon[2],RT8_lat[2])
GM453_circle_center = Point(11.858472, 60.644361)
GM452_circle_center = Point(RT8_lon[3],RT8_lat[3])
GM454_circle_center = Point(11.275028, 59.619333)
GM455_circle_center = Point(10.358917, 59.748833)
RT1_lat = [60.88889,60.435667,60.281025,60.130306,60.027056,59.91725,59.814444,59.748833,59.973611]
RT2_lat = [60.323611,60.272222,60.130306,60.027056,59.91725,59.814444,59.748833,59.973611]
RT3_lat = [59.327778,59.617417,59.743583,59.822778,59.920528,60.024306,59.973611]
RT4_lat = [61.013889,60.218611,60.067756,59.924861,59.816194,59.721278,59.65125,59.619333,59.925622]
RT5_lat = [60.012711,59.983583,59.924861,59.816194,59.721278,59.65125,59.619333,59.925622]
RT6_lat = [59.183333,59.452194,59.630412,59.665472,59.732583,59.821861,59.925622]
RT7_lat = [60.93475,60.761417,60.724861,60.657833,60.567194,60.466111]
RT8_lat = [60.323611,60.397444,60.465583,60.572944,60.6685,60.739528,60.771639,60.466111]
RT9_lat = [59.327778,59.65925,59.937806,60.147325,60.32775,60.465583,60.572944,60.6685,60.739528,60.771639,60.466111]
RT10_lat = [61.013889,60.819028,60.651194,60.570167,60.471861,60.368222,60.421361]
RT11_lat = [60.012711,60.262611,60.36525,60.474583,60.578,60.644361,60.421361]
RT12_lat = [59.419694,59.9326,60.111083,60.262611,60.36525,60.474583,60.578,60.644361,60.421361]
RT1_lon = [10.473611,10.30525,10.278583,10.252833,10.1785,10.180472,10.256944,10.358917,10.802417]
RT2_lon = [9.383333,9.863889,10.252833,10.1785,10.180472,10.256944,10.358917,10.802417]
RT3_lon = [9.75,10.214361,10.41975,10.285444,10.213278,10.211389,10.802417]
RT4_lon = [12.216667,11.969722,11.853764,11.744972,11.704639,11.595222,11.427306,11.275028,11.11405]
RT5_lon =[12.392347,12.171306,11.744972,11.704639,11.595222,11.427306,11.275028,11.11405]
RT6_lon = [11.315278,11.259556,11.217,11.410528,11.569167,11.67475,11.11405]
RT7_lon = [10.831167,10.977667,10.778139,10.616583,10.510444,11.084444]
RT8_lon = [9.383333,9.926333,10.442389,10.479722,10.590667,10.760528,10.9185,11.084444]
RT9_lon = [9.75,9.935111,10.091722,10.212453,10.3175,10.442389,10.479722,10.590667,10.760528,10.9185,11.084444]
RT10_lon = [12.216667,11.989722,11.7955,11.930556,12.001583,12.000083,11.402722]
RT11_lon = [12.392347,11.954833,12.03375,12.03525,11.9595,11.858472,11.402722]
RT12_lon = [11.464278,11.792175,11.909139,11.954833,12.03375,12.03525,11.9595,11.858472,11.402722]
GM416_lat, GM416_lon = (59.630412,11.217)
GM411_lat, GM411_lon = (59.816194,11.704639)
GM405_lat, GM405_lon = (60.027056,10.1785)
GM410_lat, GM410_lon = (59.743583,10.41975)
GM423_lat, GM423_lon = (60.36525,12.03375)
GM418_lat, GM418_lon = (60.651194,11.7955)
GM429_lat, GM429_lon = (60.572944,10.479722)
GM432_lat, GM432_lon = (60.761417,10.977667)


radius=0.03
rad = 'rad03'
import os
#flightsrwy = pd.read_csv('Output', 
#header=None,
#sep=' '
#) 
PMsystem = 'SE'
if PMsystem == 'NE':
    if radius == 0.05:
        file = 'GM418_rwy19_NEW'
    elif radius == 0.03:
        file = 'GM418_GM423_rwy19'
elif PMsystem == 'NW':
    if radius == 0.05:
        file = 'GM429_GM432_rwy19'
    elif radius == 0.03:
        file = 'GM429_GM432_rwy19'
elif PMsystem == 'SW':
    if radius == 0.05:
        file = 'GM405_GM410_rwy01'
    elif radius == 0.03:
        file = 'GM405_GM410_rwy01'
else:
    if radius == 0.05:
        file = 'GM416_GM411_rwy01'
    elif radius == 0.03:
        file = 'GM416_GM411_rwy01'
       
filename = "PM_dataset_arrival_50NM_"+file+".csv"
flightsrwy = pd.read_csv(os.path.join('Output', filename), sep=' ',
    names = ['flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity', 'beginDate', 'endDate'],
    dtype={'flightID':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'baroAltitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})

#list_col_names = ['x','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
#flightsrwy.columns = list_col_names
err = ['221001NOZ4ES','221003DLH4LF','221026WIF144','221020SAS64P','221021NOZ1151','221022SAS4433','221023LBD1','221009MDT6','221016SAS4047','221015NOZ8US',
       '221024WIF9BF','221024NOZ11G','221023N900AJ','221013SAS4545','221013NOZ6MH']
   

flightsrwy = flightsrwy[~flightsrwy['flightID'].isin(err)]
flightsrwy['time_in_final'] = flightsrwy.groupby(['flightID','endDate'])['timestamp'].transform('max')    
number_of_flights = flightsrwy['flightID'].nunique()
flightsrwy['time_to_final'] = (flightsrwy['time_in_final'] - flightsrwy['timestamp'])/60
flightsrwy['altitude_ft'] = flightsrwy['baroAltitude']*3.281/100
xx = flightsrwy.loc[(flightsrwy['flightID']=='221002SAS286')]
nflights = flightsrwy['flightID'].nunique()
print('Number of flights in original PM: ',nflights)

flights_arcs = flightsrwy.loc[(flightsrwy['altitude_ft']>=48)&(flightsrwy['altitude_ft']<=113)]
level_flights = flights_arcs.groupby('flightID').size()
df = level_flights.reset_index()
df = df.rename(columns={0:'number'})
df['group'] = df['number'].round(decimals=-1)
#occur = df.groupby('group').size().idxmax()
# if occur > 300:
#     occur = 300
occur = 350
print('The number with highest occurence (threshold): ',occur)
level_flights = level_flights.loc[(level_flights)>=occur].reset_index()
mask = flightsrwy['flightID'].isin(level_flights['flightID'])
flights_PM_level = flightsrwy[mask]
nflights_level = flights_PM_level['flightID'].nunique()
print('Number of flights in filtered subset: ',nflights_level)
flights_PM_level.to_csv('Output\PM_VP_dataset_'+PMsystem+'_'+rad+'.csv', sep=' ', encoding='utf-8', float_format='%.3f', index = False, header = False)


fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# axes = plt.gca()
# axes.legend().set_visible(False)
xx.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='blue',lw=3)
ax.axhline(50, color="red", linestyle="--")
ax.axhline(110, color="orange", linestyle="--")
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
ax.axhline(50, color="red", linestyle="--")
ax.axhline(110, color="orange", linestyle="--")
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
circle1  = plt.Circle((GM416_lon, GM416_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((GM411_lon, GM411_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((GM405_lon, GM405_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((GM410_lon, GM410_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
circle5  = plt.Circle((GM423_lon, GM423_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle5)
circle6  = plt.Circle((GM418_lon, GM418_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
circle7  = plt.Circle((GM429_lon, GM429_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle7)
circle8  = plt.Circle((GM432_lon, GM432_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle8)
#plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='blue',lw=3)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black',zorder=2)
plot11 = plt.plot(RT10_lon, RT10_lat,linewidth=1.5,color = 'black',zorder=2)
plot12 = plt.plot(RT11_lon, RT11_lat,linewidth=1.5,color = 'black',zorder=2)
#plot13 = plt.plot(RT12_lon, RT12_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([10,12.2])                                                               #setting limits for axes
ax.set_ylim([59.5,60.9])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((GM416_lon, GM416_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((GM411_lon, GM411_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((GM405_lon, GM405_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((GM410_lon, GM410_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
circle5  = plt.Circle((GM423_lon, GM423_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle5)
circle6  = plt.Circle((GM418_lon, GM418_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
circle7  = plt.Circle((GM429_lon, GM429_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle7)
circle8  = plt.Circle((GM432_lon, GM432_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle8)
#plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='blue',lw=3)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black',zorder=2)
plot11 = plt.plot(RT10_lon, RT10_lat,linewidth=1.5,color = 'black',zorder=2)
plot12 = plt.plot(RT11_lon, RT11_lat,linewidth=1.5,color = 'black',zorder=2)
#plot13 = plt.plot(RT12_lon, RT12_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([10,12.2])                                                               #setting limits for axes
ax.set_ylim([59.5,60.9])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((GM416_lon, GM416_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((GM411_lon, GM411_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((GM405_lon, GM405_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((GM410_lon, GM410_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
circle5  = plt.Circle((GM423_lon, GM423_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle5)
circle6  = plt.Circle((GM418_lon, GM418_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
circle7  = plt.Circle((GM429_lon, GM429_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle7)
circle8  = plt.Circle((GM432_lon, GM432_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle8)
#plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black',zorder=2)
plot11 = plt.plot(RT10_lon, RT10_lat,linewidth=1.5,color = 'black',zorder=2)
plot12 = plt.plot(RT11_lon, RT11_lat,linewidth=1.5,color = 'black',zorder=2)
#plot13 = plt.plot(RT12_lon, RT12_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([10,12.2])                                                               #setting limits for axes
ax.set_ylim([59.5,60.9])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


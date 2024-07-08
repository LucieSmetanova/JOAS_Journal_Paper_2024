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

LI725_lat, LI725_lon = dms2dd("594341.10N 0292816.00E")
LI725_circle_center = Point(LI725_lon, LI725_lat)
LI739_lat, LI739_lon = dms2dd("600226.20N 0293900.00E")
LI739_circle_center = Point(LI739_lon, LI739_lat)
LI760_lat, LI760_lon = dms2dd("595123.50N 0310020.80E")
LI760_circle_center = Point(LI760_lon, LI760_lat)
LI766_lat, LI766_lon = dms2dd("595123.50N 0310020.80E")
LI766_circle_center = Point(LI766_lon, LI766_lat)
LI761_lat, LI761_lon = dms2dd("594531.60N 0310432.30E")
LI761_circle_center = Point(LI761_lon, LI761_lat)
LI748_lat, LI748_lon = dms2dd("593149.50N 0305225.20E")
LI748_circle_center = Point(LI748_lon, LI748_lat)
LI754_lat, LI754_lon = dms2dd("593101.00N 0310120.90E")
LI754_circle_center = Point(LI754_lon, LI754_lat)
LI749_lat, LI749_lon = dms2dd("593533.60N 0310137.70E")
LI749_circle_center = Point(LI749_lon, LI749_lat)
LI737_lat, LI737_lon = dms2dd("600248.20N 0295828.70E")
LI737_circle_center = Point(LI737_lon, LI737_lat)
LI738_lat, LI738_lon = dms2dd("600340.10N 0294510.90E")
LI738_circle_center = Point(LI738_lon, LI738_lat)
LI740_lat, LI740_lon = dms2dd("595920.10N 0293146.70E")
LI740_circle_center = Point(LI740_lon, LI740_lat)
LI741_lat, LI741_lon = dms2dd("595505.70N 0292727.00E")
LI741_circle_center = Point(LI741_lon, LI741_lat)
LI742_lat, LI742_lon = dms2dd("595020.90N 0292638.50E")
LI742_circle_center = Point(LI742_lon, LI742_lat)
LI743_lat, LI743_lon = dms2dd("594547.90N 0292926.70E")
LI743_circle_center = Point(LI743_lon, LI743_lat)
LI733_lat, LI733_lon = dms2dd("600655.70N 0293036.40E")
LI733_circle_center = Point(LI733_lon, LI733_lat)
LI732_lat, LI732_lon = dms2dd("600820.00N 0291344.60E")
LI732_circle_center = Point(LI732_lon, LI732_lat)
LI722_lat, LI722_lon = dms2dd("593245.50N 0303016.20E")
LI722_circle_center = Point(LI722_lon, LI722_lat)
LI723_lat, LI723_lon = dms2dd("593930.70N 0294454.90E")
LI723_circle_center = Point(LI723_lon, LI723_lat)
LI724_lat, LI724_lon = dms2dd("594055.10N 0293511.60E")
LI724_circle_center = Point(LI724_lon, LI724_lat)
LI730_lat, LI730_lon = dms2dd("591507.30N 0291958.20E")
LI730_circle_center = Point(LI730_lon, LI730_lat)
LI731_lat, LI731_lon = dms2dd("592555.90N 0284907.90E")
LI731_circle_center = Point(LI731_lon, LI731_lat)
LI726_lat, LI726_lon = dms2dd("595010.40N 0292327.00E")
LI726_circle_center = Point(LI726_lon, LI726_lat)
LI727_lat, LI727_lon = dms2dd("595532.30N 0292421.40E")
LI727_circle_center = Point(LI727_lon, LI727_lat)
LI728_lat, LI728_lon = dms2dd("600020.00N 0292914.70E")
LI728_circle_center = Point(LI728_lon, LI728_lat)
LI729_lat, LI729_lon = dms2dd("600350.60N 0293724.60E")
LI729_circle_center = Point(LI729_lon, LI729_lat)
LI759_lat, LI759_lon = dms2dd("595613.40N 0304712.80E")
LI759_circle_center = Point(LI759_lon, LI759_lat)
LI765_lat, LI765_lon = dms2dd("595719.50N 0314050.10E")
LI765_circle_center = Point(LI765_lon, LI765_lat)
LI762_lat, LI762_lon = dms2dd("594047.20N 0310334.40E")
LI762_circle_center = Point(LI762_lon, LI762_lat)
LI763_lat, LI763_lon = dms2dd("593634.80N 0305909.20E")
LI763_circle_center = Point(LI763_lon, LI763_lat)
LI764_lat, LI764_lon = dms2dd("593331.30N 0305156.70E")
LI764_circle_center = Point(LI764_lon, LI764_lat)
LI746_lat, LI746_lon = dms2dd("593151.40N 0302738.90E")
LI746_circle_center = Point(LI746_lon, LI746_lat)
LI747_lat, LI747_lon = dms2dd("593150.90N 0304148.90E")
LI747_circle_center = Point(LI747_lon, LI747_lat)
LI750_lat, LI750_lon = dms2dd("594018.90N 0310637.80E")
LI750_circle_center = Point(LI750_lon, LI750_lat)
LI751_lat, LI751_lon = dms2dd("594540.40N 0310743.70E")
LI751_circle_center = Point(LI751_lon, LI751_lat)
LI752_lat, LI752_lon = dms2dd("595050.70N 0310444.00E")
LI752_circle_center = Point(LI752_lon, LI752_lat)
MADID_lat, MADID_lon = dms2dd("594530.10N 0303515.00E")
MADID_circle_center = Point(MADID_lon, MADID_lat)
BIPRI_lat, BIPRI_lon = dms2dd("594452.50N 0303356.30E")
BIPRI_circle_center = Point(BIPRI_lon, BIPRI_lat)
LEPTO_lat, LEPTO_lon = dms2dd("595109.30N 0295716.80E")
LEPTO_circle_center = Point(LEPTO_lon, LEPTO_lat)
GEBKA_lat, GEBKA_lon = dms2dd("595030.40N 0295600.80E")
GEBKA_circle_center = Point(GEBKA_lon, GEBKA_lat)

RT1_lat = [LI746_lat,LI747_lat,LI748_lat,LI749_lat,LI750_lat,LI751_lat,LI752_lat,MADID_lat]
RT2_lat = [LI754_lat,LI749_lat,LI750_lat,LI751_lat,LI752_lat,MADID_lat]
RT3_lat = [LI759_lat,LI760_lat,LI761_lat,LI762_lat,LI763_lat,LI764_lat,BIPRI_lat]
RT4_lat = [LI765_lat,LI766_lat,LI761_lat,LI762_lat,LI763_lat,LI764_lat,BIPRI_lat]
RT5_lat = [LI722_lat,LI723_lat,LI724_lat,LI725_lat,LI726_lat,LI727_lat,LI728_lat,LI729_lat,LEPTO_lat]
RT6_lat = [LI730_lat,LI724_lat,LI725_lat,LI726_lat,LI727_lat,LI728_lat,LI729_lat,LEPTO_lat]
RT7_lat = [LI731_lat,LI725_lat,LI726_lat,LI727_lat,LI728_lat,LI729_lat,LEPTO_lat]
RT8_lat = [LI737_lat,LI738_lat,LI739_lat,LI740_lat,LI741_lat,LI742_lat,LI743_lat,GEBKA_lat]
RT9_lat = [LI732_lat,LI733_lat,LI739_lat,LI740_lat,LI741_lat,LI742_lat,LI743_lat,GEBKA_lat]
    
RT1_lon = [LI746_lon,LI747_lon,LI748_lon,LI749_lon,LI750_lon,LI751_lon,LI752_lon,MADID_lon]
RT2_lon = [LI754_lon,LI749_lon,LI750_lon,LI751_lon,LI752_lon,MADID_lon]
RT3_lon = [LI759_lon,LI760_lon,LI761_lon,LI762_lon,LI763_lon,LI764_lon,BIPRI_lon]
RT4_lon = [LI765_lon,LI766_lon,LI761_lon,LI762_lon,LI763_lon,LI764_lon,BIPRI_lon]
RT5_lon = [LI722_lon,LI723_lon,LI724_lon,LI725_lon,LI726_lon,LI727_lon,LI728_lon,LI729_lon,LEPTO_lon]
RT6_lon = [LI730_lon,LI724_lon,LI725_lon,LI726_lon,LI727_lon,LI728_lon,LI729_lon,LEPTO_lon]
RT7_lon = [LI731_lon,LI725_lon,LI726_lon,LI727_lon,LI728_lon,LI729_lon,LEPTO_lon]
RT8_lon = [LI737_lon,LI738_lon,LI739_lon,LI740_lon,LI741_lon,LI742_lon,LI743_lon,GEBKA_lon]
RT9_lon = [LI732_lon,LI733_lon,LI739_lon,LI740_lon,LI741_lon,LI742_lon,LI743_lon,GEBKA_lon]

radius=0.025
rad = 'rad025'
PMsys = 'SW'

flightsrwy = pd.read_csv('PM_dataset_'+PMsys+'_'+rad+'.csv', 
header=None,
sep=' '
) 
list_col_names = ['x','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flightsrwy.columns = list_col_names
err = ['220813SDM6442','220810SDM6002', '220825SDM6402', '220825SDM6452', '220825SDM6574','220801SDM6462', '220811PBD530', '220812PBD536', '220825SDM6332',
       '220824SDM6002', '220825NWS594', '220825PBD592','220806AFL032', '220806SDM6024', '220806SDM6066', '220806UZB631',
              '220808SDM6014', '220810AFL058', '220813VDA6474','220806SVR124','220802SDM6036','220806GZP835','220801AFL018', '220801AUL532', '220801PBD508', '220806SDM6596',
                     '220808SDM6324', '220810SVR8642', '220814SDM6596', '220818PBD560',
                     '220820AFL028', '220825KAR317', '220826PBD314', '220826PBD560',
                     '220826SDM6596','220812UPEM020','220801UZB637','220821SDM6116','220824SBI1015']
flightsrwy = flightsrwy[~flightsrwy['flightID'].isin(err)]
flightsrwy = flightsrwy.drop("x", axis='columns')
flightsrwy['time_in_final'] = flightsrwy.groupby(['flightID','endDate'])['timestamp'].transform('max')    
number_of_flights = flightsrwy['flightID'].nunique()
flightsrwy['time_to_final'] = (flightsrwy['time_in_final'] - flightsrwy['timestamp'])/60
flightsrwy['altitude_ft'] = flightsrwy['baroAltitude']*3.281/100
xx = flightsrwy.loc[(flightsrwy['flightID']=='220801SVR059')]
nflights = flightsrwy['flightID'].nunique()
print('Number of flights in original PM: ',nflights)

flights_arcs = flightsrwy.loc[((flightsrwy['altitude_ft']>=47)&(flightsrwy['altitude_ft']<=53))|((flightsrwy['altitude_ft']>=57)&(flightsrwy['altitude_ft']<=63))]
level_flights = flights_arcs.groupby('flightID').size()
df = level_flights.reset_index()
df = df.rename(columns={0:'number'})
df['group'] = df['number'].round(decimals=-1)
occur = df.groupby('group').size().idxmax()
#occur = 60
print('The number with highest occurence (threshold): ',occur)
level_flights = level_flights.loc[(level_flights)>=occur].reset_index()
mask = flightsrwy['flightID'].isin(level_flights['flightID'])
flights_PM_level = flightsrwy[mask]
nflights_level = flights_PM_level['flightID'].nunique()
print('Number of flights in filtered subset: ',nflights_level)
flights_PM_level.to_csv('VP_PM_Data.csv', sep=' ', encoding='utf-8', float_format='%.3f', index = False, header = False)


fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# axes = plt.gca()
# axes.legend().set_visible(False)
xx.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='blue',lw=3)
ax.axhline(50, color="red", linestyle="--")
ax.axhline(60, color="orange", linestyle="--")
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
ax.axhline(60, color="orange", linestyle="--")
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
circle1  = plt.Circle((LI739_lon,LI739_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((LI725_lon,LI725_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((LI760_lon,LI760_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((LI761_lon,LI761_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
circle5  = plt.Circle((LI748_lon,LI748_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle5)
circle6  = plt.Circle((LI749_lon,LI749_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([29.3,31.3])                                                               #setting limits for axes
ax.set_ylim([59.3,60.3])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((LI739_lon,LI739_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((LI725_lon,LI725_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((LI760_lon,LI760_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((LI761_lon,LI761_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
circle5  = plt.Circle((LI748_lon,LI748_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle5)
circle6  = plt.Circle((LI749_lon,LI749_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([29.3,31.3])                                                               #setting limits for axes
ax.set_ylim([59.3,60.3])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((LI739_lon,LI739_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((LI725_lon,LI725_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((LI760_lon,LI760_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((LI761_lon,LI761_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
circle5  = plt.Circle((LI748_lon,LI748_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle5)
circle6  = plt.Circle((LI749_lon,LI749_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([29.3,31.3])                                                               #setting limits for axes
ax.set_ylim([59.3,60.3])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


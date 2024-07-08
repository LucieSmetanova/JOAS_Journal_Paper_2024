import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def dms2dd(as_string):
    degrees = int(as_string[:2])
    minutes = int(as_string[2:4])
    seconds = float(as_string[4:8])
    lat_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    degrees = -1*int(as_string[10:14])
    minutes = -1*int(as_string[14:16])
    seconds = -1*float(as_string[16:21])
    lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)

    return lat_dd, lon_dd

BO804_lat, BO804_lon = dms2dd('052506.00N 0740630.00W')
PAPET_lat, PAPET_lon = dms2dd('051359.10N 0741904.78W')
SUR01_lat, SUR01_lon = dms2dd('051440.07N 0742743.85W')
SUR02_lat, SUR02_lon = dms2dd('051137.19N 0743551.51W')
SUR03_lat, SUR03_lon = dms2dd('050449.17N 0744217.59W')
TOBKI_lat, TOBKI_lon = dms2dd('045630.78N 0744454.16W')
BO885_lat, BO885_lon = dms2dd('045527.75N 0743254.72W')
AMVES_lat, AMVES_lon = dms2dd('045445.99N 0742456.45W')
BO824_lat, BO824_lon = dms2dd('052019.62N 0740034.24W')
BO832_lat, BO832_lon = dms2dd('050702.01N 0735743.14W')
GERBA_lat, GERBA_lon = dms2dd('042611.64N 0745000.76W')
IRUPU_lat, IRUPU_lon = dms2dd("044607.05N 0744723.02W")
BO862_lat, BO862_lon = dms2dd("043623.25N 0750454.62W")
BO886_lat, BO886_lon = dms2dd("045016.82N 0750659.00W")
MQU_lat, MQU_lon = dms2dd("051218.00N 0745516.00W")
NOR02_lat, NOR02_lon = dms2dd("050649.75N 0744545.88W")
BO950_lat, BO950_lon = dms2dd("052457.91N 0741913.77W")
NOR01_lat, NOR01_lon = dms2dd('045651.67N 0744853.72W')
NOR02_lat, NOR02_lon = dms2dd('050649.75N 0744545.88W')
NOR03_lat, NOR03_lon = dms2dd('051459.40N 0743802.59W')
NOR04_lat, NOR04_lon = dms2dd('051838.89N 0742817.35W')
NOR05_lat, NOR05_lon = dms2dd('051749.71N 0741754.40W')
PULDI_lat, PULDI_lon = dms2dd('050227.24N 0742235.82W')
BO884_lat, BO884_lon = dms2dd('050934.60N 0745028.86W')
EDPUL_lat, EDPUL_lon = dms2dd('051655.00N 0751114.00W')
FLOTE_lat, FLOTE_lon = dms2dd('052258.47N 0745947.41W')
BO935_lat, BO935_lon = dms2dd('054005.96N 0743225.58W')

RT1_lat = [BO804_lat,PAPET_lat,SUR01_lat,SUR02_lat,SUR03_lat,TOBKI_lat,BO885_lat,AMVES_lat]
RT2_lat = [BO824_lat,PAPET_lat,SUR01_lat,SUR02_lat,SUR03_lat,TOBKI_lat,BO885_lat,AMVES_lat]
RT3_lat = [BO832_lat,PAPET_lat,SUR01_lat,SUR02_lat,SUR03_lat,TOBKI_lat,BO885_lat,AMVES_lat]
RT4_lat = [GERBA_lat,IRUPU_lat,NOR01_lat,NOR02_lat,NOR03_lat,NOR04_lat,NOR05_lat,PULDI_lat,AMVES_lat]
RT5_lat = [BO862_lat,IRUPU_lat,NOR01_lat,NOR02_lat,NOR03_lat,NOR04_lat,NOR05_lat,PULDI_lat,AMVES_lat]
RT6_lat = [BO886_lat,IRUPU_lat,NOR01_lat,NOR02_lat,NOR03_lat,NOR04_lat,NOR05_lat,PULDI_lat,AMVES_lat]
RT7_lat = [MQU_lat,BO884_lat,NOR02_lat,NOR03_lat,NOR04_lat,NOR05_lat,PULDI_lat,AMVES_lat]
RT8_lat = [BO804_lat,PAPET_lat,SUR01_lat,SUR02_lat,SUR03_lat,TOBKI_lat,BO885_lat,AMVES_lat]
RT8_lat = [BO935_lat,BO950_lat,PAPET_lat,SUR01_lat,SUR02_lat,SUR03_lat,TOBKI_lat,BO885_lat,AMVES_lat]

RT1_lon = [BO804_lon,PAPET_lon,SUR01_lon,SUR02_lon,SUR03_lon,TOBKI_lon,BO885_lon,AMVES_lon]
RT2_lon = [BO824_lon,PAPET_lon,SUR01_lon,SUR02_lon,SUR03_lon,TOBKI_lon,BO885_lon,AMVES_lon]
RT3_lon = [BO832_lon,PAPET_lon,SUR01_lon,SUR02_lon,SUR03_lon,TOBKI_lon,BO885_lon,AMVES_lon]
RT4_lon = [GERBA_lon,IRUPU_lon,NOR01_lon,NOR02_lon,NOR03_lon,NOR04_lon,NOR05_lon,PULDI_lon,AMVES_lon]
RT5_lon = [BO862_lon,IRUPU_lon,NOR01_lon,NOR02_lon,NOR03_lon,NOR04_lon,NOR05_lon,PULDI_lon,AMVES_lon]
RT6_lon = [BO886_lon,IRUPU_lon,NOR01_lon,NOR02_lon,NOR03_lon,NOR04_lon,NOR05_lon,PULDI_lon,AMVES_lon]
RT7_lon = [MQU_lon,BO884_lon,NOR02_lon,NOR03_lon,NOR04_lon,NOR05_lon,PULDI_lon,AMVES_lon]
RT8_lon = [BO804_lon,PAPET_lon,SUR01_lon,SUR02_lon,SUR03_lon,TOBKI_lon,BO885_lon,AMVES_lon]
RT8_lon = [BO935_lon,BO950_lon,PAPET_lon,SUR01_lon,SUR02_lon,SUR03_lon,TOBKI_lon,BO885_lon,AMVES_lon]


radius=0.06
rad = 'rad06'

flightsrwy = pd.read_csv('PM_dataset_'+rad+'.csv', 
header=None,
sep=' '
) 
list_col_names = ['x','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flightsrwy.columns = list_col_names
   


err = ['221201AVA253', '221201AVA4873', '221201AVA8487', '221201AVA8591',
       '221201AVA9457', '221201HK4558', '221201RPB7005', '221202AVA079',
       '221202AVA129', '221202AVA4864', '221202RPB7025', '221202TPA4001',
       '221202VVC470', '221203AVA129', '221203RPB7027', '221203VVC5851',
       '221204AVA253', '221204AVA5207', '221204AVA9723', '221204EFY8995',
       '221205AVA129', '221205AVA9457', '221205AVA9471', '221205RPB7027',
       '221206ACL1161', '221206ACL865', '221206AVA093', '221206AVA253',
       '221206AVA9551', '221207ARE4064', '221207ARE4257', '221207NSE8659',
       '221207NSE8887', '221207RPB7081', '221207TPA4001', '221208ACL1153',
       '221208EFY9035', '221209RPB7029', '221210AVA053', '221210AVA093',
       '221210FAC5727', '221210RPB7412', '221211AVA4876', '221211ULS5111',
       '221212AVA121', '221212AVA251', '221212EFY8995', '221212IBE6587',
       '221213AVA8584', '221213EFY9039', '221214AVA079', '221214AVA209',
       '221214AVA9473', '221216AVA007', '221216AVA037', '221216AVA050',
       '221216AVA079', '221216AVA8527', '221218AVA195', '221219AVA9467',
       '221220ACL864', '221221ACL1167', '221221AVA8584', '221221NSE8887',
       '221221UAL268', '221222RPB7081', '221222ULS5147', '221223AVA9399',
       '221223EFY8995', '221224VVC8325', '221225ACA094', '221225ARE4129',
       '221225RPB7027', '221226RPB7410', '221228ACL1161', '221228AVA8418',
       '221228IBE6585', '221228LAN580', '221228LPE2386', '221228RPB7410','221201ARE4323', '221201AVA253', '221201AVA4873', '221201AVA4888',
              '221201AVA9228', '221201AVA9806', '221201RPB7005', '221202AVA079',
              '221202AVA129', '221202AVA9544', '221202AVA9806', '221202AVA9842',
              '221202RPB7025', '221202VVC5913', '221203AVA129', '221203AVA8510',
              '221203AVA9818', '221203EFY8995', '221203EFY9039', '221203EFY9169',
              '221203RPB7027', '221204AVA253', '221204AVA9842', '221204EFY8995',
              '221204EFY9035', '221204ULS5133', '221205AVA129', '221205AVA8434',
              '221205AVA9471', '221205RPB7027', '221206ACL1161', '221206ACL865',
              '221206AVA093', '221206AVA253', '221206AVA4876', '221206AVA5202',
              '221207ARE4064', '221207ARE4072', '221207AVA8466', '221207AVA8560',
              '221207NSE8659', '221207NSE8887', '221207RPB7081', '221207VVC5909',
              '221207VVC5911', '221208ACL1153', '221208ARE4052', '221208ARE4068',
              '221208ARE4257', '221208EFY9035', '221209ARE4054', '221209AVA4866',
              '221209AVA5202', '221209AVA9202', '221209AVA9218', '221209VVC5796',
              '221209VVC5913', '221210AVA093', '221210AVA4866', '221210AVA9218',
              '221210NSE8721', '221211AVA4876', '221211AVA9208', '221211AVA9218',
              '221211AVA9712', '221211AVA9836', '221211ULS5133', '221212AVA9212',
              '221212AVA9228', '221212AVA9722', '221212EFY8995', '221212EFY8997',
              '221212ULS5131', '221213AVA8414', '221213AVA8512', '221213AVA8584',
              '221213AVA9208', '221213AVA9218', '221213EFY9039', '221213EFY9167',
              '221214ARE4074', '221214ARE4211', '221214ARE4255', '221214AVA079',
              '221214AVA209', '221214AVA5200', '221214AVA8560', '221214AVA8561',
              '221214AVA9206', '221215AVA9818', '221215KRE147', '221216AVA037',
              '221216AVA050', '221216AVA079', '221216AVA8408', '221216AVA8422',
              '221216RPB7243', '221216ULS5133', '221216VVC5917', '221217AVA8408',
              '221217AVA9836', '221218AVA4864', '221218AVA9812', '221219ARE4052',
              '221219AVA8510', '221220ACL864', '221220VVC5909', '221221ARE4070',
              '221221AVA8584', '221221AVA9210', '221221AVA9544', '221221AVA9812',
              '221221NSE8887', '221222EFY9039', '221222RPB7081', '221223ARE4050',
              '221223ARE4074', '221223ARE4211', '221223AVA9208', '221223AVA9374',
              '221223AVA9399', '221223EFY8995', '221223RPB7243', '221224AVA8418',
              '221225AVA8560', '221225AVA8561', '221225RPB7027', '221227AVA4864',
              '221228ACL1161', '221228ARE4052', '221228AVA9836', '221228LAN580',
              '221228RPB7243', '221228VVC5618']
flightsrwy = flightsrwy[~flightsrwy['flightID'].isin(err)]
flightsrwy = flightsrwy.drop("x", axis='columns')
flightsrwy.drop(flightsrwy[flightsrwy['lat'] == 0].index, inplace = True)
# flightsrwy.drop(flightsrwy[flightsrwy['lat'] < 3.5].index, inplace = True)
# flightsrwy.drop(flightsrwy[flightsrwy['lat'] > 8].index, inplace = True)
# flightsrwy.drop(flightsrwy[flightsrwy['lon'] < -75.8].index, inplace = True)
# flightsrwy.drop(flightsrwy[flightsrwy['lon'] > -73].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['lon'] == 0].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['rawAltitude'] == 0].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['rawAltitude'] > 18000].index, inplace = True)

flightsrwy['time_in_final'] = flightsrwy.groupby(['flightID','endDate'])['timestamp'].transform('max')    
number_of_flights = flightsrwy['flightID'].nunique()
flightsrwy['time_to_final'] = (flightsrwy['time_in_final'] - flightsrwy['timestamp'])/60
flightsrwy['altitude_ft'] = flightsrwy['rawAltitude']*3.281/100
#flightsrwy['altitude_ft']=flightsrwy['baroAltitude']
xx = flightsrwy.loc[(flightsrwy['flightID']=='221201AAL1123')]
flightsrwy = flightsrwy.sort_values(by=['flightID','timestamp'])
nflights = flightsrwy['flightID'].nunique()
print('Number of flights in original PM: ',nflights)

flights_arcs = flightsrwy.loc[(flightsrwy['altitude_ft']>=168)&(flightsrwy['altitude_ft']<=182)]
level_flights = flights_arcs.groupby('flightID').size()
df = level_flights.reset_index()
df = df.rename(columns={0:'number'})
df['group'] = df['number'].round(decimals=-1)
occur = df.groupby('group').size().idxmax()
# if occur > 300:
#     occur = 300
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
ax.axhline(170, color="red", linestyle="--")
ax.axhline(180, color="orange", linestyle="--")
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
ax.axhline(170, color="red", linestyle="--")
ax.axhline(180, color="orange", linestyle="--")
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
circle1  = plt.Circle((PAPET_lon, PAPET_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle6  = plt.Circle((NOR02_lon, NOR02_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
circle7  = plt.Circle((IRUPU_lon, IRUPU_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle7)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([-75.1,-73.75])                                                               #setting limits for axes
ax.set_ylim([4.4,5.6])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((PAPET_lon, PAPET_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle6  = plt.Circle((NOR02_lon, NOR02_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
circle7  = plt.Circle((IRUPU_lon, IRUPU_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle7)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([-75.1,-73.75])                                                               #setting limits for axes
ax.set_ylim([4.4,5.6])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((PAPET_lon, PAPET_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle6  = plt.Circle((NOR02_lon, NOR02_lat), radius, color='b',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
circle7  = plt.Circle((IRUPU_lon, IRUPU_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle7)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([-75.1,-73.75])                                                               #setting limits for axes
ax.set_ylim([4.4,5.6])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


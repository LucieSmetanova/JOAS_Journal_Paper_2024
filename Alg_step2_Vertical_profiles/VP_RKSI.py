import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def dms2dd(as_string):
    degrees = int(as_string[:2])
    minutes = int(as_string[2:4])
    seconds = float(as_string[4:8])
    lat_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    degrees = int(as_string[10:14])
    minutes = int(as_string[14:16])
    seconds = float(as_string[16:21])
    lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)

    return lat_dd, lon_dd

PY049_lat, PY049_lon = dms2dd("370817.90N 1254804.60E")
PY049_circle_center = Point(PY049_lon, PY049_lat)
PY037_lat, PY037_lon = dms2dd("370828.10N 1260325.20E")
PY037_circle_center = Point(PY037_lon, PY037_lat)
CW001_lat, CW001_lon = dms2dd("371047.30N 1262003.60E")
CW001_circle_center = Point(CW001_lon, CW001_lat)
CW002_lat, CW002_lon = dms2dd("370652.40N 1262107.40E")
CW002_circle_center = Point(CW002_lon, CW002_lat)
CW003_lat, CW003_lon = dms2dd("370336.40N 1262400.80E")
CW003_circle_center = Point(CW003_lon, CW003_lat)
CW004_lat, CW004_lon = dms2dd("370130.30N 1262816.00E")
CW004_circle_center = Point(CW004_lon, CW004_lat)
CW005_lat, CW005_lon = dms2dd("370054.30N 1263312.30E")
CW005_circle_center = Point(CW005_lon, CW005_lat)
PAMBI_lat, PAMBI_lon = dms2dd("371054.30N 1263234.40E")
PAMBI_circle_center = Point(PAMBI_lon, PAMBI_lat)
NODUN_lat, NODUN_lon = dms2dd("371110.10N 1272025.50E")
NODUN_circle_center = Point(NODUN_lon, NODUN_lat)
UPSOM_lat, UPSOM_lon = dms2dd("372838.80N 1271904.30E")
UPSOM_circle_center = Point(UPSOM_lat, UPSOM_lon)
GUDKO_lat, GUDKO_lon = dms2dd("370110.90N 1273822.90E")
GUDKO_circle_center = Point(GUDKO_lon, GUDKO_lat)
GC072_lat, GC072_lon = dms2dd("372001.00N 1272512.20E")
GC072_circle_center = Point(GC072_lon, GC072_lat)
GC071_lat, GC071_lon = dms2dd("372938.50N 1272513.70E")
GC071_circle_center = Point(GC071_lon, GC071_lat)
SEL_lat, SEL_lon = dms2dd("372449.00N 1265542.10E")
SEL_circle_center = Point(SEL_lon, SEL_lat)
KARBU_lat, KARBU_lon = dms2dd("373159.00N 1273952.00E")
KARBU_circle_center = Point(KARBU_lon, KARBU_lat)
KC067_lat, KC067_lon = dms2dd("372101.50N 1271903.70E")
KC067_circle_center = Point(KC067_lon, KC067_lat)
KC066_lat, KC066_lon = dms2dd("371401.20N 1271518.80E")
KC066_circle_center = Point(KC066_lon, KC066_lat)
ANYANG_lat, ANYANG_lon = dms2dd("372449.00N 1265542.00E")
ANYANG_circle_center = Point(ANYANG_lat, ANYANG_lon)

RT1_lat = [PY049_lat,PY037_lat,CW001_lat,CW002_lat,CW003_lat,CW004_lat,CW005_lat,PAMBI_lat]
RT2_lat = [GUDKO_lat,NODUN_lat,GC072_lat,GC071_lat,UPSOM_lat,SEL_lat]
RT3_lat = [KARBU_lat,GC071_lat,UPSOM_lat,KC067_lat,KC066_lat,SEL_lat]

RT1_lon = [PY049_lon,PY037_lon,CW001_lon,CW002_lon,CW003_lon,CW004_lon,CW005_lon,PAMBI_lon]
RT2_lon = [GUDKO_lon,NODUN_lon,GC072_lon,GC071_lon,UPSOM_lon,SEL_lon]
RT3_lon = [KARBU_lon,GC071_lon,UPSOM_lon,KC067_lon,KC066_lon,SEL_lon]

radius=0.03
rad = 'rad03'

flightsrwy = pd.read_csv('PM_Data'.csv', 
header=None,
sep=' '
) 
list_col_names = ['x','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flightsrwy.columns = list_col_names
flightsrwy = flightsrwy.drop("x", axis='columns')   
err = ['221202TWB172', '221201ASV528', '221202JJA2206', '221203KAL320',
       '221215KAL630', '221222AAR7139','221202AAR736', '221202AAR740', '221202AAR762', '221202CES7041',
              '221202HVN408', '221202JJA2904', '221202JNA052', '221202KAL314',
              '221202KAL628', '221202KAL690', '221202PAL468', '221202SWM215',
              '221202VJC960', '221201AAR740', '221201AAR742', '221201BAV450',
              '221201JJA2204', '221201KAL630', '221202AAR390', '221202AAR704',
              '221202AAR970', '221202AFR193', '221202AIH512', '221202APG884',
              '221202APG9048', '221202BOX571', '221202CEB188', '221202CPA410',
              '221202FDX6076', '221202HVN430', '221202JJA4908', '221202KAL320',
              '221202KAL375', '221202KAL624', '221202KAL646', '221202KAL660',
              '221202KAL696', '221202KAL756', '221202KAL8442', '221202KLM832',
              '221202TGW842', '221202TGW896', '221202VJC836', '221202VJC838',
              '221202VJC878', '221202VJC880', '221202VJC962', '221202VJC974',
              '221202WGN5274', '221203AAR7149', '221203AIC312', '221203AIH512',
              '221203APG884', '221203APZ632', '221203KAL362', '221203KAL8186',
              '221203TAX700', '221201TWB102', '221202LAO923', '221208ABL748',
              '221208BAV450', '221208CEB186', '221208HVN430', '221208HVN440',
              '221208JJA2508', '221208KAL178', '221208AAR392', '221208AAR734',
              '221208AAR988', '221208ABL788', '221208ASV512', '221208BOX571',
              '221208CKK257', '221208GTI555', '221208HVN408', '221208JNA026',
              '221208KAL180', '221208KAL316', '221208KAL624', '221208KAL652',
              '221208KAL664', '221208KAL672', '221208KAL690', '221208LAO923',
              '221208JJA4206', '221208JJA4908', '221208JNA018', '221208KAL644',
              '221215AIH2426', '221215APG884', '221215APZ632', '221215CES7041',
              '221215CPA410', '221215CRK628', '221215DAL288', '221215HKE630',
              '221215JJA2206', '221215JJA4908', '221215JJA9206', '221215JNA942F',
              '221215KAL186', '221215KAL478', '221215KAL756', '221215PAC238D','221201JJA1402', '221208KAL615','221202AAR602', '221201AAR105', '221201AAR1115', '221201AAR113',
                     '221201AAR241', '221201AAR271', '221201AAR754', '221201ABL163',
                     '221201ABL171', '221201AIH3114', '221201ANA8475', '221201ANZ75',
                     '221201ASV714', '221201CPA035', '221201DAL159', '221201FDX5101',
                     '221201GTI4545', '221201GTI8529', '221201JJA1103', '221201JJA1107',
                     '221201JJA1403', '221201JJA1601', '221201JJA3101', '221201JJA3405',
                     '221201JNA062', '221201JNA206', '221201JNA222', '221201JNA224',
                     '221201KAL036', '221201KAL038', '221201KAL074', '221201KAL094',
                     '221201KAL1492', '221201KAL422', '221201KAL552', '221201KAL672',
                     '221201MAA3935', '221201PAC213', '221201TWB216', '221201TWB252',
                     '221201TWB296', '221201TWB302', '221201TWB308', '221202AAL281',
                     '221202AAR247', '221202ACA063', '221202ANA8475', '221202ASV724',
                     '221202DAL159', '221202DAL171', '221202JJA1301', '221202JJA1401',
                     '221202JJA1961', '221202KAL024', '221202KAL054', '221202KAL072',
                     '221202KAL1420', '221202KAL270', '221202KAL278', '221202KAL742',
                     '221202KAL792', '221202TWB212', '221202TWB216', '221202TWB292',
                     '221202TWB296', '221203AAR111', '221203AAR131', '221203AAR135',
                     '221203AAR191', '221203ABL155', '221203ABL165', '221203APJ0011',
                     '221203ASV712', '221203ASV724', '221203CKS656', '221203CKS812',
                     '221203CPA035', '221203FDX5432', '221203GEC8385', '221203JJA1171',
                     '221203JJA1301', '221203JJA1401', '221203JJA3105', '221203JNA024',
                     '221203JNA026', '221203JNA202', '221203JNA226', '221203KAL1420',
                     '221203KAL422', '221203KAL552', '221203KAL554', '221203KAL558',
                     '221203KAL628', '221203KAL644', '221203KAL726', '221203KLM862',
                     '221203PAC787', '221203PAL494', '221203TWB214', '221203TWB292',
                     '221203TWB302', '221202AAR105', '221202JJA1403', '221208AAL281',
                     '221208AAR111', '221208AAR221', '221208AAR231', '221208AAR271',
                     '221208AAR602', '221208ABL155', '221208ABL171', '221208ABL173',
                     '221208ACA063', '221208ANZ75', '221208APJ0005', '221208ASV702',
                     '221208ASV714', '221208CKS816', '221208CKS838', '221208DAL159',
                     '221208DAL171', '221208DAL197', '221208FDX5101', '221208FDX5154',
                     '221208FDX5434', '221208JJA1105', '221208JJA1171', '221208JJA1301',
                     '221208JJA1303', '221208JJA1601', '221208JNA202', '221208JNA224',
                     '221208JNA234', '221208JNA282', '221208JNA644', '221208KAL018',
                     '221208KAL024', '221208KAL038', '221208KAL054', '221208KAL074',
                     '221208KAL082', '221208KAL092', '221208KAL094', '221208KAL402',
                     '221208KAL704', '221208KAL724', '221208KAL726', '221208KAL766',
                     '221208KAL8312', '221208AAR181', '221208JJA9103', '221208PAC785',
                     '221215AAL281', '221215AAR101', '221215AAR231', '221215AAR271',
                     '221215AAR602', '221215AAR704', '221215AAR762', '221215ACA061',
                     '221215ANA8475', '221215ANZ75', '221215APZ102', '221215ASV702',
                     '221215ASV724', '221215CPA035', '221215DAL159', '221215GEC8405',
                     '221215GTI523A', '221215JJA1103', '221215JJA1405', '221215JJA1601',
                     '221215JJA1901', '221215JJA1971', '221215JJA2508', '221215JJA3105',
                     '221215JJA3405', '221215JNA206', '221215JNA214', '221215JNA224',
                     '221215JNA226', '221215JNA246', '221215KAL036', '221215KAL042',
                     '221215KAL072', '221215KAL074', '221215KAL082', '221215KAL1420',
                     '221215KAL252', '221215KAL262', '221215KAL280', '221215KAL558',
                     '221215KAL616', '221215KAL628', '221215KAL634', '221215KAL704',
                     '221215KAL706', '221215KAL726', '221215KAL728', '221215KAL742',
                     '221215KAL766', '221215KAL792', '221215KLM862', '221215MAS066',
                     '221215PAC213', '221215PAC213D', '221222AAL281', '221222AAR131',
                     '221222AAR201', '221222AAR221', '221222AAR231', '221222AAR243',
                     '221222AAR754', '221222AAR762', '221222ABL163', '221222ACA027',
                     '221222ANZ75', '221222APJ0005', '221222APJ0809', '221222ASV714',
                     '221222ASV724', '221222ASV728','221203JNA232','221201TWB284','221202KAL626']
flightsrwy = flightsrwy[~flightsrwy['flightID'].isin(err)]

flightsrwy['time_in_final'] = flightsrwy.groupby(['flightID','endDate'])['timestamp'].transform('max')    
number_of_flights = flightsrwy['flightID'].nunique()
flightsrwy['time_to_final'] = (flightsrwy['time_in_final'] - flightsrwy['timestamp'])/60
flightsrwy['altitude_ft'] = flightsrwy['rawAltitude']*3.281/100
xx = flightsrwy.loc[(flightsrwy['flightID']=='220801SVR059')]
nflights = flightsrwy['flightID'].nunique()
print('Number of flights in original PM: ',nflights)

flights_arcs = flightsrwy.loc[(flightsrwy['altitude_ft']>=128)&(flightsrwy['altitude_ft']<=183)]
level_flights = flights_arcs.groupby('flightID').size()
df = level_flights.reset_index()
df = df.rename(columns={0:'number'})
df['group'] = df['number'].round(decimals=-1)
occur = df.groupby('group').size().idxmax()
if occur > 300:
    occur = 300
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
circle1  = plt.Circle((NODUN_lon,NODUN_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((ANYANG_lon,ANYANG_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((UPSOM_lon,UPSOM_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((CW001_lon,CW001_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([126.86,127.45])                                                               #setting limits for axes
ax.set_ylim([37.05,37.63])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((NODUN_lon,NODUN_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((ANYANG_lon,ANYANG_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((UPSOM_lon,UPSOM_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((CW001_lon,CW001_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([126.86,127.45])                                                               #setting limits for axes
ax.set_ylim([37.05,37.63])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((NODUN_lon,NODUN_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((ANYANG_lon,ANYANG_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((UPSOM_lon,UPSOM_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((CW001_lon,CW001_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([126.86,127.45])                                                               #setting limits for axes
ax.set_ylim([37.05,37.63])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


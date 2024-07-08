import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def dms2dd(as_string):
    degrees = int(as_string[:2])
    minutes = int(as_string[2:4])
    seconds = float(as_string[4:9])
    lat_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    degrees = -1*int(as_string[10:14])
    minutes = -1*int(as_string[14:16])
    seconds = -1*float(as_string[16:21])
    lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)

    return lat_dd, lon_dd

EKREN_lat, EKREN_lon = dms2dd('533843.00N 0054553.10W')
ELBON_lat, ELBON_lon = dms2dd('533534.10N 0060921.60W')
ASDER_lat, ASDER_lon = dms2dd('533346.70N 0062226.40W')
AKIVA_lat, AKIVA_lon = dms2dd('533856.00N 0062709.60W')
ADNAL_lat, ADNAL_lon = dms2dd('534153.90N 0063541.50W')
ADNAL_circle_center = Point(ADNAL_lon, ADNAL_lat)
APRUT_lat, APRUT_lon = dms2dd('534149.00N 0064534.90W')
DW865_lat, DW865_lon = dms2dd('533842.80N 0065358.40W')
DW866_lat, DW866_lon = dms2dd('533329.10N 0065827.20W')
IFBAP_lat, IFBAP_lon = dms2dd('533230.80N 0064006.20W')
BAMLI_lat, BAMLI_lon = dms2dd('540828.50N 0063904.00W')
EPIDU_lat, EPIDU_lon = dms2dd('534903.50N 0063554.80W')
OLAPO_lat, OLAPO_lon = dms2dd('534649.00N 0071740.60W')
RUBAR_lat, RUBAR_lon = dms2dd('530808.90N 0054805.40W')
DETAX_lat, DETAX_lon = dms2dd('531430.70N 0061235.60W')
BERMO_lat, BERMO_lon = dms2dd('531738.90N 0062450.80W')
BABON_lat, BABON_lon = dms2dd('531303.30N 0063056.50W')
BABON_circle_center = Point(BABON_lon, BABON_lat)
BIVDI_lat, BIVDI_lon = dms2dd('531059.50N 0064005.60W')
DW754_lat, DW754_lon = dms2dd('531202.30N 0064942.60W')
DW755_lat, DW755_lon = dms2dd('531554.20N 0065704.50W')
OSLEX_lat, OSLEX_lon = dms2dd('532155.80N 0064144.50W')
SUTEX_lat, SUTEX_lon = dms2dd('524927.70N 0065549.30W')
DIRUM_lat, DIRUM_lon = dms2dd('530009.70N 0063940.00W')
KANUS_lat, KANUS_lon = dms2dd('530630.50N 0062652.10W')
BUNED_lat, BUNED_lon = dms2dd('523721.90N 0063748.20W')
OSGAR_lat, OSGAR_lon = dms2dd('530257.90N 0071612.80W')
ASDER_lat, ASDER_lon = dms2dd("533346.70N 0062226.40W")
ASDER_circle_center = Point(ASDER_lon, ASDER_lat)
BERMO_lat, BERMO_lon = dms2dd("531738.90N 0062450.80W")
BERMO_circle_center = Point(BERMO_lon, BERMO_lat)

RT1_lat = [EKREN_lat,ELBON_lat,ASDER_lat,AKIVA_lat,ADNAL_lat,APRUT_lat,DW865_lat,DW866_lat,IFBAP_lat]
RT2_lat = [BAMLI_lat,EPIDU_lat,ADNAL_lat,APRUT_lat,DW865_lat,DW866_lat,IFBAP_lat]
RT3_lat = [OLAPO_lat,EPIDU_lat,ADNAL_lat,APRUT_lat,DW865_lat,DW866_lat,IFBAP_lat]
RT4_lat = [RUBAR_lat,DETAX_lat,BERMO_lat,BABON_lat,BIVDI_lat,DW754_lat,DW755_lat,OSLEX_lat]
RT5_lat = [BUNED_lat,DIRUM_lat,KANUS_lat,BABON_lat,BIVDI_lat,DW754_lat,DW755_lat,OSLEX_lat]
RT6_lat = [SUTEX_lat,DIRUM_lat,KANUS_lat,BABON_lat,BIVDI_lat,DW754_lat,DW755_lat,OSLEX_lat]
RT7_lat = [OSGAR_lat,DIRUM_lat,KANUS_lat,BABON_lat,BIVDI_lat,DW754_lat,DW755_lat,OSLEX_lat]

RT1_lon = [EKREN_lon,ELBON_lon,ASDER_lon,AKIVA_lon,ADNAL_lon,APRUT_lon,DW865_lon,DW866_lon,IFBAP_lon]
RT2_lon = [BAMLI_lon,EPIDU_lon,ADNAL_lon,APRUT_lon,DW865_lon,DW866_lon,IFBAP_lon]
RT3_lon = [OLAPO_lon,EPIDU_lon,ADNAL_lon,APRUT_lon,DW865_lon,DW866_lon,IFBAP_lon]
RT4_lon = [RUBAR_lon,DETAX_lon,BERMO_lon,BABON_lon,BIVDI_lon,DW754_lon,DW755_lon,OSLEX_lon]
RT5_lon = [BUNED_lon,DIRUM_lon,KANUS_lon,BABON_lon,BIVDI_lon,DW754_lon,DW755_lon,OSLEX_lon]
RT6_lon = [SUTEX_lon,DIRUM_lon,KANUS_lon,BABON_lon,BIVDI_lon,DW754_lon,DW755_lon,OSLEX_lon]
RT7_lon = [OSGAR_lon,DIRUM_lon,KANUS_lon,BABON_lon,BIVDI_lon,DW754_lon,DW755_lon,OSLEX_lon]

radius=0.02

comm = ''
rad = 'rad02'

flightsrwy2 = pd.DataFrame()
for week in ['week3']:
            # ,'week4']:
    flights = pd.read_csv('PM_WEST_dataset_v3_'+rad+'.csv', 
    header=None,
    sep=' '
    ) 
    list_col_names = ['x','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
    flights.columns = list_col_names
    flightsrwy2 = pd.concat([flightsrwy2,flights])
    flightsrwy = flights.copy()
    flightsrwy = flightsrwy.drop("x", axis='columns')


    flightsrwy['time_in_final'] = flightsrwy.groupby(['flightID','endDate'])['timestamp'].transform('max')    
    number_of_flights = flightsrwy['flightID'].nunique()
    flightsrwy['time_to_final'] = (flightsrwy['time_in_final'] - flightsrwy['timestamp'])/60
    flightsrwy['altitude_ft'] = flightsrwy['baroAltitude']*3.281/100
    xx = flightsrwy.loc[(flightsrwy['flightID']=='220722KLM937')]
    nflights = flightsrwy2['flightID'].nunique()
    print('Number of flights in original PM: ',nflights)

    flights_arcs = flightsrwy.loc[((flightsrwy['altitude_ft']>=67)&(flightsrwy['altitude_ft']<=73))|((flightsrwy['altitude_ft']>=77)&(flightsrwy['altitude_ft']<=83))]
    level_flights = flights_arcs.groupby('flightID').size()
    df = level_flights.reset_index()
    df = df.rename(columns={0:'number'})
    df['group'] = df['number'].round(decimals=-1)
    occur = df.groupby('group').size().idxmax()
    #occur = occur - 10
    print('The number with highest occurence (threshold): ',occur)
    level_flights = level_flights.loc[(level_flights)>=occur].reset_index()
    mask = flightsrwy['flightID'].isin(level_flights['flightID'])
    flights_non_PM = flightsrwy[~mask]
    flights_PM_level = flightsrwy[mask]
    nflights_level = flights_PM_level['flightID'].nunique()
    nflights_nonPM = flights_non_PM['flightID'].nunique()
    print('Number of flights in filtered subset: ',nflights_level)
    flights_PM_level.to_csv('PM_VP_WEST_dataset_'+rad+'.csv', sep=' ', encoding='utf-8', float_format='%.3f', index = False, header = False)
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
    for i, g in flights_non_PM.groupby(['flightID','endDate']):
        g.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
    # axes = plt.gca()
    # axes.legend().set_visible(False)
    #xx.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='blue',lw=3)
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
    circle1  = plt.Circle((BERMO_lon,BERMO_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((ASDER_lon,ASDER_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((BABON_lon,BABON_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((ADNAL_lon,ADNAL_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black')
    plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black')
    plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black')
    plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black')
    plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black')
    plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black')
    plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black')
    # axes = plt.gca()
    # axes.legend().set_visible(False)
    ax.set_xlim([-7.2,-6.2])                                                               #setting limits for axes
    ax.set_ylim([53,54])
    ax.set(xlabel=None)
    ax.grid()
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()

    fig, ax = plt.subplots(figsize=(9,9))
    for i, g in flightsrwy.groupby(['flightID','endDate']):
        g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
    circle1  = plt.Circle((BERMO_lon,BERMO_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((ASDER_lon,ASDER_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((BABON_lon,BABON_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((ADNAL_lon,ADNAL_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black')
    plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black')
    plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black')
    plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black')
    plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black')
    plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black')
    plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black')
    # axes = plt.gca()
    # axes.legend().set_visible(False)
    ax.set_xlim([-7.2,-6.2])                                                               #setting limits for axes
    ax.set_ylim([53,54])
    ax.set(xlabel=None)
    ax.grid()
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()
    
    fig, ax = plt.subplots(figsize=(9,9))
    for i, g in flights_non_PM.groupby(['flightID','endDate']):
        g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
    circle1  = plt.Circle((BERMO_lon,BERMO_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((ASDER_lon,ASDER_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((BABON_lon,BABON_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    circle1  = plt.Circle((ADNAL_lon,ADNAL_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
    ax.add_patch(circle1)
    plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black')
    plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black')
    plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black')
    plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black')
    plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black')
    plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black')
    plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black')
    # axes = plt.gca()
    # axes.legend().set_visible(False)
    ax.set_xlim([-7.2,-6.2])                                                               #setting limits for axes
    ax.set_ylim([52.8,54])
    ax.set(xlabel=None)
    ax.grid()
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()



# fig, ax = plt.subplots(figsize=(9,9))
# xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# circle1  = plt.Circle((BERMO_lon,BERMO_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle1)
# circle1  = plt.Circle((ASDER_lon,ASDER_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle1)
# circle1  = plt.Circle((BABON_lon,BABON_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle1)
# circle1  = plt.Circle((ADNAL_lon,ADNAL_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle1)
# plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black')
# plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black')
# plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black')
# plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black')
# plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black')
# plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black')
# plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black')
# # axes = plt.gca()
# # axes.legend().set_visible(False)
# ax.set_xlim([-7.2,-6.2])                                                               #setting limits for axes
# ax.set_ylim([53,54])
# ax.set(xlabel=None)
# ax.grid()
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# plt.show()


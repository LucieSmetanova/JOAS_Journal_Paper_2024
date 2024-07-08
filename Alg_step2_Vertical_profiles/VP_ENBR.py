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

LUNUR_lat, LUNUR_lon = dms2dd('605023.50N 0060506.90E')
DIRBI_lat, DIRBI_lon = dms2dd('603720.26N 0055123.99E')
BR625_lat, BR625_lon = dms2dd('603253.91N 0054647.00E')
LUTIV_lat, LUTIV_lon = dms2dd('603206.39N 0053637.34E')
BR623_lat, BR623_lon = dms2dd('603522.61N 0053428.32E')
BR622_lat, BR622_lon = dms2dd('603803.48N 0053000.66E')
BR621_lat, BR621_lon = dms2dd('603949.41N 0052356.51E')
BR620_lat, BR620_lon = dms2dd('604026.92N 0051556.28E')
GILVA_lat, GILVA_lon = dms2dd('603029.12N 0051649.48E')
PESUR_lat, PESUR_lon = dms2dd('601435.70N 0063507.30E')
BR627_lat, BR627_lon = dms2dd('602122.53N 0060714.83E')
BR624_lat, BR624_lon = dms2dd('602838.60N 0053641.53E')
LEGTA_lat, LEGTA_lon = dms2dd('594918.61N 0054915.29E')
LUSAP_lat, LUSAP_lon = dms2dd('600757.44N 0054231.11E') #ONLY SHORT PART; FEW WAYPOINTS ARE MISSING
EPADU_lat, EPADU_lon = dms2dd('594647.95N 0045420.38E')
BENTI_lat, BENTI_lon = dms2dd('600533.47N 0044858.90E')
BR634_lat, BR634_lon = dms2dd('602415.14N 0044332.34E')
BR633_lat, BR633_lon = dms2dd('602730.71N 0044110.11E')
IRLOB_lat, IRLOB_lon = dms2dd('603058.52N 0044111.66E')
BR632_lat, BR632_lon = dms2dd('603413.52N 0044337.54E')
BR631_lat, BR631_lon = dms2dd('603652.06N 0044810.72E')
BR630_lat, BR630_lon = dms2dd('603844.57N 0045519.02E')
NEPAM_lat, NEPAM_lon = dms2dd('602910.96N 0050105.14E')
MODNI_lat, MODNI_lon = dms2dd('600210.50N 0035951.00E')
BR637_lat, BR637_lon = dms2dd('601355.55N 0042016.98E')
BR636_lat, BR636_lon = dms2dd('602146.37N 0042016.98E')
ETNOR_lat, ETNOR_lon = dms2dd('603725.30N 0035743.40E')
SANDO_lat, SANDO_lon = dms2dd('603327.62N 0042139.17E')
BR635_lat, BR635_lon = dms2dd('603150.98N 0043114.03E')
NIDGI_lat, NIDGI_lon = dms2dd('610340.20N 0044834.80E')
BR638_lat, BR638_lon = dms2dd('604814.20N 0044005.55E')
TUNIX_lat, TUNIX_lon = dms2dd('603640.23N 0043349.43E')
LUNUR_lat, LUNUR_lon = dms2dd('605023.50N 0060506.90E')
ROXET_lat, ROXET_lon = dms2dd('602550.34N 0055052.08E')
BR734_lat, BR734_lon = dms2dd('601046.09N 0054218.39E')
BR733_lat, BR733_lon = dms2dd('600730.97N 0054441.89E')
RATUG_lat, RATUG_lon = dms2dd('600403.14N 0054442.73E')
BR732_lat, BR732_lon = dms2dd('600047.68N 0054221.53E')
BR731_lat, BR731_lon = dms2dd('595808.05N 0053755.88E')
BR730_lat, BR730_lon = dms2dd('595613.23N 0053058.84E')
GODID_lat, GODID_lon = dms2dd('600544.40N 0052502.21E')
PESUR_lat, PESUR_lon = dms2dd('601435.70N 0063507.30E')
BR736_lat, BR736_lon = dms2dd('601316.09N 0055058.46E')
DIBMA_lat, DIBMA_lon = dms2dd('594007.56N 0055046.43E')
LEGTA_lat, LEGTA_lon = dms2dd('594918.61N 0054915.29E')
LATSI_lat, LATSI_lon = dms2dd('595817.54N 0055239.87E')
BR735_lat, BR735_lon = dms2dd('600311.41N 0055432.22E')
NIDGI_lat, NIDGI_lon = dms2dd('610340.20N 0044834.80E')
NIDIN_lat, NIDIN_lon = dms2dd('604030.97N 0044712.89E')
LELMI_lat, LELMI_lon = dms2dd('602545.52N 0044621.71E')
BR724_lat, BR724_lon = dms2dd('600615.11N 0044950.93E')
BR723_lat, BR723_lon = dms2dd('600247.29N 0044949.14E')
IBLIR_lat, IBLIR_lon = dms2dd('595931.67N 0045209.36E')
BR722_lat, BR722_lon = dms2dd('595651.74N 0045634.12E')
BR721_lat, BR721_lon = dms2dd('595506.61N 0050231.36E')
BR720_lat, BR720_lon = dms2dd('595429.34N 0051020.71E')
RIVIP_lat, RIVIP_lon = dms2dd('600427.21N 0050929.36E')
BR727_lat, BR727_lon = dms2dd('600503.85N 0042235.81E')
BR726_lat, BR726_lon = dms2dd('600707.97N 0044000.92E')
ALUVA_lat, ALUVA_lon = dms2dd('592327.40N 0045810.10E')
GENVU_lat, GENVU_lon = dms2dd('593736.90N 0045551.40E')
OKLAN_lat, OKLAN_lon = dms2dd('595218.16N 0044633.50E')
BR725_lat, BR725_lon = dms2dd('595703.04N 0044331.29E')
IRLOB_circle_center = Point(IRLOB_lon, IRLOB_lat)
BR634_circle_center = Point(BR634_lon, BR634_lat)
BR635_circle_center = Point(BR635_lon, BR635_lat)

RT1_lat = [LUNUR_lat,DIRBI_lat,BR625_lat,LUTIV_lat,BR623_lat,BR622_lat,BR621_lat,BR620_lat,GILVA_lat]
RT2_lat = [PESUR_lat,BR627_lat,BR624_lat,LUTIV_lat,BR623_lat,BR622_lat,BR621_lat,BR620_lat,GILVA_lat]
RT3_lat = [DIBMA_lat,LEGTA_lat,LUSAP_lat,BR624_lat,LUTIV_lat,BR623_lat,BR622_lat,BR621_lat,BR620_lat,GILVA_lat]
RT4_lat = [NIDGI_lat,BR638_lat,TUNIX_lat,BR635_lat,IRLOB_lat,BR632_lat,BR631_lat,BR630_lat,NEPAM_lat]
RT5_lat = [ETNOR_lat,SANDO_lat,BR635_lat,IRLOB_lat,BR632_lat,BR631_lat,BR630_lat,NEPAM_lat]
RT6_lat = [MODNI_lat,BR637_lat,BR636_lat,BR634_lat,BR633_lat,IRLOB_lat,BR632_lat,BR631_lat,BR630_lat,NEPAM_lat]
RT7_lat = [ALUVA_lat,GENVU_lat,EPADU_lat,BENTI_lat,BR634_lat,BR633_lat,IRLOB_lat,BR632_lat,BR631_lat,BR630_lat,NEPAM_lat]
RT8_lat = [LUNUR_lat,ROXET_lat,BR734_lat,BR733_lat,RATUG_lat,BR732_lat,BR731_lat,BR730_lat,GODID_lat]
RT9_lat = [PESUR_lat,BR736_lat,BR734_lat,BR733_lat,RATUG_lat,BR732_lat,BR731_lat,BR730_lat,GODID_lat]
RT10_lat = [DIBMA_lat,LEGTA_lat,LATSI_lat,BR735_lat,RATUG_lat,BR732_lat,BR731_lat,BR730_lat,GODID_lat]
RT11_lat = [NIDGI_lat,NIDIN_lat,LELMI_lat,BR724_lat,BR723_lat,IBLIR_lat,BR722_lat,BR721_lat,BR720_lat,RIVIP_lat]
RT12_lat = [ETNOR_lat,LELMI_lat,BR724_lat,BR723_lat,IBLIR_lat,BR722_lat,BR721_lat,BR720_lat,RIVIP_lat]
RT13_lat = [MODNI_lat,BR727_lat,BR726_lat,BR724_lat,BR723_lat,IBLIR_lat,BR722_lat,BR721_lat,BR720_lat,RIVIP_lat]
RT14_lat = [ALUVA_lat,GENVU_lat,OKLAN_lat,BR725_lat,IBLIR_lat,BR722_lat,BR721_lat,BR720_lat,RIVIP_lat]

RT1_lon = [LUNUR_lon,DIRBI_lon,BR625_lon,LUTIV_lon,BR623_lon,BR622_lon,BR621_lon,BR620_lon,GILVA_lon]
RT2_lon = [PESUR_lon,BR627_lon,BR624_lon,LUTIV_lon,BR623_lon,BR622_lon,BR621_lon,BR620_lon,GILVA_lon]
RT3_lon = [DIBMA_lon,LEGTA_lon,LUSAP_lon,BR624_lon,LUTIV_lon,BR623_lon,BR622_lon,BR621_lon,BR620_lon,GILVA_lon]
RT4_lon = [NIDGI_lon,BR638_lon,TUNIX_lon,BR635_lon,IRLOB_lon,BR632_lon,BR631_lon,BR630_lon,NEPAM_lon]
RT5_lon = [ETNOR_lon,SANDO_lon,BR635_lon,IRLOB_lon,BR632_lon,BR631_lon,BR630_lon,NEPAM_lon]
RT6_lon = [MODNI_lon,BR637_lon,BR636_lon,BR634_lon,BR633_lon,IRLOB_lon,BR632_lon,BR631_lon,BR630_lon,NEPAM_lon]
RT7_lon = [ALUVA_lon,GENVU_lon,EPADU_lon,BENTI_lon,BR634_lon,BR633_lon,IRLOB_lon,BR632_lon,BR631_lon,BR630_lon,NEPAM_lon]
RT8_lon = [LUNUR_lon,ROXET_lon,BR734_lon,BR733_lon,RATUG_lon,BR732_lon,BR731_lon,BR730_lon,GODID_lon]
RT9_lon = [PESUR_lon,BR736_lon,BR734_lon,BR733_lon,RATUG_lon,BR732_lon,BR731_lon,BR730_lon,GODID_lon]
RT10_lon = [DIBMA_lon,LEGTA_lon,LATSI_lon,BR735_lon,RATUG_lon,BR732_lon,BR731_lon,BR730_lon,GODID_lon]
RT11_lon = [NIDGI_lon,NIDIN_lon,LELMI_lon,BR724_lon,BR723_lon,IBLIR_lon,BR722_lon,BR721_lon,BR720_lon,RIVIP_lon]
RT12_lon = [ETNOR_lon,LELMI_lon,BR724_lon,BR723_lon,IBLIR_lon,BR722_lon,BR721_lon,BR720_lon,RIVIP_lon]
RT13_lon = [MODNI_lon,BR727_lon,BR726_lon,BR724_lon,BR723_lon,IBLIR_lon,BR722_lon,BR721_lon,BR720_lon,RIVIP_lon]
RT14_lon = [ALUVA_lon,GENVU_lon,OKLAN_lon,BR725_lon,IBLIR_lon,BR722_lon,BR721_lon,BR720_lon,RIVIP_lon]

radius=0.025
rad = 'rad025'

flightsrwy = pd.read_csv('data.csv', 
header=None,
sep=' '
) 
list_col_names = ['m','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flightsrwy.columns = list_col_names
err22 = ['221020BHL71S', '221020BHL930', '221021BHL242', '221022BHL782','221005BHL939','221009WIF414','221005WIF418', '221005WIF424', '221011FOX12W', '221016MDT1',
       '221016SZS899', '221024WIF418', '221027WIF418','221004FOX47W','221012WIF507', '221028WIF503','221028WIF503']

for i in err22:
    flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == i].index, inplace = True)

flightsrwy['time_in_final'] = flightsrwy.groupby(['flightID','endDate'])['timestamp'].transform('max')    
number_of_flights = flightsrwy['flightID'].nunique()
flightsrwy = flightsrwy.drop("m", axis='columns')
flightsrwy['time_to_final'] = (flightsrwy['time_in_final'] - flightsrwy['timestamp'])/60
flightsrwy['altitude_ft'] = flightsrwy['baroAltitude']*3.281/100
xx = flightsrwy.loc[(flightsrwy['flightID']=='220602SWR442')]
nflights = flightsrwy['flightID'].nunique()
print('Number of flights in original PM: ',nflights)

flights_arcs = flightsrwy.loc[(flightsrwy['altitude_ft']>=39)&(flightsrwy['altitude_ft']<=83)]
level_flights = flights_arcs.groupby('flightID').size()
df = level_flights.reset_index()
df = df.rename(columns={0:'number'})
df['group'] = df['number'].round(decimals=-1)
occur = df.groupby('group').size().idxmax()
if occur > 100:
    occur = 100
print('The number with highest occurence (threshold): ',occur)
level_flights = level_flights.loc[(level_flights)>=occur].reset_index()
mask = flightsrwy['flightID'].isin(level_flights['flightID'])
flights_PM_level = flightsrwy[mask]
flights_non_PM = flightsrwy[~mask]
nflights_level = flights_PM_level['flightID'].nunique()
nflights_nonPM = flights_non_PM['flightID'].nunique()
print('Number of flights in filtered subset: ',nflights_level)
flights_PM_level.to_csv('PM_VP_dataset_'+rad+'.csv', sep=' ', encoding='utf-8', float_format='%.3f', index = False, header = False)


fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# axes = plt.gca()
# axes.legend().set_visible(False)
xx.plot(x='time_to_final', y='altitude_ft', ax=ax, label=str(i),legend=False,color='blue',lw=3)
ax.axhline(40, color="red", linestyle="--")
ax.axhline(80, color="orange", linestyle="--")
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
ax.axhline(40, color="red", linestyle="--")
ax.axhline(80, color="orange", linestyle="--")
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
circle1  = plt.Circle((IRLOB_lon,IRLOB_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((BR634_lon,BR634_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((BR635_lon,BR635_lat), radius, color='g', linewidth = 1.5,fill = False,zorder=3)
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
plot13 = plt.plot(RT12_lon, RT12_lat,linewidth=1.5,color = 'black')
plot14 = plt.plot(RT13_lon, RT13_lat,linewidth=1.5,color = 'black')
plot15 = plt.plot(RT14_lon, RT14_lat,linewidth=1.5,color = 'black')
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([4.5,6])
ax.set_ylim([59.8,60.75])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((IRLOB_lon,IRLOB_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((BR634_lon,BR634_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((BR635_lon,BR635_lat), radius, color='g', linewidth = 1.5,fill = False,zorder=3)
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
plot13 = plt.plot(RT12_lon, RT12_lat,linewidth=1.5,color = 'black')
plot14 = plt.plot(RT13_lon, RT13_lat,linewidth=1.5,color = 'black')
plot15 = plt.plot(RT14_lon, RT14_lat,linewidth=1.5,color = 'black')
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([4.5,6])
ax.set_ylim([59.8,60.75])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)plt.show()

# fig, ax = plt.subplots(figsize=(9,9))
# xx.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
# circle1  = plt.Circle((IRLOB_lon,IRLOB_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle1)
# circle1  = plt.Circle((BR634_lon,BR634_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle1)
# circle1  = plt.Circle((BR635_lon,BR635_lat), radius, color='g', linewidth = 1.5,fill = False,zorder=3)
# ax.add_patch(circle1)
# plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black')
# plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black')
# plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black')
# plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black')
# plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black')
# plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black')
# plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black')
# plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black')
# plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black')
# plot11 = plt.plot(RT10_lon, RT10_lat,linewidth=1.5,color = 'black')
# plot12 = plt.plot(RT11_lon, RT11_lat,linewidth=1.5,color = 'black')
# plot13 = plt.plot(RT12_lon, RT12_lat,linewidth=1.5,color = 'black')
# plot14 = plt.plot(RT13_lon, RT13_lat,linewidth=1.5,color = 'black')
# plot15 = plt.plot(RT14_lon, RT14_lat,linewidth=1.5,color = 'black')
# # axes = plt.gca()
# # axes.legend().set_visible(False)
# ax.set_xlim([4.5,6])
# ax.set_ylim([59.8,60.75])
# ax.set(xlabel=None)
# ax.grid()
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# plt.show()

fig, ax = plt.subplots(figsize=(9,9))
for i, g in flights_non_PM.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.3)
circle1  = plt.Circle((IRLOB_lon,IRLOB_lat), radius, color='b', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((BR634_lon,BR634_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle1  = plt.Circle((BR635_lon,BR635_lat), radius, color='g', linewidth = 1.5,fill = False,zorder=3)
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
plot13 = plt.plot(RT12_lon, RT12_lat,linewidth=1.5,color = 'black')
plot14 = plt.plot(RT13_lon, RT13_lat,linewidth=1.5,color = 'black')
plot15 = plt.plot(RT14_lon, RT14_lat,linewidth=1.5,color = 'black')
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([4.5,6])
ax.set_ylim([59.8,60.75])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()

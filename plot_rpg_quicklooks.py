import numpy as np
import netCDF4
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import dates
import datetime

f_name1 = 'placeholder.nc'

plotyear = 2018 #int(input('year (YYYY):'))
plotmonth =1 #int(input('month (MM):'))
plotday =1 #int(input('day (DD):'))

#plot_date= mpl.dates.date2num(datetime.datetime(year=plotyear,month=plotmonth,day=plotday,minute=0)) #10 min offset, first mean of the day is 0:10
time_loc=[]
for i in range (0,1440):
  temp=datetime.datetime(2018,1,1,0,0,0) + datetime.timedelta(minutes=i)
  time_loc.append(temp)

array_test=np.random.rand(240,1440) #test for 1 min interval and 50 m height resolution, 240 levels and 1440 min/d
array_test=array_test*100-80 #generate some "low" values to be left out
#array_test[array_test < -40] = np.nan #values below -40 dBz are disregarded

line_test=np.random.rand(1440)
line_test=line_test*100+50

rain_test=np.random.rand(1440)*50

level=np.linspace(0.,12.,240)

array_test=np.ma.masked_invalid(array_test)

### plot ###

#load color map and define lowest color to be white
my_cmap = mpl.cm.get_cmap('jet')
my_cmap.set_under('w')

#create figure
fig=plt.figure(figsize=(20,60))
hfmt = dates.DateFormatter('%H:%M')  #set date format to HH:MM

#reflectivity plot
ref=fig.add_subplot(611)  #add reflectivity subplot
ref.xaxis_date()  # time format for x axis
ref.xaxis.set_major_formatter(hfmt)  # acquire date format from hfmt

steps_ref = np.arange(-40, 21,5)
cMap = plt.get_cmap(my_cmap)
ref.grid(color='black',linestyle=':',linewidth='0.5')
cMap.set_bad(color='white', alpha=1.)
norm = mpl.colors.BoundaryNorm(steps_ref, cMap.N)
cp=plt.pcolormesh(time_loc, level, array_test,vmin=-40, vmax=20, cmap=cMap, norm=norm)
cbar= plt.colorbar(cp)
cbar.set_label('dBz')
ref.axes.tick_params(axis='both', direction='inout', length=10, width=1.5)
plt.axis([time_loc[0],time_loc[-1],0,12])
plt.xlabel('time (UTC)')
plt.ylabel('height (km)')


#mean doppler velocity plot
mdv=fig.add_subplot(612, sharex=ref) #add mean doppler velocity subplot
mdv.xaxis_date()  # time format for x axis
mdv.xaxis.set_major_formatter(hfmt)  # acquire date format from hfmt

steps_mdv = np.arange(-4, 4.1,0.25)
cMap = plt.get_cmap(my_cmap)
mdv.grid(color='black',linestyle=':',linewidth='0.5')
cMap.set_bad(color='white', alpha=1.)
norm = mpl.colors.BoundaryNorm(steps_mdv, cMap.N)
cp=plt.pcolormesh(time_loc, level, array_test,vmin=-4, vmax=4, cmap=cMap, norm=norm)
cbar= plt.colorbar(cp)
cbar.set_label('m/s')
mdv.axes.tick_params(axis='both', direction='inout', length=10, width=1.5)
plt.axis([time_loc[0],time_loc[-1],0,12])
plt.xlabel('time (UTC)')
plt.ylabel('height (km)')


#spectral width plot
sw=fig.add_subplot(613, sharex=ref) #add spectral width subplot
sw.xaxis_date()  # time format for x axis
sw.xaxis.set_major_formatter(hfmt)  # acquire date format from hfmt

steps_sw = np.arange(0, 2.1,0.25)
cMap = plt.get_cmap(my_cmap)
sw.grid(color='black',linestyle=':',linewidth='0.5')
cMap.set_bad(color='white', alpha=1.)
norm = mpl.colors.BoundaryNorm(steps_sw, cMap.N)
cp=plt.pcolormesh(time_loc, level, array_test,vmin=0, vmax=2, cmap=cMap, norm=norm)
cbar= plt.colorbar(cp, ticks=steps_sw)
cbar.set_label('m/s')
sw.axes.tick_params(axis='both', direction='inout', length=10, width=1.5)
plt.axis([time_loc[0],time_loc[-1],0,12])
plt.xlabel('time (UTC)')
plt.ylabel('height (km)')


#linear depolarisation ratio plot
ldr=fig.add_subplot(614, sharex=ref) #add linear depolarisation ratio subplot
ldr.xaxis_date()  # time format for x axis
ldr.xaxis.set_major_formatter(hfmt)  # acquire date format from hfmt

steps_ldr = np.arange(-30, 1,5)
cMap = plt.get_cmap(my_cmap)
ldr.grid(color='black',linestyle=':',linewidth='0.5')
cMap.set_bad(color='white', alpha=1.)
norm = mpl.colors.BoundaryNorm(steps_ldr, cMap.N)
cp=plt.pcolormesh(time_loc, level, array_test,vmin=-30, vmax=0, cmap=cMap, norm=norm)
cbar= plt.colorbar(cp, ticks=steps_ldr)
cbar.set_label('dB')
ldr.axes.tick_params(axis='both', direction='inout', length=10, width=1.5)
plt.axis([time_loc[0],time_loc[-1],0,12])
plt.xlabel('time (UTC)')
plt.ylabel('height (km)')


#brightness temperature plot
tb=fig.add_subplot(615, sharex=ref) #add brightness temperature subplot
tb.xaxis_date()  # time format for x axis
tb.xaxis.set_major_formatter(hfmt)  # acquire date format from hfmt

cp=plt.plot(time_loc, line_test, color="black")
tb.grid(color='black',linestyle=':',linewidth='0.5')
tb.axes.tick_params(axis='both', direction='inout', length=10, width=1.5)
plt.axis([time_loc[0],time_loc[-1],25,175])
plt.xlabel('time (UTC)')
plt.ylabel('brightness temperature (K)')


#rain rate plot
rr=fig.add_subplot(616, sharex=ref) #add rain rate subplot
rr.xaxis_date()  # time format for x axis
rr.xaxis.set_major_formatter(hfmt)  # acquire date format from hfmt

cp=plt.bar(time_loc, rain_test,width=0.001,color="blue",edgecolor="blue")
rr.grid(color='black',linestyle=':',linewidth='0.5')
rr.axes.tick_params(axis='both', direction='inout', length=10, width=1.5)
plt.axis([time_loc[0],time_loc[-1],0,50])
plt.xlabel('time (UTC)')
plt.ylabel('rain rate (mm/h)')






plt.subplots_adjust(hspace = 0.75)
plt.suptitle('LIMRAD measurements '+str(plotday)+'-'+str(plotmonth)+'-'+str(plotyear))

#plt.savefig('test.png', bbox_inches='tight')
plt.show()

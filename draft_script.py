# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:33:11 2018

@author: mreza
"""

import pandas as pd
import numpy as np
import def_weather_stations as dws
from matplotlib import mlab
from matplotlib import dates as mdates
from scipy import stats
import tkinter as tk
from tkinter import filedialog
import os




   
#root = tk.Tk() 
#root.withdraw()        
#fp_maintfilt = filedialog.askopenfilename(title = "Import maintenance file",defaultextension ='.xlsx',
#       filetypes = (("CSV files","*.xlsx"),("all files","*.*")),parent = root)                    
fp,si,pi,data,d_type,station_name,fn,t_start,t_end = \
dws.defuiopen("Select the first '*.CSV' file",[]) #select and import the first file
t_int,_ = dws.defcheck_int(data)                                      
if t_int > 1:                                                                                          
    data = dws.definterval_fix(data,d_type) # unify the time interval
data,pi,si = dws.deffix_columns(pi,si,data,d_type)                                        
if d_type == "Local":
    data,si,pi = dws.defEC_unit(data,station_name,si,pi)
data,si = dws.defmaint("3",[],data,station_name,si,d_type) # replace the maintenance with nan


time1 = data.iloc[:,0]
fy = time1.iloc[0].year
ly = time1.iloc[-1].year
time2 = pd.DataFrame(np.nan,index=range(len(time1)),columns=["timestamp","year","month","day"])
time2.loc[:,"timestamp"] = time1
print("Making new date dataframe with seperated date values")
for i in range(len(time1)):
    time2.loc[i,"year"] = time2.loc[i,"timestamp"].year
    time2.loc[i,"month"] = time2.loc[i,"timestamp"].month
    time2.loc[i,"day"] = time2.loc[i,"timestamp"].day
    
    
frst_col = ["January","February","March","April","May","Jun",
            "July","August","September","October","November","December"]
clmn_ind = ["Month","Nfull_month","MEAN T","STD T","MEAN P","STD P"]
units = ["-","#","[Deg C]","[Deg C]","[mm/M]","[mm/M]"]
output = pd.DataFrame(np.nan,index=range(14),columns=clmn_ind)
output.iloc[2:,0] = frst_col
output.iloc[0,:] = clmn_ind   
output.iloc[1,:] = units  
if d_type == "Local":
    t_int = 48
    par = ["AirTC_Avg","Rain_mm_Tot"]               
elif d_type == "Satellite":
    t_int = 24
    par = ["Air temperature","Precipitation"]
    
print("Calculating MEAN & STD")    
for m in range(1,13):
    print("Working on " + frst_col[m-1])
    m_ind = []
    nm = 0 # number of full month
    for y in range(fy,ly+1):
        B1 = time2.loc[:,"month"] == m
        B2 = time2.loc[:,"year"] == y
        B = np.logical_and(B1,B2)
        ind_temp = B.index[B].tolist()
        temp_T = pd.DataFrame(data.loc[ind_temp,par[0]])
        temp_P = pd.DataFrame(data.loc[ind_temp,par[1]])
        nan_ind_T = pd.isnull(temp_T).any(1).nonzero()[0]
        nan_ind_P = pd.isnull(temp_P).any(1).nonzero()[0]
        nan_ind = max(len(nan_ind_T),len(nan_ind_P))
        if abs(len(ind_temp)-nan_ind)/t_int >= 28: # if number of recorded data in that month is more than 28 days
            nm = nm + 1 
            m_ind = m_ind + ind_temp
    output.loc[m+1,"MEAN T"] = np.round(np.nanmean(np.array(data.loc[m_ind,par[0]])),2)
    output.loc[m+1,"MEAN P"] = np.round(np.nansum(np.array(data.loc[m_ind,par[1]]))/nm,2)                            
    output.loc[m+1,"STD T"] = np.round(np.nanstd(np.array(data.loc[m_ind,par[0]])),2)
    output.loc[m+1,"STD P"] = np.round(np.nanstd(np.array(data.loc[m_ind,par[1]])),2)
    output.loc[m+1,"Nfull_month"] = nm
sht_name = os.path.basename(fp)
sht_name = sht_name[:-4]
auto_fname = "Monthly_mean_std.xls"
output_path = fp.replace(os.path.basename(fp),auto_fname) #file path without file name   
output.to_excel(output_path, sheet_name=sht_name, na_rep='None', float_format='%G',header=False, index=False)







nan_ind = pd.isnull(data.iloc[0,:]).any(1).nonzero()[0]





#print("________________________________________ IMPORT THE MAINTENANCE FILE")    
#root = tk.Tk() 
#root.withdraw()         
#fp_maintfilt = filedialog.askopenfilename(title = "Import maintenance file",defaultextension ='.xlsx',
#       filetypes = (("CSV files","*.xlsx"),("all files","*.*")),parent = root)
#
#
#fp_s,si_s,pi_s,data_s,d_type_s,station_name_s,fn_s,t_start_s,t_end_s = dws.defuiopen("",[])
##fp_l,si_l,pi_l,data_l,d_type_l,station_name_l,fn_l,t_start_l,t_end_l = dws.defuiopen("",[])
#
#t_int_s,nan_ind_s = dws.defcheck_int(data_s)
##t_int_l,_ = dws.defcheck_int(data_l)                                        
#if t_int_s > 1:                                                                                           
#    data_s = dws.definterval_fix(data_s,d_type_s) # unify the time interval                                        
##if t_int_l > 1:                                                                                          
##    data_l = dws.definterval_fix(data_l,d_type_l) # unify the time interval
#data_s,pi_s,si_s = dws.deffix_columns(pi_s,si_s,data_s,d_type_s)                                        
##data_l,pi_l,si_l = dws.deffix_columns(pi_l,si_l,data_l,d_type_l)
#if d_type_s == "Local":
#   data_s,si_s,pi_s = dws.defEC_unit(data_s,station_name_s,si_s,pi_s)
##if d_type_l == "Local":                                          
##    data_l,si_l,pi_l = dws.defEC_unit(data_l,station_name_l,si_l,pi_l)
##
#data_s,si_s = dws.defmaint("1",fp_maintfilt,data_s,station_name_s,si_s,d_type_s) # replace the maintenance with nan                                              




































#
#
#
#
#
#
#                                                            
#                fig = plt.gcf() #figure
#                ax = plt.gca() #ax
#                ax.set_xlim(tstart,tend) #X axis limit
#                ax.set_ylim(ymn[i],ymx[i]) #Y axis limit
#                plt.xlabel("Time (yy-mm-dd HH-MM)", color='black', fontsize = 12, fontweight='bold') # x label
#                plt.ylabel("["+p_unit+"]", color='black', fontsize = 12, fontweight='bold') # y label
#                if yinc != []: # set the Y axis increment same as the user input value
#                    ax.yaxis.set_ticks(np.arange(ymn, ymx, yinc))
#                elif yinc == []:
#                    ax.yaxis.set_ticks(np.round(np.linspace(ymn[i],ymx[i],10),1))
#                ttl = param.iloc[ind_p[i]-2] #name pf the plotted parameter
#                if ttl[0] == " ":
#                    ttl = ttl[1:] #delete the extra space before the parameter name     
#                plt.title(ttl, color='black', fontsize = 12, fontweight='bold') # plot title
#                myFmt = mdates.DateFormatter('%y-%m-%d %H:%M') # X axis date format
#                ax.xaxis.set_major_formatter(myFmt) # set the selected format to the X axis
#                fig.autofmt_xdate() # change X axis label angel
#                plt.tick_params(direction='out', length=5, width=2, labelsize=10) # tick configuration
##                plt.figtext(0.1,0.03,"File name: "+fn,fontsize=11) # add the file name belowe the plot 
#                fig.set_size_inches((8.27,11.69), forward=True) # set size of the figure
#                plt.grid() # grid the plot
#            plt.subplots_adjust(left=0.13, bottom=0.35, right=0.95, top=0.92, wspace=0.2, hspace=0.15)                
#            if sv_nsv == "2" or sv_nsv == "3": # if user asks for save the plot
#                for z in range(len(hq_as)):
#                    tts = tstart.to_pydatetime() #convert start time to py time format
#                    tte = tend.to_pydatetime() #convert end time to py time format
#                    p_ts = str(tts.year)[-2:]+str(tts.month)[-2:]+str(tts.day)[-2:] #convert the satrt to string format for name of the saved plot
#                    p_te = str(tte.year)[-2:]+str(tte.month)[-2:]+str(tte.day)[-2:] #convert the end to string format for name of the saved plot
#                    temp_fn = fn.replace(".csv","") #temporary file name without.csv for save name                    
#                    frmt = [".jpg",".png",".pdf",".csv"]
#                    extn = frmt[int(hq_as[z])-1]
#                    f_name = temp_fn+"_"+p_name1+"_"+p_name2+"_"+p_ts+"_"+p_te+extn #generate a name for the saved file
#                    f_npath = fp1+f_name # path to save the plot
#                    ii = 0
#                    while True: #check if the name already exsits and generate new name by adding number
#                        if os.path.exists(f_npath):
#                            ii = ii+1
#                            f_name = temp_fn+"_"+p_name1+"_"+p_name2+"_"+p_ts+"_"+p_te+"_("+str(ii)+")"+extn
#                            f_npath = fp1+f_name
#                        else:
#                            break
#                    if hq_as[z] == "4":
#                        data_csv.to_csv(f_npath , sep=',', na_rep = "None", float_format='%G', index=False, encoding='utf-8')                            
#                    else:
#                        fig.savefig(fname = f_npath, dpi = 600) # save the figure 600 dpi quality
#                    print("As-----> "+f_name) #print the name of the saved plot
#            if sv_nsv == "1" or sv_nsv == "3": # to show the plot                
#                if platform == "win32": # in windows platform
#                    print("________________________________________ ATTENTION \n"
#                          "* In case of using 'WINDOWS COMMAND PROMPT': \n"
#                          "* Close the opened figure(s) manually to continue")
#                    plt.show() # show the plot
#                elif platform == "darwin": # in mac
#                    plt.show(block=False) # show the plot
#            sctn = "9"
#        
        
        
        
        
        
        
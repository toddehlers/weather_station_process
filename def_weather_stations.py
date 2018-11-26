# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 06:00:55 2017

@author: M.Reza Ershadi
         mohammadreza.ershadi@student.uni-tuebingen.de
         (mreza.ershadi@web.de)

Written in: Anaconda 3 (Python 3.6)
("=============================================================================")
("          EARTHSHAPE CHILE WEATHER STATIONS DATA MANAGEMENT (V_8)           ")
("=============================================================================")
"""

"""=============================================================================
FUNCTION (Modules):
Check the modules
If they are available in the system import them
Otherwise print the missing ones for the user
============================================================================="""
msng_pkg=[]
try:
    import sys
    from sys import platform
except:
    msng_pkg = ["sys"]
    pass
#..............................................................................
try:
    from subprocess import call as spc
except:
    msng_pkg.append("os")
    pass
#..............................................................................
try:
    import os
except:
    msng_pkg.append("os")
    pass
#..............................................................................
if platform == "win32":
    try:
        import winsound
        frequency = 1000  # Set Frequency To 2500 Hertz
        duration = 100  # Set Duration To 1000 ms == 1 second
    except:
        msng_pkg.append("winsound")
        pass 
#..............................................................................
#try:
#    import glob
#except:
#    msng_pkg.append("glob")
#    pass        
#..............................................................................
try:
    import numpy as np
except:
    msng_pkg.append("numpy")
    pass
#..............................................................................
try:
    import pandas as pd
except:
    msng_pkg.append("pandas")
    pass
#..............................................................................
try:
    from scipy import stats
#    from scipy import signal
except:
    msng_pkg.append("scipy")
    pass
#..............................................................................    
try:   
    if platform == "darwin":
        import matplotlib       
        matplotlib.use("TKAgg")  
    from matplotlib import pyplot as plt
    from matplotlib import dates as mdates 
    from matplotlib.patches import Rectangle
    plt.rcParams.update({'figure.max_open_warning': 0})
except:
    msng_pkg.append("matplotlib")
    pass
#..............................................................................
try:
    import tkinter as tk
    from tkinter import filedialog
except:
    msng_pkg.append("tkinter")
    pass
#..............................................................................
#try:
#    from  more_itertools import unique_everseen
#except:
#    msng_pkg.append("more_itertools")
#    pass
#..............................................................................
from openpyxl import load_workbook
# check the missing packages and print them for the user
if len(msng_pkg) > 0:
    print("________________________________________ Missing modules(s) \n"
         "Please install them and run the code again")
    for items in msng_pkg:
        print(items)
    input("Press *ENTRE* to exit...")
    sys.exit("Missing modules(s)")
"""=============================================================================
FUNCTION (Check the operating system):
Sometimes, especially for the plots the functions for different operating
systems are different
============================================================================="""
if platform == "linux" or platform == "linux2":
    print("________________________________________ SYSTEM INFO \n"
          "* Operating system: LINUX \n"
          "* Current path: "+ os.getcwd())
elif platform == "darwin":
    print("________________________________________ SYSTEM INFO \n" 
          "* Operating system: OS X \n"
          "* Current path: "+ os.getcwd())
elif platform == "win32":
    print("________________________________________ SYSTEM INFO \n" 
          "* Operating system: WINDOWS \n"
          "* Current path: "+ os.getcwd())
"""=============================================================================
FUNCTION (main menu):
Display the MAIN MENU and ask the user to choose
This menu can be displayed in two ways
Short one and extended one
============================================================================="""
def defwhat():
    print("________________________________________")
    print("   =       =  =====  =   =  =   =")
    print("   ==     ==  =      ==  =  =   =")
    print("   = =   = =  =====  = = =  =   =")
    print("   =  = =  =  =      =  ==  =   =")
    print("   =   =   =  =====  =   =   === ")
    what = input("________________________________________"
                 "\n0: EXTENDED MENU !!!" 
                 "\n1: FILE REAPORT"
                 "\n2: PLOT"
                 "\n3: APPEND TWO FILES"
                 "\n4: FILL THE GAPS (NONE)"
                 "\n5: Monthly Excel file (from T and P)"
                 "\nH: HELP"
                 "\nQ: QUIT \n"
                 "Enter a number >>> ")
    if what == "0": # switch the menu from short to extended
        print("________________________________________")
        print("   =       =  =====  =   =  =   =")
        print("   ==     ==  =      ==  =  =   =")
        print("   = =   = =  =====  = = =  =   =")
        print("   =  = =  =  =      =  ==  =   =")
        print("   =   =   =  =====  =   =   === ")
        what = input("________________________________________"
                     "\n0: ABRIDGED MENU !!! \n"
                     "\n1: FILE REAPORT \n"
                     "***After Execution: \n"
                     "   -Import a *.csv file (local or satellite) \n"                     
                     "   -Extract and display all the information in the file \n"               
                     "   -Optional: Display and save the missing data (none) as txt \n"
                     "\n2: PLOT \n"
                     "***After Execution: \n"                 
                     "   -Import a *.csv files (local or satellite) \n"
                     "   -Extract and display all the information in the file \n"
                     "   -Select a parameter to plot by choosing: \n"
                     "    * time period, plot style, Y axis \n"
                     "    * high quality save (600 dpi as jpg, png, pdf) and display\n"             
                     "\n3: APPEND TWO FILES (combine two files vertically) \n"
                     "***After Execution: \n"                 
                     "   -Import 2 *.csv files (local or satellite but from same station) \n"                     
                     "   -The order of import (older & newer) does not matter \n"
                     "   -Extract and display all the information in both files \n"
                     "   -Check the compatibility of the files \n"
                     "   -Append the newer file below the older file and save the combined file \n"                  
                     "   -Extract and display all the information of the newly combined file \n"                 
                     "\n4: FILL THE GAPS (fill the missing satellite data (none)) \n"
                     "***After Execution: \n"                 
                     "   -Import a satellite.csv file \n"                     
                     "   -Import an associated local.csv file \n"
                     "   -Extract and display all the information in both files \n"
                     "   -Unifying the time interval in both files (if they are not unified) \n"
                     "   -Check the compatibility of the files \n"
                     "   -Fill the missing satellite data (none) by its local data and save the new file \n"
                     "   -Extract and display all the information in the new file \n"
                     "\n5: Monthly Excel file (from T and P) \n"
                     "\nH: HELP \n"
                     "\nQ: QUIT \n \n"
                     "Enter a number >>> ")
    return what    
"""**********************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
**********************************************************************************************************"""
"""PACKAGE OF FUNCTIONS (GENERAL)"""
"""=============================================================================
FUNCTION (readme):
This function loads the HELP.txt which includs all the information about the program
============================================================================="""
def def_help():
    fp = os.getcwd()
    if platform == "darwin":
        print('\a')
        spc(["open",fp+"/HELP.txt"])
    elif platform == "win32":
        winsound.Beep(frequency, duration)
        os.startfile(fp+"\HELP.txt")
"""=============================================================================
FUNCTION (open *.CSV file):
It opens a file dialog and user can easily select a *.SCV file
It recognise the file type (satellite or local) 
Extract the path of the selected file, information from the initial lines
of the selected file and the main data
============================================================================="""
def defuiopen(title_text,fp):
    if len(fp) == 0:
        fp,si,pi,data = [],[],[],[] #file path, first line of the csv file, parameters, data
#..............................................................................
# to open a file dialog    
        root = tk.Tk() 
        root.withdraw()
#..............................................................................
# make a sound when opens a file dialog    
        if platform == "darwin": # in mac
            print('\a') 
        elif platform == "win32": # in windows
            winsound.Beep(frequency, duration)
#..............................................................................
# open a file dialog and extrac the path of the selected file        
        fp = filedialog.askopenfilename(title = title_text,defaultextension ='.csv',
               filetypes = (("CSV files","*.csv"),("all files","*.*")),parent = root) 
#..............................................................................
    if len(fp) != 0: # if user select a csv file correctly
        si = pd.read_csv(fp, sep=',', nrows=1, header=None, dtype=str) # first line
        if si.iloc[0, 0] == "TOA5": # if LOCAL data
            d_type = "Local"
            station_name = si.iloc[0, 1] # station name
            pi = pd.read_csv(fp, sep=',', skiprows=[0], nrows=3, header=None, dtype=str) # lines 2,3,4 as parameters
            pi.columns = list(pi.iloc[0,:])
            data = pd.read_csv(fp, sep=',', skiprows=[0,1,2,3], header=None, dtype=str) # read the data (everything after line 4)
            data.columns = list(pi.iloc[0,:])
        else: # if SATELLITE data
            d_type = "Satellite"
            if ("appended_file" in list(si.iloc[0,:])) or ("filtered" in list(si.iloc[0,:])) or \
            ("crct_unit" in list(si.iloc[0,:])) or ("filled" in list(si.iloc[0,:])):
                pi = pd.read_csv(fp, sep=',', skiprows=[0], nrows=2, header=None, dtype=str)
                pi.columns = list(pi.iloc[0,:])
                data = pd.read_csv(fp, sep=',', skiprows=[0,1,2], header=None, dtype=str)
                data.columns = list(pi.iloc[0,:])
                station_name = data.iloc[1, 1] # station name
            else:
                pi = pd.DataFrame(np.nan,index = [0,1],columns = list(si.iloc[0,:]))
                pi.iloc[0,:] = list(si.iloc[0,:])
                pi.iloc[1,:] = ["-","-","Deg C","%","W/m²","m³/m³","Deg C","m/s","m/s","Deg","mm","mbar"]
                data = pd.read_csv(fp, sep=',', skiprows=[0], header=None, dtype=str)
                data.columns = list(pi.iloc[0,:])
                si = pd.DataFrame(np.nan,index = [1], columns = range(pi.shape[1]))
                station_name = data.iloc[1, 1] # station name
        if si.shape[1] < pi.shape[1]:
            sii = pd.DataFrame(" ",[0],range(pi.shape[1]))
            sii.iloc[0,0:si.shape[1]] = si.iloc[0,:]
            si = sii
#..............................................................................
# print basic file info
    if len(fp) != 0: # check if any file is selected
        fn = os.path.basename(fp) # extract the name of the csv file            
    if ' ' in station_name:
        station_name = station_name.replace(' ','')
    if '_' in station_name:
        station_name = station_name.replace('_','')             
    station_name = station_name[0].upper() + station_name[1:].lower()
    if station_name == "Lacampana":
        station_name = "La Campana"
    if station_name == "Santagracia":
        station_name = "Santa Gracia"
    if station_name == "Nahuelbuta":
        station_name = "Nahuelbuta"
    if station_name == "Pandeazucar":
#        station_name = "Pan de Azu" + u"\u0301" + "car"
        station_name = "Pan de Azucar"
    if station_name == "Wannetue":
        station_name = "Tuebingen"            
    data = data.replace(to_replace = 'None', value = np.nan) #replace any NONE value with numpy.nan
    data = data.replace(to_replace = ' None', value = np.nan) #replace any NONE value with numpy.nan
    data = data.replace(to_replace = 'None ', value = np.nan) #replace any NONE value with numpy.nan
    n_p = data.shape[1] # number of parameters (columns)    
    data.iloc[:,0] = pd.to_datetime(data.iloc[:,0]) # convert the first column of the data to time format
    if d_type == "Local": # for local data
        data.iloc[:,1:] = data.iloc[:,1:].astype(float) # change the format of all the data except time to float
    else: # for satellite data
        data.iloc[:,1] = data.iloc[:,1].astype(str) # change the format of the second column (station name) to string
        data.iloc[:,2:] = data.iloc[:,2:].astype(float) # change the format of the rest of the data to float
    t_start = data.iloc[0, 0] # date and time of the first recorded data
    t_end = data.iloc[len(data) - 1, 0] # date and time of the last recorded data   
    print("File name:--------------- " + fn)             
    print("Data type:--------------- " + d_type + "\n"
          "Station name:------------ " + station_name + "\n"
          "Number of columns:------- " + str(n_p))
    print("First record:------------ " + str(t_start))
    print("Last record:------------- " + str(t_end))                 
    return fp,si,pi,data,d_type,station_name,fn,t_start,t_end
"""=============================================================================
FUNCTION (save as *.CSV file):
It opens a file dialog and let the user to save the new file
It need "si" as the first line of the csv file, "pi" as all the rows related to the parameters
and "data" and the type of the file as local or satellite
============================================================================="""
def defuisave(fp,si,pi,data,d_type,station_name,prcss):
    si = si.replace(to_replace = 'None', value = " ") #replace any NONE value with numpy.nan
    si = si.replace(to_replace = 'nan', value = " ") #replace any NONE value with numpy.nan
    si = si.replace(to_replace = np.nan, value = " ") #replace any NONE value with numpy.nan
    pi.columns = range(data.shape[1]) # change the parameters columns name to number
    data.columns = range(data.shape[1]) # change the data columns name to number
    hinf = si.append(pi,ignore_index=True) # append "pi" below "si" and reset the rows index number
    output = hinf.append(data,ignore_index=True) # append "data" below the "si and pi" and reset the rows index
    hdr = False # no header for the new csv file
#..............................................................................
# to open a file dialog             
    root = tk.Tk()
    root.withdraw()
#..............................................................................
# make a sound when opens a file dialog     
    if platform == "darwin": # in mac
        print('\a')
    elif platform == "win32": # in windows
        winsound.Beep(frequency, duration)
#..............................................................................
# ask the user where to save the file and the name of the new filw       
    tstart = data.iloc[0,0] # first record
    tend = data.iloc[len(data) - 1,0] # last record
    tts = tstart.to_pydatetime() #convert start time to py time format
    tte = tend.to_pydatetime() #convert end time to py time format
    p_ts = str(tts.year)[-2:]+"."+str(tts.month)[-2:]+"."+str(tts.day)[-2:] #convert the satrt to string format for name of the saved plot
    p_te = str(tte.year)[-2:]+"."+str(tte.month)[-2:]+"."+str(tte.day)[-2:] #convert the end to string format for name of the saved plot
    if station_name == "La Campana":
        station_name = "LC"
    if station_name == "Santa Gracia":
        station_name = "SG"
    if station_name == "Nahuelbuta":
        station_name = "Na"
    if station_name == "Pan de Azu" + u"\u0301" + "car" or station_name == "Pan de Azucar":
        station_name = "PdA"
    if d_type == "Local":
        d_type = "loc"
    if d_type == "Satellite":
        d_type = "sat"        
    auto_fname = station_name + "_" + d_type + "_" + p_ts + "_" + p_te + "_" + prcss + ".csv"
    output_path = fp.replace(os.path.basename(fp),auto_fname) #file path without file name
    ii = 0
    while True: #check if the name already exists and generate new name by adding number
        if os.path.exists(output_path):
            ii = ii+1
            auto_fname = station_name + "_" + d_type + "_" + p_ts + "_" + p_te + "_" + prcss + "_("+str(ii)+")" + ".csv"
            output_path = fp.replace(os.path.basename(fp),auto_fname) #file path without file name
        else:
            break
# save the new file in the users location by the selected name if user selec a path  
    output.to_csv(output_path , sep=',', na_rep = "None", float_format='%G', index=False,
              header=hdr, encoding='utf-8') 
    print("all ok5")	
    data.columns = list(pi.iloc[0,:]) # switch the data columns to the parametrs name
    print("The new file saved as:" + auto_fname)
    return output_path,output,data
"""=============================================================================
FUNCTION (interval period):

============================================================================="""
def def_intper(data):
    time = data.iloc[:,0] # time vector
    dtime = pd.Series(index = range(len(time)))    
    for i in range(len(time)-1):
        dtime[i] = time[i+1] - time[i] # time difference between two adjacent row
    tt = pd.DataFrame(index = range(len(time)) , columns = ["time","delta_time"]) # new dataframe    
    tt.iloc[:,0] = time
    tt.iloc[:,1] = dtime
    temp2 = []
    temp3 = []
    start = 0
    for i in range(len(time)-1):
        temp2 = (dtime[i] == dtime[i+1])
        if temp2 == False: # in case of two different adjacent time interval
            end = i+1
            dt_m = dtime[i] / np.timedelta64(1,"m") # calculate the difference based on minute
            dt_h = dtime[i] / np.timedelta64(1,"h") # calculate the difference based on hour
            dt_d = dtime[i] / np.timedelta64(1,"D") # calculate the difference based on day
            if dt_d >= 1: # if the difference was greater than a day use DAY as unit
                dt2 = round(dt_d,1)
                dt_unit = "Day(s)"
            elif dt_h >= 1: # if the difference was greater than a day use HOUR as unit
                dt2 = round(dt_h,1)
                dt_unit = "Hour(s)"
            else: # if the difference was greater than a day use MINUTE as unit
                dt2 = round(dt_m,1)
                dt_unit = "Minute(s)"
            N_data = end - start # count how many data were recorded with this time interval
            temp3.append([time[start],time[end],N_data,dtime[i],dt2,dt_unit,start,end]) # store all the info in a list
            start = i+1 # start counting from the new interval               
    N_periods = pd.DataFrame(index = range(len(temp3)),columns = \
                             ["t_start","t_end","N_data","dt","dt2","dt_unit","i_start","i_end"])
    for i in range(len(temp3)): # add the info from each interval to the final dataframe
        N_periods.iloc[i,0] = temp3[i][0]
        N_periods.iloc[i,1] = temp3[i][1]
        N_periods.iloc[i,2] = temp3[i][2]
        N_periods.iloc[i,3] = temp3[i][3]
        N_periods.iloc[i,4] = temp3[i][4]
        N_periods.iloc[i,5] = temp3[i][5]
        N_periods.iloc[i,6] = temp3[i][6]
        N_periods.iloc[i,7] = temp3[i][7]
    N_periods.iloc[-1,1] = time[len(time)-1] # set last recorded time for the last time interval period
    N_periods.iloc[-1,2] = N_periods.iloc[-1,2]+1 # count the number of last time interval one more
    N_periods.iloc[-1,-1] = N_periods.iloc[-1,-1]+1 # add one to the last index of the last time interval
    return N_periods
"""=============================================================================
FUNCTION (file info):
This function extracts and print the information of the selected file such as:
type of the data, station name, data, recorded time intervals, index of rows with
missing value
def_intper
============================================================================="""
def defext_info(fp,si,pi,data,prnt):
    appf = False # not appended file
    crctun = False
    filt = False
    if len(fp) != 0: # check if any file is selected
        fn = os.path.basename(fp) # extract the name of the csv file
#..............................................................................
# Type of the data (local,satellite,appended)        
    if si.iloc[0, 0] == "TOA5": # check if it is a local data
        d_type = "Local" # type of the data
        station_name = si.iloc[0, 1] # station name
        if "Appended" in list(si.iloc[0,:]): # check if this file was appended before
            appf = True # appended file 
            apnd1 = si.iloc[0,8] # first source of the appended file
            apnd2 = si.iloc[0,10] # second source of the appended file
        if "crct_unit" in list(si.iloc[0,:]):
            crctun = True
            crctun1 = si.iloc[0,13]
        if "filtered" in list(si.iloc[0,:]):
            filt = True
            filt1 = si.iloc[0,15]
    else:
        d_type = "Satellite" # type of the data
        station_name = data.iloc[1, 1] # station name
        if "Appended" in list(si.iloc[0,:]): #
            appf = True # appended file
            apnd1 = si.iloc[0,0] # first source of the appended file
            apnd2 = si.iloc[0,2] # second source of the appended file
#.............................................................................. 
# coorect the format of the station name
    if ' ' in station_name:
        station_name = station_name.replace(' ','')
    if '_' in station_name:
        station_name = station_name.replace('_','')             
    station_name = station_name[0].upper() + station_name[1:].lower()
    if station_name == "Lacampana":
        station_name = "La Campana"
    if station_name == "Santagracia":
        station_name = "Santa Gracia"
    if station_name == "Nahuelbuta":
        station_name = "Nahuelbuta"
    if station_name == "Pandeazucar":
        station_name = "Pan de Azu" + u"\u0301" + "car"
    if station_name == "Wannetue":
        station_name = "Tuebingen"        
#..............................................................................     
    data.columns = pi.iloc[0] # set the parameters name as columns name 
    data = data.replace(to_replace = 'None', value = np.nan) #replace any NONE value with numpy.nan
    data = data.replace(to_replace = ' None', value = np.nan) #replace any NONE value with numpy.nan
    data = data.replace(to_replace = 'None ', value = np.nan) #replace any NONE value with numpy.nan
    n_p = data.shape[1] # number of parameters (columns)
#..............................................................................    
    data.iloc[:,0] = pd.to_datetime(data.iloc[:,0]) # convert thje first column of the data to time format
    if d_type == "Local": # for local data
        data.iloc[:,1:] = data.iloc[:,1:].astype(float) # change the format of all the data except time to float
    else: # for satellite data
        data.iloc[:,1] = data.iloc[:,1].astype(str) # change the format of the second column (station name) to string
        data.iloc[:,2:] = data.iloc[:,2:].astype(float) # change the format of the rest of the data to float
#..............................................................................
    t_start = data.iloc[0, 0] # date and time of the first recorded data
    t_end = data.iloc[len(data) - 1, 0] # date and time of the last recorded data
    nan_ind = pd.isnull(data).any(1).nonzero()[0] # find the index of rows with at least one missing (nan) value
    time = data.iloc[:,0] # time vector
    t_delta_time = []
    for i in range(1,len(time)): 
        t_delta_time.append(str(time[i]-time[i-1])) # time difference between two adjacent row
    delta_t,icx = np.unique(t_delta_time,return_counts=True) # count the number of different time interval
    t_int = len(delta_t) # number of different recorded time interval
    N_periods = def_intper(data) # extract the information of the recorded time intervals
#..............................................................................
# print the file report    
    if prnt == True:
        print("File name:------------------------------------- " + fn)
        if appf == True:
            print("This is an appended file: \n"
                  + apnd1 + "\n"
                  + apnd2 + "\n")
        if crctun == True:
            print("The file has corrected units until: " + crctun1)
        if filt == True:
            print("This is a maintenance and anomalies filtered file until: " + filt1)             
        print("Data type:------------------------------------- " + d_type + "\n"
              "Station name:---------------------------------- " + station_name + "\n"
              "Number of columns:----------------------------- " + str(n_p))
        print("First record:---------------------------------- " + str(t_start))
        print("Last record:----------------------------------- " + str(t_end))
        if len(nan_ind) != 0:
            print("Number of rows with missing data (none):------- " + str(len(nan_ind)))        
        for i in range(len(N_periods)):
            temp1 = N_periods.iloc[i,:]
            temp2 = {"from":str(temp1[0]),"to":str(temp1[1]),"dt":str(temp1[4]),"dt_unit":temp1[5],"data":str(temp1[2])}
            print("{0[from]:19} --> {0[to]:19} || Recorded interval: {0[dt]:5}{0[dt_unit]:9} || Number of data: {0[data]:5}".format(temp2))                 
    return d_type,station_name,data,t_int,nan_ind
"""=============================================================================
FUNCTION (Unique time interval):
If there is more than one time interval in the file or
if there are some gaps (like missing rows) it makes new row(s) filled by "nan"
to correct the whole file with one unique timestamp based on the file type
"30 min" for local files
"1 hour" for satellite files 
============================================================================="""
def definterval_fix(data,d_type):
    if d_type == "Local":
        ini_int = 30 # local time step
        time_type = "m" #minutes
    elif d_type == "Satellite":
        ini_int = 1 # satellite time step
        time_type = "h" # hour
    time = data.iloc[:,0] # first column of the data as time column
    len_dat = len(time) # number of recorded data
    t_delta_time = []
    t_delta_ind = []
    gaps = []
    for i in range(1,len(time)):
        t_delta_time.append(str(time[i]-time[i-1])) # list of time difference between two adjacent row
        if int((time[i]-time[i-1]) / np.timedelta64(ini_int,time_type)) > 1: # if the difference is bigger than one unit (30 min or 1h depends to the type)
            t_delta_ind.append(i) # store that index
            n_gap = int((time[i]-time[i-1]) / np.timedelta64(ini_int,time_type))-1 # count how many rows are missing between those two rows
            gaps.append(n_gap) # make a list of the gaps
            len_dat = len_dat + n_gap # increase the length of the data by the number of missing gaps
    for i in range(1,len_dat): # now with the new length of the data
        t_delta_time.append(str(time[i]-time[i-1])) # list of time difference between two adjacent row
        if int((time[i]-time[i-1]) / np.timedelta64(ini_int,time_type)) > 1: # if the difference is bigger than one unit (30 min or 1h depends to the type)
            t_delta_ind.append(i) # store that index
            n_gap = int((time[i]-time[i-1]) / np.timedelta64(ini_int,time_type))-1 # count how many rows are missing between those two rows
            nRn = pd.DataFrame(index=range(n_gap),columns=data.columns.values) # make a new data frame with the size of the missing rows between two adjacent row
            for j in range(n_gap):
                nRn.iloc[j,0] = data.iloc[i-1,0] + pd.to_timedelta(str(((j+1)*ini_int))+time_type) # set the new time (the first missing row is the time of the upper row plus unit of time depends on the type of the data)
                nRn.iloc[j,1] = data.iloc[0,1] # station name in the second column of the satellite data
            data = data.iloc[:i,:].append(nRn).append(data.iloc[i:,:]).reset_index(drop=True) # add the new missing dataframe between the two rows
            time = data.iloc[:,0] # update the time vector
    if d_type == "Local":        
        data.iloc[:,1] = range(1,len(data)+1) #Update the number of records in the second columns of the LOCAL data      
    return data
"""=============================================================================
FUNCTION (fix the columns names and parameters):
============================================================================="""
def deffix_columns(pi,si,data,d_type):
    data = pi.append(data, ignore_index=True)
    if d_type == "Local": # default column names for LOCAL file
        for i in pi.iloc[0,:]:
            if ("WSData2_WVc(3)" in i):
                pi.loc[0,i] = "WSData2_WVc"
                pi.columns = pi.iloc[0,:]
                data.columns = pi.iloc[0,:]
        org_col = ["TIMESTAMP","RECORD","BattV_Avg","PTemp_C_Avg","AirTC_Avg","RH",
                   "PVap_Avg","SlrW_Avg","SlrMJ_Tot","VWC_Avg","GrTemp_Avg","EC_Avg",
                   "P_Avg","PA_Avg","VR_Avg","WS_ms_Avg","WS_ms_max","WS_ms_min"
                   ,"WindDir_Avg","WS_ms_S_WVT","WindDir_D1_WVT","WSData2_WVc","Rain_mm_Tot",
                   "BP_mbar_Avg","NaNCounter","WSDiag","VaporPres","SeaLevelPres"]
        org_col2 = ["TS","RN","Volts","Deg C","Deg C","%","kPa","W/m²","MJ/m²","m³/m³"\
                    ,"Deg C","mS/m","-","nSec","-","m/s","m/s"\
                    ,"m/s","Deg","m/s","Deg","Deg","mm","mbar","-","-","-","-"]
        org_col3 = ["-","-","Avg","Avg","Avg","Smp","Avg","Avg","Tot","Avg","Avg","Avg","Avg","Avg"\
                    ,"Avg","Avg","Max","Min","Avg","WVc","WVc","WVc","Tot","Avg","Smp","Smp","Smp","Smp"]
    elif d_type == "Satellite": # default column names for SATELLITE file
        for i in pi.iloc[0,:]:
            if i[0] == " ":
                pi.loc[0,i] = i[2:]                
        org_col = ["Timestamp","Station name","Air temperature","Air relative humidity",
                   "Solar radiation","Soil water content","Soil temperature","Wind speed",
                   "Wind max","Wind direction","Precipitation","Air pressure"]
        org_col2 = ["-","-","Deg C","%","W/m²","m³/m³","Deg C","m/s","m/s","Deg","mm","mbar"]   
    temp = [x for x in org_col if x not in pi.iloc[0,:]]    
    for i in range(len(temp)):
        data[temp[i]] = np.nan
    data = data[org_col]
    data.iloc[0,:] = org_col
    if d_type == "Local":
        data.iloc[1,:] = org_col2
        data.iloc[2,:] = org_col3
        pi = data.iloc[:3,:].reset_index(drop=True)
        data = data.iloc[3:,:].reset_index(drop=True)
    elif d_type == "Satellite":
        data.iloc[1,:] = org_col2
        pi = data.iloc[:2,:].reset_index(drop=True)
        data = data.iloc[2:,:].reset_index(drop=True)
#..............................................................................
# Conver units
    data = data.replace(to_replace = 'None', value = np.nan) #replace any NONE value with numpy.nan
    data = data.replace(to_replace = ' None', value = np.nan) #replace any NONE value with numpy.nan
    data = data.replace(to_replace = 'None ', value = np.nan) #replace any NONE value with numpy.nan        
    data.iloc[:,0] = pd.to_datetime(data.iloc[:,0]) # convert thje first column of the data to time format
    if d_type == "Local": # for local data
        data.iloc[:,1:] = data.iloc[:,1:].astype(float) # change the format of all the data except time to float
    else: # for satellite data
        data.iloc[:,1] = data.iloc[:,1].astype(str) # change the format of the second column (station name) to string
        data.iloc[:,2:] = data.iloc[:,2:].astype(float) # change the format of the rest of the data to float        
    if si.shape[1] < pi.shape[1]:
        sii = pd.DataFrame(" ",[0],range(pi.shape[1]))
        sii.iloc[0,0:si.shape[1]] = si.iloc[0,:]
        si = sii
    return data,pi,si
"""=============================================================================
FUNCTION ():
============================================================================="""
def defcheck_int(data):
    nan_ind = pd.isnull(data).any(1).nonzero()[0] # find the index of rows with at least one missing (nan) value
    time = data.iloc[:,0] # time vector
    t_delta_time = []
    for i in range(1,len(time)): 
        t_delta_time.append(str(time[i]-time[i-1])) # time difference between two adjacent row
    delta_t,icx = np.unique(t_delta_time,return_counts=True) # count the number of different time interval
    t_int = len(delta_t) # number of different recorded time interval
    return t_int, nan_ind
"""=============================================================================
FUNCTION ():
============================================================================="""
def defmaint(maintfilt,fp,data,station_name,si,d_type):   
    if maintfilt == "1" and len(fp) != 0:
        # read the maintenance file and filter the data by replacing them with nan   
        if station_name == "La Campana":
            sheet = "LC"
        if station_name == "Nahuelbuta":
            sheet = "Na"
        if station_name == "Santa Gracia":
            sheet = "SG"
        if station_name == "Pan de Azu" + u"\u0301" + "car" or station_name == "Pan de Azucar":
            sheet = "PdA"        
        mf = pd.read_excel(fp,sheet,header=None)
        mf.columns = range(mf.shape[1])
        for i in range(4,mf.shape[0]):
            fst = mf.iloc[i,0]
            fnd = mf.iloc[i,1]
            try:
                B1 = data.iloc[:,0] >= fst
                B2 = data.iloc[:,0] <= fnd
                B = np.logical_and(B1,B2)
                m_ind = B.index[B].tolist()
                
                B = mf.iloc[i,2:] == "None"
                if d_type == "Satellite":            
                    m_col = B.index[B].tolist()
                    m_col2 = mf.iloc[3,m_col].reset_index(drop=True)
                    m_col3 = m_col2.dropna(axis=0, how='any').tolist()
                    data.iloc[m_ind,m_col3] = np.nan
                elif d_type == "Local":
                    m_col = B.index[B].tolist()
                    m_col2 = mf.iloc[1,m_col].reset_index(drop=True)
                    m_col3 = m_col2.dropna(axis=0, how='any').tolist()
                    data.iloc[m_ind,m_col3] = np.nan
            except:
                pass
    if (maintfilt == "1") or (maintfilt == "2"):
#..............................................................................    
        # fix the zero value in soil temperature
        if d_type == "Local":
            soil_sensor = ["VWC_Avg","GrTemp_Avg","EC_Avg","P_Avg","PA_Avg","VR_Avg"]
            B1 = (data.loc[:,"GrTemp_Avg"] == 0)
            B2 = (data.loc[:,"VWC_Avg"] == 0)
            B = np.logical_and(B1,B2)
            fail_ind = B.index[B].tolist()
            data.loc[fail_ind,soil_sensor] = np.nan        
        elif d_type == "Satellite":
            B1 = (data.iloc[:,5] == 0)
            B2 = (data.iloc[:,6] == 0)
            B = np.logical_and(B1,B2)
            fail_ind = B.index[B].tolist()
            data.iloc[fail_ind,[5,6]] = np.nan 
#..............................................................................
        # wind_diag (only works for LOCAL files)
        wind_sensor = ["WS_ms_Avg","WS_ms_max","WS_ms_min","WindDir_Avg","WS_ms_S_WVT","WindDir_D1_WVT","WSData2_WVc"]        
        if d_type == "Local":            
            B1 = (data.loc[:,"WSDiag"] != 0)
            temp = data.loc[:,"WSDiag"].replace(to_replace = np.nan, value = "None")
            B2 = (temp != "None")
            B = np.logical_and(B1,B2)
            fail_ind = B.index[B].tolist()
            data.loc[fail_ind,wind_sensor] = np.nan
#..............................................................................
        # filter wind parameters based on anomalies in wind speed average
        if d_type == "Local":
            B = (data.loc[:,"WS_ms_Avg"] > 10)
            fail_ind = B.index[B].tolist()
            data.loc[fail_ind,wind_sensor] = np.nan
        elif d_type == "Satellite":
            B = (data.iloc[:,7] > 10)
            fail_ind = B.index[B].tolist()
            data.iloc[fail_ind,[7,8,9]] = np.nan
#..............................................................................
        # filter wind parameters based on anomalies in wind speed max
        if d_type == "Local":    
            B = (data.loc[:,"WS_ms_max"] > 20)
            fail_ind = B.index[B].tolist()
            data.loc[fail_ind,wind_sensor] = np.nan
        elif d_type == "Satellite":
            B = (data.iloc[:,8] > 20)
            fail_ind = B.index[B].tolist()
            data.iloc[fail_ind,[7,8,9]] = np.nan            
#..............................................................................
        # filter wind parameters based on anomalies in wind direction
        if d_type == "Local":    
            B = (data.loc[:,"WindDir_Avg"] > 360)
            fail_ind = B.index[B].tolist()
            data.loc[fail_ind,wind_sensor] = np.nan
        elif d_type == "Satellite":
            B = (data.iloc[:,9] > 360)
            fail_ind = B.index[B].tolist()
            data.iloc[fail_ind,[7,8,9]] = np.nan

    if d_type == "Local":
        si.iloc[0,12] = "filtered"
        si.iloc[0,13] = data.iloc[-1,0]   
    if d_type == "Satellite":
        si.iloc[0,4] = "filtered"
        si.iloc[0,5] = data.iloc[-1,0]
    if (maintfilt == "3"):
        pass

#    if station_name == "La Campana":
#        maint_per = [["2016.11.14 16:00","2016.11.14 18:00"],
#                     ["2017.05.08 9:00","2017.05.08 14:00"],
#                     ["2018.03.11 8:30","2018.03.11 11:30"]]
#    if station_name == "Nahuelbuta":
#        maint_per = [["2016.11.04 9:30","2016.11.04 10:30"],
#                     ["2017.05.05 9:00","2017.05.05 16:30"],
#                     ["2018.03.08 8:30","2018.03.08 11:00"]]
#    if station_name == "Santa Gracia":
#        maint_per = [["2016.11.10 11:00","2016.11.10 11:30"],
#                     ["2017.05.15 11:00","2017.05.15 15:00"],
#                     ["2018.03.18 9:00","2018.03.18 11:30"]]
#    if station_name == "Pan de Azu" + u"\u0301" + "car":
#        maint_per = [["2016.11.08 12:30","2016.11.08 14:00"],
#                     ["2017.05.11 8:00","2017.05.11 11:30"],
#                     ["2018.03.14 15:30","2018.03.14 17:30"]]
   
    return data,si
"""=============================================================================
FUNCTION (Fix EC_Avg unit for local files):

============================================================================="""
def defEC_unit(data,station_name,si,pi):
    if station_name == "La Campana":
        ind_c = pd.to_datetime("2017-05-08 12:30")
    if station_name == "Nahuelbuta":
        ind_c = pd.to_datetime("2017-05-05 16:00")
    if station_name == "Santa Gracia":
        ind_c = pd.to_datetime("2017-05-15 16:00")
    if station_name == "Pan de Azucar":
        ind_c = pd.to_datetime("2017-05-11 11:30")


    if si.iloc[0,14] != "crct_unit":
        B = data.iloc[:,0] < ind_c
        indB = B.index[B].tolist()
        data.loc[indB,"EC_Avg"] = data.loc[indB,"EC_Avg"] * 100
        
        B = data.iloc[:,0] >= ind_c
        indB = B.index[B].tolist()
        data.loc[indB,"EC_Avg"] = data.loc[indB,"EC_Avg"] / 10
        
        si.iloc[0,14] = "crct_unit"
        si.iloc[0,15] = data.iloc[-1,0]
        pi.loc[1,"EC_Avg"] = "mS/m"
    else:
        crct_end = pd.to_datetime(si.iloc[0,15])
        if crct_end < data.iloc[-1,0]:
            B = data.iloc[:,0] > crct_end
            indB = B.index[B].tolist()
            data.loc[indB,"EC_Avg"] = data.loc[indB,"EC_Avg"] * 100
            si.iloc[0,15] = data.iloc[-1,0]
            pi["EC_Avg"] = "mS/m" 
            
    return data,si,pi 
"""**********************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
**********************************************************************************************************"""
"""PACKAGE OF FUNCTIONS (FILE INFO)"""
"""FUNCTION START"""
"""=============================================================================
FUNCTION (Extract missing data and time periods as a .txt report):

============================================================================="""
def defmissing_ext(fp,pi,data,nan_ind,wtd):
    NP_ind,N_data,N_periods = [],[],[] # empty lis of the outputs
#..............................................................................    
    if wtd == "2" or wtd == "3": # make a full report of the missing values (dates and parameters)
        N_data = pd.DataFrame(index = range(len(nan_ind)),columns=range(data.shape[1]-1)) # the missing values in the rows
        NP_ind = pd.DataFrame(index = range(len(nan_ind)),columns=range(data.shape[1]-2)) # the columns index with missing values
        for i in range(len(nan_ind)):
            N_data.iloc[i,0] = data.iloc[nan_ind[i],0] # time of the missing row as first column
            NP_ind_temp = np.where(pd.isnull(data.iloc[nan_ind[i],:]))[0] # index of the columns with missing values in each row
            for j in range(len(NP_ind_temp)):
                NP_ind.iloc[i,j] = NP_ind_temp[j] 
                N_data.iloc[i,j+1] = str(pi.iloc[0,NP_ind_temp[j]]) # name of the missing parameters in each row
#..............................................................................
# if the rows with missing values are next to each other, consider it as a period of time and find the first and last time of that period
# if there are rows with missing values with time distance from other missing rows, just consider it individually                
    if wtd == "1" or wtd == "3": # make a simple periodic list of the missing values (only dates)
        temp2 = [] 
        lst_N_periods = []       
        for i in range(len(nan_ind)):  
            if i == len(nan_ind)-1: # temp1 for the last row with missing value
                temp1 = (nan_ind[i]-1 == nan_ind[i-1]) # TRUE if the last two missing rows are next to each other
            else: # temp1 for the other rows
                temp1 = (nan_ind[i]+1 == nan_ind[i+1]) # TRUE if there are two missing rows next to each other
#..............................................................................
            if temp1 == True: #if two rows with missing values are next to each other
                temp2.append(nan_ind[i]) # add the index of that row to the end of temp2
                if i == len(nan_ind)-1: # if "i" is the last row of the missing rows
                    lst_N_periods.append([data.iloc[min(temp2),0],data.iloc[nan_ind[i],0]]) # make a time period from the min of temp2 to the present "i"
            elif temp1 == False and temp2 != []:
                lst_N_periods.append([data.iloc[min(temp2),0],data.iloc[nan_ind[i],0]]) # period of time
                temp2 = []
            elif temp1 == False and temp2 == []:
                lst_N_periods.append([data.iloc[nan_ind[i],0],np.nan]) # individual time
            elif temp1 == False and i == len(nan_ind)-1:
                lst_N_periods.append([data.iloc[nan_ind[i],0],np.nan]) # individual time
#..............................................................................            
        N_periods = pd.DataFrame(index = range(len(lst_N_periods)),columns = ["F","T"])
        for i in range(len(lst_N_periods)):
            N_periods.iloc[i,0] = lst_N_periods[i][0] #period starts
            N_periods.iloc[i,1] = lst_N_periods[i][1] #period ends
#..............................................................................
    fn = os.path.basename(fp) # take the name of the selected csv file
    fn_temp = fn.replace("csv","txt") # chenge the csv to txt
    ftemp = fp.replace(fn,"") # remove the name of the csv file from the file path
#..............................................................................    
    if wtd == "2" or wtd == "3": # save the full report as txt in same folder as the selected csv file
        N_data.to_csv(ftemp+"Missing_full_"+fn_temp , sep=',', float_format='%G',
                      index=False, header=False, encoding='utf-8')
        if platform == "darwin":
            print('\a')
            spc(["open",ftemp+"Missing_full_"+fn_temp])
        elif platform == "win32":
            winsound.Beep(frequency, duration)
            os.startfile(ftemp+"Missing_full_"+fn_temp) # open the generated txt file 
#..............................................................................                  
    if wtd == "1" or wtd == "3": # save the periodic report as txt in same folder as the selected csv file            
        N_periods.to_csv(ftemp+"Missing_periods_"+fn_temp , sep=',', float_format='%G',
                         index=False, header=False, encoding='utf-8')
        if platform == "darwin":
            print('\a')
            spc(["open",ftemp+"Missing_periods_"+fn_temp])
        elif platform == "win32":
            winsound.Beep(frequency, duration)
            os.startfile(ftemp+"Missing_periods_"+fn_temp)               
    input("________________________________________ SAVE AND OPEN THE MISSING DATA \n"
          "* Saved as:-------------- Missing_(full/periods)_" +fn_temp + "\n"
          "* In:-------------------- " + ftemp + "\n"          
          "Press any key (MAIN MENU) >>> ")            
    return NP_ind,N_data,N_periods
"""=============================================================================
FUNCTION (File info and time interval correction):
This function exctracts the file information and print a report of it
Checks if the recording time intervals are unique
There is no input or output for this function
Three functions are using inside this function:
1-defuiopen: opens a file dialog for the user to import a csv.file
2-defext_info: extracts the selected files info and print a report of it
3-defmissing_ext: looks for the missing values and make a report of them as .txt
============================================================================="""
def deffile_info():
    #filepath, firstline, parameters, data, index of rows with missing data
    fp,si,pi,data,nan_ind = [],[],[],[],[] 
    wtd = [] # what to do?
#..............................................................................    
    while True:
        print("________________________________________ IMPORT A FILE ")
        fp,si,pi,data = defuiopen("Select a *.CSV file") # select a new file
        if len(fp) == 0: # if the user doesn't select anything ask to try again or go back to main menu
            while True:
                re_imp = input ("________________________________________ NO IMPORTED FILE"
                                "\n1: Try again"
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> ") 
                if re_imp == "1":
                    break
                if re_imp == "mm":
                    return
#..............................................................................                
        else: # if the user select a correct scv file
            # get a report of the selected file as:
            # type of the file, station name, recorded data, _, index of rows with missing values 
            print("________________________________________ FILE REPORT")
            d_type,station_name,data,_,nan_ind = defext_info(fp,si,pi,data,True) 
            input("press any key to continue >>> ")
#..............................................................................            
            if len(nan_ind) > 0: # if there are rows with missing values, get a report of them
                while True:
                    wtd = input("________________________________________ EXTRACT THE MISSING DATA (NONE) "
                                "\n1: Only timestamp (faster) in a period format"
                                "\n2: Timestamp and the missing data (none) \n" +
                                "   *Not recommended for too many missing rows (more than 1500 rows)"
                                "\n3: Options 1 and 2"
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> ")
                    if wtd == "1" or wtd == "2" or wtd == "3":
                        print("________________________________________ SEARCHING FOR THE MISSING DATA \n"
                              "please wait...")
                        _,_,_ = defmissing_ext(fp,pi,data,nan_ind,wtd) # look for the missing values and make a report of them
                        return
                    elif wtd == "mm":
                        return
            else:
                return                                            
"""**********************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
**********************************************************************************************************"""
"""PACKAGE OF FUNCTIONS (PLOT)"""
"""=============================================================================
FUNCTION (trend and detrend):
Moving average
Linear trend
Detrend
============================================================================="""
def deftrend(LPF_m,data,datplt,ind_p):
    datLPF,datDeTr,regLine = [],[],[]
    try:
        dta = data.iloc[:,ind_p].as_matrix(columns=None)
    except:
        dta = data[:,ind_p]      
    dta[dta==-9999] = np.nan
    nt,nv = dta.shape #get number of time steps and variables
    nan_ind = []
    if ("3" in datplt) or ("4" in datplt):
        datLPF    = np.zeros((nt,nv)) #create matrix of zeros for low pass filtered data
        datLPF.fill(np.nan) #reset to NaN      
        for i in range(int((LPF_m-1)/2)-1,int(nt-((LPF_m-1)/2))): #loop through time steps (leave margin depending on LPF setup)
            for v in range(nv): #count missing values for variables separately
                missCount = 0 #reset missing values counter to zero
                sumV = 0.0      #reset sums            
                for j in range(LPF_m): #loop through indices for one mean calculation
                    t = int(i-(((LPF_m-1)/2))+j) #calculate actual time steps for indices                
                    if pd.isnull(dta[t,v]) == True:
                        missCount = int(missCount+1) #update missing value counter if needed          
                    else:
                        sumV = sumV + dta[t,v] #sum up data (that does not include missing values)
                if missCount == LPF_m: #all values used for one mean are missing values                   
                    datLPF[i,v] = np.nan #assign missing value to LPF data
                else:
                    datLPF[i,v] = sumV / (LPF_m-missCount) #calculate mean (sum/no. of values that weren't missing values)    
                nan_ind = list(pd.isnull(dta[:,[v]]).any(1).nonzero()[0])
                datLPF[nan_ind,v] = np.nan
    if ("2" in datplt) or ("5" in datplt) or ("6" in datplt):
        x = np.arange((nt)).reshape(nt)
        datDeTr  = np.zeros((nt,nv)) #create matrix of zeros for detrended data
        regLine  = np.zeros((nt,nv)) #create matrix of zeros for regression line        
        for v in range(nv):
            ind_not_nan = ~np.isnan(dta[:,v])            
            y = dta[:,v]
            m,b,_,_,_ = stats.linregress(x[ind_not_nan],y[ind_not_nan])
            regLine[:,v] = m*x+b           
            datDeTr[:,v] = y-(m*x)       
    return datLPF,datDeTr,regLine
"""=============================================================================
FUNCTION (plot_NORMAL):

============================================================================="""
def defrun_plot_normal():
    sctn_end = [] # section end is for modifying the already generated plots
    sctn = "1" # section 1 (import a file)
    while True:       
        if ("1" in sctn) or ("1" in sctn_end):
            while True:
                maintfilt = input("________________________________________ FILTER (MAINTENANCE & ANOMALIES) ???"
                             "\n1: YES (I have the maintenance file)"
                             "\n2: YES (I don't have the maintenance file)"
                             "\n3: NO (keep the data as it is)"
                             "\nmm: MAIN MENU \n"
                             "Enter a number >>> ")
                if maintfilt == "mm":
                    return
                elif maintfilt == "1":
                    print("________________________________________ IMPORT THE MAINTENANCE FILE")    
                    root = tk.Tk() 
                    root.withdraw()   
                    if platform == "darwin": # in mac
                        print('\a') 
                    elif platform == "win32": # in windows
                        winsound.Beep(frequency, duration)      
                    fp_maintfilt = filedialog.askopenfilename(title = "Import maintenance file",defaultextension ='.xlsx',
                           filetypes = (("CSV files","*.xlsx"),("all files","*.*")),parent = root)                    
                    break
                elif maintfilt == "2" or maintfilt == "3":
                    fp_maintfilt = []
                    break
                else:
                    pass                
            while True:
                print("________________________________________ IMPORT A *.CSV FILE")
                print("________________________________________ FILE REPORT (first file)")
                fp,si,pi,data,d_type,station_name,fn,t_start,t_end = \
                defuiopen("Select the first '*.CSV' file",[]) #select and import the first file
                if len(fp) == 0: # check if any file is selected
                    while True:
                        re_imp = input ("________________________________________ NO IMPORTED FILE"
                                        "\n1: Try again"
                                        "\nmm: MAIN MENU \n"
                                        "Enter a number >>> ") 
                        if re_imp == "1": # try to select a file
                            break
                        if re_imp == "mm": # back to the main menu
                            return
                else:
                    break
            while True:
                confirm = input("________________________________________ SELECT "
                                "\n1: Ooops, this is a wrong file (pick another)"
                                "\n2: NEXT (select a parameter)"
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> " )
                if confirm == "1": # select a wrong file (go back to select another one)
                    sctn = "1"
                    break
                elif confirm == "mm": # back to the main menu
                    return
                elif confirm == "2": # correct file, go to next step
                    print("________________________________________ PLEASE WAIT ... ")
                    print("Checking time intervals")
                    t_int,_ = defcheck_int(data)                                      
                    if t_int > 1:                                                
                        print("Unifying time intervals (data 1)")                                           
                        data = definterval_fix(data,d_type) # unify the time interval
                    print("Checking the columns and parameters (data 1)")
                    data,pi,si = deffix_columns(pi,si,data,d_type)                                        
                    if d_type == "Local":
                        print("Checking the units (data 1)")
                        data,si,pi = defEC_unit(data,station_name,si,pi)
                    if maintfilt == "1" or maintfilt == "2":
                        print("Filtering the anomalies and maintenances (data 1)")
                        data,si = defmaint(maintfilt,fp_maintfilt,data,station_name,si,d_type) # replace the maintenance with nan                       
                    t_start = data.iloc[0, 0] # date and time of the first recorded data
                    t_end = data.iloc[len(data) - 1, 0] # date and time of the last recorded data
                    sctn = "2" # permission for section 2                    
                    break
#==============================================================================                
        if sctn_end != []:
            sctn = []
        if "1" in sctn_end:
            sctn = "2"
            sctn_end = []
#==============================================================================                
        if ("2" in sctn) or ("2" in sctn_end): # section 2 (select parameters)
            fp1 = fp.replace(fn,"") #file path without file name
            time = data.iloc[:,0] # time vector
            if d_type == "Local":
                t_int_str = "30 minutes" # local time interval               
            elif d_type == "Satellite":
                t_int_str = "1 hour" # satellite time interval
            units = pi.iloc[1,2:].reset_index(drop=True) # units for local parameters
            param = pi.iloc[0,2:].reset_index(drop=True) # name of the parameters
            input_par=""
            for i in range(1,len(param)+1): # list of the parameters and their units in the selected file
                input_par = input_par + ("\n"+str(i)+":"+param[i-1]+" ["+units[i-1]+"]")             
            while True: # show the parameters to plot and let the user to select
                temp_p = input("________________________________________ PARAMETER [UNIT] \n"
                               "* USE COMMA TO COMBINE THEM \n"
                               + input_par[1:]+
                               "\nall: Plot all the parameters"
                               "\nb: BACK"
                               "\nmm: MAIN MENU \n"
                               "Enter a number (or combine them) >>> ")
                if temp_p == "b": # back
                    sctn = "1"
                    break
                elif temp_p == "mm": # main menu
                    return
                elif temp_p == "all": # select all
                    ind_p = list(np.arange(len(param))+2) #True colomn(s) of the seleceted parameter(s) 
                    sctn = "3" # permission for section 3                   
                    break                    
                else:
                    try:
                        int(temp_p.replace(",","")) # check if all the users input are only numbers and comma
                        temp_p2 = [int(x.strip())+1 for x in temp_p.split(',')] # list of the index of the selected parameters seperated by comma
                        if min(temp_p2) >= 2 and max(temp_p2) <= len(param)+1: # chek if the input values are in the range
                            ind_p = temp_p2 #True colomn(s) of the seleceted parameter(s)    
                            sctn = "3"  # permission for section 3                 
                            break
                        else: # in case of wrong input try again or main menu
                            while True:
                                par_again = input("________________________________________ WRONG INPUT (out of the range)"
                                                  "\n1: Try again"
                                                  "\nmm: MAIN MENU \n"
                                                  "Enter a number >>> ")
                                if par_again == "1":    
                                    break
                                elif par_again == "mm":
                                    return                            
                    except: # in case of wrong input try again or main menu
                        while True:
                            par_again = input("________________________________________ WRONG INPUT (wrong format)"
                                              "\n1: Try again"
                                              "\nmm: MAIN MENU \n"
                                              "Enter a number >>> ")
                            if par_again == "1":    
                                break
                            elif par_again == "mm":
                                return
            print("________________________________________ Detrending \n" 
                  "please wait...")
            _,dtrnd,LinTRND_w = deftrend([],data,["2","7"],ind_p) # calculate linear trend and detrend the selected parameters                          
#==============================================================================                
        if sctn_end != []:
            sctn = []
        if "2" in sctn_end:
            sctn = "3"
            sctn_end = []                            
#==============================================================================                
        if ("3" in sctn) or ("3" in sctn_end): # section 3 (select time period)
            while True: # select a time period to plot
                ind_t = input("________________________________________ TIME PERIOD"
                              "\n* Digit and 'd' (e.g. 1d plots last day)" # number of last days
                              "\n* Digit and 'w' (e.g. 4w plots last four weeks)" # number of last weeks
                              "\nall: The whole dataset" # plot the whole dataset
                              "\nman: Enter a time period manually (specific date and time)" # input a specific time period to plot
                              "\nb: BACK"
                              "\nmm: MAIN MENU \n"
                              "Enter a number >>> ")
                if ind_t == "b":
                    if sctn_end != []:
                        sctn_end = []
                        sctn = "9"
                        break
                    else:
                        sctn = "2"
                        break                    
                elif ind_t == "mm":
                    return
                elif ind_t == "all": # in case of plotting whole dataset
                    tstart = t_start
                    tend = t_end
                    ind_ts = int(time.loc[time == tstart].index.values) #index of the first record (start)
                    ind_te = int(time.loc[time == tend].index.values)+1 #index of the last record (end)
                    sctn = "4"                    
                    break
                elif ind_t == "man": # input the time period manually
                    while True:
                        try:
                            print("________________________________________ ATTENTION \n"
                                  "* First recorded data:-----------> " + str(t_start) + "\n"
                                  "* Last recorded data:------------> " + str(t_end) + "\n"
                                  "* Recorded interval:-------------> " + t_int_str + "\n"
                                  "________________________________________ ENTER (YYYY-MM-DD HH:MM)")
                            tstart = pd.to_datetime(input("Start:---------------------------> "))
                            tend = pd.to_datetime(input("End:-----------------------------> "))
                            if tstart >= t_start and tstart < t_end and tend <= t_end and tend > t_start:
                                ind_ts = int(time.loc[time == tstart].index.values) #index of the selected time (start)
                                ind_te = int(time.loc[time == tend].index.values)+1 #index of the selected time (end) 
                                sctn = "4"
                                break
                            else:                           
                                while True:
                                    man_again = input("________________________________________ WRONG INPUT (out of the range)"
                                          "\n1: Try again"
                                          "\nb: BACK"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> ")
                                    if man_again == "b" or man_again == "1":    
                                        break
                                    elif man_again == "mm":
                                        return
                                if man_again == "b":
                                    break                        
                        except:
                            while True:
                                man_again = input("________________________________________ WRONG INPUT (wrong format)"
                                      "\n1: Try again"
                                      "\nb: BACK"
                                      "\nmm: MAIN MENU \n"
                                      "Enter a number >>> ")
                                if man_again == "b" or man_again == "1":    
                                    break
                                elif man_again == "mm":
                                    return
                            if man_again == "b":
                                break                                                                        
                else:
                    try:
                        int(ind_t[:-1])
                        if (ind_t[-1] == "d" or ind_t[-1] == "w"):
                            if ind_t[-1] == "w":
                                ind_t = str(int(ind_t[:-1])*7)+"d"
                            tstart = t_end - pd.to_timedelta(ind_t)
                            tstart = tstart.to_pydatetime()
                            tstart = pd.Timestamp(str(tstart.year)+ "-"+ str(tstart.month) + "-" + str(tstart.day))
                            tend = t_end                            
                            if tstart >= t_start and tstart < t_end and tend <= t_end and tend > t_start:
                                ind_ts = int(time.loc[time == tstart].index.values) #index of the selected time (start)
                                ind_te = int(time.loc[time == tend].index.values)+1 #index of the selected time (end)                               
                                sctn = "4"
                                break
                            else:
                                while True:
                                    man_again = input("________________________________________ OUT OF THE RANGE"
                                          "\n1: Try again"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> ")
                                    if man_again == "1":    
                                        break
                                    elif man_again == "mm":
                                        return
                    except:
                        while True:
                            man_again = input("________________________________________ WRONG FORMAT"
                                  "\n1: Try again"
                                  "\nmm: MAIN MENU \n"
                                  "Enter a number >>> ")
                            if man_again == "1":    
                                break
                            elif man_again == "mm":
                                return
                if sctn == "4":
                    break                                    
#==============================================================================                
        if sctn_end != []:
            sctn = [] 
#==============================================================================
        if ("4" in sctn) or ("4" in sctn_end): # section 4 (what to show in the plot)
            while True:
                LPF_m = []
                datplt = input("________________________________________ DATA IN PLOT"
                              "\n1: Original data" # data (dataframe)
                              "\n2: De_trended data" # dtrnd (array)
                              "\n3: Moving average of the original data" # mavg_orig
                              "\n4: Moving average of the de_trended data" # mavg_dtrnd
                              "\n5: Linear trend of the whole dataset" # LinTRND_w
                              "\n6: Linear trend of the chosen time period" # LinTRND_tp
                              "\nall: Plot all"
                              "\nb: BACK"
                              "\nmm: MAIN MENU \n"
                              "Enter a number (or combine them by comma) >>> ")
                if datplt == "b":
                    if sctn_end != []:
                        sctn_end = []
                        sctn = "9"
                        break
                    else:
                        sctn = "3"
                        break                    
                if datplt == "mm":
                    return            
                if ("1" in datplt) or ("2" in datplt) or ("3" in datplt) or ("4" in datplt) or\
                ("5" in datplt) or ("6" in datplt) or ("all" in datplt):
                    if ("3" in datplt) or ("4" in datplt) or ("all" in datplt):
                        while True: # in case of moving average enter the number of samples
                            LPF_m = input("________________________________________ MOVING AVERAGE SAMPLES"
                                              "\nb: BACK"
                                              "\nmm: MAIN MENU \n"
                                              "Enter the number of samples to calculate moving average (odd integer): >>> ")
                            if LPF_m == "b":
                                break
                            if LPF_m == "mm":
                                return
                            try:
                                mavgs = int(round(float(LPF_m),0))
                                if (mavgs % 2) == 0: #if sample number for means is even
                                    mavgs = str(mavgs + 1)
                                else:
                                    mavgs = str(mavgs)                                    
                                print("________________________________________ CALCULATING MOVING AVERAGE \n"
                                      "please wait...")
                                if ("3" in datplt) or ("all" in datplt):
                                    mavg_orig,_,_ = deftrend(int(mavgs),data,["3"],ind_p) # moving average of the original data
                                if ("4" in datplt) or ("all" in datplt):    
                                    mavg_dtrnd,_,_ = deftrend(int(mavgs),dtrnd,["4"],range(LinTRND_w.shape[1])) # moving average of the detrended data
                                if d_type == "Satellite": # show the label of the moving average in the legend
                                    mavg_samp = mavgs + "h"
                                elif d_type == "Local": # show the label of the moving average in the legend
                                    mavg_samp = str(int(mavgs)/2) + "h"
                                break
                            except:
                                   input("WRONG INPUT, press ENTER and try again...")
                    if LPF_m != "b":                                   
                        if ("6" in datplt) or ("all" in datplt):
                            _,_,LinTRND_tp = deftrend([],data.iloc[ind_ts:ind_te,:],["6"],ind_p) # linear trend of the chosen time period
                        sctn = "5"
                        break
#==============================================================================                
        if sctn_end != []:
            sctn = [] 
#==============================================================================
        if ("5" in sctn) or ("5" in sctn_end): # section 5 (plot style)
            while True:
                pltyp = input("________________________________________ PLOT STYLE "
                              "\n1: Line & Scatter (recommended)"
                              "\n2: Line"
                              "\n3: Scatter"
                              "\nb: BACK"
                              "\nmm: MAIN MENU \n"
                              "Enter a number >>> ")
                if pltyp == "b":
                    if sctn_end != []:
                        sctn_end = []
                        sctn = "9"
                        break
                    else:
                        sctn = "4"
                        break                    
                elif pltyp == "mm":
                    return
                elif pltyp == "1" or pltyp == "2" or pltyp == "3":     
                    sctn = "6"
                    break
#==============================================================================                
        if sctn_end != []:
            sctn = [] 
#==============================================================================
        if ("6" in sctn) or ("6" in sctn_end) or ("3" in sctn_end) or ("4" in sctn_end): # section 6 (y axis)                
            while True:        
                ymn,ymx = [],[]
                ymn_org,ymx_org = [],[]
                ymn_data,ymx_data = np.nan , np.nan
                ymn_dtrnd,ymx_dtrnd = np.nan , np.nan
                ymn_mavg_orig,ymx_mavg_orig = np.nan, np.nan
                ymn_mavg_dtrnd,ymx_mavg_dtrnd = np.nan, np.nan
                ymn_ltrnd_w,ymx_ltrnd_w,ymn_ltrnd_tp,ymx_ltrnd_tp = np.nan, np.nan, np.nan, np.nan
                for i in range(len(ind_p)): # plot each chosen parameter
                    if "1" in datplt or ("all" in datplt): # original data
                        ymn_data = np.nanmin(np.array(data.iloc[ind_ts:ind_te,ind_p[i]])) # min of the selected time period
                        ymx_data = np.nanmax(np.array(data.iloc[ind_ts:ind_te,ind_p[i]])) # max of the selected time period               
                    if "2" in datplt or ("all" in datplt): # detrended data
                        ymn_dtrnd = np.nanmin(dtrnd[ind_ts:ind_te,i]) # min of the selected time period
                        ymx_dtrnd = np.nanmax(dtrnd[ind_ts:ind_te,i]) # max of the selected time period
                    if "3" in datplt or ("all" in datplt): # moving average original
                        ymn_mavg_orig = np.nanmin(mavg_orig[ind_ts:ind_te,i]) # min of the selected time period
                        ymx_mavg_orig = np.nanmax(mavg_orig[ind_ts:ind_te,i]) # max of the selected time period                            
                    if "4" in datplt or ("all" in datplt): # moving average detrend
                        ymn_mavg_dtrnd = np.nanmin(mavg_dtrnd[ind_ts:ind_te,i]) # min of the selected time period
                        ymx_mavg_dtrnd = np.nanmax(mavg_dtrnd[ind_ts:ind_te,i]) # max of the selected time period                       
                    if "5" in datplt or ("all" in datplt): # linear trend of the whole dataset
                        ymn_ltrnd_w = np.nanmin(LinTRND_w[ind_ts:ind_te,i]) # min of the selected time period (dtrend data)
                        ymx_ltrnd_w = np.nanmax(LinTRND_w[ind_ts:ind_te,i]) # max of the selected time period (dtrend data)                        
                    if "6" in datplt or ("all" in datplt): # linear trend of the chosen time period
                        ymn_ltrnd_tp = np.nanmin(LinTRND_tp[:,i]) # min of the selected time period (dtrend data)
                        ymx_ltrnd_tp = np.nanmax(LinTRND_tp[:,i]) # max of the selected time period (dtrend data)                        
                    ymn_tmp = np.nanmin([ymn_data,ymn_dtrnd,ymn_mavg_orig,ymn_mavg_dtrnd,ymn_ltrnd_w,ymn_ltrnd_tp])
                    ymx_tmp = np.nanmax([ymx_data,ymx_dtrnd,ymx_mavg_orig,ymx_mavg_dtrnd,ymx_ltrnd_w,ymx_ltrnd_tp])
                    if ymn_tmp == ymx_tmp:
                        if ymn_tmp == 0:
                            ymn_tmp = -1
                            ymx_tmp = 1
                        else:
                            ymn_tmp = ymn_tmp + (ymn_tmp * 0.1)
                            ymx_tmp = ymx_tmp - (ymx_tmp * 0.1)                        
                    ymn_org.append(ymn_tmp) 
                    ymx_org.append(ymx_tmp) 
                    ymn.append(ymn_tmp - (abs(ymn_tmp-ymx_tmp)*0.1)) # min of the selected time period - 10% as min Y limit
                    ymx.append(ymx_tmp + (abs(ymn_tmp-ymx_tmp)*0.1)) # max of the selected time period + 10% as max Y limit
                    yinc = [] # major axis increment
                if len(ind_p) > 1:
                    sctn = "7"
                    break
                if len(ind_p) == 1: # it is possible to chose the y axis in case of only plot one parameter                   
                    if ("3" in sctn_end) or ("4" in sctn_end):
                        input("Please adjust the 'Y AXIS' \n"
                              "PRESS ENTER TO CONTINUE >>> ")                    
                    yax_typ = input("________________________________________ Y AXIS (min & max) "
                                  "\n1: -10% min & +10% max"
                                  "\n2: Enter manually"
                                  "\nb: BACK"
                                  "\nmm: MAIN MENU \n"
                                  "Enter a number >>> ")
                    if yax_typ == "b":
                        if sctn_end != []:
                            sctn_end = []
                            sctn = "9"
                            break
                        else:
                            sctn = "5"
                            break                        
                    elif yax_typ == "mm":
                        return
                    elif yax_typ == "1":
                        sctn = "7"            
                        break                        
                    elif yax_typ == "2":                                    
                        while True:
                            try:
                                print("________________________________________ Y AXIS (min & max & increment)")
                                ymn =  int(input("ENTER Y AXIS min value:-------------> "))
                                ymx =  int(input("ENTER Y AXIS max value:-------------> "))
                                yinc = int(input("ENTER Y AXIS increment value:-------> "))
                                if ymn < ymx:            
                                    break
                            except:
                                while True:
                                    y_again = input("________________________________________ WRONG INPUT"
                                          "\n1: Try again"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> ")
                                    if y_again == "1":    
                                        break
                                    elif y_again == "mm":
                                        return
                sctn = "7"            
                break                                    
#==============================================================================                
        if sctn_end != []:
            sctn = [] 
#============================================================================== 
        if ("7" in sctn) or ("7" in sctn_end): # section 7 (number of subplots and how to save)
            hq_as = []
            sv_nsv = []
            while True:
                htplt = input("________________________________________ HOW MANY SUBPLOTS "
                              "\n1: One plot per page"
                              "\n2: Two subplots per page"
                              "\n3: Three subplots per page"
                              "\nb: BACK"
                              "\nmm: MAIN MENU \n"
                              "Enter a number >>> ")
                if htplt == "b":
                    if sctn_end != []:
                        sctn_end = []
                        sctn = "9"
                        break
                    else:
                        sctn = "6"
                        break
                if htplt == "mm":
                    return
                if htplt=="1" or htplt=="2" or htplt=="3":                           
                    while True:                
                        sv_nsv = input("________________________________________ SAVE AND DISPLAY (600 dpi)"
                                      "\n1: Just display"
                                      "\n2: Just save"
                                      "\n3: Save & Display"
                                      "\nb: BACK"
                                      "\nmm: MAIN MENU \n"
                                      "Enter a number >>> ")
                        if sv_nsv == "b":
                            break
                        if sv_nsv == "mm":
                            return
                        if sv_nsv == "1":                        
                            sctn = "8"
                            break
                        if sv_nsv == "2" or sv_nsv == "3":
                            while True:
                                hq_as = input("________________________________________ SAVE FORMAT (600 dpi)"
                                              "\n1: as *.jpg"
                                              "\n2: as *.png"
                                              "\n3: as *.pdf"
                                              "\n4: as *.csv"
                                              "\nb: BACK"
                                              "\nmm: MAIN MENU \n"
                                              "Enter a number >>> ")
                                hq_as = hq_as.replace(",","")
                                if hq_as == "b":
                                    break
                                elif hq_as == "mm":
                                    return
                                elif ("1" in hq_as) or ("2" in hq_as) or ("3" in hq_as) or ("4" in hq_as):
                                    break
                            if ("1" in hq_as) or ("2" in hq_as) or ("3" in hq_as) or ("4" in hq_as):
                                break
                    if ("1" in hq_as) or ("2" in hq_as) or ("3" in hq_as) or ("4" in hq_as) or (sv_nsv == "1"):
                        sctn = "8"
                        break                            
#==============================================================================                
        if sctn_end != []:
            sctn = "8"                     
#==============================================================================
        if "8" in sctn: # section 8 (ready to plot- put everything together)
            plt_dirs = fp1+"FIGURES" # name of a new folder (directory) to save the plots           
            x = np.array(time.iloc[ind_ts:ind_te]) #time vector (x axis) in array format
            data_csv = pd.DataFrame(index=range(len(x)),columns=["Timestamps"]) # make a time column in a csv file
            data_csv["Timestamps"] = x 
            n_figures = len(ind_p)//int(htplt) + (len(ind_p) % int(htplt) > 0) # number of figures needed
            sbplt_last = len(ind_p) % int(htplt) # number of subplots in the last figure
            k = 0 # parameters to plot (increasing)
            tmp_name_csv = ""
#            row_lab = ["M.An.","Mdn.","S.D.","PCTL. 95%"]
            if htplt == "1": # set size and location for different number of subplots
                lgnd_lc=(-0.11, -0.3) # legend location
                yax_inc = 10 # number of ticks in Y axis
                b_t = 0.35 # the bottom of the figure
                h_s = 0.2 # the horizontal space
            elif htplt == "2":
                lgnd_lc=(-0.11, -0.6)
                yax_inc = 7
                b_t = 0.35
                h_s = 0.2
            elif htplt == "3":
                lgnd_lc=(-0.11, -0.9)
                yax_inc = 5
                b_t = 0.35
                h_s = 0.23
            if sbplt_last != 0:   
                if sbplt_last == 1:
                    lgnd_lc_lf=(-0.11, -0.3) 
                    b_t_lf = 0.35 
                    h_s_lf = 0.2                    
                if sbplt_last == 2:
                    lgnd_lc_lf=(-0.11, -0.6)
                    b_t_lf = 0.35
                    h_s_lf = 0.2                                                 
            for i in range(n_figures): # in each figure:
                if i == n_figures-1 and sbplt_last != 0:
                    if sbplt_last == 1:
                        col_lab = [""]
                        axs = np.ndarray(1, dtype = "object")
                        fig,axs[0] = plt.subplots(1, sharex=True, num=str(i), figsize=(6,7))
                    else:
                        col_lab = [""]*sbplt_last
                        fig,axs = plt.subplots(sbplt_last, sharex=True, num=str(i), figsize=(6,7))
                else:
                    col_lab = [""]*int(htplt)
                    if int(htplt) == 1:
                        axs = np.ndarray(1, dtype = "object")
                        fig,axs[0] = plt.subplots(1, sharex=True, num=str(i), figsize=(6,7))
                    else:
                        fig,axs = plt.subplots(int(htplt), sharex=True, num=str(i), figsize=(6,7))
                j = 0 # subplots (increasing in each loop and for the next figure starts from 0 again)
                tmp_name = ""
                while j+1 <= int(htplt): # plot parameter in a figure till the J(th) parameter is bigger than number of subplots per figure
                    if k > len(ind_p)-1:
                        break
                    p_name = param.iloc[ind_p[k]-2] #name pf the plotted parameter
                    if p_name[0] == " ":
                        p_name = p_name[1:]
                    p_unit = units.iloc[ind_p[k]-2] #unit of the parameter
                    if ("1" in datplt) or ("all" in datplt): #plot the original data
                        y = np.array(data.iloc[ind_ts:ind_te,ind_p[k]]) #original data as Y axis
                        data_csv[p_name+" (Orig.)"] = y # in the csv file
                        if pltyp == "2":
                            axs[j].plot(x,y,'dimgray',label="Orig. data") #line plot
                        if pltyp == "3":
                            axs[j].scatter(x,y,2,'dimgray',label="Orig. data") #scatter plot
                        elif pltyp == "1":
                            axs[j].plot(x,y,'o-',color='dimgray',markersize=1,linewidth=1,label="Orig. data") #line and scatter plot
                    if ("2" in datplt) or ("all" in datplt): # plot the linear trend and detrend
                        y = dtrnd[ind_ts:ind_te,k] #detrend data as Y axis
                        data_csv[p_name+" (DTRND)"] = y
                        if pltyp == "2":
                            axs[j].plot(x,y,'red',label="DTRND data") #line plot
                        elif pltyp == "3":
                            axs[j].scatter(x,y,2,'red',label="DTRND data") #scatter plot
                        elif pltyp == "1":
                            axs[j].plot(x,y,'o-',color='red',markersize=1,linewidth=1,label="DTRND data") #line and scatter plot
                    if ("3" in datplt) or ("all" in datplt): 
                        y = mavg_orig[ind_ts:ind_te,k]
                        data_csv[p_name+" (" + mavg_samp + " Mavg_orig.)"] = y
                        if pltyp == "2":
                            axs[j].plot(x,y,'lime',label=mavg_samp + " Mavg_orig.") #line plot
                        elif pltyp == "3":
                            axs[j].scatter(x,y,2,'lime',label=mavg_samp + " Mavg_orig.") #scatter plot
                        elif pltyp == "1":
                            axs[j].plot(x,y,'o-',color='lime',markersize=0.5,linewidth=0.5,label=mavg_samp + " Mavg_orig.") #line and scatter plot
                    if ("4" in datplt) or ("all" in datplt):
                        y = mavg_dtrnd[ind_ts:ind_te,k] 
                        data_csv[p_name+" (" + mavg_samp + " Mavg_dtrnd)"] = y
                        if pltyp == "2":
                            axs[j].plot(x,y,'green',label=mavg_samp + " Mavg_dtrnd") #line plot
                        elif pltyp == "3":
                            axs[j].scatter(x,y,2,'green',label=mavg_samp + " Mavg_dtrnd") #scatter plot
                        elif pltyp == "1":
                            axs[j].plot(x,y,'o-',color='green',markersize=0.5,linewidth=0.5,label=mavg_samp + " Mavg_dtrnd") #line and scatter plot
                    if ("5" in datplt) or ("all" in datplt):
                        y = LinTRND_w[ind_ts:ind_te,k]
                        data_csv[p_name+" (LinTRND_w)"] = y
                        axs[j].plot(x,y,'-',color='blue',linewidth=1,label="LinTRND_w") #line plot
                    if ("6" in datplt) or ("all" in datplt):
                        y = LinTRND_tp[:,k]
                        data_csv[p_name+" (LinTRND_tp)"] = y
                        axs[j].plot(x,y,'--',color='blue',linewidth=1,label="LinTRND_tp") #line plot                        
                    axs[j].set_xlim(tstart,tend) #X axis limit
                    axs[j].set_ylim(ymn[k],ymx[k]) #Y axis limit
                    axs[j].set_ylabel("["+p_unit+"]", color='black', fontsize = 10, fontweight='bold') # y label
                    if yinc != []: # set the Y axis increment same as the user input value
                        axs[j].yaxis.set_ticks(np.arange(ymn, ymx, yinc))
                    elif yinc == []:
                        dif_y = ymx_org[k]-ymn_org[k] # difference of max and min Y
                        if dif_y < 1: # round the Y axis  
                            rnd_dgt = 3 # rounded digit                       
                        if dif_y >= 1 and dif_y < 10:
                            rnd_dgt = 2 
                        if dif_y >= 10 and dif_y < 100:
                            rnd_dgt = 1 
                        if dif_y >= 100:
                            rnd_dgt = 0                          
                        axs[j].yaxis.set_ticks(np.round(np.linspace(ymn_org[k],ymx_org[k],yax_inc),rnd_dgt))
                    myFmt = mdates.DateFormatter('%y-%m-%d %H:%M') # X axis date format
                    xlbl = "Time (yy-mm-dd HH-MM)"                                        
                    axs[j].xaxis.set_major_formatter(myFmt) # set the selected format to the X axis                     
                    axs[j].set_title(p_name, color='black', fontsize = 10, fontweight='bold') # plot title
                    axs[j].tick_params(direction='out', length=4, width=1.5, labelsize=8) # tick configuration
#                    axs[j].locator_params(axis='x', nbins=7)
                    axs[j].grid() # grid the plot
                    col_lab[j] = p_name                         
                    j = j + 1 # go to next subplot
                    k = k + 1 # go to next parameter
                    tmp_name = tmp_name + "_" + p_name # combine names in case of multiomle parameter in one figure
                    tmp_name_csv = tmp_name_csv + "_" + p_name # combine names of all the parameters in all the figures and subplots                                          
                axs[j-1].set_xlabel(xlbl, color='black', fontsize = 10, fontweight='bold')
#                table_vals = [y_MAN,y_MED,y_SDV,y_PER]
                plt.figtext(0.05,0.965,station_name,fontsize=12,fontweight='bold') # station name at the top left
                fig.autofmt_xdate()
                if i == n_figures-1 and sbplt_last != 0:
                    plt.subplots_adjust(left=0.13, bottom=b_t_lf, right=0.93, top=0.93, wspace=0.2, hspace=h_s_lf) # dimension and location of subplots                
                    plt.legend(loc='upper left', bbox_to_anchor=lgnd_lc_lf, ncol=3, fontsize=8) # the legend 
                else:
                    plt.subplots_adjust(left=0.13, bottom=b_t, right=0.93, top=0.93, wspace=0.2, hspace=h_s) # dimension and location of subplots                
                    plt.legend(loc='upper left', bbox_to_anchor=lgnd_lc, ncol=3, fontsize=8) # the legend
                if sv_nsv == "2" or sv_nsv == "3": # if user asks for save the plot
                    if not os.path.exists(plt_dirs):
                        os.makedirs(plt_dirs) # make a new directory for figures                
                    for z in range(len(hq_as)): # generate names to save each figure for each format
                        tts = tstart.to_pydatetime() #convert start time to py time format
                        tte = tend.to_pydatetime() #convert end time to py time format
                        p_ts = str(tts.year)[-2:]+"."+str(tts.month)[-2:]+"."+str(tts.day)[-2:] #convert the satrt to string format for name of the saved plot
                        p_te = str(tte.year)[-2:]+"."+str(tte.month)[-2:]+"."+str(tte.day)[-2:] #convert the end to string format for name of the saved plot
                        temp_fn = fn.replace(".csv","") #temporary file name without.csv for save name
                        frmt = [".jpg",".png",".pdf",".csv"]
                        extn = frmt[int(hq_as[z])-1]
                        f_name = temp_fn+"_"+ tmp_name +"_"+p_ts+"_"+p_te+extn #generate a name for the saved file
                        f_name_csv = temp_fn+"_"+ tmp_name_csv +"_"+p_ts+"_"+p_te+extn
                        f_npath = plt_dirs+"/"+f_name # path to save the plot
                        f_npath_csv = plt_dirs+"/"+f_name_csv # path to save the plot data as csv
                        ii = 0
                        while True: #check if the name already exsits and generate new name by adding number
                            if os.path.exists(f_npath):
                                ii = ii+1
                                f_name = temp_fn+"_"+ tmp_name +"_"+p_ts+"_"+p_te+"_("+str(ii)+")"+extn
                                f_npath = plt_dirs+"/"+f_name
                            else:
                                break
                        ii = 0                            
                        while True: #check if the name already exsits and generate new name by adding number
                            if os.path.exists(f_npath_csv):
                                ii = ii+1
                                f_name_csv = temp_fn+"_"+ tmp_name_csv +"_"+p_ts+"_"+p_te+"_("+str(ii)+")"+extn
                                f_npath_csv = plt_dirs+"/"+f_name_csv
                            else:
                                break                            
                        if hq_as[z] != "4":
                            if platform == "darwin": # in mac
                                fig.savefig(filename = f_npath, dpi = 600, orientation='portrait', papertype="a4") # save the figure 600 dpi quality 
                            elif platform == "win32": # in windows
                                fig.savefig(fname = f_npath, dpi = 600, orientation='portrait', papertype="a4") # save the figure 600 dpi quality
                        if i == 0:
                            print("Saved in: -----> "+plt_dirs) #print the name of the saved plot                        
                        print("As-----> "+f_name) #print the name of the saved plot
            if "4" in hq_as:
                data_csv.to_csv(f_npath_csv , sep=',', na_rep = "None", float_format='%G', index=False, encoding='utf-8')
            if sv_nsv == "1" or sv_nsv == "3": # to show the plot
                if platform == "win32": # in windows platform
                    print("________________________________________ ATTENTION \n"
                          "* In case of using 'WINDOWS COMMAND PROMPT': \n"
                          "* Close the opened figure(s) manually to continue")
                    plt.show() # show the plot
                elif platform == "darwin": # in mac
                    plt.show(block=False) # show the plot
            sctn = "9"        
#============================================================================== 
        if "9" in sctn :
            sctn = "8"                       
            while True:
                sctn_end = input("________________________________________ MODIFICATION \n"
                               "* By selecting 1 or 2, all the steps must be cheked again \n"
                               "* Options 3 to 7 can be combined (e.g. 35 changes the time period and plot style)"
                               "\n1: Import another file"
                               "\n2: From the current file plot another 'PARAMETER'"
                               "\n3: Change the 'TIME PERIOD'"
                               "\n4: Change the 'DATA IN PLOT'"
                               "\n5: Change the 'PLOT STYLE'"
                               "\n6: Chaneg the 'Y AXIS TYPE'"
                               "\n7: Chaneg the 'SAVE AND DISPLAY'"
                               "\nmm: MAIN MENU \n"
                               "Enter a number >>> ")
                plt.close("all")
                if sctn_end == "mm":
                    return
                else:
                    try:
                        int(sctn_end)
                        if (("1" in sctn_end) or ("2" in sctn_end) or ("3" in sctn_end) or
                            ("4" in sctn_end) or ("5" in sctn_end) or ("6" in sctn_end) or
                            ("7" in sctn_end)) and (("8" not in sctn_end) or 
                            ("9" not in sctn_end) or ("0" not in sctn_end)):
                            break
                    except:
                        while True:
                            end_again = input("________________________________________ WRONG INPUT"
                                  "\n1: Try again"
                                  "\nmm: MAIN MENU \n"
                                  "Enter a number >>> ")
                            if end_again == "1":
                                break
                            elif end_again == "mm":
                                return    
"""=============================================================================
FUNCTION (plot_TODD):
Plots any parameters in different types from the selected file
line-scatter-line&scatter
1,2 or 3 subplots per figure
table below the plots with mean annual, median, standard deviation and percentile95
1-defuiopen
2-defext_info
3-definterval_fix
4-deftrend
============================================================================="""
def defrun_plot_TODD():
    sctn_end = [] # section end is for modifying the already generated plots
    sctn = "1" # section 1 (import a file)
    while True:       
        if ("1" in sctn) or ("1" in sctn_end):
            while True:
                maintfilt = input("________________________________________ FILTER (MAINTENANCE & ANOMALIES) ???"
                             "\n1: YES (I have the maintenance file)"
                             "\n2: YES (I don't have the maintenance file)"
                             "\n3: NO (keep the data as it is)"
                             "\nmm: MAIN MENU \n"
                             "Enter a number >>> ")
                if maintfilt == "mm":
                    return
                elif maintfilt == "1":
                    print("________________________________________ IMPORT THE MAINTENANCE FILE")    
                    root = tk.Tk() 
                    root.withdraw()   
                    if platform == "darwin": # in mac
                        print('\a') 
                    elif platform == "win32": # in windows
                        winsound.Beep(frequency, duration)      
                    fp_maintfilt = filedialog.askopenfilename(title = "Import maintenance file",defaultextension ='.xlsx',
                           filetypes = (("CSV files","*.xlsx"),("all files","*.*")),parent = root)                    
                    break
                elif maintfilt == "2" or maintfilt == "3":
                    fp_maintfilt = []
                    break
                else:
                    pass            
            while True:
                print("________________________________________ FILE REPORT (first file)")
                fp,si,pi,data,d_type,station_name,fn,t_start,t_end = \
                defuiopen("Select the first '*.CSV' file",[]) #select and import the first file
                if len(fp) == 0: # check if any file is selected
                    while True:
                        re_imp = input ("________________________________________ NO IMPORTED FILE"
                                        "\n1: Try again"
                                        "\nmm: MAIN MENU \n"
                                        "Enter a number >>> ") 
                        if re_imp == "1": # try to select a file
                            break
                        if re_imp == "mm": # back to the main menu
                            return
                else:
                    break
            while True:
                confirm = input("________________________________________ SELECT "
                                "\n1: Ooops, this is a wrong file (pick another)"
                                "\n2: NEXT (select a parameter)"
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> " )
                if confirm == "1": # select a wrong file (go back to select another one)
                    sctn = "1"
                    break
                elif confirm == "mm": # back to the main menu
                    return
                elif confirm == "2": # correct file, go to next step
                    print("________________________________________ PLEASE WAIT ... ")
                    print("Checking time intervals")
                    t_int,_ = defcheck_int(data)                                      
                    if t_int > 1:                                                
                        print("Unifying time intervals (data 1)")                                           
                        data = definterval_fix(data,d_type) # unify the time interval
                    print("Checking the columns and parameters (data 1)")
                    data,pi,si = deffix_columns(pi,si,data,d_type)                                        
                    if d_type == "Local":
                        print("Checking the units (data 1)")
                        data,si,pi = defEC_unit(data,station_name,si,pi)
                    if maintfilt == "1" or maintfilt == "2":
                        print("Filtering the anomalies and maintenances (data 1)")
                        data,si = defmaint(maintfilt,fp_maintfilt,data,station_name,si,d_type) # replace the maintenance with nan   
                    t_start = data.iloc[0, 0] # date and time of the first recorded data
                    t_end = data.iloc[len(data) - 1, 0] # date and time of the last recorded data
                    sctn = "2" # permission for section 2                    
                    break
#==============================================================================                
        if sctn_end != []:
            sctn = []
        if "1" in sctn_end:
            sctn = "2"
            sctn_end = []
#==============================================================================                
        if ("2" in sctn) or ("2" in sctn_end): # section 2 (select parameters)
            fp1 = fp.replace(fn,"") #file path without file name
            time = data.iloc[:,0] # time vector
            if d_type == "Local":
                t_int_str = "30 minutes" # local time interval               
            elif d_type == "Satellite":
                t_int_str = "1 hour" # satellite time interval
            units = pi.iloc[1,2:].reset_index(drop=True) # units for local parameters
            param = pi.iloc[0,2:].reset_index(drop=True) # name of the parameters
            input_par=""
            for i in range(1,len(param)+1): # list of the parameters and their units in the selected file
                input_par = input_par + ("\n"+str(i)+":"+param[i-1]+" ["+units[i-1]+"]")             
            while True: # show the parameters to plot and let the user to select
                temp_p = input("________________________________________ PARAMETER [UNIT] \n"
                               "* USE COMMA TO COMBINE THEM \n"
                               + input_par[1:]+
                               "\nall: Plot all the parameters"
                               "\nb: BACK"
                               "\nmm: MAIN MENU \n"
                               "Enter a number (or combine them) >>> ")
                if temp_p == "b": # back
                    sctn = "1"
                    break
                elif temp_p == "mm": # main menu
                    return
                elif temp_p == "all": # select all
                    ind_p = list(np.arange(len(param))+2) #True colomn(s) of the seleceted parameter(s) 
                    sctn = "3" # permission for section 3                   
                    break                    
                else:
                    try:
                        int(temp_p.replace(",","")) # check if all the users input are only numbers and comma
                        temp_p2 = [int(x.strip())+1 for x in temp_p.split(',')] # list of the index of the selected parameters seperated by comma
                        if min(temp_p2) >= 2 and max(temp_p2) <= len(param)+1: # chek if the input values are in the range
                            ind_p = temp_p2 #True colomn(s) of the seleceted parameter(s)    
                            sctn = "3"  # permission for section 3                 
                            break
                        else: # in case of wrong input try again or main menu
                            while True:
                                par_again = input("________________________________________ WRONG INPUT (out of the range)"
                                                  "\n1: Try again"
                                                  "\nmm: MAIN MENU \n"
                                                  "Enter a number >>> ")
                                if par_again == "1":    
                                    break
                                elif par_again == "mm":
                                    return                            
                    except: # in case of wrong input try again or main menu
                        while True:
                            par_again = input("________________________________________ WRONG INPUT (wrong format)"
                                              "\n1: Try again"
                                              "\nmm: MAIN MENU \n"
                                              "Enter a number >>> ")
                            if par_again == "1":    
                                break
                            elif par_again == "mm":
                                return
            print("________________________________________ Detrending \n" 
                  "please wait...")
            _,dtrnd,LinTRND_w = deftrend([],data,["2","7"],ind_p) # calculate linear trend and detrend the selected parameters                          
#==============================================================================                
        if sctn_end != []:
            sctn = []
        if "2" in sctn_end:
            sctn = "3"
            sctn_end = []                            
#==============================================================================                
        if ("3" in sctn) or ("3" in sctn_end): # section 3 (select time period)
#..............................................................................
# Find the best time range based on recorded data (the biggest range including the most number of full year)
            ibs,ibe = 0 ,[] # index of best start and best end
            for i in range(len(time)-1,-1,-1): # find the last recorded in Dec for mean annual
                if time[i].month == time[ibs].month \
                    and time[i].day == time[ibs].day \
                    and time[i].year > time[ibs].year:
                    ibe = i
                    N_year_T2 = (time[ibe].year - time[ibs].year) # count the number of years for mean
                    T_type2 = True
                    type2_text =  "The best time period with maximum full years (" + str(time[ibs]) + " --> " + str(time[ibe]) + ")"                   
                    type2_text2 = str(time[ibs].year)+"."+str(time[ibs].month)+"."+ str(time[ibs].day)+"-"+str(time[ibe].year)+"."+str(time[ibe].month)+"."+ str(time[ibe].day)
                    break
                else:
                    type2_text =  "Not available" 
            while True: # select a time period to plot
                ind_t = input("________________________________________ TIME PERIOD"
                              "\nbest: " + type2_text + # number of last days
                              "\nall: The whole dataset (" + str(time[0]) + " --> " + str(time.iloc[-1]) + ")"# plot the whole dataset
                              "\nman: Enter a time period manually (specific date and time)" # input a specific time period to plot
                              "\nb: BACK"
                              "\nmm: MAIN MENU \n"
                              "Enter a number >>> ")
#                ind_t = input("________________________________________ TIME PERIOD"
#                              "\n* Digit and 'd' (e.g. 1d plots last day)" # number of last days
#                              "\n* Digit and 'w' (e.g. 4w plots last four weeks)" # number of last weeks
#                              "\nall: The whole dataset" # plot the whole dataset
#                              "\nman: Enter a time period manually (specific date and time)" # input a specific time period to plot
#                              "\nb: BACK"
#                              "\nmm: MAIN MENU \n"
#                              "Enter a number >>> ")
                if ind_t == "b":
                    if sctn_end != []:
                        sctn_end = []
                        sctn = "9"
                        break
                    else:
                        sctn = "2"
                        break                    
                elif ind_t == "mm":
                    return
                elif ind_t == "best": # in case of plotting best time period
                    tstart = time[ibs]
                    tend = time[ibe]              
                    ind_ts = ibs #index of the first record (start)
                    ind_te = ibe #index of the last record (end)
                    sctn = "4"                    
                    break                    
                elif ind_t == "all": # in case of plotting whole dataset
                    tstart = t_start
                    tend = t_end
                    ind_ts = int(time.loc[time == tstart].index.values) #index of the first record (start)
                    ind_te = int(time.loc[time == tend].index.values)+1 #index of the last record (end)
                    sctn = "4"                    
                    break
                elif ind_t == "man": # input the time period manually
                    while True:
                        try:
                            print("________________________________________ ATTENTION \n"
                                  "* No statistic parameters in case of chosen time period smaller than 1 year! \n"
                                  "* First recorded data:-----------> " + str(t_start) + "\n"
                                  "* Last recorded data:------------> " + str(t_end) + "\n"
                                  "* Recorded interval:-------------> " + t_int_str + "\n"
                                  "________________________________________ ENTER (YYYY-MM-DD HH:MM)")
                            tstart = pd.to_datetime(input("Start:---------------------------> "))
                            tend = pd.to_datetime(input("End:-----------------------------> "))
                            if tstart >= t_start and tstart < t_end and tend <= t_end and tend > t_start:
                                ind_ts = int(time.loc[time == tstart].index.values) #index of the selected time (start)
                                ind_te = int(time.loc[time == tend].index.values)+1 #index of the selected time (end) 
                                sctn = "4"
                                break
                            else:                           
                                while True:
                                    man_again = input("________________________________________ WRONG INPUT (out of the range)"
                                          "\n1: Try again"
                                          "\nb: BACK"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> ")
                                    if man_again == "b" or man_again == "1":    
                                        break
                                    elif man_again == "mm":
                                        return
                                if man_again == "b":
                                    break                        
                        except:
                            while True:
                                man_again = input("________________________________________ WRONG INPUT (wrong format)"
                                      "\n1: Try again"
                                      "\nb: BACK"
                                      "\nmm: MAIN MENU \n"
                                      "Enter a number >>> ")
                                if man_again == "b" or man_again == "1":    
                                    break
                                elif man_again == "mm":
                                    return
                            if man_again == "b":
                                break                                                                        
#                else:
#                    try:
#                        int(ind_t[:-1])
#                        if (ind_t[-1] == "d" or ind_t[-1] == "w"):
#                            if ind_t[-1] == "w":
#                                ind_t = str(int(ind_t[:-1])*7)+"d"
#                            tstart = t_end - pd.to_timedelta(ind_t)
#                            tstart = tstart.to_pydatetime()
#                            tstart = pd.Timestamp(str(tstart.year)+ "-"+ str(tstart.month) + "-" + str(tstart.day))
#                            tend = t_end                            
#                            if tstart >= t_start and tstart < t_end and tend <= t_end and tend > t_start:
#                                ind_ts = int(time.loc[time == tstart].index.values) #index of the selected time (start)
#                                ind_te = int(time.loc[time == tend].index.values)+1 #index of the selected time (end)                               
#                                sctn = "4"
#                                break
#                            else:
#                                while True:
#                                    man_again = input("________________________________________ OUT OF THE RANGE"
#                                          "\n1: Try again"
#                                          "\nmm: MAIN MENU \n"
#                                          "Enter a number >>> ")
#                                    if man_again == "1":    
#                                        break
#                                    elif man_again == "mm":
#                                        return
#                    except:
#                        while True:
#                            man_again = input("________________________________________ WRONG FORMAT"
#                                  "\n1: Try again"
#                                  "\nmm: MAIN MENU \n"
#                                  "Enter a number >>> ")
#                            if man_again == "1":    
#                                break
#                            elif man_again == "mm":
#                                return
                if sctn == "4":
                    break                                    
#==============================================================================                
        if sctn_end != []:
            sctn = [] 
#==============================================================================
        if ("4" in sctn) or ("4" in sctn_end): # section 4 (what to show in the plot)
            while True:
                LPF_m = []
                datplt = input("________________________________________ DATA IN PLOT"
                              "\n1: Original data" # data (dataframe)
                              "\n2: De_trended data" # dtrnd (array)
                              "\n3: Moving average of the original data" # mavg_orig
                              "\n4: Moving average of the de_trended data" # mavg_dtrnd
                              "\n5: Linear trend of the whole dataset" # LinTRND_w
                              "\n6: Linear trend of the chosen time period" # LinTRND_tp
                              "\nall: Plot all"
                              "\nb: BACK"
                              "\nmm: MAIN MENU \n"
                              "Enter a number (or combine them by comma) >>> ")
                if datplt == "b":
                    if sctn_end != []:
                        sctn_end = []
                        sctn = "9"
                        break
                    else:
                        sctn = "3"
                        break                    
                if datplt == "mm":
                    return            
                if ("1" in datplt) or ("2" in datplt) or ("3" in datplt) or ("4" in datplt) or\
                ("5" in datplt) or ("6" in datplt) or ("all" in datplt):
                    if ("3" in datplt) or ("4" in datplt) or ("all" in datplt):
                        while True: # in case of moving average enter the number of samples
                            LPF_m = input("________________________________________ MOVING AVERAGE SAMPLES"
                                              "\nb: BACK"
                                              "\nmm: MAIN MENU \n"
                                              "Enter the number of samples to calculate moving average (odd integer): >>> ")
                            if LPF_m == "b":
                                break
                            if LPF_m == "mm":
                                return
                            try:
                                mavgs = int(round(float(LPF_m),0))
                                if (mavgs % 2) == 0: #if sample number for means is even
                                    mavgs = str(mavgs + 1)
                                else:
                                    mavgs = str(mavgs)                                    
                                print("________________________________________ CALCULATING MOVING AVERAGE \n"
                                      "please wait...")
                                if ("3" in datplt) or ("all" in datplt):
                                    mavg_orig,_,_ = deftrend(int(mavgs),data,["3"],ind_p) # moving average of the original data
                                if ("4" in datplt) or ("all" in datplt):    
                                    mavg_dtrnd,_,_ = deftrend(int(mavgs),dtrnd,["4"],range(LinTRND_w.shape[1])) # moving average of the detrended data
                                if d_type == "Satellite": # show the label of the moving average in the legend
                                    mavg_samp = mavgs + "h"
                                elif d_type == "Local": # show the label of the moving average in the legend
                                    mavg_samp = str(int(mavgs)/2) + "h"
                                break
                            except:
                                   input("WRONG INPUT, press ENTER and try again...")
                    if LPF_m != "b":                                   
                        if ("6" in datplt) or ("all" in datplt):
                            _,_,LinTRND_tp = deftrend([],data.iloc[ind_ts:ind_te,:],["6"],ind_p) # linear trend of the chosen time period
                        sctn = "5"
                        break
#==============================================================================                
        if sctn_end != []:
            sctn = [] 
#==============================================================================
        if ("5" in sctn) or ("5" in sctn_end): # section 5 (plot style)
            while True:
                pltyp = input("________________________________________ PLOT STYLE "
                              "\n1: Line & Scatter (recommended)"
                              "\n2: Line"
                              "\n3: Scatter"
                              "\nb: BACK"
                              "\nmm: MAIN MENU \n"
                              "Enter a number >>> ")
                if pltyp == "b":
                    if sctn_end != []:
                        sctn_end = []
                        sctn = "9"
                        break
                    else:
                        sctn = "4"
                        break                    
                elif pltyp == "mm":
                    return
                elif pltyp == "1" or pltyp == "2" or pltyp == "3":     
                    sctn = "6"
                    break
#==============================================================================                
        if sctn_end != []:
            sctn = [] 
#==============================================================================
        if ("6" in sctn) or ("6" in sctn_end) or ("3" in sctn_end) or ("4" in sctn_end): # section 6 (y axis)                
            while True:        
                ymn,ymx = [],[]
                ymn_org,ymx_org = [],[]
                ymn_data,ymx_data = np.nan , np.nan
                ymn_dtrnd,ymx_dtrnd = np.nan , np.nan
                ymn_mavg_orig,ymx_mavg_orig = np.nan, np.nan
                ymn_mavg_dtrnd,ymx_mavg_dtrnd = np.nan, np.nan
                ymn_ltrnd_w,ymx_ltrnd_w,ymn_ltrnd_tp,ymx_ltrnd_tp = np.nan, np.nan, np.nan, np.nan
                for i in range(len(ind_p)): # plot each chosen parameter
                    if "1" in datplt or ("all" in datplt): # original data
                        ymn_data = np.nanmin(np.array(data.iloc[ind_ts:ind_te,ind_p[i]])) # min of the selected time period
                        ymx_data = np.nanmax(np.array(data.iloc[ind_ts:ind_te,ind_p[i]])) # max of the selected time period               
                    if "2" in datplt or ("all" in datplt): # detrended data
                        ymn_dtrnd = np.nanmin(dtrnd[ind_ts:ind_te,i]) # min of the selected time period
                        ymx_dtrnd = np.nanmax(dtrnd[ind_ts:ind_te,i]) # max of the selected time period
                    if "3" in datplt or ("all" in datplt): # moving average original
                        ymn_mavg_orig = np.nanmin(mavg_orig[ind_ts:ind_te,i]) # min of the selected time period
                        ymx_mavg_orig = np.nanmax(mavg_orig[ind_ts:ind_te,i]) # max of the selected time period                            
                    if "4" in datplt or ("all" in datplt): # moving average detrend
                        ymn_mavg_dtrnd = np.nanmin(mavg_dtrnd[ind_ts:ind_te,i]) # min of the selected time period
                        ymx_mavg_dtrnd = np.nanmax(mavg_dtrnd[ind_ts:ind_te,i]) # max of the selected time period                       
                    if "5" in datplt or ("all" in datplt): # linear trend of the whole dataset
                        ymn_ltrnd_w = np.nanmin(LinTRND_w[ind_ts:ind_te,i]) # min of the selected time period (dtrend data)
                        ymx_ltrnd_w = np.nanmax(LinTRND_w[ind_ts:ind_te,i]) # max of the selected time period (dtrend data)                        
                    if "6" in datplt or ("all" in datplt): # linear trend of the chosen time period
                        ymn_ltrnd_tp = np.nanmin(LinTRND_tp[:,i]) # min of the selected time period (dtrend data)
                        ymx_ltrnd_tp = np.nanmax(LinTRND_tp[:,i]) # max of the selected time period (dtrend data)                        
                    ymn_tmp = np.nanmin([ymn_data,ymn_dtrnd,ymn_mavg_orig,ymn_mavg_dtrnd,ymn_ltrnd_w,ymn_ltrnd_tp])
                    ymx_tmp = np.nanmax([ymx_data,ymx_dtrnd,ymx_mavg_orig,ymx_mavg_dtrnd,ymx_ltrnd_w,ymx_ltrnd_tp])
                    if ymn_tmp == ymx_tmp:
                        if ymn_tmp == 0:
                            ymn_tmp = -1
                            ymx_tmp = 1
                        else:
                            ymn_tmp = ymn_tmp + (ymn_tmp * 0.1)
                            ymx_tmp = ymx_tmp - (ymx_tmp * 0.1)                    
                    ymn_org.append(ymn_tmp) 
                    ymx_org.append(ymx_tmp) 
                    ymn.append(ymn_tmp - (abs(ymn_tmp-ymx_tmp)*0.1)) # min of the selected time period - 10% as min Y limit
                    ymx.append(ymx_tmp + (abs(ymn_tmp-ymx_tmp)*0.1)) # max of the selected time period + 10% as max Y limit
                    yinc = [] # major axis increment
                if len(ind_p) > 1:
                    sctn = "7"
                    break
                if len(ind_p) == 1: # it is possible to chose the y axis in case of only plot one parameter                   
                    if ("3" in sctn_end) or ("4" in sctn_end):
                        input("Please adjust the 'Y AXIS' \n"
                              "PRESS ENTER TO CONTINUE >>> ")                    
                    yax_typ = input("________________________________________ Y AXIS (min & max) "
                                  "\n1: -10% min & +10% max"
                                  "\n2: Enter manually"
                                  "\nb: BACK"
                                  "\nmm: MAIN MENU \n"
                                  "Enter a number >>> ")
                    if yax_typ == "b":
                        if sctn_end != []:
                            sctn_end = []
                            sctn = "9"
                            break
                        else:
                            sctn = "5"
                            break                        
                    elif yax_typ == "mm":
                        return
                    elif yax_typ == "1":
                        sctn = "7"            
                        break                        
                    elif yax_typ == "2":                                    
                        while True:
                            try:
                                print("________________________________________ Y AXIS (min & max & increment)")
                                ymn =  int(input("ENTER Y AXIS min value:-------------> "))
                                ymx =  int(input("ENTER Y AXIS max value:-------------> "))
                                yinc = int(input("ENTER Y AXIS increment value:-------> "))
                                if ymn < ymx:            
                                    break
                            except:
                                while True:
                                    y_again = input("________________________________________ WRONG INPUT"
                                          "\n1: Try again"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> ")
                                    if y_again == "1":    
                                        break
                                    elif y_again == "mm":
                                        return
                sctn = "7"            
                break                                    
#==============================================================================                
        if sctn_end != []:
            sctn = [] 
#============================================================================== 
        if ("7" in sctn) or ("7" in sctn_end): # section 7 (number of subplots and how to save)
            hq_as = []
            sv_nsv = []
            while True:
                htplt = input("________________________________________ HOW MANY SUBPLOTS "
                              "\n1: One plot per page"
                              "\n2: Two subplots per page"
                              "\n3: Three subplots per page"
                              "\nb: BACK"
                              "\nmm: MAIN MENU \n"
                              "Enter a number >>> ")
                if htplt == "b":
                    if sctn_end != []:
                        sctn_end = []
                        sctn = "9"
                        break
                    else:
                        sctn = "6"
                        break
                if htplt == "mm":
                    return
                if htplt=="1" or htplt=="2" or htplt=="3":                           
                    while True:                
                        sv_nsv = input("________________________________________ SAVE AND DISPLAY (600 dpi)"
                                      "\n1: Just display"
                                      "\n2: Just save"
                                      "\n3: Save & Display"
                                      "\nb: BACK"
                                      "\nmm: MAIN MENU \n"
                                      "Enter a number >>> ")
                        if sv_nsv == "b":
                            break
                        if sv_nsv == "mm":
                            return
                        if sv_nsv == "1":                        
                            sctn = "8"
                            break
                        if sv_nsv == "2" or sv_nsv == "3":
                            while True:
                                hq_as = input("________________________________________ SAVE FORMAT (600 dpi)"
                                              "\n1: as *.jpg"
                                              "\n2: as *.png"
                                              "\n3: as *.pdf"
                                              "\n4: as *.csv"
                                              "\nb: BACK"
                                              "\nmm: MAIN MENU \n"
                                              "Enter a number >>> ")
                                hq_as = hq_as.replace(",","")
                                if hq_as == "b":
                                    break
                                elif hq_as == "mm":
                                    return
                                elif ("1" in hq_as) or ("2" in hq_as) or ("3" in hq_as) or ("4" in hq_as):
                                    break
                            if ("1" in hq_as) or ("2" in hq_as) or ("3" in hq_as) or ("4" in hq_as):
                                break
                    if ("1" in hq_as) or ("2" in hq_as) or ("3" in hq_as) or ("4" in hq_as) or (sv_nsv == "1"):
                        sctn = "8"
                        break                            
#==============================================================================                
        if sctn_end != []:
            sctn = "8"                     
#==============================================================================
        if "8" in sctn: # section 8 (ready to plot- put everything together)
            plt_dirs = fp1+"FIGURES" # name of a new folder (directory) to save the plots           
            x = np.array(time.iloc[ind_ts:ind_te]) #time vector (x axis) in array format
            time_table = time.iloc[ind_ts:ind_te]
#..............................................................................
# Type1 statistic value in the table (only Jan to Dec)
            ind_mean1,ind_mean2 = [],[]            
            for i in range(len(time_table)): # find the fisrt recorded in Jan for mean annual
                if time_table[i].month == 1 and time_table[i].day == 1:
                    ind_mean1 = i
                    break
            for i in range(len(time_table)-1,-1,-1): # find the last recorded in Dec for mean annual
                if time_table[i].month == 12 and time_table[i].day == 31:
                    ind_mean2 = i
                    break
            if ind_mean1 > ind_mean2: # check if the found DEC is older the JAN (is it a year at least)
                T_type1 = False
            else:
                T_type1 = True
                N_year_T1 = (time_table[ind_mean2].year - time_table[ind_mean1].year) + 1 # count the number of years for mean
                type1_text2 = str(time_table[ind_mean1].year)+"."+str(time_table[ind_mean1].month)+"."+ str(time_table[ind_mean1].day)+\
                "-"+str(time_table[ind_mean2].year)+"."+str(time_table[ind_mean2].month)+"."+ str(time_table[ind_mean2].day)
#..............................................................................
            A = [time.iloc[ind_ts],time.iloc[ind_te-1]] # first and last date of chosen time period
            B = [mdates.date2num(A[0]),mdates.date2num(A[1])] # convert the coshen time period to number
            C = np.round(np.linspace(B[0],B[1],7),3) # 7 equal time label
            D = []
            for i in range(len(C)):
                D.append(mdates.num2date(C[i])) # convert the date as number to date again
            data_csv = pd.DataFrame(index=range(len(x)),columns=["Timestamps"]) # make a time column in a csv file
            data_csv["Timestamps"] = x 
            n_figures = len(ind_p)//int(htplt) + (len(ind_p) % int(htplt) > 0) # number of figures needed
            sbplt_last = len(ind_p) % int(htplt) # number of subplots in the last figure
            k = 0 # parameters to plot (increasing)
            tmp_name_csv = ""
            row_lab = ["M.An.","Mdn.","S.D.","PCTL. 95%"]
            if htplt == "1": # set size and location for different number of subplots
                lgnd_lc=(-0.11, -0.125) # legend location
                yax_inc = 10 # number of ticks in Y axis
                b_t = 0.35 # the bottom of the figure
                h_s = 0.2 # the horizontal space
                b_box = [0.07, -0.5, 0.36, 0.26] # tables coordinate [top left x , top left y, right, bottom]
                col_width = [0.28] # column width of the table
            elif htplt == "2":
                lgnd_lc=(-0.11, -0.275)
                yax_inc = 7
                b_t = 0.35
                h_s = 0.2
                b_box = [0.07, -1.09, 0.64, 0.55]
                col_width = [0.28]*2
            elif htplt == "3":
                lgnd_lc=(-0.11, -0.43)
                yax_inc = 5
                b_t = 0.35
                h_s = 0.23
                b_box = [0.07, -1.68, 0.92, 0.825]
                col_width = [0.28]*3
            if sbplt_last != 0:   
                if sbplt_last == 1:
                    lgnd_lc_lf=(-0.11, -0.125) 
                    b_t_lf = 0.35 
                    h_s_lf = 0.2 
                    b_box_lf = [0.07, -0.5, 0.47, 0.26] 
                    col_width_lf = [0.45]                    
                if sbplt_last == 2:
                    lgnd_lc_lf=(-0.11, -0.275)
                    b_t_lf = 0.35
                    h_s_lf = 0.2
                    b_box_lf = [0.07, -1.09, 0.77, 0.55]
                    col_width_lf = [0.45]*2                                                    
            for i in range(n_figures): # in each figure:
            # (i) is the figure
            # (j) is the subplot in teh figure
            # (k) is the parameter in the subplot
                if i == n_figures-1 and sbplt_last != 0:
                    if sbplt_last == 1:
                        col_lab = [""]
                        axs = np.ndarray(1, dtype = "object")
                        fig,axs[0] = plt.subplots(1, sharex=True, num=str(i), figsize=(6,7))
                    else:
                        col_lab = [""]*sbplt_last
                        fig,axs = plt.subplots(sbplt_last, sharex=True, num=str(i), figsize=(6,7))
                else:
                    col_lab = [""]*int(htplt)
                    if int(htplt) == 1:
                        axs = np.ndarray(1, dtype = "object")
                        fig,axs[0] = plt.subplots(1, sharex=True, num=str(i), figsize=(6,7))
                    else:
                        fig,axs = plt.subplots(int(htplt), sharex=True, num=str(i), figsize=(6,7))
                j = 0 # subplots (increasing in each loop and for the next figure starts from 0 again)
                tmp_name = ""
                y_MAN1,y_MED1,y_SDV1,y_PER1 = ["None"]*len(col_lab),["None"]*len(col_lab),["None"]*len(col_lab),["None"]*len(col_lab)
                y_MAN2,y_MED2,y_SDV2,y_PER2 = ["None"]*len(col_lab),["None"]*len(col_lab),["None"]*len(col_lab),["None"]*len(col_lab)
                y_MAN,y_MED,y_SDV,y_PER = ["None"]*len(col_lab),["None"]*len(col_lab),["None"]*len(col_lab),["None"]*len(col_lab)
                while j+1 <= int(htplt): # plot parameter in a figure till the J(th) parameter is bigger than number of subplots per figure
                    if k > len(ind_p)-1:
                        break
                    p_name = param.iloc[ind_p[k]-2] #name pf the plotted parameter
                    if p_name[0] == " ":
                        p_name = p_name[1:]
                    p_unit = units.iloc[ind_p[k]-2] #unit of the parameter
                    if ("1" in datplt) or ("all" in datplt): #plot the original data
                        y = np.array(data.iloc[ind_ts:ind_te,ind_p[k]]) #original data as Y axis
                        data_csv[p_name+" (Orig.)"] = y # in the csv file
                        if pltyp == "2":
                            axs[j].plot(x,y,'dimgray',label="Orig. data") #line plot
                        if pltyp == "3":
                            axs[j].scatter(x,y,2,'dimgray',label="Orig. data") #scatter plot
                        elif pltyp == "1":
                            axs[j].plot(x,y,'o-',color='dimgray',markersize=1,linewidth=1,label="Orig. data") #line and scatter plot
                    if ("2" in datplt) or ("all" in datplt): # plot the linear trend and detrend
                        y = dtrnd[ind_ts:ind_te,k] #detrend data as Y axis
                        data_csv[p_name+" (DTRND)"] = y
                        if pltyp == "2":
                            axs[j].plot(x,y,'red',label="DTRND data") #line plot
                        elif pltyp == "3":
                            axs[j].scatter(x,y,2,'red',label="DTRND data") #scatter plot
                        elif pltyp == "1":
                            axs[j].plot(x,y,'o-',color='red',markersize=1,linewidth=1,label="DTRND data") #line and scatter plot
                    if ("3" in datplt) or ("all" in datplt): 
                        y = mavg_orig[ind_ts:ind_te,k]
                        data_csv[p_name+" (" + mavg_samp + " Mavg_orig.)"] = y
                        if pltyp == "2":
                            axs[j].plot(x,y,'lime',label=mavg_samp + " Mavg_orig.") #line plot
                        elif pltyp == "3":
                            axs[j].scatter(x,y,2,'lime',label=mavg_samp + " Mavg_orig.") #scatter plot
                        elif pltyp == "1":
                            axs[j].plot(x,y,'o-',color='lime',markersize=0.5,linewidth=0.5,label=mavg_samp + " Mavg_orig.") #line and scatter plot
                    if ("4" in datplt) or ("all" in datplt):
                        y = mavg_dtrnd[ind_ts:ind_te,k] 
                        data_csv[p_name+" (" + mavg_samp + " Mavg_dtrnd)"] = y
                        if pltyp == "2":
                            axs[j].plot(x,y,'green',label=mavg_samp + " Mavg_dtrnd") #line plot
                        elif pltyp == "3":
                            axs[j].scatter(x,y,2,'green',label=mavg_samp + " Mavg_dtrnd") #scatter plot
                        elif pltyp == "1":
                            axs[j].plot(x,y,'o-',color='green',markersize=0.5,linewidth=0.5,label=mavg_samp + " Mavg_dtrnd") #line and scatter plot
                    if ("5" in datplt) or ("all" in datplt):
                        y = LinTRND_w[ind_ts:ind_te,k]
                        data_csv[p_name+" (LinTRND_w)"] = y
                        axs[j].plot(x,y,'-',color='blue',linewidth=1,label="LinTRND_w") #line plot
                    if ("6" in datplt) or ("all" in datplt):
                        y = LinTRND_tp[:,k]
                        data_csv[p_name+" (LinTRND_tp)"] = y
                        axs[j].plot(x,y,'--',color='blue',linewidth=1,label="LinTRND_tp") #line plot                        
                    axs[j].set_xlim(tstart,tend) #X axis limit
                    axs[j].set_ylim(ymn[k],ymx[k]) #Y axis limit
                    axs[j].set_ylabel("["+p_unit+"]", color='black', fontsize = 10, fontweight='bold') # y label
                    if yinc != []: # set the Y axis increment same as the user input value
                        axs[j].yaxis.set_ticks(np.arange(ymn, ymx, yinc))
                    elif yinc == []:
                        dif_y = ymx_org[k]-ymn_org[k] # difference of max and min Y
                        if dif_y < 1: # round the Y axis  
                            rnd_dgt = 3 # rounded digit                       
                        if dif_y >= 1 and dif_y < 10:
                            rnd_dgt = 2 
                        if dif_y >= 10 and dif_y < 100:
                            rnd_dgt = 1 
                        if dif_y >= 100:
                            rnd_dgt = 0                          
                        axs[j].yaxis.set_ticks(np.round(np.linspace(ymn_org[k],ymx_org[k],yax_inc),rnd_dgt))
                    axs[j].xaxis.set_ticks(D)
                    if time.iloc[ind_te-1]-time.iloc[ind_ts] > pd.to_timedelta("7d"):
                        myFmt = mdates.DateFormatter('%y-%m-%d') # X axis date format
                        xlbl = "Time (yy-mm-dd)"
                    else:
                        myFmt = mdates.DateFormatter('%y-%m-%d\n%H:%M') # X axis date format
                        xlbl = "Time (yy-mm-dd HH-MM)"                                        
                    axs[j].xaxis.set_major_formatter(myFmt) # set the selected format to the X axis
                    axs[j].set_title(p_name, color='black', fontsize = 10, fontweight='bold') # plot title
                    axs[j].tick_params(direction='out', length=4, width=1.5, labelsize=8) # tick configuration
                    axs[j].grid() # grid the plot
                    col_lab[j] = p_name
#..............................................................................
# statistic value type 1 (calculation)                    
                    if T_type1 == True:
                        if data.columns[ind_p[k]] == "Precipitation" or data.columns[ind_p[k]] == "Rain_mm_Tot":
                            y_MAN1[j] = np.round(np.nansum(np.array(data.iloc[ind_mean1:ind_mean2,ind_p[k]]))/N_year_T1,rnd_dgt) # calculate the mean annual only from Jan to Dec                            
                        else:
                            y_MAN1[j] = np.round(np.nanmean(np.array(data.iloc[ind_mean1:ind_mean2,ind_p[k]])),rnd_dgt) # calculate the mean annual only from Jan to Dec
                    y_MED1[j] = np.round(np.nanmedian(np.array(data.iloc[ind_mean1:ind_mean2,ind_p[k]])),rnd_dgt) # calculate the median
                    y_SDV1[j] = np.round(np.nanstd(np.array(data.iloc[ind_mean1:ind_mean2,ind_p[k]])),rnd_dgt) # calculate the standard deviation
                    y_PER1[j] = np.round(np.nanpercentile(np.array(data.iloc[ind_mean1:ind_mean2,ind_p[k]]),95),rnd_dgt) # calculate the 95% percentile              
#..............................................................................
# statistic value type 2 (calculation)                     
                    if T_type2 == True:
                        if data.columns[ind_p[k]] == "Precipitation" or data.columns[ind_p[k]] == "Rain_mm_Tot":
                            y_MAN2[j] = np.round(np.nansum(np.array(data.iloc[ibs:ibe,ind_p[k]]))/N_year_T2,rnd_dgt) # calculate the mean annual only from Jan to Dec                            
                            unit_MAN =  " [" + p_unit + "/a]"
                        else:
                            y_MAN2[j] = np.round(np.nanmean(np.array(data.iloc[ibs:ibe,ind_p[k]])),rnd_dgt) # calculate the mean annual only from Jan to Dec
                            unit_MAN = " [" + p_unit + "]"
                    y_MED2[j] = np.round(np.nanmedian(np.array(data.iloc[ibs:ibe,ind_p[k]])),rnd_dgt) # calculate the median
                    y_SDV2[j] = np.round(np.nanstd(np.array(data.iloc[ibs:ibe,ind_p[k]])),rnd_dgt) # calculate the standard deviation
                    y_PER2[j] = np.round(np.nanpercentile(np.array(data.iloc[ibs:ibe,ind_p[k]]),95),rnd_dgt) # calculate the 95% percentile  
#..............................................................................
                    y_MAN[j] =  str(y_MAN1[j]) + " / " + str(y_MAN2[j]) + unit_MAN
                    y_MED[j] =  str(y_MED1[j]) + " / " + str(y_MED2[j]) + " [" + p_unit + "]"
                    y_SDV[j] =  str(y_SDV1[j]) + " / " + str(y_SDV2[j]) + " [" + p_unit + "]"
                    y_PER[j] =  str(y_PER1[j]) + " / " + str(y_PER2[j]) + " [" + p_unit + "]"
#..............................................................................                    
                    j = j + 1 # go to next subplot
                    k = k + 1 # go to next parameter
                    tmp_name = tmp_name + "_" + p_name # combine names in case of multiple parameter in one figure
                    tmp_name_csv = tmp_name_csv + "_" + p_name # combine names of all the parameters in all the figures and subplots                                          
                axs[j-1].set_xlabel(xlbl, color='black', fontsize = 10, fontweight='bold')
                table_vals = [y_MAN,y_MED,y_SDV,y_PER]
                plt.figtext(0.05,0.965,station_name,fontsize=12,fontweight='bold') # station name at the top left
                if i == n_figures-1 and sbplt_last != 0:
                    plt.subplots_adjust(left=0.13, bottom=b_t_lf, right=0.93, top=0.93, wspace=0.2, hspace=h_s_lf) # dimension and location of subplots                
                    plt.legend(loc='upper left', bbox_to_anchor=lgnd_lc_lf, ncol=3, fontsize=8) # the legend 
                    the_table = plt.table(cellText=table_vals, rowLabels=row_lab, rowLoc='center',
                                          colLabels=col_lab, colLoc='center', colWidths=col_width_lf,
                                          loc='upper left', bbox=b_box_lf)  # the table
                else:
                    plt.subplots_adjust(left=0.13, bottom=b_t, right=0.93, top=0.93, wspace=0.2, hspace=h_s) # dimension and location of subplots                
                    plt.legend(loc='upper left', bbox_to_anchor=lgnd_lc, ncol=3, fontsize=8) # the legend                 
                    the_table = plt.table(cellText=table_vals, rowLabels=row_lab, rowLoc='center',
                                          colLabels=col_lab, colLoc='center', colWidths=col_width,
                                          loc='upper left', bbox=b_box)                    
                the_table.auto_set_font_size(False)
                the_table.set_fontsize(8.5)
                abbr1 = "Orig.: Original, DTRND: Detrend, Mavg: Moving average, LinTRND: Linear trend" # abbreviations
                abbr2 = "w: whole dataset, tp: chosen time period, h: hour" # abbreviations
                abbr3 = "M.An.: Mean Annual, Mdn.: Median, S.D.: Standard Deviation, PCTL.: Percentile, *(" + type1_text2 + " / " + type2_text2 + ")"  # abbreviations
                plt.figtext(0.05,0.04,abbr1,fontsize=6) # show abbreviations below the plot
                plt.figtext(0.05,0.025,abbr2,fontsize=6) # show abbreviations below the plot
                plt.figtext(0.05,0.01,abbr3,fontsize=6) # show abbreviations below the plot
                if sv_nsv == "2" or sv_nsv == "3": # if user asks for save the plot
                    if not os.path.exists(plt_dirs):
                        os.makedirs(plt_dirs) # make a new directory for figures                
                    for z in range(len(hq_as)): # generate names to save each figure for each format
                        tts = tstart.to_pydatetime() #convert start time to py time format
                        tte = tend.to_pydatetime() #convert end time to py time format
                        p_ts = str(tts.year)[-2:]+"."+str(tts.month)[-2:]+"."+str(tts.day)[-2:] #convert the satrt to string format for name of the saved plot
                        p_te = str(tte.year)[-2:]+"."+str(tte.month)[-2:]+"."+str(tte.day)[-2:] #convert the end to string format for name of the saved plot
                        temp_fn = fn.replace(".csv","") #temporary file name without.csv for save name
                        frmt = [".jpg",".png",".pdf",".csv"]
                        extn = frmt[int(hq_as[z])-1]
                        f_name = temp_fn+"_"+ tmp_name +"_"+p_ts+"_"+p_te+extn #generate a name for the saved file
                        f_name_csv = temp_fn+"_"+ tmp_name_csv +"_"+p_ts+"_"+p_te+extn
                        f_npath = plt_dirs+"/"+f_name # path to save the plot
                        f_npath_csv = plt_dirs+"/"+f_name_csv # path to save the plot data as csv
                        ii = 0
                        while True: #check if the name already exsits and generate new name by adding number
                            if os.path.exists(f_npath):
                                ii = ii+1
                                f_name = temp_fn+"_"+ tmp_name +"_"+p_ts+"_"+p_te+"_("+str(ii)+")"+extn
                                f_npath = plt_dirs+"/"+f_name
                            else:
                                break
                        ii = 0                            
                        while True: #check if the name already exsits and generate new name by adding number
                            if os.path.exists(f_npath_csv):
                                ii = ii+1
                                f_name_csv = temp_fn+"_"+ tmp_name_csv +"_"+p_ts+"_"+p_te+"_("+str(ii)+")"+extn
                                f_npath_csv = plt_dirs+"/"+f_name_csv
                            else:
                                break                            
                        if hq_as[z] != "4":
                            if platform == "darwin": # in mac
                                fig.savefig(filename = f_npath, dpi = 600, orientation='portrait', papertype="a4") # save the figure 600 dpi quality 
                            elif platform == "win32": # in windows
                                fig.savefig(fname = f_npath, dpi = 600, orientation='portrait', papertype="a4") # save the figure 600 dpi quality
                        if i == 0:
                            print("Saved in: -----> "+plt_dirs) #print the name of the saved plot                        
                        print("As-----> "+f_name) #print the name of the saved plot
            if "4" in hq_as:
                data_csv.to_csv(f_npath_csv , sep=',', na_rep = "None", float_format='%G', index=False, encoding='utf-8')
            if sv_nsv == "1" or sv_nsv == "3": # to show the plot
                if platform == "win32": # in windows platform
                    print("________________________________________ ATTENTION \n"
                          "* In case of using 'WINDOWS COMMAND PROMPT': \n"
                          "* Close the opened figure(s) manually to continue")
                    plt.show() # show the plot
                elif platform == "darwin": # in mac
                    plt.show(block=False) # show the plot
            sctn = "9"        
#============================================================================== 
        if "9" in sctn :
            sctn = "8"                       
            while True:
                sctn_end = input("________________________________________ MODIFICATION \n"
                               "* By selecting 1 or 2, all the steps must be cheked again \n"
                               "* Options 3 to 7 can be combined (e.g. 35 changes the time period and plot style)"
                               "\n1: Import another file"
                               "\n2: From the current file plot another 'PARAMETER'"
                               "\n3: Change the 'TIME PERIOD'"
                               "\n4: Change the 'DATA IN PLOT'"
                               "\n5: Change the 'PLOT STYLE'"
                               "\n6: Chaneg the 'Y AXIS TYPE'"
                               "\n7: Chaneg the 'SAVE AND DISPLAY'"
                               "\nmm: MAIN MENU \n"
                               "Enter a number >>> ")
                plt.close("all")
                if sctn_end == "mm":
                    return
                else:
                    try:
                        int(sctn_end)
                        if (("1" in sctn_end) or ("2" in sctn_end) or ("3" in sctn_end) or
                            ("4" in sctn_end) or ("5" in sctn_end) or ("6" in sctn_end) or
                            ("7" in sctn_end)) and (("8" not in sctn_end) or 
                            ("9" not in sctn_end) or ("0" not in sctn_end)):
                            break
                    except:
                        while True:
                            end_again = input("________________________________________ WRONG INPUT"
                                  "\n1: Try again"
                                  "\nmm: MAIN MENU \n"
                                  "Enter a number >>> ")
                            if end_again == "1":
                                break
                            elif end_again == "mm":
                                return
"""**********************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
**********************************************************************************************************"""  
"""PACKAGE OF FUNCTIONS (append two files)"""
"""=============================================================================
FUNCTION (Check the columns names and parameters):
During the appending process if the two selected files have columns which
are not similar (names, order of the names and number of columns) it finds them
and correct them. This process is based on comparing each file by a set of
reference columns name and order, then identify the extra and missing one and
add them. Of course these new columns must be filled by "nan"
============================================================================="""        
def defcheck_columns(pi1,data1,pi2,data2,d_type):
    data1  = pi1.append(data1, ignore_index=True) # append the data below the parameters info (first fiel)
    data2  = pi2.append(data2, ignore_index=True) # append the data below the parameters info (second fiel)
    if d_type == "Local": # default column names for LOCAL file
        for i in pi1.iloc[0,:]:
            if ("WSData2_WVc(3)" in i):
                pi1.loc[0,i] = "WSData2_WVc"
                pi1.columns = pi1.iloc[0,:]
                data1.columns = pi1.iloc[0,:]
        for i in pi2.iloc[0,:]:
            if ("WSData2_WVc(3)" in i):
                pi2.loc[0,i] = "WSData2_WVc"
                pi2.columns = pi2.iloc[0,:]
                data2.columns = pi2.iloc[0,:]
        org_col = ["TIMESTAMP","RECORD","BattV_Avg","PTemp_C_Avg","AirTC_Avg","RH",
                   "PVap_Avg","SlrW_Avg","SlrMJ_Tot","VWC_Avg","GrTemp_Avg","EC_Avg",
                   "P_Avg","PA_Avg","VR_Avg","WS_ms_Avg","WS_ms_max","WS_ms_min"
                   ,"WindDir_Avg","WS_ms_S_WVT","WindDir_D1_WVT","WSData2_WVc","Rain_mm_Tot",
                   "BP_mbar_Avg","NaNCounter","WSDiag","VaporPres","SeaLevelPres"]
        org_col2 = ["TS","RN","Volts","Deg C","Deg C","%","kPa","W/m²","MJ/m²","m³/m³"\
                    ,"Deg C","mS/m","-","nSec","-","m/s","m/s"\
                    ,"m/s","Deg","m/s","Deg","Deg","mm","mbar","-","-","-","-"]
        org_col3 = ["","","Avg","Avg","Avg","Smp","Avg","Avg","Tot","Avg","Avg","Avg","Avg","Avg"\
                    ,"Avg","Avg","Max","Min","Avg","WVc","WVc","WVc","Tot","Avg","Smp","Smp","Smp","Smp"]
    elif d_type == "Satellite": # default column names for SATELLITE file
        org_col = ["Timestamp"," Station name"," Air temperature"," Air relative humidity",
                   " Solar radiation"," Soil water content"," Soil temperature"," Wind speed",
                   " Wind max"," Wind direction"," Precipitation"," Air pressure"]     
#..............................................................................   
    lst1 = pi1.iloc[0,:]     
    temp1 = [x for x in org_col if x not in lst1]    
    lst2 = pi2.iloc[0,:]     
    temp2 = [x for x in org_col if x not in lst2] 
    for i in range(len(temp1)):
        data1[temp1[i]] = np.nan
    data1 = data1[org_col]
    data1.iloc[1,:] = org_col2
    data1.iloc[2,:] = org_col3
    for i in range(len(temp2)):
        data2[temp2[i]] = np.nan
    data2 = data2[org_col]       
    data2.iloc[1,:] = org_col2
    data2.iloc[2,:] = org_col3               
#    extra_data1_df = data1.drop(data1.columns.intersection(data2.columns),axis=1) # it is in 1 but not in 2
#    extra_data2_df = data2.drop(data1.columns.intersection(data2.columns),axis=1) # it is in 2 but not in 1
#    extra_data1_col = list(extra_data1_df.columns.values) # list of parameters data1 which are not in data2
#    extra_data2_col = list(extra_data2_df.columns.values) # list of parameters data2 which are not in data1
#    for i in range(len(extra_data2_col)):
#        data1[extra_data2_col[i]] = np.nan # add extra columns in data2 to data1 and fill with nan
#    for i in range(len(extra_data1_col)):
#        data2[extra_data1_col[i]] = np.nan # add extra columns in data1 to data2 and fill with nan
 
#    new_org_temp = org_col + list(extra_data1_df) + list(extra_data2_df) # combine original parameters and extra data1 and extra data2
#    new_org = list(unique_everseen(new_org_temp)) # drop the multiple parameters (make the list unique)
#..............................................................................
#    try:
#        data1 = data1[org_col_emerg]
#    except:
#        data1 = data1[new_org] # set the new parameters name on data1
#    data1.iloc[0] = list(data1.columns.values) # set the first row of data1 as new parameters name
#    if len(list(extra_data2_df)) > 0: # if there are extra parameters in data2
#        data1.loc[1:2,list(extra_data2_df)] = data2.loc[1:2,list(extra_data2_df)]
#    data1 = data1.fillna(np.nan)
##..............................................................................
#    try:
#        data2 = data2[org_col_emerg]
#    except:
#        data2 = data2[new_org]    
#    data2.iloc[0] = list(data2.columns.values)
#    if len(list(extra_data1_df)) > 0:
#        data2.loc[1:2,list(extra_data1_df)] = data1.loc[1:2,list(extra_data1_df)]
#    data2 = data2.fillna(np.nan)
    return data1,data2
"""=============================================================================
 FUNCTION (start the appending process):                             
1-defcheck_columns
2-definterval_fix
3-defEC_unit
4-defuisave
============================================================================="""
def defapnd_strt(fp1,si1,pi1,data1,d_type1,fn1,fp2,si2,pi2,data2,d_type2,fn2,station_name1):
#..............................................................................        
    ts1 = pd.to_datetime(data1.iloc[0, 0]) # start time of first (old) file
    te2 = pd.to_datetime(data2.iloc[len(data2) - 1, 0]) # end time of first (old) file
    te1 = pd.to_datetime(data1.iloc[len(data1) - 1, 0]) # end time of second (new) file
    ts2 = pd.to_datetime(data2.iloc[0, 0]) # start time of second (new) file
#..............................................................................
# data type and their associated time interval     
    if d_type1 == "Local": 
        fx_int = 30
        fx_typ = "m"
    elif d_type1 == "Satellite":
        fx_int = 1
        fx_typ = "h"
#..............................................................................
# check the compatibility of number of columns between two files        
    if pi1.shape[1] != pi2.shape[1]:
        input("________________________________________ DISTINCT COLUMNS \n"
              "* It'll be fixed during the appending process :) \n"
              "Press any key to continue >>> ")
#.............................................................................. 
# check if there is a time gap at the boundary of the two files
# calculate the duration of the missing data and number of missing rows depends on the default interval
    if ts2-te1 > pd.to_timedelta(str(fx_int)+fx_typ):
        input("________________________________________ TIME GAP \n"
              "* Time gap between the selected files:--------------- " + str(ts2-te1) + "\n"
              "* Missing row(s) between the selected files:---------- "
              + str(int((ts2-te1) / np.timedelta64(fx_int,fx_typ))-1) + "\n"
              "Press any key to continue >>> ")
#.............................................................................. 
    while True: # confirm to run the appending process   
        confirm = input("________________________________________ READY TO APPEND"
                        "\n1: Start appending" 
                        "\nmm: MAIN MENU \n" 
                        "Enter a number >>> ")
        if confirm == "mm":
            return fp1,si1,pi1,data1,d_type1,fn1
#.............................................................................. 
# append the files        
        elif confirm == "1":
            print("________________________________________ APPENDING \n" # name of the files which are appending
                  + fn1 + "\n"
                  + fn2 + "\n"
                  "Please wait...")
#..............................................................................
# add some information to the first line
# it shows the history of the appending process of this new file              
            if d_type1 == "Local": # append LOCAL data
                station_info = si1
                station_info.iloc[0, 5] = si1.iloc[0, 5] + " 'Appended' " + si2.iloc[0, 5]
                station_info.iloc[0, 6] = si1.iloc[0, 6] + " 'Appended' " + si2.iloc[0, 6]
                station_info[8] = "FILE1: '" + fn1 + "' FROM: '" + str(ts1) + "' TO: '" + str(te1) +  "'"
                station_info[9] = "&"
                station_info[10] = "FILE2: '" + fn2 + "' FROM: '" + str(ts2) + "' TO: '" + str(te2) + "'"
                station_info[11] = "Appended"
                if si2.iloc[0,12] == "filtered":
                    station_info[12] = "filtered"
                    station_info[13] = si2[13]
                if si2.iloc[0,14] == "crct_unit":
                    station_info[14] = "crct_unit"
                    station_info[15] = si2[15]                    
                station_info = station_info.astype(str)
                station_info[(station_info == 'nan')] = ''
                station_info[(station_info == 'None')] = ''              
            elif d_type1 == "Satellite": # append SATELLITE data               
                station_info = si1
                station_info.iloc[0,0] = "FILE1: '" + fn1 + "' FROM: '" + str(ts1) + "' TO: '" + str(te1) +  "'"
                station_info.iloc[0,1] = "&"
                station_info.iloc[0,2] = "FILE2: '" + fn2 + "' FROM: '" + str(ts2) + "' TO: '" + str(te2) + "'"
                station_info.iloc[0,3] = "Appended"
                if si2.iloc[0,4] == "filtered":
                    station_info[4] = "filtered"
                    station_info[5] = si2[5]
#..............................................................................
            data = data1.append(data2, ignore_index=True) #append the second file below the firs file and reset the index number
            data = data.replace(to_replace = np.nan, value ="None") # replace the nan values with NONE
            print("Checking the time intervals at the boundary of the files")
            data = definterval_fix(data,d_type1) # fix the time interval of the new appended file and get the corrected data as an output
            data.iloc[:,1] = range(1,len(data)+1) #Update the number of records                     
#..............................................................................                
            print("________________________________________ DONE ")
            print("________________________________________ SAVE THE NEW FILE")
            prcss = "A" #merged
            output_path,output,data = defuisave(fp1,station_info,pi1,data,d_type1,station_name1,prcss) # save the generated new file as the user want
            print("________________________________________ FILE REPORT (new file)")
            fp1,si1,pi1,data1,d_type1,station_name1,fn1,t_start1,t_end1 = \
            defuiopen("",output_path) # consider the new generated file as a new input file            
            input("press any key to continue >>> ")
            return fp1,si1,pi1,data1,d_type1,station_name1,fn1
"""=============================================================================
FUNCTION:
It appends two local files below each other, before the appending process it checks
which of the two selected files is older and put it in top of the newer one,
It checks the number of columns and the time gaps at the boundary of the selected files
New columns after columns correction and new rows after time gaps (missing rows)
correction will be filled by "nan".
1-defuiopen
2-defapnd_strt
============================================================================="""
def defrun_append():
    while True:
        maintfilt = input("________________________________________ FILTER (MAINTENANCE & ANOMALIES) ???"
                     "\n1: YES (I have the maintenance file)"
                     "\n2: YES (I don't have the maintenance file)"
                     "\n3: NO (keep the data as it is)"
                     "\nmm: MAIN MENU \n"
                     "Enter a number >>> ")
        if maintfilt == "mm":
            return
        elif maintfilt == "1":
            print("________________________________________ IMPORT THE MAINTENANCE FILE")    
            root = tk.Tk() 
            root.withdraw()   
            if platform == "darwin": # in mac
                print('\a') 
            elif platform == "win32": # in windows
                winsound.Beep(frequency, duration)      
            fp_maintfilt = filedialog.askopenfilename(title = "Import maintenance file",defaultextension ='.xlsx',
                   filetypes = (("CSV files","*.xlsx"),("all files","*.*")),parent = root)                    
            break
        elif maintfilt == "2" or maintfilt == "3":
            fp_maintfilt = []
            break
        else:
            pass
# Import the first file    
    while True:
        tmp = []
        print("________________________________________ IMPORT THE FIRST FILE ")
        print("________________________________________ FILE REPORT (first file)")
        fp1,si1,pi1,data1,d_type1,station_name1,fn1,t_start1,t_end1 = \
        defuiopen("Select the first '*.CSV' file",[]) #select and import the first file
        if len(fp1) == 0:
            while True: # check if the user selected any file or not
                re_imp = input ("________________________________________ NO IMPORTED FILE"
                                "\n1: Try again"
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> ") 
                if re_imp == "1":
                    break
                if re_imp == "mm":
                    return
        else: 
            while True: # confirm the selected file or select another one
                confirm = input("________________________________________ SELECT"
                                "\n1: Ooops, this is a wrong file (pick another)" 
                                "\n2: NEXT (import the second file) "
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> " )
                if confirm == "1":
                    break
                elif confirm == "mm":
                    return
                elif confirm == "2":                    
#.............................................................................. 
# Import the second file                     
                    while True:
                        print("________________________________________ IMPOER A '" + d_type1.upper() + "' FILE FROM '" + station_name1.upper() + "' STATION")
                        print("________________________________________ FILE REPORT (second file)")
                        fp2,si2,pi2,data2,d_type2,station_name2,fn2,t_start2,t_end2 = \
                        defuiopen("Select the second '*.CSV' file",[]) #select and import the second file
                        if len(fp2) == 0:
                            while True: # check if the user selected any file or not
                                re_imp = input ("________________________________________ NO IMPORTED FILE"
                                                "\n1: Try again"
                                                "\nmm: MAIN MENU \n"
                                                "Enter a number >>> ") 
                                if re_imp == "1":
                                    break
                                if re_imp == "mm":
                                    return
                        else: 
                            cntnu = True
#..............................................................................
                            print("________________________________________ PLEASE WAIT ... ")
                            print("Checking the compatibility of the files")                             
                            if t_start1==t_start2 and t_end1==t_end2: # error if both files are identical
                                cntnu = False
                                while True:
                                    tmp = input("________________________________________ IDENTICAL FILES"
                                          "\n1: Import the second file again"
                                          "\n2: Change the first file"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> " )
                                    if tmp == "2":
                                        break
                                    elif tmp == "mm":
                                        return
                                    elif tmp == "1":
                                        cntnu = True
                                        break
#..............................................................................
                            if d_type2 != d_type1: # error if both files are not from same type
                                cntnu = False
                                while True:
                                    tmp = input("________________________________________ NOT A " + d_type1.upper() + "FILE"
                                          "\n1: Import the second file again"
                                          "\n2: Change the first file"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> " )
                                    if tmp == "2":
                                        break
                                    elif tmp == "mm":
                                        return
                                    elif tmp == "1":
                                        cntnu = True
                                        break
#..............................................................................
                            if station_name2 != station_name1: # error if both files are not from same station
                                cntnu = False
                                while True:
                                    tmp = input("________________________________________ NOT FROM " + station_name1.upper() + "STATION"
                                          "\n1: Import the second file again"
                                          "\n2: Change the first file"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> " )
                                    if tmp == "2":
                                        break
                                    elif tmp == "mm":
                                        return
                                    elif tmp == "1":
                                        cntnu = True
                                        break
#..............................................................................
                            tend1 = pd.to_datetime(data1.iloc[len(data1) - 1, 0]) # convert the last recorded time of the first file to time format
                            tstart2 = pd.to_datetime(data2.iloc[0, 0]) # convert the first recorded time of the second file to time format
                            if tend1 > tstart2: # check which file is older to be on top and consider as file 1
                                fpt1,sit1,pit1,datat1,d_typet1,station_namet1,fnt1,t_startt1,t_endt1 = fp1,si1,pi1,data1,d_type1,station_name1,fn1,t_start1,t_end1
                                fp1,si1,pi1,data1,d_type1,station_name1,fn1,t_start1,t_end1 = fp2,si2,pi2,data2,d_type2,station_name2,fn2,t_start2,t_end2
                                fp2,si2,pi2,data2,d_type2,station_name2,fn2,t_start2,t_end2 = fpt1,sit1,pit1,datat1,d_typet1,station_namet1,fnt1,t_startt1,t_endt1    
                            if t_start1 == t_start2 or t_end1 == t_end2 or t_start2 < t_end1 or t_end1 > t_start2: # error if there is an overlap in time
                                cntnu = False
                                while True:
                                    tmp = input("________________________________________ OVERLAP IN TIME \n"
                                          "\n1: Import the second file again"
                                          "\n2: Change the first file"
                                          "\nmm: MAIN MENU \n"
                                          "Enter a number >>> " )   
                                    if tmp == "2":
                                        break
                                    elif tmp == "mm":
                                        return
                                    elif tmp == "1":
                                        cntnu = True
                                        break
#..............................................................................
                            if cntnu == True: # if there is no problem on the imported files
                                print("The imported files are compatible for appending process")
                                while True: # confirm the second file
                                    confirm = input("________________________________________ SELECT"
                                                    "\n1: Ooops, this is a wrong file (pick another)"
                                                    "\n2: NEXT (Check time intervals & columns & units & maintenance and anomalies)"
                                                    "\nmm: MAIN MENU \n"
                                                    "Enter a number >>> " )
                                    if confirm == "1":
                                        break
                                    elif confirm == "mm":
                                        return
                                    elif confirm == "2":
#..............................................................................                                        
# filtering and corrections (columns & time intervals & EC_unit & maintenance and anomalies)                                    
                                        print("________________________________________ PLEASE WAIT ... ")
                                        print("Checking time intervals (data 1)")
                                        t_int1,_ = defcheck_int(data1)
                                        print("Checking time intervals (data 2)")
                                        t_int2,_ = defcheck_int(data2)                                        
                                        if t_int1 > 1:                                                
                                            print("Unifying time intervals (data 1)")                                           
                                            data1 = definterval_fix(data1,d_type1) # unify the time interval                                        
                                        if t_int2 > 1:                                                
                                            print("Unifying time intervals (data 2)")                                           
                                            data2 = definterval_fix(data2,d_type2) # unify the time interval
                                        print("Checking the columns and parameters (data 1)")
                                        data1,pi1,si1 = deffix_columns(pi1,si1,data1,d_type1)                                        
                                        print("Checking the columns and parameters (data 2)")
                                        data2,pi2,si2 = deffix_columns(pi2,si2,data2,d_type2)
                                        if d_type1 == "Local":
                                            print("Checking the units (data 1)")
                                            data1,si1,pi1 = defEC_unit(data1,station_name1,si1,pi1)
                                        if d_type2 == "Local":                                          
                                            print("Checking the units (data 2)")
                                            data2,si2,pi2 = defEC_unit(data2,station_name2,si2,pi2)
                                        if maintfilt == "1" or maintfilt == "2":
                                            print("Filtering the anomalies and maintenances (data 1)")
                                            data1,si1 = defmaint(maintfilt,fp_maintfilt,data1,station_name1,si1,d_type1) # replace the maintenance with nan                                              
                                            print("Filtering the anomalies and maintenances (data 2)")
                                            data2,si2 = defmaint(maintfilt,fp_maintfilt,data2,station_name2,si2,d_type2) # replace the maintenance with nan
#..............................................................................                                        
# start the appending process and get the new appended file as an output
                                        fp1,si1,pi1,data1,d_type1,station_name1,fn1 = \
                                                     defapnd_strt(fp1,si1,pi1,data1,d_type1,fn1,
                                                     fp2,si2,pi2,data2,d_type2,fn2,station_name1)
#.............................................................................. 
# ask if the user want to append another file to the new generated file                                                     
                                        while True:
                                            app_agn = input("________________________________________ SELECT"
                                                        "\n1: Append another file to the new generated file"
                                                        "\nmm: MAIN MENU \n"
                                                        "Enter a number >>> " )
                                            if app_agn == "mm":
                                                return
                                            elif app_agn == "1":
                                                break
                                        if app_agn == "1":
                                            break
                        if tmp == "2":
                            break                                        
                if tmp == "2":
                    break
"""**********************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
**********************************************************************************************************"""
"""PACKAGE OF FUNCTIONS (fill the satellite gaps)"""
"""=============================================================================
FUNCTION (After extract info):

============================================================================="""        
def deffill_comp(data_s,data_l,nan_ind_s,fn_s,fn_l):            
    ts_s = pd.to_datetime(data_s.iloc[0, 0]) # first recorded time in satellite data    
    te_s = pd.to_datetime(data_s.iloc[len(data_s) - 1, 0]) # last recorded time in satellite data
    ts_l = pd.to_datetime(data_l.iloc[0, 0]) # first recorded time in local data      
    te_l = pd.to_datetime(data_l.iloc[len(data_l) - 1, 0]) # last recorded time in local data         
    par = ["TIMESTAMP","AirTC_Avg","RH","SlrW_Avg","VWC_Avg","GrTemp_Avg",
           "WS_ms_Avg","WS_ms_max","WindDir_Avg","Rain_mm_Tot","BP_mbar_Avg"] # column names of satellite file as it is written in local files
    new_local = data_l[par] #from the local file only pick the satellite parameters columns (same local file but all the unnecessary parameters are removed)
    date_local = list(new_local.iloc[:,0].astype(str)) #time column of the new local data
    d_nan = data_s.iloc[nan_ind_s,0] #Index of the missing rows in the satellite file
    date_nan = list(d_nan.astype(str)) #Date of the missing rows in the satellite file
#Find the index of the rows in the local file which has a same date as the rows
#in the satellite file with "None" value
    j=[]
    for i in range(len(date_nan)):
        try:
            temp = date_local.index(str(date_nan[i]))
            j.append(temp) #Index (local file) of all the missing data which can be filled
        except:
            pass
    figtxt = ("* Satellite file: " + fn_s + "\n  "
              + str(ts_s) + " ---> " + str(te_s) + " (Dark area)\n  "
              "Timestamps with missing data (none): " + str(len(nan_ind_s)) + " (Red dots) \n \n"
              "* Local file: " + fn_l + "\n  "
              + str(ts_l) + " ---> " + str(te_l) + " (Green area)\n  "
              "Gaps might be filled: ~" + str(len(j)) + "(Blue dots)")       
    print("________________________________________ ATTENTION \n"
          "* Satellite file: " + fn_s + "\n"
          "  " + str(ts_s) + " ---> " + str(te_s) + "\n"
          "  Timestamps with missing data (none): " + str(len(nan_ind_s)) + "\n \n"
          "* Local file: " + fn_l + "\n"
          "  " + str(ts_l) + " ---> " + str(te_l) + "\n"
          "  Gaps might be filled: ~" + str(len(j)))              
    xn_lnplt = data_s.iloc[nan_ind_s,0]
    yn_lnplt = pd.DataFrame(1 , index = range(len(nan_ind_s)), columns=[0])
    xc_lnplt = (pd.DataFrame(date_local)).iloc[j,0]
    xc_lnplt = pd.to_datetime(xc_lnplt)
    yc_lnplt = pd.DataFrame(0.75 , index = range(len(j)), columns=[0])
    start1 = mdates.date2num(data_s.iloc[0,0])
    end1 = mdates.date2num(data_s.iloc[len(data_s)-1,0])
    wdth1 = end1 - start1
    start2 = mdates.date2num(data_l.iloc[0,0])
    end2 = mdates.date2num(data_l.iloc[len(data_l)-1,0])
    wdth2 = end2 - start2
    plt.figure()
    fig = plt.gcf()
    ax = plt.gca()
    rect1 = Rectangle((start1,0),wdth1,1, facecolor="gray",edgecolor="black")
    rect2 = Rectangle((start2,0),wdth2,0.75, facecolor="lime",edgecolor="darkgreen")
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    plt.plot(xn_lnplt, yn_lnplt,'or',markersize=3)
    plt.plot(xc_lnplt, yc_lnplt,'ob',markersize=3)
#    locator = mdates.AutoDateLocator(minticks=3)
#    formatter = mdates.AutoDateFormatter(locator)
#    ax.xaxis.set_major_locator(locator)
    myFmt = mdates.DateFormatter('%y-%m-%d %H:%M')
    plt.title("Distribution of missing and filled data", fontsize = 14, fontweight='bold')
    ax.xaxis.set_major_formatter(myFmt)
    ax.axes.get_yaxis().set_visible(False)
    extrm = round((max(end1,end2) - min(start1,start2)) / 10)
    plt.xlim([min(start1,start2) - extrm, max(end1,end2) + extrm])
    plt.ylim([0, 5])
    plt.xticks(np.unique(np.array([start1,start2,end2,end1])))
    plt.xlabel("Time (yy-mm-dd HH-MM)", color='black', fontsize = 14, fontweight='bold')
    fig.autofmt_xdate()
    plt.figtext(0.2,0.48,figtxt,size=14)
    fig.set_size_inches((9, 5), forward=True)
    ax.set_aspect(round((max(end1,end2) - min(start1,start2)) / 9))
    if platform == "win32":
        print("________________________________________ ATTENTION \n"
              "* In case of using 'WINDOWS COMMAND PROMPT': \n"
              "* Close the opened figure(s) manually to continue")
        plt.show()
    elif platform == "darwin":
        plt.show(block=False)
    return new_local,j
"""=============================================================================
FUNCTION (After extract info):

============================================================================="""        
def deffill_run(fp_s,new_local,j,data_s,nan_ind_s,si_s,pi_s,d_type_s,station_name_s):
    output = data_s
    for i in range(len(j)):
        if j[i] == 0:
            pass
        else:
            AirTC_Avg = np.mean([new_local.iloc[j[i],1],new_local.iloc[j[i]-1,1]])
            RH = np.mean([new_local.iloc[j[i],2],new_local.iloc[j[i]-1,2]])
            SlrW_Avg = np.mean([new_local.iloc[j[i],3],new_local.iloc[j[i]-1,3]])
            VWC_Avg = np.mean([new_local.iloc[j[i],4],new_local.iloc[j[i]-1,4]])
            GrTemp_Avg = np.mean([new_local.iloc[j[i],5],new_local.iloc[j[i]-1,5]])
            WS_ms_Avg = np.mean([new_local.iloc[j[i],6],new_local.iloc[j[i]-1,6]])
            WS_ms_max = np.max([new_local.iloc[j[i],7],new_local.iloc[j[i]-1,7]])
            WindDir_Avg = np.mean([new_local.iloc[j[i],8],new_local.iloc[j[i]-1,8]])
            Rain_mm_Tot = np.sum([new_local.iloc[j[i],9],new_local.iloc[j[i]-1,9]])
            BP_mbar_Avg = np.mean([new_local.iloc[j[i],10],new_local.iloc[j[i]-1,10]])
            fill_row = [AirTC_Avg,RH,SlrW_Avg,VWC_Avg,GrTemp_Avg,WS_ms_Avg,
                        WS_ms_max,WindDir_Avg,Rain_mm_Tot,BP_mbar_Avg]
            output.iloc[nan_ind_s[i],2:] = fill_row
    print("________________________________________ DONE ")
    print("________________________________________ SAVE THE NEW FILE")
    prcss = "F" #filled
    output_path,output,data_sf = defuisave(fp_s,si_s,pi_s,output,d_type_s,station_name_s,prcss)    
    print("________________________________________ NEW FILE INFO")
    fp_s,si_s,pi_s,data_s,d_type_s,station_name_s,fn_s,t_start_s,t_end_s = \
    defuiopen("",output_path) # consider the new generated file as an input satellite file
    input("press any key (MAIN MENU) >>> ")    
    return fp_s,si_s,data_s,d_type_s,station_name_s,data_s
"""=============================================================================
FUNCTION:
This function finds the row(s) in the satellite file which at least have one
missing data ("None"). It extract the time of that row, find the similar time in
the relevant local file and replace that missing row with its local data
The replacing process is a bit tricky since the satellite data was recorded every
1 hour and the local data every 30 minutes, therefore to fill the missing satellite
row an appropriate calculation for each parameter must be used. for example:
to fill air temperature at 14:00 in satellite file, the average of 14:00 and 13:30 at
local file must be calculated. for different parameter it's different
(could be also sum or max or min). At the end it check the new file and ask for save
1- defuiopen
2- defext_info
3- definterval_fix
4- deffill_run
============================================================================="""
def defsat_fill():
    while True:
        maintfilt = input("________________________________________ FILTER (MAINTENANCE & ANOMALIES) ???"
                     "\n1: YES (I have the maintenance file)"
                     "\n2: YES (I don't have the maintenance file)"
                     "\n3: NO (keep the data as it is)"
                     "\nmm: MAIN MENU \n"
                     "Enter a number >>> ")
        if maintfilt == "mm":
            return
        elif maintfilt == "1":
            print("________________________________________ IMPORT THE MAINTENANCE FILE")    
            root = tk.Tk() 
            root.withdraw()   
            if platform == "darwin": # in mac
                print('\a') 
            elif platform == "win32": # in windows
                winsound.Beep(frequency, duration)      
            fp_maintfilt = filedialog.askopenfilename(title = "Import maintenance file",defaultextension ='.xlsx',
                   filetypes = (("CSV files","*.xlsx"),("all files","*.*")),parent = root)                    
            break
        elif maintfilt == "2" or maintfilt == "3":
            fp_maintfilt = []
            break
        else:
            pass    
    while True:  
#..............................................................................
# import a satellite file        
        print("________________________________________ IMPORT A SATELLITE FILE")
        print("________________________________________ FILE REPORT (satellite)")
        fp_s,si_s,pi_s,data_s,d_type_s,station_name_s,fn_s,t_start_s,t_end_s = \
        defuiopen("Select the first '*.CSV' file",[]) #select and import the first file
        if len(fp_s) == 0:
            while True:
                re_imp = input ("________________________________________ NO IMPORTED FILE"
                                "\n1: Try again"
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> ") 
                if re_imp == "1":
                    break
                if re_imp == "mm":
                    return
        else:
#..............................................................................
            if d_type_s != 'Satellite':
                input("________________________________________ ATTENTION REQUIRED \n"
                      "* This is not a 'SATELLITE' file \n"
                      "press any key and import a 'SATELLITE' file >>> ")
            else:
                while True:
#..............................................................................
# confirm or reject the imported satellite file                    
                    confirm = input("________________________________________ SELECT"
                                    "\n1: Ooops, this is a wrong file (pick another)"
                                    "\n2: NEXT (import an associated (same station) 'LOCAL' file)"
                                    "\nmm: MAIN MENU \n"
                                    "Enter a number >>> ")
                    if confirm == "1":
                        break
                    elif confirm == "mm":
                        return
                    elif confirm == "2":
                        app_agn =[]
                        while True:
#..............................................................................
# import an associated local file                            
                            print("________________________________________ IMPOER A LOCAL FILE FROM '" + station_name_s.upper() + "' STATION") 
                            print("________________________________________ FILE REPORT (local)")
                            fp_l,si_l,pi_l,data_l,d_type_l,station_name_l,fn_l,t_start_l,t_end_l = \
                            defuiopen("Select the first '*.CSV' file",[]) #select and import the first file
                            if len(fp_l) == 0:
                                while True:
                                    re_imp = input ("________________________________________ NO IMPORTED FILE"
                                                    "\n1: Try again"
                                                    "\nmm: MAIN MENU \n"
                                                    "Enter a number >>> ") 
                                    if re_imp == "1":
                                        break
                                    if re_imp == "mm":
                                        return
                            else:
#..............................................................................
# confirm or reject the imported local file                               
                                if d_type_l != 'Local':
                                    input("________________________________________ NOT A LOCAL FILE \n"
                                          "press any key and import an associated (same station) 'LOCAL' file >>> ")
                                elif station_name_s != station_name_l:
                                    input("________________________________________ NOT FROM " + station_name_s.upper() + "STATION"
                                          "press any key and import an associated (same station) 'LOCAL' file >>> ")
                                else:
                                    while True:
                                        confirm = input("________________________________________ SELECT"
                                                        "\n1: Ooops, this is a wrong file (pick another)"
                                                        "\n2: NEXT (check the time gaps, time intervals and filtering)"
                                                        "\nmm: MAIN MENU \n"
                                                        "Enter a number >>> ")
                                        if confirm == "mm":
                                            return
                                        elif confirm == "2":
#..............................................................................
# fixing local data
                                            print("________________________________________ PLEASE WAIT ... ")
                                            print("Checking time intervals")
                                            t_int_s,nan_ind_s = defcheck_int(data_s)
                                            t_int_l,_ = defcheck_int(data_l)                                        
                                            if t_int_s > 1:                                                
                                                print("Unifying time intervals (Satellite)")                                           
                                                data_s = definterval_fix(data_s,d_type_s) # unify the time interval                                        
                                            if t_int_l > 1:                                                
                                                print("Unifying time intervals (Local)")                                           
                                                data_l = definterval_fix(data_l,d_type_l) # unify the time interval
                                            print("Checking the columns and parameters (Satellite)")
                                            data_s,pi_s,si_s = deffix_columns(pi_s,si_s,data_s,d_type_s)                                        
                                            print("Checking the columns and parameters (Local)")
                                            data_l,pi_l,si_l = deffix_columns(pi_l,si_l,data_l,d_type_l)
                                            if d_type_s == "Local":
                                                print("Checking the units (Satellite)")
                                                data_s,si_s,pi_s = defEC_unit(data_s,station_name_s,si_s,pi_s)
                                            if d_type_l == "Local":                                          
                                                print("Checking the units (Local)")
                                                data_l,si_l,pi_l = defEC_unit(data_l,station_name_l,si_l,pi_l)
                                            if maintfilt == "1" or maintfilt == "2":
                                                print("Filtering the anomalies and maintenances (Satellite)")
                                                data_s,si_s = defmaint(maintfilt,fp_maintfilt,data_s,station_name_s,si_s,d_type_s) # replace the maintenance with nan                                              
                                                print("Filtering the anomalies and maintenances (Local)")
                                                data_l,si_l = defmaint(maintfilt,fp_maintfilt,data_l,station_name_l,si_l,d_type_l) # replace the maintenance with nan                                                                                         
#..............................................................................
# find if satellite file has missing date at the beginning of the data.
# Satellite file is started later than the local data
                                            if data_s.iloc[0,0] > data_l.iloc[0,0]:
                                                A_str = str(data_s.iloc[0,0]) # start date of satellite record
                                                B = data_l.iloc[:,0] == A_str
                                                t_ind = B.index[B].tolist() # index of the first satellite record in local data
                                                t_ind = t_ind[0] - 2 # find 1 hour before
                                                if (data_l.iloc[0,0]).minute != 0:
                                                    rng = pd.date_range(start=data_l.iloc[1,0], end=data_l.iloc[t_ind,0], freq='H') # make a missing time range in satellite file
                                                else:
                                                    rng = pd.date_range(start=data_l.iloc[0,0], end=data_l.iloc[t_ind,0], freq='H') # make a missing time range in satellite file
                                                temp_df = pd.DataFrame(np.nan,index=range(len(rng)),columns=data_s.columns.tolist())
                                                temp_df.iloc[:,0] = rng
                                                temp_df.iloc[:,1] = station_name_s 
                                                data_s = temp_df.append(data_s, ignore_index=True)
                                            nan_ind_s = pd.isnull(data_s).any(1).nonzero()[0] # find the index of rows with at least one missing (nan) value
#..............................................................................
# visualizing missing values                                            
                                            new_local,j = deffill_comp(data_s,data_l,nan_ind_s,fn_s,fn_l)
#..............................................................................
# start to look for the missing values and try to fill them by the local data 
                                            while True:                                               
                                                confirm = input("________________________________________ SELECT"
                                                                "\n1: Fill the missing data (none)"
                                                                "\nmm: MAIN MENU \n" 
                                                                "Enter a number >>> " )
                                                if confirm == "mm":
                                                    return
                                                elif confirm == "1":
                                                    print("________________________________________ FILLING THE GAPS \n"
                                                          "please wait...")
                                                    fp_s,si_s,data_s,d_type_s,station_name_s,data_s = \
                                                    deffill_run(fp_s,new_local,j,data_s,nan_ind_s,si_s,pi_s,d_type_s,station_name_s)
                                                    while True:
                                                        app_agn = input("________________________________________ SELECT"
                                                                    "\n1: Use another local file to fill more gaps"
                                                                    "\nmm: MAIN MENU \n"
                                                                    "Enter a number >>> " )
                                                        if app_agn == "mm":
                                                            return
                                                        elif app_agn == "1":
                                                            break
                                                if app_agn == "1":
                                                    break
                                        if app_agn == "1":
                                            break
"""**********************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
**********************************************************************************************************"""
"""=============================================================================
FUNCTION: calculate monthly mean and std of temperature and precipitation
============================================================================="""
def defexcel():
    while True:
        maintfilt = input("________________________________________ FILTER (MAINTENANCE & ANOMALIES) ???"
                     "\n1: YES (I have the maintenance file)"
                     "\n2: YES (I don't have the maintenance file)"
                     "\n3: NO (keep the data as it is)"
                     "\nmm: MAIN MENU \n"
                     "Enter a number >>> ")
        if maintfilt == "mm":
            return
        elif maintfilt == "1":
            print("________________________________________ IMPORT THE MAINTENANCE FILE")    
            root = tk.Tk() 
            root.withdraw()   
            if platform == "darwin": # in mac
                print('\a') 
            elif platform == "win32": # in windows
                winsound.Beep(frequency, duration)      
            fp_maintfilt = filedialog.askopenfilename(title = "Import maintenance file",defaultextension ='.xlsx',
                   filetypes = (("CSV files","*.xlsx"),("all files","*.*")),parent = root)                    
            break
        elif maintfilt == "2" or maintfilt == "3":
            fp_maintfilt = []
            break
        else:
            pass
#..............................................................................            
    while True:
        print("________________________________________ FILE REPORT (first file)")
        fp,si,pi,data,d_type,station_name,fn,t_start,t_end = \
        defuiopen("Select the first '*.CSV' file",[]) #select and import the first file
        if len(fp) == 0: # check if any file is selected
            while True:
                re_imp = input ("________________________________________ NO IMPORTED FILE"
                                "\n1: Try again"
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> ") 
                if re_imp == "1": # try to select a file
                    break
                if re_imp == "mm": # back to the main menu
                    return
        else:            
            while True:
                confirm = input("________________________________________ SELECT "
                                "\n1: Ooops, this is a wrong file (pick another)"
                                "\n2: NEXT (calculation and making the Excel file)"
                                "\nmm: MAIN MENU \n"
                                "Enter a number >>> " )
                if confirm == "1": # select a wrong file (go back to select another one)
                    break
                elif confirm == "mm": # back to the main menu
                    return []
                elif confirm == "2": # correct file, go to next step
                    print("________________________________________ PLEASE WAIT ... ")
                    print("Checking time intervals")
                    t_int,_ = defcheck_int(data)                                      
                    if t_int > 1:                                                
                        print("Unifying time intervals (data 1)")                                           
                        data = definterval_fix(data,d_type) # unify the time interval
                    print("Checking the columns and parameters (data 1)")
                    data,pi,si = deffix_columns(pi,si,data,d_type)                                        
                    if d_type == "Local":
                        print("Checking the units (data 1)")
                        data,si,pi = defEC_unit(data,station_name,si,pi)
                    if maintfilt == "1" or maintfilt == "2":
                        print("Filtering the anomalies and maintenances (data 1)")
                        data,si = defmaint(maintfilt,fp_maintfilt,data,station_name,si,d_type) # replace the maintenance with nan
#..............................................................................       
                    time1 = data.iloc[:,0]
                    fy = time1.iloc[0].year
                    ly = time1.iloc[-1].year
                    time2 = pd.DataFrame(np.nan,index=range(len(time1)),columns=["timestamp","year","month","day"])
                    time2.loc[:,"timestamp"] = time1
#..............................................................................                    
                    print("Making a dataframe with seperated date values")
                    for i in range(len(time1)):
                        time2.loc[i,"year"] = time2.loc[i,"timestamp"].year
                        time2.loc[i,"month"] = time2.loc[i,"timestamp"].month
                        time2.loc[i,"day"] = time2.loc[i,"timestamp"].day                                                
                    frst_col = ["January","February","March","April","May","Jun",
                                "July","August","September","October","November","December"]
                    clmn_ind = ["Month","Nmonth","Ndays","MEAN T","STD T","MEAN P","STD P"]
                    units = ["-","#","","[Deg C]","[Deg C]","[mm/M]","[mm/M]"]
                    temp_un =  list(range(fy,ly+1))
                    for i in temp_un:
                        units[2] = units[2] + " / " + str(i)
                    units[2] = units[2][3:]   
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
#..............................................................................                        
                    print("Calculating MEAN & STD")    
                    for m in range(1,13):
                        print("Working on " + frst_col[m-1])
                        m_ind = []
                        nm = 0 # number of full month
                        output.loc[m+1,"Ndays"] = ""
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
                            days_month = round(abs(len(ind_temp)-nan_ind)/t_int,0) # total number of recorded data (day) in a month
                            output.loc[m+1,"Ndays"] = output.loc[m+1,"Ndays"] + " / " +  str(days_month)
                            if days_month >= 28: # if number of recorded data in that month is more than 28 days
                                nm = nm + 1 
                                m_ind = m_ind + ind_temp
                        output.loc[m+1,"Nmonth"] = nm                     
                        tt = output.loc[m+1,"Ndays"]
                        output.loc[m+1,"Ndays"] = tt[3:]
                        if nm >= 1:        
                            output.loc[m+1,"MEAN T"] = np.round(np.nanmean(np.array(data.loc[m_ind,par[0]])),2)
                            output.loc[m+1,"MEAN P"] = np.round(np.nansum(np.array(data.loc[m_ind,par[1]]))/nm,2)                            
                            output.loc[m+1,"STD T"] = np.round(np.nanstd(np.array(data.loc[m_ind,par[0]])),2)
                            output.loc[m+1,"STD P"] = np.round(np.nanstd(np.array(data.loc[m_ind,par[1]])),2)
#..............................................................................                        
                    sht_name = os.path.basename(fp)
                    sht_name = sht_name[:-4]
                    auto_fname = "Monthly_mean_std.xlsx"
                    output_path = fp.replace(os.path.basename(fp),auto_fname) #file path without file name
                    if os.path.exists(output_path):
                        book = load_workbook(output_path)
                        writer = pd.ExcelWriter(output_path, engine = 'openpyxl')
                        writer.book = book
                    else:                        
                        writer = pd.ExcelWriter(output_path,engine='xlsxwriter')
                    output.to_excel(writer, sheet_name=sht_name, na_rep='None', float_format='%G',header=False, index=False)
                    writer.save()
                    writer.close()
                    input("The new file saved at: \n" 
                          + fp + "\n"
                          + "as: " + auto_fname + "\n"
                          + "sheet: " + sht_name + "\n"
                          + "press any key (MAIN MENU) >>> ")
                    break
            break
"""**********************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
**********************************************************************************************************"""
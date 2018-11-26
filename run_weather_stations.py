# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 06:00:55 2017

@author: M.Reza Ershadi / University of Tübingen
         mohammadreza.ershadi@student.uni-tuebingen.de 
         (mreza.ershadi@web.de)
         
Written in: Anaconda 3 (Python 3.6)
("=============================================================================")
("          EARTHSHAPE CHILE WEATHER STATIONS DATA MANAGEMENT (V_8)           ")
("=============================================================================")
"""

#print("=============================================================================")
#print("=============================================================================")
#print("                 =    =  ======  =       =       ======                M.R.E.")
#print("                 =    =  =       =       =       =    =                      ")
#print("                 ======  ======  =       =       =    =                      ")
#print("                 =    =  =       =       =       =    =                      ")
#print("                 =    =  ======  ======  ======  ======                M.R.E.")
print("=============================================================================")
print("          EARTHSHAPE CHILE WEATHER STATIONS DATA MANAGEMENT (V_8)           ")
print("=============================================================================")
#print("***THE CODE***\n"
#      "*Anaconda 3 (Python 3.6) \n")
#print("***THE PROGRAM***\n"
#      "*Use this program only with:\n"
#      "*EARTHSHAPE CHILE WEATHER STATIONS DATA to:\n"
#      " -Look at the details of the files \n"
#      " -Plot the data \n"
#      " -Append files \n"
#      " -Fill the missing data (None) \n")
#print("***ATTENTION***\n"
#      "*Try to use 'TERMINAL' or 'WINDOWS COMMAND PROMPT' to run the program \n"
#      "*Always use the given numbers as an input except (mm for MAIN MENU & b for BACK). \n"
#      "*Be careful about the popup windows! \n"
#      " -They come with a sound and sometimes they are behind the other programs. \n")
#print("***KNOWN BUGS***\n"
#      "*In Windows Command Prompt: \n"
#      " -The interactive plot doesn't work, which means: \n"
#      " -After you plot something you should close it manually to continue. \n" 
#      "*If you are using SPYDER in MAC: \n"
#      " -The opened file dialog freezes. \n")
#input("Press any key to START >>> ")

import def_weather_stations as dws
"""=============================================================================
RUN THE CODE
============================================================================="""
while True:   
    what = dws.defwhat()    
    if what == "1":
         dws.deffile_info()                  
    elif what == "2":
        plot_for = input("________________________________________ PLOT FOR TODD ???"
                         "\n1: NORMAL POLT"
                         "\n2: JUST FOR TODD \n"
                         "Enter a number >>> ")
        if plot_for == "1":
            dws.defrun_plot_normal()
        elif plot_for == "2":          
            dws.defrun_plot_TODD()
    elif what == "3":      
         dws.defrun_append()       
    elif what == "4":      
         dws.defsat_fill()
    elif what == "5":
         doutput = dws.defexcel()
    elif what == "H":
        try:        
            dws.def_help()
        except:
            input("OOPS, The 'HELP' file is missing \n"
                  "Press any key...")            
            pass                
    elif what == "Q":
        print("========================= BYE BYE ...")
        break
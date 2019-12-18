# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:05:56 2019

@author: mzly903
"""
# -*- coding: utf-8 -*-

import gmplot 
from pyflightdata import FlightData

f=FlightData()

AKL = f.get_airport_details('AKL')

HRK = f.get_airport_details('HRK')
  
latit_AKL, longit_AKL = AKL['position']['latitude'], AKL['position']['longitude']

latit_HRK, longit_HRK = HRK['position']['latitude'], HRK['position']['longitude']

latitude_list = [ latit_HRK, latit_AKL] 
longitude_list = [  longit_HRK ,longit_AKL] 
  
gmap3 = gmplot.GoogleMapPlotter(latit_AKL, longit_AKL, 73) 
  

gmap3.scatter( latitude_list, longitude_list, '# FF0000', size = 40, marker = False ) 

gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width = 2.5) 
  
gmap3.draw( "C:\\Users\\mzly903\\Desktop\\mapAKL_HRK.html" ) 
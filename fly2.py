# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:05:56 2019

@author: mzly903
"""
# -*- coding: utf-8 -*-

import gmplot 
from pyflightdata import FlightData

class airports():
    
    def __init__ (self, airport_dep, airport_arr):
        f=FlightData()
        self.airport_dep = f.get_airport_details(airport_dep)
        self.airport_arr = f.get_airport_details(airport_arr)
        
    def simple_line(self):
        

        latit_dep =  self.airport_dep['position']['longitude']
        longit_dep = self.airport_dep['position']['latitude']
        latit_arr, longit_arr = self.airport_arr['position']['latitude'],  self.airport_arr['position']['longitude']
        
        latitude_list = [float(latit_dep), float(latit_arr)]
        longitude_list = [float(longit_dep) , float(longit_arr)] 
        
        gmap3 = gmplot.GoogleMapPlotter(latit_dep, longit_dep, 20)
        gmap3.scatter( latitude_list, longitude_list, '# FF0000', size = 40, marker = False ) 
        gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width = 2.5) 
        return gmap3.draw( 'C:\\Users\\mzly903\\Desktop\\map' +str(latit_dep) + '.html' ) 
        


r = airports('AKL', 'KBP')
r.simple_line()
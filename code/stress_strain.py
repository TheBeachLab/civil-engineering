#!/usr/bin/env python3

# Stress ans Strain analysis
# Structural engineering open tools
# by Francisco Sanchez Arroyo
# Dec 2018, Barcelona
# MIT license

import platform
import os
import time

# clear screen


def cls():
    # Function to clear the screen
    if platform.system() == 'Windows':
        os.system('cls')  # windows
    elif platform.system() == 'Darwin' or 'Linux':
        os.system('clear')  # linux, osx


# materials dictionary name, young, poisson, etc
steel = {'name': 'Mild Steel',
         'density': 1800, 'density_units': 'kg/m3',
         'young': 21000, 'young_units': 'MPa', 'poisson': 0.3}
alu = {'name': 'Aluminum Alloys', 'density': 1800, 'density_units': 'kg/m3',
       'young': 21000, 'young_units': 'MPa', 'poisson': 0.33}
timber = {'name': 'Timber', 'density': 1800, 'density_units': 'kg/m3',
          'young': 21000, 'young_units': 'MPa', 'poisson': 0.3}

# sections dictionary
sections = {'I': '''
  <-- b -->   
t  XXXXXXXX  |
      XX     | 
e---->XX     h
      XX     |
   XXXXXXXX  |''', 'T': '''
   <-- b -->   
t  XXXXXXXX  |
      XX     | 
e---->XX     h
      XX     |
      XX     |''', 'R': '''
  <-- b -->   
  XXXXXXXX  |
  XXXXXXXX  |
  XXXXXXXX  h
  XXXXXXXX  |
  XXXXXXXX  |''', 'RH': '''
   <-- b -->   
t-->XXXXXXXX  |
    XX    XX  |
e-->XX    XX  h
    XX    XX  |
    XXXXXXXX  |''', 'C': '''
       |-r-->   
     xxxx             
  xXXXXXXXXx       
 xXXXXXXXXXXx      
 xXXXXXXXXXXx      
  xXXXXXXXXx        
     xXXx     ''', 'CH': '''
       |-r-->   
     x  x             
  x        x            

 x          x <-- e     
 x          x      
  x        x        
     x  x     '''
            }

print('Select material (s)teel, (a)luminum or (t)imber:')
mat = input()s
print(steel['name'])
print(sections['RH'])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:57:52 2024

@author: pancho

Write a convertToFahrenheit() function with a degreesCelsius parameter. This function returns the number of this temperature in degrees Fahrenheit. Then write a function named convertToCelsius() with a degreesFahrenheit parameter and returns a number of this temperature in degrees Celsius. 
"""

def convertToFahrenheit(degreesCelsius):
    fahrenheit = degreesCelsius × (9 / 5) + 32 
    return round(fahrenheit,2)

def convertToCelsius(degreesFahrenheit):
   celsius = (degreesFahrenheit - 32) × (5 / 9)
   return round(celsius,2)
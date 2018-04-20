# -*- coding:utf-8 -*-
"""
@author:Levy
@file:gisconvert.py
@time:2018/4/1918:46
"""
# 投影坐标系转地理坐标系
from pyproj import Proj, transform

inProj = Proj(init='epsg:26713') # NAD27 UTM 13N (X,Y)
outProj = Proj(init='epsg:4267') # NAD27 GEOGRAPHIC COORDINATE SYSTEM(LONGITUDE, LATITUDE)
x1,y1 = 525063.00, 5465840.00
x2,y2 = transform(inProj,outProj,x1,y1) # Transform this x,y point to geographic coordinate
print (x2,y2)

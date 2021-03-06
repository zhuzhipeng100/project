import openpyxl
import pandas as pd
import os
exec(open("chicago_community_areas.py").read())
"""
In order to convert the location of the CTA L stations
into the name of the neighborhood which each station belongs,
I have used the codes which belong to python library "chicago_neighborhood_finder,"
created by a data scientist "Craig. M. Booth."
Since the chicago_community_areas.py is written for Python 2.7, I have converted
some of the codes so that they could be run in Python 3.

The "chicago_community_areas.py" should be run to import the geocoding functions,
and get_community_area_coords() must be run to generate the dictionary of which
keys are names of neighborhood and the values are list of lists containing longitude and 
latitude.
"""
areas = get_community_area_coords()

df = pd.read_csv('../raw_file/school_quality.csv', header=None)

lng1 = df.loc[:,1][0:1218]
lng2 = df.loc[:,1][1218:] 
lat1 = df.loc[:,2][0:1218]
lat2 = df.loc[:,2][1218:]
df["lat"] = lat1.append(lng2)
df["lng"] = lng1.append(lat2)
df['community'] = df.apply(lambda col: get_neighborhood_for_point(col["lng"], col["lat"], areas), axis=1)

map = pd.read_csv('Community Area populations.csv')
map["Community Area"] = map["Community Area"].str.strip()
df.drop(df.columns[[1,2,3,5,6]], axis=1, inplace=True)

m = {}
for i in range(len(map)):
    m[map["Community Area"][i].strip()] = map["Num"][i]

m["Garfield Park"] = 27
m["Bucktown"] = 22
m["West Loop"] = 32
m["United Center"] = 28
m["Little Italy, UIC"] = 28
m["Mckinley Park"] = 59
m["Grand Crossing"] = 69
m["Andersonville"] = 77
m["Little Village"] = 30
m["River North"] = 8
m["Ukrainian Village"] = 24
m["Printers Row"] = 32
m["East Village"] = 24
m["Wicker Park"] = 24
m["Sauganash,Forest Glen"] = 12
m["Old Town"] = 8
m["Chinatown"] = 32
m["Galewood"] = 25
m["Sheffield & DePaul"] = 7
m["Boystown"] = 6
m["Rush & Division"] = 8

df["community"].replace(m, inplace=True)
df.columns = ['date', 'score', 'community']
df = df.pivot_table("score", "community", "date")
df[2015] = (df[2014]+df[2016])/2
df.loc[26] = [54, 52, 60, 57, 58]
df.loc[67] = [42, 39, 54, 51, 53]
df = df.unstack(level=0)
df = df.to_frame()
df = pd.DataFrame(df.to_records())
df = df.astype(int)
df = df.rename(columns={'0': 'score'})
df = df.sort_index(by=["date", "community"])
df.to_csv("../django_ui/search/data/final_school_data.csv", index=False)

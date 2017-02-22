import pandas as pd
import openpyxl

dta = pd.read_csv('/home/student/project/CTA_Ridership.csv')

dta = dta.sort(['date','rides'], axis = 0, ascending =[True, False])

# pd.dta.sort_values(['date', 'rides'], axis=0)
dta['date'] = pd.to_datetime(dta['date'])
dta = dta.groupby('date').head(10)
# dta = dta.groupby('date')['rides'].transform(sum)

# dta.to_csv('/home/zpzhu/cs122-win-17-zpzhu/pa3/ui/project/cta_data.csv')
def calctot(df):
    #delete columns
    df = df.drop(['station_id', 'stationname', 'date', 'daytype'], axis = 1)
    #append sum row, ignoring non-numeric column metrics
    return df.append(df.sum(numeric_only=True), ignore_index=True)

#groupby and reset index
nc =  dta.groupby('date').apply(calctot).reset_index()
#delete old index column
nc = nc.drop(['level_1'], axis=1)
#add new column onto the dataframe

# dta['rides1'] = pd.Series(nc, index = dta['date'])

#fill NaN to value tot
dta['date'] = dta['date'].fillna('tot')
date_sort = dta.sort('date')
    
# dta['date'] = dta.to_datetime(dta.Date)
# df.sort('Date')

# a dictionary containing the area code for the stations
name = {'18th': 31,
 '35-Bronzeville-IIT': 35,
 '35th/Archer': 59,
 '43rd': 38,
 '47th-Dan Ryan': 37,
 '47th-South Elevated': 35,
 '51st': 40,
 '63rd-Dan Ryan': 68,
 '69th': 69,
 '79th': 44,
 '87th': 44,
 '95th/Dan Ryan': 49,
 'Adams/Wabash': 32,
 'Addison-Brown': 5,
 'Addison-North Main': 6,
 "Addison-O'Hare": 16,
 'Argyle': 3,
 'Armitage': 7,
 'Ashland-Lake': 28,
 'Ashland-Orange': 31,
 'Ashland/63rd': 68,
 'Belmont-North Main': 6,
 "Belmont-O'Hare": 21,
 'Berwyn': 77,
 'Bryn Mawr': 77,
 'California-Cermak': 30,
 'California-Lake': 27,
 'California/Milwaukee': 22,
 'Central Park': 29,
 'Central-Lake': 32,
 'Cermak-Chinatown': 33,
 'Cermak-McCormick Place': 33,
 'Chicago/Franklin': 8,
 'Chicago/Milwaukee': 24,
 'Chicago/State': 4,
 'Cicero-Forest Park': 25,
 'Cicero-Lake': 25,
 'Clark/Division': 32,
 'Clark/Lake': 32,
 'Clinton-Forest Park': 28,
 'Conservatory': 27,
 'Cumberland': 10,
 'Damen-Brown': 4,
 'Damen/Milwaukee': 24,
 'Diversey': 7,
 'Division/Milwaukee': 24,
 'East 63rd-Cottage Grove': 42,
 'Francisco': 14,
 'Fullerton': 7,
 'Garfield-Dan Ryan': 37,
 'Garfield-South Elevated': 40,
 'Grand/Milwaukee': 24,
 'Grand/State': 8,
 'Granville': 77,
 'Halsted-Orange': 31,
 'Halsted/63rd': 68,
 "Harlem-O'Hare": 10,
 'Harrison': 32,
 'Homan': 27,
 'Howard': 1,
 'Indiana': 38,
 'Irving Park-Brown': 5,
 'Jackson/Dearborn': 32,
 'Jackson/State': 32,
 'Jarvis': 1,
 'Jefferson Park': 11,
 'Kedzie-Brown': 14,
 'Kedzie-Cermak': 29,
 'Kedzie-Homan-Forest Park': 27,
 'Kedzie-Lake': 27,
 'Kedzie-Midway': 63,
 'Kimball': 14,
 'King Drive': 42,
 'Kostner': 26,
 'LaSalle': 32,
 'LaSalle/Van Buren': 32,
 'Lake/State': 32,
 'Laramie': 25,
 'Lawrence': 3,
 'Library': 32,
 'Logan Square': 22,
 'Loyola': 1,
 'Madison/Wabash': 32,
 'Medical Center': 28,
 'Merchandise Mart': 32,
 'Midway Airport': 56,
 'Monroe/Dearborn': 32,
 'Monroe/State': 32,
 'Montrose-Brown': 4,
 "Montrose-O'Hare": 14,
 'Morgan-Lake': 28,
 'Morse': 1,
 'North/Clybourn': 8,
 "O'Hare Airport": 76,
 'Oak Park-Forest Park': 36,
 'Paulina': 6,
 'Polk': 28,
 'Pulaski-Cermak': 29,
 'Pulaski-Forest Park': 26,
 'Pulaski-Lake': 26,
 'Pulaski-Orange': 57,
 'Quincy/Wells': 32,
 'Racine': 28,
 'Randolph/Wabash': 32,
 'Rockwell': 4,
 'Roosevelt': 33,
 'Sedgwick': 8,
 'Sheridan': 6,
 'Southport': 6,
 'Sox-35th-Dan Ryan': 34,
 'State/Lake': 32,
 'Thorndale': 77,
 'UIC-Halsted': 28,
 'Washington/Dearborn': 32,
 'Washington/State': 32,
 'Washington/Wells': 32,
 'Wellington': 6,
 'Western-Brown': 4,
 'Western-Cermak': 31,
 'Western-Forest Park': 32,
 'Western-Orange': 58,
 'Western/Milwaukee': 22,
 'Wilson': 3}

date_sort["community"] = date_sort["stationname"].replace(name, inplace=False)
date_sort = date_sort[date_sort["date"] >= "2012-01-01"]
date_sort = date_sort.reset_index(drop=True)
date_sort = date_sort.drop(date_sort.columns[[0,1,3]], axis=1)
date_sort.to_csv("final_cta_data.csv")

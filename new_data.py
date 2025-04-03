#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:18:00 2025

@author: oh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'AppleGothic'


# 데이터 읽기 (1987 ~ 1999)
df_1987 = pd.read_csv('./dataverse_files_1987-1999/1987.csv')
df_1988 = pd.read_csv('./dataverse_files_1987-1999/1988.csv')
df_1989 = pd.read_csv('./dataverse_files_1987-1999/1989.csv')
df_1990 = pd.read_csv('./dataverse_files_1987-1999/1990.csv')
df_1991 = pd.read_csv('./dataverse_files_1987-1999/1991.csv')
df_1992 = pd.read_csv('./dataverse_files_1987-1999/1992.csv')
df_1993 = pd.read_csv('./dataverse_files_1987-1999/1993.csv')
df_1994 = pd.read_csv('./dataverse_files_1987-1999/1994.csv')
df_1995 = pd.read_csv('./dataverse_files_1987-1999/1995.csv')
df_1996 = pd.read_csv('./dataverse_files_1987-1999/1996.csv')
df_1997 = pd.read_csv('./dataverse_files_1987-1999/1997.csv')
df_1998 = pd.read_csv('./dataverse_files_1987-1999/1998.csv')
df_1999 = pd.read_csv('./dataverse_files_1987-1999/1999.csv')

# 데이터 읽기 (2000  ~ 2008)
df_2000 = pd.read_csv('./dataverse_files_2000-2008/2000.csv')
df_2001 = pd.read_csv('./dataverse_files_2000-2008/2001.csv', encoding= 'latin1')
df_2002 = pd.read_csv('./dataverse_files_2000-2008/2002.csv', encoding= 'latin1')
df_2003 = pd.read_csv('./dataverse_files_2000-2008/2003.csv')
df_2004 = pd.read_csv('./dataverse_files_2000-2008/2004.csv')
df_2005 = pd.read_csv('./dataverse_files_2000-2008/2005.csv')
df_2006 = pd.read_csv('./dataverse_files_2000-2008/2006.csv')
df_2007 = pd.read_csv('./dataverse_files_2000-2008/2007.csv')
df_2008 = pd.read_csv('./dataverse_files_2000-2008/2008.csv')



# 데이터 로드 및 통합
years = list(range(1987, 2009))  # 1987~2008년까지
dataframes = []

for year in years:
    if year < 2000:
        file_path = f'./dataverse_files_1987-1999/{year}.csv'
    else:
        file_path = f'./dataverse_files_2000-2008/{year}.csv'
    
    df = pd.read_csv(file_path, encoding='latin1')  # 일부 파일에서 'latin1' 인코딩 필요
    dataframes.append(df)

# 모든 연도 데이터를 하나로 합치기
df_all = pd.concat(dataframes, ignore_index=True)

# 사용 불가능한 컬럼 제거
drop_cols = ["TailNum", "AirTime", "TaxiIn", "TaxiOut", "CancellationCode",
             "CarrierDelay", "WeatherDelay", "NASDelay", "SecurityDelay", "LateAircraftDelay"]
df_all = df_all.drop(columns=drop_cols)

# 결측치 제거
df_all = df_all.dropna(subset=["DepTime", "ArrTime", "DepDelay", "ArrDelay", "ActualElapsedTime", "Distance"])

# 출발 시간대(HH) 컬럼 추가
df_all["DepHour"] = df_all["CRSDepTime"] // 100

# 연도별 분석
yearly_weekday_delay = df_all.groupby(["Year", "DayOfWeek"])["ArrDelay"].mean().unstack()
yearly_hourly_delay = df_all.groupby(["Year", "DepHour"])["ArrDelay"].mean().unstack()

# 시각화 (연도별 요일별 평균 도착 지연)
plt.figure(figsize=(12, 6))
for year in years:
    plt.plot(yearly_weekday_delay.columns, yearly_weekday_delay.loc[year], label=year)
plt.xlabel("요일 (1=월, 7=일)")
plt.ylabel("평균 도착 지연 (분)")
plt.title("연도별 요일별 평균 도착 지연")
plt.legend()
plt.show()

# 시각화 (연도별 출발 시간대별 평균 도착 지연)
plt.figure(figsize=(12, 6))
for year in years:
    plt.plot(yearly_hourly_delay.columns, yearly_hourly_delay.loc[year], label=year)
plt.xlabel("출발 시간대 (시)")
plt.ylabel("평균 도착 지연 (분)")
plt.title("연도별 출발 시간대별 평균 도착 지연")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

'''
3. 시간이 지남에 따라 다양한 장소 간을 비행하는 사람의 수는 어떻게 변하나?
'''

df_all.info()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 116212331 entries, 0 to 118914457
Data columns (total 20 columns):
 #   Column             Dtype  
---  ------             -----  
 0   Year               int64  
 1   Month              int64  
 2   DayofMonth         int64  
 3   DayOfWeek          int64  
 4   DepTime            float64
 5   CRSDepTime         int64  
 6   ArrTime            float64
 7   CRSArrTime         int64  
 8   UniqueCarrier      object 
 9   FlightNum          int64  
 10  ActualElapsedTime  float64
 11  CRSElapsedTime     float64
 12  ArrDelay           float64
 13  DepDelay           float64
 14  Origin             object 
 15  Dest               object 
 16  Distance           float64
 17  Cancelled          int64  
 18  Diverted           int64  
 19  DepHour            int64  
dtypes: float64(7), int64(10), object(3)
memory usage: 18.2+ GB
'''

# 연도별 비행 횟수 집계
df_yearly = df_all.groupby("Year").size().reset_index(name="FlightCount")

# 월별 비행 횟수 집계
df_monthly = df_all.groupby(["Year", "Month"]).size().reset_index(name="FlightCount")

plt.figure(figsize=(12, 6))
sns.lineplot(x="Year", y="FlightCount", data=df_yearly, marker="o")
plt.title("연도별 비행 횟수 변화")
plt.xlabel("Year")
plt.ylabel("Flight Count")
plt.grid()
plt.show()





































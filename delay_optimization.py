#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:13:21 2025

@author: oh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

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

plt.rcParams['font.family'] = 'AppleGothic'

'''
주제
1. 지연을 최소화하려면 비행에 가장 적합한 시간대/요일/시간은 언제인가?
3. 시간이 지남에 따라 다양한 장소 간을 비행하는 사람의 수는 어떻게 변하나?
5. 한 공항의 지연으로 인해 다른 공항의 지연이 발생하는 연쇄적 실패를 감지할 수 있는지? 
'''
'''
주제 1 분석 과정
1. 데이터 전처리
2. 요일별 평균 지연 분석
3. 시간대별 평균 지연 분
4. 위 시각화 내용을 바탕으로 분석
'''

# 1. 데이터 전처리
df_1987.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1311826 entries, 0 to 1311825
Data columns (total 29 columns):
 #   Column             Non-Null Count    Dtype  
---  ------             --------------    -----  
 0   Year               1311826 non-null  int64  
 1   Month              1311826 non-null  int64  
 2   DayofMonth         1311826 non-null  int64  
 3   DayOfWeek          1311826 non-null  int64  
 4   DepTime            1292141 non-null  float64
 5   CRSDepTime         1311826 non-null  int64  
 6   ArrTime            1288326 non-null  float64
 7   CRSArrTime         1311826 non-null  int64  
 8   UniqueCarrier      1311826 non-null  object 
 9   FlightNum          1311826 non-null  int64  
 10  TailNum            0 non-null        float64
 11  ActualElapsedTime  1288326 non-null  float64
 12  CRSElapsedTime     1311826 non-null  int64  
 13  AirTime            0 non-null        float64
 14  ArrDelay           1288326 non-null  float64
 15  DepDelay           1292141 non-null  float64
 16  Origin             1311826 non-null  object 
 17  Dest               1311826 non-null  object 
 18  Distance           1310811 non-null  float64
 19  TaxiIn             0 non-null        float64
 20  TaxiOut            0 non-null        float64
 21  Cancelled          1311826 non-null  int64  
 22  CancellationCode   0 non-null        float64
 23  Diverted           1311826 non-null  int64  
 24  CarrierDelay       0 non-null        float64
 25  WeatherDelay       0 non-null        float64
 26  NASDelay           0 non-null        float64
 27  SecurityDelay      0 non-null        float64
 28  LateAircraftDelay  0 non-null        float64
dtypes: float64(16), int64(10), object(3)
memory usage: 290.2+ MB
'''

# 1-1. 사용 불가능한 컬럼 삭제
drop_cols = ["TailNum", "AirTime", "TaxiIn", "TaxiOut", "CancellationCode",
             "CarrierDelay", "WeatherDelay", "NASDelay", "SecurityDelay", "LateAircraftDelay"]
df_1987_edit = df_1987.drop(columns=drop_cols)

# 1-2. DepTime, ArrTime, DepDelay, ArrDelay, ActualElapsedTime 결측치 제거 (운항되지 않은 항공편)
df_1987_edit = df_1987_edit.dropna(subset=["DepTime", "ArrTime", "DepDelay", "ArrDelay", "ActualElapsedTime"])

# 1-3. Distance 결측치 제거
df_1987_edit = df_1987_edit.dropna(subset=["Distance"])

df_1987_edit.info()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 1287333 entries, 0 to 1311825
Data columns (total 19 columns):
 #   Column             Non-Null Count    Dtype  
---  ------             --------------    -----  
 0   Year               1287333 non-null  int64  
 1   Month              1287333 non-null  int64  
 2   DayofMonth         1287333 non-null  int64  
 3   DayOfWeek          1287333 non-null  int64  
 4   DepTime            1287333 non-null  float64
 5   CRSDepTime         1287333 non-null  int64  
 6   ArrTime            1287333 non-null  float64
 7   CRSArrTime         1287333 non-null  int64  
 8   UniqueCarrier      1287333 non-null  object 
 9   FlightNum          1287333 non-null  int64  
 10  ActualElapsedTime  1287333 non-null  float64
 11  CRSElapsedTime     1287333 non-null  int64  
 12  ArrDelay           1287333 non-null  float64
 13  DepDelay           1287333 non-null  float64
 14  Origin             1287333 non-null  object 
 15  Dest               1287333 non-null  object 
 16  Distance           1287333 non-null  float64
 17  Cancelled          1287333 non-null  int64  
 18  Diverted           1287333 non-null  int64  
dtypes: float64(6), int64(10), object(3)
memory usage: 196.4+ MB
'''

# 2. 요일별 평균 도착 지연 시간
weekday_delay = df_1987_edit.groupby("DayOfWeek")["ArrDelay"].mean()
print(weekday_delay)
'''
DayOfWeek
1     9.425128
2    11.507030
3    11.231316
4     9.755787
5     8.790235
6     5.925770
7     9.155907
Name: ArrDelay, dtype: float64
'''
# 3. 출발 시간대(시)별 평균 도착 지연 시간
df_1987_edit["DepHour"] = df_1987_edit["CRSDepTime"] // 100  # HHMM을 시간(HH)으로 변환
hourly_delay = df_1987_edit.groupby("DepHour")["ArrDelay"].mean()
print(hourly_delay)
'''
DepHour
0      7.761712
1      7.740681
2      2.534946
3      2.786780
4      7.774112
5      2.240285
6      4.339554
7      5.325486
8      6.911759
9      8.331523
10     7.716883
11     8.278986
12     9.519745
13     8.816096
14     9.196793
15    10.010532
16    11.727220
17    12.057164
18    12.944528
19    12.574704
20    12.644165
21    11.678047
22    11.209213
23     9.292648
Name: ArrDelay, dtype: float64
'''


# 요일별 지연 시간 시각화
weekday_labels = ["월", "화", "수", "목", "금", "토", "일"]

plt.figure(figsize=(8, 5))
plt.bar(weekday_delay.index, weekday_delay.values, color="skyblue")

# x축 라벨을 숫자가 아닌 요일 한글로 설정
plt.xticks(ticks=weekday_delay.index, labels=weekday_labels)

plt.xlabel("요일")
plt.ylabel("평균 도착 지연 (분단위)")
plt.title("요일별 평균 도착 지연")
plt.ylim(4,)  # y축 최소값 설정


# 시간대별 지연 시간 시각화
plt.figure(figsize=(10, 5))
plt.plot(hourly_delay.index, hourly_delay.values, marker="o", linestyle="-", color="red")
plt.xlabel("출발시간")
plt.ylabel("평균 도착 지연 (분단위)")
plt.title("출발시간대에 따른 평균 도착 지연")
plt.xticks(range(24))  # 24시간 표시
plt.grid(True)
plt.show()

'''
3. 시간이 지남에 따라 다양한 장소 간을 비행하는 사람의 수는 어떻게 변하나?
'''
'''
분석과정
1. 분석에 필요한 컬럼만 추출한 후 새로운 데이터프레임으로 생성후 병합
'''


# 분석용 데이터를 저장할 폴더 설정
output_dir = "./processed_data"

# 1987~2008년 데이터 처리
for year in range(1987, 2009):  # 2008년까지 포함
    if year < 2000:
        file_path = f"./dataverse_files_1987-1999/{year}.csv"
    else:
        file_path = f"./dataverse_files_2000-2008/{year}.csv"

    try:
        # 필요한 컬럼만 선택하여 로드
        df_year = pd.read_csv(file_path, encoding='latin1', usecols=["Year", "Origin", "Dest"])
        
        # 연도 정보가 없는 경우 추가
        df_year["Year"] = year  

        # 파일을 분석용 데이터 폴더에 CSV로 저장
        output_file = f"{output_dir}/flights_{year}.csv"
        df_year.to_csv(output_file, index=False)
        
        print(f"{year}년 데이터 저장 완료: {output_file}")

    except Exception as e:
        print(f"{year}년 데이터 처리 실패: {e}")

# 년도별 데이터 분석
df_yearly = []

for year in range(1987, 2009):
    df_temp = pd.read_csv(f"./processed_data/flights_{year}.csv")
    df_yearly.append({"Year": year, "TotalFlights": len(df_temp)})

df_yearly = pd.DataFrame(df_yearly)

# 시각화 1

plt.figure(figsize=(12,6))
plt.plot(df_yearly["Year"], df_yearly["TotalFlights"], marker='o', linestyle='-', color='b')
plt.xlabel("년도")
plt.ylabel("총 비행수")
plt.title("년도별 비행수 비교 (1987-2008)")
plt.grid(True)
plt.show()

# 시각화 2 (히트맵으로 시각화 진행)


# 연도별 데이터를 저장할 리스트
dfs = []

for year in range(1987, 2009):  
    df_temp = pd.read_csv(f"./processed_data/flights_{year}.csv")
    
    # 출발지-목적지를 하나의 Route 컬럼으로 합치기 (예: 'JFK → LAX')
    df_temp["Route"] = df_temp["Origin"] + " → " + df_temp["Dest"]
    
    # 유니크한 노선 개수 계산
    unique_routes = df_temp["Route"].nunique()
    
    # 저장
    dfs.append({"Year": year, "UniqueRoutes": unique_routes})

# 데이터프레임 변환
df_routes = pd.DataFrame(dfs)

# 시각화
plt.figure(figsize=(12,6))
plt.plot(df_routes["Year"], df_routes["UniqueRoutes"], marker='o', linestyle='-', color='g')
plt.xlabel("Year")
plt.ylabel("Unique Routes")
plt.title("연도별 새로운 여행 노선 개수 변화")
plt.grid(True)
plt.show()

'''
5. 한 공항의 지연으로 인해 다른 공항의 지연이 발생하는 연쇄적 실패를 감지할 수 있는지? 
'''
'''
분석과정
1. 분석에 필요한 컬럼만 추출한 후 새로운 데이터프레임으로 생성후 병합
'''

import os

# 입력 데이터 경로
data_path_1987_1999 = "./dataverse_files_1987-1999"
data_path_2000_2008 = "./dataverse_files_2000-2008"

# 출력 데이터 경로
output_dir = "./data_edit"
os.makedirs(output_dir, exist_ok=True)  # 출력 폴더 생성

# 사용할 컬럼 목록
columns_to_keep = [
    "Year", "Month", "DayofMonth", "DayOfWeek", 
    "DepTime", "CRSDepTime", "ArrTime", "CRSArrTime", 
    "UniqueCarrier", "FlightNum", "Origin", "Dest", 
    "DepDelay", "ArrDelay", "Cancelled", "Diverted"
]

# 1987~2008년 데이터 처리
for year in range(1987, 2009):  # 2008년까지 포함
    if year < 2000:
        file_path = os.path.join(data_path_1987_1999, f"{year}.csv")
    else:
        file_path = os.path.join(data_path_2000_2008, f"{year}.csv")

    try:
        # 필요한 컬럼만 선택하여 로드
        df_year = pd.read_csv(file_path, encoding='latin1', usecols=columns_to_keep)

        # 연도 정보가 없는 경우 추가
        df_year["Year"] = year  

        # 파일을 분석용 데이터 폴더에 CSV로 저장
        output_file = os.path.join(output_dir, f"flights_{year}.csv")
        df_year.to_csv(output_file, index=False)

        print(f" {year}년 데이터 저장 완료: {output_file}")

    except Exception as e:
        print(f"{year}년 데이터 처리 실패: {e}")

# 분석 

# 입력 데이터 경로
input_dir = "./data_edit"

# 병합할 데이터 리스트
data_list = []

# 1987~2008년 데이터 병합
for year in range(1987, 2009):  # 2008년까지 포함
    file_path = os.path.join(input_dir, f"flights_{year}.csv")

    try:
        # CSV 파일 로드
        df_year = pd.read_csv(file_path)

        # 연도별 데이터 추가
        df_year["Year"] = year

        # 데이터 리스트에 추가
        data_list.append(df_year)

        print(f"{year}년 데이터 로드 완료: {file_path}")

    except Exception as e:
        print(f"{year}년 데이터 로드 실패: {e}")

# 모든 연도 데이터 병합
final_data = pd.concat(data_list, ignore_index=True)

# 최적화된 데이터 저장
output_file = os.path.join(input_dir, "merged_flight_data.csv")
final_data.to_csv(output_file, index=False)


#--------------------------------------------
# 전처리 - 병합 과정

# 입력 데이터 경로
data_path_1987_1999 = "./dataverse_files_1987-1999"
data_path_2000_2008 = "./dataverse_files_2000-2008"

# 출력 데이터 경로
output_dir = "./data_edit"
os.makedirs(output_dir, exist_ok=True)  # 출력 폴더 생성

# 사용할 컬럼 목록
columns_to_keep = [
    "Year", "Month", "DayofMonth", "DayOfWeek", 
    "DepTime", "CRSDepTime", "ArrTime", "CRSArrTime", 
    "UniqueCarrier", "FlightNum", "Origin", "Dest", 
    "DepDelay", "ArrDelay", "Cancelled", "Diverted"
]

# 1987~2008년 데이터 처리
for year in range(1987, 2009):  # 2008년까지 포함
    if year < 2000:
        file_path = os.path.join(data_path_1987_1999, f"{year}.csv")
    else:
        file_path = os.path.join(data_path_2000_2008, f"{year}.csv")

    try:
        # 필요한 컬럼만 선택하여 로드
        df_year = pd.read_csv(file_path, encoding='latin1', usecols=columns_to_keep)

        # 결측치 제거
        df_year.dropna(subset=["DepDelay", "ArrDelay"], inplace=True)

        # 출발 및 도착 시간을 4자리 문자열로 변환 (예: 830 → "0830")
        df_year["DepTime"] = df_year["DepTime"].fillna(0).astype(int).astype(str).str.zfill(4)
        df_year["ArrTime"] = df_year["ArrTime"].fillna(0).astype(int).astype(str).str.zfill(4)

        # 지연 데이터를 정수형으로 변환
        df_year["DepDelay"] = df_year["DepDelay"].astype(int)
        df_year["ArrDelay"] = df_year["ArrDelay"].astype(int)

        # 연도 정보가 없는 경우 추가
        df_year["Year"] = year  

        # 파일을 분석용 데이터 폴더에 CSV로 저장
        output_file = os.path.join(output_dir, f"flights_{year}.csv")
        df_year.to_csv(output_file, index=False)

        print(f" {year}년 데이터 저장 완료: {output_file}")

    except Exception as e:
        print(f" {year}년 데이터 처리 실패: {e}")

# 입력 데이터 경로
input_dir = "./data_edit"

# 병합할 데이터 리스트
data_list = []

# 1987~2008년 데이터 병합
for year in range(1987, 2009):  # 2008년까지 포함
    file_path = os.path.join(input_dir, f"flights_{year}.csv")

    try:
        # CSV 파일 로드
        df_year = pd.read_csv(file_path)

        # 데이터 리스트에 추가
        data_list.append(df_year)

        print(f" {year}년 데이터 로드 완료: {file_path}")

    except Exception as e:
        print(f" {year}년 데이터 로드 실패: {e}")

# 데이터 병합 및 저장
output_file = os.path.join(input_dir, "merged_flight_data.csv")

if data_list:  # 데이터 리스트가 비어있지 않은 경우에만 병합
    final_data = pd.concat(data_list, ignore_index=True)
    final_data.to_csv(output_file, index=False)
    print(f"병합 완료! 최종 데이터 저장: {output_file}")
else:
    print("병합할 데이터가 없습니다.")

# 분석

# 병합된 데이터 로드
data_path = "./data_edit/merged_flight_data.csv"
df = pd.read_csv(data_path)

# 필요한 컬럼 선택
columns_to_use = ["Year", "Month", "DayofMonth", "FlightNum", "UniqueCarrier", 
                  "DepTime", "ArrTime", "CRSDepTime", "CRSArrTime",
                  "DepDelay", "ArrDelay", "Origin", "Dest"]
df = df[columns_to_use]

# 결측치 제거
df.dropna(subset=["DepDelay", "ArrDelay"], inplace=True)

# 날짜별, 도착 공항 기준으로 정렬
df.sort_values(by=["Year", "Month", "DayofMonth", "ArrTime"], inplace=True)


# 도착 공항에서 다음 항공편의 출발 지연을 연결
df["NextDepDelay"] = df.groupby(["Year", "Month", "DayofMonth", "Dest"])["DepDelay"].shift(-1)

# 연쇄적 지연 여부 감지
df["DelayImpact"] = (df["ArrDelay"] > 15) & (df["NextDepDelay"] > 15)

# 연쇄적 지연이 발생한 비율 계산
impact_rate = df["DelayImpact"].mean() * 100
print(f" 연쇄적 지연 발생 확률: {impact_rate:.2f}%")

# 공항별 연쇄적 지연 비율 계산
airport_delay_impact = df.groupby("Origin")["DelayImpact"].mean() * 100

# 상위 10개 공항 출력
print(airport_delay_impact.nlargest(10))

plt.rcParams['font.family'] = 'AppleGothic'

plt.figure(figsize=(10, 6))
top_airports = airport_delay_impact.nlargest(10)
sns.barplot(x=top_airports.values, y=top_airports.index, palette="Reds")
plt.xlabel("연쇄 지연 발생 확률 (%)")
plt.ylabel("공항")
plt.title("연쇄 지연이 가장 심한 공항 TOP 10")
plt.show()



























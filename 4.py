# 시리즈를 이용한 데이터프레임
import pandas as pd

kospi = pd.Series([1915, 1961, 2026, 2467, 2041],
                  index = [2014, 2015, 2016, 2017, 2018], name = 'KOSPI')
# print(kospi)

kosdaq = pd.Series([542, 682, 631, 798, 675],
                   index = [2014, 2015, 2016, 2017, 2018], name='KOSDAQ')
# print(kosdaq)

df = pd.DataFrame({kospi.name: kospi, kosdaq.name: kosdaq})
print(df)

# 리스트를 이용한 데이터 프레임 생성
columns = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018]
rows = []
rows.append([1915, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 675])
df = pd.DataFrame(rows, columns=columns, index = index)
print(df)

# 데이터 처리

for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])

for row in df.itertuples(name='KRX'): # 튜플로 반환
    print(row)
for row in df.itertuples():
    print(row[0], row[1], row[2])

for idx, row in df.iterrows(): # iterrows는 itertuples와 비슷
    print(idx, row[0], row[1])
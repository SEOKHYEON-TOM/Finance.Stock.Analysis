# KOSPI와 다우존스 지수 비교
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04')      # 2000년 이후의 다우존스 지수 데이터를 야후 파이낸스로부터 다운
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')      # 2000년 이후의 코스피 데이터를 야후 파이낸스로부터 다운

# import matplotlib.pyplot as plt
# plt.figure(figsize=(9, 5))
# plt.plot(dow.index, dow.Close, 'r--', label='Dow Jones Industrial')
# plt.plot(kospi.index, kospi.Close, 'b', label='KOSPI')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show() # 지수 기준값이 달라 비교하기 어렵다.

d = (dow.Close / dow.Close.loc['2000-01-04']) * 100
k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100

# import matplotlib.pyplot as plt
# plt.figure(figsize=(9, 5))
# plt.plot(d.index, d, 'r--', label='Dow Jones Industrial Average')
# plt.plot(k.index, k, 'b', label='KOSPI')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

# 다우존스 지수와 KOSPI의 관계 분석 - 산점도
print(len(dow), len(kospi)) # 산점도를 그리려면 x(독립변수)와 y(종속변수)의 사이즈가 같아야함
#
# plt.scatter(dow, kospi, marker='.')
df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
# print(df) 비어있는 곳에는 NaN으로 채워짐
# plt.scatter(df['DOW'], df['KOSPI'], marker='.') # NaN때문에 실행 안됨
# 데이터프레임의 fillna()함수를 이용해 NaN을 채울 수 있음, 인수로 bfill을 주면 NaN 뒤에 있는 값으로 NaN을 덮어쓴다.
df = df.fillna(method='bfill')
# print(df) 마지막 항에 NaN이 있음, ffill을 인수로 주어 마지막 이전 행에 있던 값으로 NaN을 덮어 쓸 수 있다
df = df.fillna(method='ffill')

import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show() # 산점도 그래프로는 정확한 분석이 어려움, 선형 회귀 분석으로 더 정확히 분석해보자!

# 선형 회귀 분석 # 사이파이 패키지의 서브 패키지인 스탯츠의 linregress()함수를 이용하면 시리즈 객체 두 개만으로 간단히 선형 회귀 모델을 생성하여 분석할 수 있다.
from scipy import stats
regr = stats.linregress(df['DOW'], df['KOSPI'])
print(regr) # slope 기울기 intercept y절편 rvalue 상관계수 pvalue p값 stderr 표준편차

# 데이터프레임으로 상관계수 구하기
print(df.corr())
# 시리즈로 상관계수 구하기
print(df['DOW'].corr(df['KOSPI'])) # dr.DOW.corr(df.KOSPI)와 같음

# 결정계수: 관측된 데이터에서 추정한 회귀선이 실제로 데이터를 어느 정도 설명하는지를 나타내는 계수, 두 변수의 상관관계 정도를 나타내는 상관계수를 제곱한 값
r_value = df['DOW'].corr(df['KOSPI'])
print(r_value)
r_squared = r_value ** 2
print(r_squared)

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

print(sec.head(10)) # Adj Close가 수정종가, 국내 주식에 대해선 잘못 나옴

tmp_msft = msft.drop(columns='Volume')
print(tmp_msft.tail())

print(sec.index)
print(sec.columns)
print(msft.columns)

# 종가 데이터 그래프 출력
#
# import matplotlib.pyplot as plt
# plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
# plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
# plt.show()

# 일간 변동률로 주가 비교하기
print(type(sec['Close'])) # 데이터프레임의 칼럼의 자료형은 시리즈
print(sec['Close'])
print(sec['Close'].shift(1)) # shift() 함수는 데이터를 이동시킬 때 사용하는 함수, 인수로 n을 줄 경우 전체 데이터가 n행 씩 뒤로 이동한다.
# NAN (Not A Number)
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
sec_dpc.iloc[0] = 0
print(sec_dpc.head())

# 주가 일간 변동률 히스토그램
# 히스토그램, 도수 분포를 나타내는 그래프, 데이터값들에 대한 구간별 빈도수를 막대 형태로 나타낸다. 이때 구간 수를 빈스(bins)라고 함
# import matplotlib.pyplot as plt
# sec_dpc = (sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
# sec_dpc.iloc[0] = 0
# plt.hist(sec_dpc, bins=30)
# plt.grid(True)
# plt.show() # fat tail 분포에 가까움 https://en.wikipedia.org/wiki/Fat-tailed_distribution
# print(sec_dpc.describe())

# 일간 변동률 누적합(Cumulative Sum) 구하기
# 누적합은 시리즈에서 제공하는 cusum()함수를 이용하여 구함
sec_dpc_cs = sec_dpc.cumsum()

# 삼성과 마이크로 소프트의 주식수익율 비교
msft_dpc = (msft['Close'] - msft['Close'].shift(1)) / msft['Close'].shift(1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cs = msft_dpc.cumsum()

import matplotlib.pyplot as plt
plt.plot(sec.index, sec_dpc_cs, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cs, 'r--', label='Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()




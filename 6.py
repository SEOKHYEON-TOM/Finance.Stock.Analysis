# KOSPI_MDD, Maximum Drawdown 최대손실낙폭
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')   # KOSPI지수의 심볼 ^KS11

window = 252    # 산정 기간에 해당하는 window값은 1년 동안의 개장일을 252일로 어림잡아 설정했다
peak = kospi['Adj Close'].rolling(window, min_periods=1).max() # KOSPI 종가 칼럼에서 1년(거래일 기준) 기간 단위로 최고치 peak를 구한다.
drawdown = kospi['Adj Close']/peak - 1.0     # drawdown은 최고치(peak)대비 현재 KOSPI 종가가 얼마나 하락했는지를 구함
max_dd = drawdown.rolling(window, min_periods=1).min()     # drawdown에서 1년 기간 단위로 최저치 max_dd를 구함. 마이너스값이기 때문에 최저치가 바로 최대 손실 낙폭이 됨.

plt.figure(figsize=(9, 7))
plt.subplot(211) # 2행 1열 중 1행에 그린다.
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212) # 2행 1열 중 2행에 그린다.
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()

print(max_dd.min())
print(max_dd[max_dd==-0.5453665130144085]) # MDD를 기록한 기간을 구하려면 인덱싱 조건(max_dd==-~)을 적용시킨다.
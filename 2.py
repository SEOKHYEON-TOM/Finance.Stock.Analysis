import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0]) # 리스트로 시리즈 생성
print(s) # 0부터 시작하는 정수형 인덱스 자동 생성

s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8]) # s시리즈의 인덱스 변경
s.index.name = 'MY_IDX' # 인덱스명 설정
print(s)

s.name = 'MY_SERIES' # 시리즈명 설정
print(s)

# 데이터 추가
s[5.9] = 5.5
print(s)

ser = pd.Series([6.7, 4.2], index=[6.8, 8.0]) # ser 시리즈를 생성
s = s.append(ser) # append로 기존 s 시리즈에 신규 ser 시리즈를 추가
print(s)

# 데이터 인덱싱
print(s.index[-1])
print(s.values[-1])
print(s.loc[8.0]) # 로케이션 인덱서를 사용해 인덱스값에 해당하는 데이터를 표시함
print(s.iloc[-1]) # []안에 지정한 정수 인덱스에 해당하는 값을 표시
# 결괏값이 복수 개일 때 배열로 반환하는 values와 달리, iloc은 시리즈로 반환하는 차이점이 있음.
print(s.values[:])
print(s.iloc[:])

# 데이터 삭제
print(s.drop(8.0)) # s.drop(s.index[-1])과 같다. # 삭제한 결과를 s시리즈에도 반영하려면 s = s.drop(8.0)

# 시리즈 정보 보기
print(s.describe())

# 시리즈 출력하기
import matplotlib.pyplot as plt
S = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2]) # 시리즈 생성
S.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8, 5.9, 6.8, 8.0]) # 시리즈 인덱스 변경
S.index.name = 'MY_IDX' # 시리즈 인덱스명 설정
S.name = 'MY_SERIES' # 시리즈 이름 설정

plt.title("ELLIOTT_WAVE")
plt.plot(S, 'bs--') # 시리즈를 bs--(푸른 사각형과 점선) 형태로 출력
plt.xticks(s.index) # x축의 눈금값을 S 시리즈의 인덱스값으로 설정
plt.yticks(s.values) # y축의 눈금값을 S 시리즈의 데이터값으로 설정
plt.grid(True)
plt.show()
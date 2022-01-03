import numpy as np

A = np.array([[1, 2], [3, 4]])
print(A)
print(type(A))  # 타입
print(A.shape)  # 배열 크기
print(A.ndim)  # 배열의 차원
print(A.dtype)  # 원소 자료형
print(A.max(), A.mean(), A.min(), A.sum())

print(A[0], A[1])
print(A[0][0], A[0][1], A[1][0], A[1][1])
print(A[0, 0], A[0, 1], A[1, 0], A[1, 1])
print(A[A > 1])

print(A.T) # A.Transpose()와 같음
print(A.flatten()) # dimension: 2 -> 1

# 원소별(element-wise) 계산
print(A + A) # np.add(A, A)와 같음
print(A - A) # np.subtrace(A, A)와 같음
print(A * A) # np.multiply(A, A)와 같음
print(A / A) # np.divide(A, A)와 같음

# 브로드 캐스팅 / 행렬의 크기가 달라도 연산할 수 있게 크기가 작은 행렬을 확장해줌.
B = np.array([10, 100])
print(B * A)

# 내적(inner product)
print(B.dot(B)) # np.dot(B, B)와 같음 # 1차원 배열끼리의 곱, 앞에 오는 1차원 배열을 행 벡터, 뒤에 오는 1차원 배열을 열 벡터로
print(A.dot(B)) # A 행렬(2 * 2)과 B 행렬(2 * 1)의 내적 곱


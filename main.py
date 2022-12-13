#반복문

#while문보다는 for문을 주로 쓴다

#while문
i = 1
result = 0

# i가 9보다 작거나 같을 떄 아래 코드를 반복적으로 실행
while i <= 9:
  result += i
  i += 1
print(result)

# for문 기본
array = [9, 8, 7, 6, 5]

for x in array:
  print(x)

# 1부터 30까지의 합을 for문을 통해 풀기
result = 0

for i in range(1, 31):
  result += i
print(result)

#1부터 9까지의 홀수의 합을 구하기
# continue 사용하기

result = 0

for i in range(1, 10):
  if i % 2 == 0:
    continue
  result += i

print(result)

#break 사용하기
i = 1

while True:
  print("현재 i의 값:", i)
  if i == 5:
    break
  i += 1

# 반복문 중첩
for i in range(2, 10):
  for j in range(1, 10):
    print(i, "X", j, "=", i * j)
  print()

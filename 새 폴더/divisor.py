import sys # [cite: 301]

# 커맨드 라인에서 첫 번째 인수를 받아 정수로 변환합니다. [cite: 303]
number = int(sys.argv[1])

# 1부터 'number' 자신까지 반복합니다. [cite: 304, 308]
for i in range(1, number + 1):
    
    # 'number'를 'i'로 나누었을 때 나머지가 0인지 확인합니다. [cite: 305, 309, 312]
    if number % i == 0:
        
        # 약수일 경우, 줄바꿈 없이 숫자를 출력하고 한 칸 띄웁니다. [cite: 306]
        print(i, end=" ")

# 모든 약수를 출력한 뒤, 마지막에 한 번 줄바꿈을 합니다. [cite: 307]
print()
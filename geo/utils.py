import math # math 모듈을 가져옵니다. [cite: 444]

# 피타고라스 정리 (a^2 + b^2 = c^2)를 계산하여 빗변 c를 반환하는 함수
def pythagoras(a, b): 
    # c = sqrt(a**2 + b**2)
    c = math.sqrt(a**2 + b**2) 
    return c 

# 원의 넓이 (Area = pi * r^2)를 계산하여 반환하는 함수
def circle(r): 
    # math.pi를 사용하고, 넓이 공식은 r**2 입니다. (자료에는 r*2로 오타가 있는 것으로 보입니다. r^2이 맞습니다.)
    area = math.pi * r**2 
    # 자료의 코드는 area = math.pi * r * 2 로 되어 있습니다.  (실제로는 r**2가 맞습니다.)
    return area 
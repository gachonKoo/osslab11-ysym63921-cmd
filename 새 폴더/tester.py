import geo.utils as utils # geo 패키지의 utils 모듈을 'utils'라는 별칭으로 가져옵니다. [cite: 435]

# 1. 피타고라스 정리 계산 (a=3, b=4)
# calculate the length of hypotenuse (c) when a=3 and b=4 [cite: 440]
a, b = 3, 4 
c = utils.pythagoras(a, b) # utils 모듈의 pythagoras 함수 호출
print('c =', c) 

# 2. 원의 넓이 계산 (r=10)
# calculate the area of circle with radius r=10 [cite: 456]
r = 10 
area = utils.circle(r) # utils 모듈의 circle 함수 호출
print('area =', area) 
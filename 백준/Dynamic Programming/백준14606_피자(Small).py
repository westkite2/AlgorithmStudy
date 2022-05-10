N = int(input())
floor = [0] * 11 #N의 개수에 따른 즐거움의 값을 저장

#점화식을 적용할 수 없는 값은 미리 계산
floor[1] = 0 #N=1이면 즐거움은 0
floor[2] = 1 #N=2이면 즐거움은 1

#N=3부터 현재 개수까지 순차적으로 즐거움 값을 계산
for i in range(3, N+1):
    k = i//2 #N을 반으로 나눈 값
    floor[i] = k * (i-k) + floor[k] + floor[i-k] #즐거움값 + 절반1 + 절반2    
print(floor[N])

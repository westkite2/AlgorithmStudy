n = int(input())
cnt = n//3 + n%3 #총 횟수
if cnt % 2 == 0:
    print("SK")
else:
    print("CY")

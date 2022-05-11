N = int(input())
cnt = N//3 + N%3
if cnt % 2 == 0:
    print("SK")
else:
    print("CY")

l, c = map(int, input().split())
bet = list(map(str, input().split()))
bet.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
ans = []

def checkmo(ans):
    mo = 0
    ja = 0
    for i in range(l):
        if ans[i] in vowels:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        return True
    else:
        return False
    
def func(j):
    if len(ans) is l:
        if checkmo(ans) is False:
            return
        for i in ans:
            print(i, end="")
        print()
        return
    for i in range(j, c):
        ans.append(bet[i])
        func(i+1)
        ans.pop()
func(0)

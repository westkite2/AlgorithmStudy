dwarf = [int(input()) for _ in range(9)]
total = sum(dwarf)
n1 = 0
n2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if total-(dwarf[i]+dwarf[j]) == 100:
            n1, n2 = dwarf[i], dwarf[j]
            break

dwarf.remove(n1)
dwarf.remove(n2)
dwarf.sort()

for i in dwarf:
    print(i)

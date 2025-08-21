from collections import Counter
s = "uueraccar"
res = Counter(s)
print(res)

for i,j in res.items():
    if j == 1:
        print(i)
        break
    else:
        print(i)
        continue

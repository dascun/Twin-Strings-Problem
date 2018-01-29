a = ['cdab','abcd']
b = ['dcba','abcd']

n = len(a)
result = []

for i in range(n):
    odd_a = []
    even_a = []
    odd_b = []
    even_b = []
    j = len(a[i])
    k = len(b[i])
    if j == k:
        for l in range(j):
            if l % 2 == 0:
                odd_a.append(a[i][l])
                odd_b.append(b[i][l])

            else:
                even_a.append(a[i][l])
                even_b.append(b[i][l])

    else:
        result.append('No')
        break
    if (set(odd_a) == set(odd_b)) & (set(even_a) == set(even_b)):
        result.append('Yes')
    else:
        result.append('No')

print(result)

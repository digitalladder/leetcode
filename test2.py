t = int(input())
for i in range(t):
  n,k = input().split(' ')
  n,k = int(n),int(k)
  p = list(map(int, input().split(' ')))
  w = list(map(int, input().split(' ')))
  p.sort()
  w.sort()
  res = 0
  l,j = n-1,k-1
  while l >=0 and j >= 0:
    if p[l] <= w[j]:
      res += 1
      l -= 1
      j -= 1
    else:
      l -= 1
  print(res)
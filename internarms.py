a, b = map(int, input().split()) 
for u in range(a, b + 1):
   order = len(str(u))
   sum = 0
   temp = u
   while temp > 0:
       digit = temp % 10
       u += digit ** order
       temp //= 10
   if u == sum:
       print(num)

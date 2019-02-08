n = int(input())
s = 0
temp = n
while temp > 0:
   digit = temp % 10
   s += digit ** 3
   temp //= 10
if n == s:
   print("yes")
else:
   print("no")

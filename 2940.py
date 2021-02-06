velocity = int(input())
time = int(input())
s = velocity*time
while s < 0:
  s += 108
  if s >= 0:
   print(s + 1)
while s > 108:
  s -= 108
  if s <= 108:
   print(s - 1)
else:
 print(s - 1)

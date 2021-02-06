x = int(input())
hour = 0

while x > 59:
    x -= 60
    hour += 1

while hour > 23:
    hour -= 24

print(hour, x)
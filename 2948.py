sec = int(input())
hour = 0
minute = 0

while sec > 3599:
    sec -= 3600
    hour += 1
while sec > 59:

    sec -= 60
    minute += 1

while hour > 23:
    hour -= 24

while minute > 59:
    minute -= 60
    hour += 1

minute = str(minute)
if len(minute) == 1:
    minute = "0" + minute
sec = str(sec)
if len(sec) == 1:
    sec = "0" + sec
print(hour, ":", minute,":", sec, sep = "")
 
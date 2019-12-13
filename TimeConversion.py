# coding: utf-8
# Your code here!
def timeConversion(s):
    print(s)
    time = s.split(":")
    print(time)
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
            print(time)
    else:
        if time[0] == "12":
            time[0] = "00"
            print(time)
    time2 = ':'.join(time)
    print(time2)
    print(str(time2[:8]))
    print(str(time2[:-2]))
s = input()
timeConversion(s)

# output
# 07:05:45PM
# ['07', '05', '45PM']
# ['19', '05', '45PM']
# 19:05:45PM
# 19:05:45
# 19:05:45

# input
# 07:05:45PM
    
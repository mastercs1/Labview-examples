import math

# x = sin(t) ( e^ cos(t) - 2cos(4t)-sin^5 (t/12))
# y = cos(t) ( e^ cos(t) - 2cos(4t)-sin^5 (t/12))
# 0 <=t <=12 pi


def expcost(t):
    return math.exp(math.cos(t))


def sinpower(t):
    return (2 * math.cos(4*t))-math.sin(t/12)**5


def xcord(t):
    return math.sin(t) * (expcost(t) - sinpower(t))


def ycord(t):
    return math.cos(t) * (expcost(t) - sinpower(t))


def getXYcord(num_points):
        interval = 12 * math.pi / num_points
        xy_list = []
        for j in range(num_points):
            xy_list.append([xcord(interval*j), ycord(interval*j)])
        return xy_list

print (getXYcord(10000))

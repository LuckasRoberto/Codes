def f(x):
    return x**3


def derivative(x):
    h = 1./1000.
    rise = f(x+h) - f(x)
    run = h
    slope = rise/run
    return slope



def integral(startx, endx, ret):
    width = (float(endx) - float(startx))/ret
    runningSum = 0
    for i in range(ret):
        height = f(startx +i*width)
        area = height*width
        runningSum += area
    return runningSum

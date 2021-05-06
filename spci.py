from matplotlib import pyplot as pit 
from scipy import signal


window =  signal.hann(51)
pit.plot(window)

z = pit.show()

print (z)


#example 2 iteration
postcodes = {
        "Shepard Bush": 1991,
        "phantom hive": 1992,
        "Duke": 1993
        }
for area,code in postcodes.items():
    print("post code of %s is %d"%(area,code))

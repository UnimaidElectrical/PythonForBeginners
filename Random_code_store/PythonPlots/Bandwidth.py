
#Bandwidth and Packet size plot
import numpy as np
import matplotlib.pyplot as plt

x = [64,128,256,512,1024,1400]
# Index positions for x-axis
xindex = list(range(len(x)))
y1 = [95.5, 202, 376, 750, 960, 991] #baseline
y2 = [84.5, 170, 320, 670, 782, 930] #firewall
plt.ylim(0,1000)

# plot with index as x
plt.plot(xindex,y1, 'g', linestyle= 'dashed', linewidth=2, marker= 'D', label='Baseline')
plt.plot(xindex,y2, 'r', linestyle= 'dashed', linewidth=2, marker= 'D', label='Firewall')

plt.xlabel('Packet Size (Bytes)')
plt.ylabel('Bandwidth (Mbps)') 

plt.xticks(xindex, x)
plt.title('OvS Performance')
plt.legend()
plt.savefig('OvSbaselineAndFirewall.png')
plt.show()

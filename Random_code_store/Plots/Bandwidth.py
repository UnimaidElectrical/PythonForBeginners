
#Simple Bandwidth and Packet size plot for performance analysis

import numpy as np
import matplotlib.pyplot as plt

x = [64,128,256,512,1024,1400,1500]
y1 = [70,140,280,360,520,700,850]
y2 = [93,160,310,400,580,800,980]

plt.plot(x,y1, 'g', linestyle= 'dashed', linewidth=2, marker= 'D', label='Baseline')
plt.plot(x,y2, 'r', linestyle= 'dashed', linewidth=2, marker= 'D', label='Firewall')
plt.title('Dataplane Performance')
plt.xlabel('Packet Size (Bytes)')
plt.ylabel('Bandwidth (Mbps)')
plt.legend()
plt.show()
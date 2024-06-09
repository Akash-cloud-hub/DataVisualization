import matplotlib.pyplot as plt
import numpy as np


# plt.plot([1,2,3,4,5])

plt.plot([1,2,3,4],[5,6,7,8],color = 'red' , linestyle = 'dashdot' , linewidth = 6 )
# plt.show()

plt.clf()

year = np.array([2018 , 2019 , 2020 , 2021 , 2022 , 2023 ])
rank = np.array([7,3,5,9,2,1])
grades = np.array([40 , 95 , 88 , 35 , 98 , 100])

plt.plot(year , rank , color='red')

plt.plot(year , grades , color='green' , marker = 'o')


x = [1,2,3,4,5,6]
y = [1,22,352,31,523,123]

x1 = [32,12,53,2,3,42]
y1 = [3,342 , 531 , 22 , 34 , 4210]
plt.clf()
plt.scatter(x,y)
# plt.show()

plt.clf()
plt.scatter(x1,y1 , color = 'red' , marker='x')
# plt.show()

plt.clf()
plt.scatter([x,y],[x1,y1],s= 100 , marker = "*")
# plt.show()

x = np.array(['A','B','C','D','E'])
y = np.array([3,8,10,11,19])

plt.clf()
plt.bar(x,y)
plt.show()
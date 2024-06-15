import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
my_labels = ["Apples" , "Bananas" , "Cherries" , "Mangoes"]
my_explode = [0.2,0,0,0]
my_colors = ["red","orange","blue","yellow"]

plt.pie(y, labels = my_labels,startangle=90,explode = my_explode , shadow=True , colors=my_colors )
plt.legend(title="Legend")
plt.show()
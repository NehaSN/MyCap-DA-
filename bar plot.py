import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'test1':60, 'test2':85, 'test3':65,
		'test4':75}
tests = list(data.keys())
marks = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(tests, marks, color ='green',
		width = 0.3)

plt.xlabel("Cycle tests")
plt.ylabel("Marks")
plt.title("Marks obtained in previous tests")
plt.show()

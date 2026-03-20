import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [10,20,15,30,34,12,3,4,65,65,76,87] 

plt.scatter(x, y, color='blue', s=50, label="Points")

plt.title("Scatter Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()

plt.show()
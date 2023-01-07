import mylibrary as lib
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('graphs/input.txt'))  #getting those variables into this code

plt.subplot(2, 1, 1)
plt.plot(X,Y)

plt.subplot(2, 1, 2)
plt.plot(X2,Y2)

plt.subplot(2, 1, 3)
plt.plot(X3,Y3)
plt.show()
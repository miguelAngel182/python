import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y=np.log(x)

plt.plot(x,y,label='y=log(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de la función log(x)')
plt.legend()
plt.show()
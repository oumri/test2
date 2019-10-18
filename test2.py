import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 4, 6])
y = np.array([2, 3, 5, 1])
plt.plot(x, y)

plt.show() # affiche la figure a l'ecran

x = np.linspace(0, 2*np.pi, 30)
y1 = np.cos(x)
y2 = np.sin(x)
plt.plot(x, y1,"r--", label="cos(x)")
plt.plot(x, y2, "b:o", label="sin(x)")
#y = np.cos(x)
#plt.plot(x, y)
#plt.plot(x, y, label="cos(x)")
plt.xlim(-1, 5)
plt.ylim(0, 1)
plt.title("Fonction cosinus")
plt.legend()
plt.xlabel("abscisses")
plt.ylabel("ordonnees")
plt.show() # affiche la figure a l'ecran

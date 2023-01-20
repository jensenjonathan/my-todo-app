import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


class Complex:
    def __init__(self, x, y):  # this becomes the value of Complex
        self.re = x
        self.im = y

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + other.re * self.im)

    def modl(self):
        return (self.re ** 2 + self.im ** 2) ** .5

    def conj(self):
        return Complex(self.re, -self.im)

    def phase(self):
        return np.arctan(self.im / self.re)

    def __repr__(self):
        return '(%f, %f)' % (self.re, self.im)


'''The above functions define basic math operations for basic aritmetic
operations. Automatically implemented when using complex types.'''
voltage = float(input('Enter voltage: '))
capacitance = float(input('Enter capacitance: '))
inductance = float(input('Enter inductance: '))

'''impedance = np.zeros(199)
phase = np.zeros(199)
lplot = np.zeros(199)
for index, x in enumerate(np.arange(0.01, 2, 0.01)):
    impedance[index] = voltage / Complex.modl(Complex(resistance, 1 / (x * capacitance) - x * inductance))
    phase[index] = Complex.phase(Complex(resistance, 1 / (x * capacitance) - x * inductance))
    lplot[index] = x

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(lplot, impedance, lw = 1, c = 'r')
plt.xlim([0, 2])
plt.xlabel('Frequency');   plt.ylabel('Mag of Impedance')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(lplot, phase, lw = 1, c = 'b')
plt.xlim([0, 2])
plt.xlabel('Frequency');   plt.ylabel('Phase')
plt.grid(True)
plt.show()'''


def f(resistance, impedance):
    return voltage / Complex.modl(Complex(resistance,
                                          1 / (impedance * capacitance) - impedance * inductance))


x2 = np.linspace(0.01, 2, 50)
y2 = np.linspace(0.01, 2, 50)

X, Y = np.meshgrid(x2, y2)
Z = f(X, Y)  # Z has to take meshgrid as an argument

fig = plt.figure(2)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, color='green')
ax.set_title('Current Magnitude')
plt.xlabel('Resistance')
plt.ylabel('Frequency')
plt.show()

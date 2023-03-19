import matplotlib.pyplot as plt
import numpy as np
import sympy
from scipy import integrate

z = sympy.Symbol("z", real=True)
e = sympy.Symbol("e", real=True)
y = sympy.Function("y")

ode = -y(z).diff(z, 2) + z * y(z) - e * y(z)
sympy.Eq(ode, 0)
ode_sol = sympy.dsolve(ode)
ode_sol_1 = ode_sol.rhs.args[0].args[1]
ode_sol_2 = ode_sol.rhs.args[1].args[1]
ode_sol_1_func = sympy.lambdify(z, ode_sol_1, ("numpy", "sympy"))
ode_sol_2_func = sympy.lambdify(z, ode_sol_2, ("numpy", "sympy"))

if False:
    print('ready to write')
    with open('ode_sol_1.txt', 'w') as f:
        print(ode_sol_1_func(np.linspace(-15, 5, 200)), file=f)
    with open('ode_sol_2.txt', 'w') as f:
        print(ode_sol_2_func(np.linspace(-15, 5, 200)), file=f)
    print('done writing')
#fig, ax = plt.subplots(1, 2, figsize=(8, 4))
#ax[0].plot(np.linspace(-15, 5, 200), ode_sol_1_func(np.linspace(-15, 5, 200)))
#ax[1].plot(np.linspace(-15, 5, 200), ode_sol_2_func(np.linspace(-15, 5, 200)))



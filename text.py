import random
import colorama
from colorama import Fore
tol = 9999999999999999999
str(tol)
for i in range(tol):
    x = random.randint (0,1)
    y = random.randint (0,1)
    z = random.randint (0,1)
    a = random.randint (0,1)
    b = random.randint (0,1)
    c = random.randint (0,1)
    xx = str(x)
    yy = str(y)
    zz = str(z)
    aa = str(a)
    bb = str(b)
    cc = str(c)
    vala = str((xx + yy + zz + aa + bb + cc))
    valb = str((cc + aa + bb + yy + zz + xx))
    valc = str((xx + cc + yy + bb + zz + aa))
    print(Fore.GREEN + vala, valb, valc, vala, valb, valc, vala, valc, valb)
    

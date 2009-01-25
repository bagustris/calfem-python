# example exs3 
# ----------------------------------------------------------------
# PURPOSE 
#    Analysis of a plane truss.
# ----------------------------------------------------------------

# REFERENCES
#     Ola Dahlblom 2004-09-07
#     Jonas Lindemann 2009-01-25
# ----------------------------------------------------------------

from numpy import *
from pycalfem import *

# ----- Topology matrix Edof -------------------------------------

Edof = array([
    [1,2,5,6],
    [5,6,7,8],
    [3,4,5,6]
])

# ----- Stiffness matrix K and load vector f ---------------------

K=mat(zeros((8,8)))
f=mat(zeros((8,1)))
f[5]=-80e3

# ----- Element properties ---------------------------------------
 
E=2.0e11
A1=6.0e-4
A2=3.0e-4
A3=10.0e-4
ep1=array([E,A1])
ep2=array([E,A2])
ep3=array([E,A3])
 
#----- Element coordinates --------------------------------------

ex1=array([0., 1.6])
ex2=array([1.6, 1.6])
ex3=array([0., 1.6])

ey1=array([0., 0.])
ey2=array([0., 1.2])
ey3=array([1.2, 0.])
 
#----- Element stiffness matrices  ------------------------------

Ke1=bar2e(ex1,ey1,ep1)	 
Ke2=bar2e(ex2,ey2,ep2)
Ke3=bar2e(ex3,ey3,ep3)	
 
#----- Assemble Ke into K ---------------------------------------

K=assem(Edof[0,:],K,Ke1)
K=assem(Edof[1,:],K,Ke2)
K=assem(Edof[2,:],K,Ke3)

print("Stiffness matrix K:")
print(K)
 
#----- Solve the system of equations ----------------------------

bc=array([1,2,3,4,7,8])
[a,r]=solveq(K,f,bc)

print("Displacements a:")
print(a)

print("Reaction forces r:")
print(r)

#----- Element forces -------------------------------------------

ed1=extract(Edof[0,:],a);
N1=bar2s(ex1,ey1,ep1,ed1)
ed2=extract(Edof[1,:],a);
N2=bar2s(ex2,ey2,ep2,ed2)
ed3=extract(Edof[2,:],a);	
N3=bar2s(ex3,ey3,ep3,ed3)

print("N1 = "+str(N1))
print("N2 = "+str(N2))
print("N3 = "+str(N3))
 

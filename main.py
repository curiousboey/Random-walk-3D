import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import product, combinations

no_of_steps = 100
no_of_times= 10
length_of_cube= 10

r = [-length_of_cube, length_of_cube]
fig= plt.figure()
ax = fig.gca(projection='3d')

for s, e in combinations(np.array(list(product(r, r, r))), 2):
   if np.sum(np.abs(s-e)) == r[1]-r[0]:
      ax.plot3D(*zip(s, e), color="b")

plt.grid(False)
plt.axis('off')
plt.show()

out=0
inside= 0
out_at_least_once= 0
in_always= 0

random_walk = ([-1,0,0],[0,1,0],[1,0,0],[0,-1,0],[0,0,1],[0,0,-1])
for m in range(no_of_times):
   walk = []
   walk2= [0,0,0]
   always_in= 0
   atleast_out= 0
   for n in range(no_of_steps):
      r= random_walk[int(np.random.randint(0,6,1))]
      j = [a + b for a, b in zip(walk2, r)]
      walk2 = j
      walk.append(walk2)
      if (np.abs(walk2[0]) or np.abs(walk2[1]) or np.abs(walk2[2])) > length_of_cube:
         atleast_out1= atleast_out + 1
         atleast_out= atleast_out1
      else:
         always_in1= always_in + 1
         always_in= always_in1

   if always_in == no_of_steps:
      in_always1= in_always + 1
      in_always= in_always1
   else:
      out_at_least_once1= out_at_least_once + 1
      out_at_least_once= out_at_least_once1

   if (np.abs(walk[no_of_steps-1][0]) or np.abs(walk[no_of_steps-1][1]) or np.abs(walk[no_of_steps-1][2])) > length_of_cube:
      out1 = out + 1
      out= out1
   else:
      in1 = inside + 1
      inside= in1
   x_points = [0]
   y_points = [0]
   z_points = [0]
   for p in range(no_of_steps):
      x_points.append(walk[p][0])
      y_points.append(walk[p][1])
      z_points.append(walk[p][2])
   ax.plot3D(x_points,y_points,z_points)
plt.show()

print('Total number of particles (outside)= ', out)
print('Total number of particles (inside)= ', inside)
print('Total number of particle reached outside the box= ', out_at_least_once)
print('Total number of particle remains inside the box= ', in_always)
print('Percentage of particle outside of the box= ', (out/no_of_times)*100,'%')
print('Percentage of particle inside of the box= ', (inside/no_of_times)*100,'%')







from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


 # read in reference sets and negate all objectives
reference_set = 1*np.loadtxt('../data_ref/Borg_lake.set')

reference_set[:,1] = -reference_set[:,1]
reference_set[:,0] = -reference_set[:,0]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.ylim([0.92, 1.02])
plt.xlim([0, 2.5])
ax.set_zlim(0.25, 0.55)
#plt.gca().invert_xaxis()
#plt.gca().invert_yaxis()


ax.set_yticks(np.arange(0.92, 1.02, 0.02))
ax.set_xticks(np.arange(0.0, 2.5, 0.5))
ax.set_zticks(np.arange(0.25, 0.55, 0.1))

z = reference_set[:,0]
x = -reference_set[:,1]
y = -reference_set[:,2]
color = -reference_set[:,3]




f=ax.scatter(x, y, z, c=color, marker='o',cmap='coolwarm')

#ax.set_facecolor('white')
ax.set_xlabel('Phosphorus Concentration',fontsize=14)
ax.set_ylabel('Inertia',fontsize=14)
ax.set_zlabel('Economic Benefit',fontsize=14)
ax.set_title("Borg Reference Set",fontsize=18)
#ax.tick_params(axis = 'both', which = 'major', labelsize = 14)



#ax.xaxis.labelpad = 20
#ax.yaxis.labelpad = 20
#ax.zaxis.labelpad = 20


cbar = plt.colorbar(f)
cbar.set_label('Reliability',fontsize=14)
cbar.ax.tick_params(labelsize=12)

ax.scatter(min(x),max(y),0.55 , c='black', s=500, linewidth=0, marker='*',)
fig.set_size_inches(8, 6)

#cbar = plt.colorbar(f)
#cbar.set_label('Reliability',fontsize=12)
#cbar.ax.tick_params(labelsize=14)

fig.savefig("Borg_Reference_Set.png")

##########################################################
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


 # read in reference sets and negate all objectives
reference_set = 1*np.loadtxt('../data_ref/NSGAII_lake.set')

reference_set[:,1] = -reference_set[:,1]
reference_set[:,0] = -reference_set[:,0]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.ylim([0.92, 1.02])
plt.xlim([0, 2.5])
ax.set_zlim(0.25, 0.55)
#plt.gca().invert_xaxis()
#plt.gca().invert_yaxis()


ax.set_yticks(np.arange(0.92, 1.02, 0.02))
ax.set_xticks(np.arange(0.0, 2.5, 0.5))
ax.set_zticks(np.arange(0.25, 0.55, 0.1))

z = reference_set[:,0]
x = -reference_set[:,1]
y = -reference_set[:,2]
color = -reference_set[:,3]




f=ax.scatter(x, y, z, c=color, marker='o',cmap='coolwarm')

#ax.set_facecolor('white')
ax.set_xlabel('Phosphorus Concentration',fontsize=14)
ax.set_ylabel('Inertia',fontsize=14)
ax.set_zlabel('Economic Benefit',fontsize=14)
ax.set_title("NSGAII Reference Set",fontsize=18)
#ax.tick_params(axis = 'both', which = 'major', labelsize = 14)



#ax.xaxis.labelpad = 20
#ax.yaxis.labelpad = 20
#ax.zaxis.labelpad = 20


cbar = plt.colorbar(f)
cbar.set_label('Reliability',fontsize=14)
cbar.ax.tick_params(labelsize=12)

ax.scatter(min(x),max(y),0.55 , c='black', s=500, linewidth=0, marker='*',)
fig.set_size_inches(8, 6)

#cbar = plt.colorbar(f)
#cbar.set_label('Reliability',fontsize=12)
#cbar.ax.tick_params(labelsize=14)

fig.savefig("NSGAII_Reference_Set.png")

##########################################################
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


 # read in reference sets and negate all objectives
reference_set = 1*np.loadtxt('../data_ref/lake.ref')

reference_set[:,1] = -reference_set[:,1]
reference_set[:,0] = -reference_set[:,0]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.ylim([0.92, 1.02])
plt.xlim([0, 2.5])
ax.set_zlim(0.25, 0.55)
#plt.gca().invert_xaxis()
#plt.gca().invert_yaxis()


ax.set_yticks(np.arange(0.92, 1.02, 0.02))
ax.set_xticks(np.arange(0.0, 2.5, 0.5))
ax.set_zticks(np.arange(0.25, 0.55, 0.1))

z = reference_set[:,0]
x = -reference_set[:,1]
y = -reference_set[:,2]
color = -reference_set[:,3]




f=ax.scatter(x, y, z, c=color, marker='o',cmap='coolwarm')

#ax.set_facecolor('white')
ax.set_xlabel('Phosphorus Concentration',fontsize=14)
ax.set_ylabel('Inertia',fontsize=14)
ax.set_zlabel('Economic Benefit',fontsize=14)
ax.set_title("Overall Reference Set",fontsize=18)
#ax.tick_params(axis = 'both', which = 'major', labelsize = 14)



#ax.xaxis.labelpad = 20
#ax.yaxis.labelpad = 20
#ax.zaxis.labelpad = 20


cbar = plt.colorbar(f)
cbar.set_label('Reliability',fontsize=14)
cbar.ax.tick_params(labelsize=12)

ax.scatter(min(x),max(y),0.55 , c='black', s=500, linewidth=0, marker='*',)
fig.set_size_inches(8, 6)

#cbar = plt.colorbar(f)
#cbar.set_label('Reliability',fontsize=12)
#cbar.ax.tick_params(labelsize=14)

fig.savefig("Overall_Reference_Set.png")


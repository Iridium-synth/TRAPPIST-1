import numpy as np #Imports Python mathematical functions library
import matplotlib.pyplot as plt #Imports plot library
import os
my_path = os.path.dirname(os.path.abspath(__file__))+"/" # Figures out the absolute path

my_file = 'Trappist1_starsytem_orbits_BW.svg'

#plt.style.use('dark_background')
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
line_width = 1
#color_palete = list(['#2CBDFE','#47DBCD','#F5B14C',"#b66efa","#9d0007",'#F3A0F2','#9D2EC5','#661D98'])
#color_palete = list(["#ad9d5a",'#F5B14C',"#227ed4",'#1db35e',"#fdfdfd","#b66efa",'#661D98'])
color_palete = list(["#fdfdfd",'#fdfdfd',"#fdfdfd",'#fdfdfd',"#fdfdfd","#fdfdfd",'#fdfdfd'])

color_palete = list(["#3f3f3f",'#3f3f3f',"#3f3f3f",'#3f3f3f',"#3f3f3f","#3f3f3f",'#3f3f3f'])

CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'
"#b66efa"
"#9d0007"

def calculate_radius(a,e):
    """
    a = Semi-major Axis. The largest radii measured from the body being orbited to the farthest point in the orbit
    e = Eccentricity. Description of the shape of the orbit. An eccentricity of 0 means the orbit is perfectly circular; an eccentricity between 0 and 1 is an elliptical orbit
    """
    cos = np.cos
    pi = np.pi
    theta = np.linspace(0,10*pi, 360)
    r = (a*(1-e**2))/(1+e*cos(theta))
    return r, theta

# TRAPPIST-1 STAR
ax.scatter(0, 0, c="#a80a15", s=100, cmap='hsv', alpha=0.90)

# TRAPPIST-1b
a = 0.01162 # Semi-major Axis.
e = 0.00622 # Eccentricity. 
rb, thetab = calculate_radius(a,e)
ax.plot(thetab, rb, color=color_palete[0], linewidth=line_width, linestyle='solid')

# TRAPPIST-1c
a = 0.01581512  # Semi-major Axis. 
e = 0.00654 # Eccentricity. 
rc, thetac = calculate_radius(a,e)
ax.plot(thetac, rc, color=color_palete[1], linewidth=line_width, linestyle='solid')

# TRAPPIST-1d
a = 0.02228038  # Semi-major Axis. 
e = 0.00837 # Eccentricity. 
rc, thetac = calculate_radius(a,e)
ax.plot(thetac, rc, color=color_palete[2], linewidth=line_width, linestyle='solid')

# TRAPPIST-1e
a = 0.02928285  # Semi-major Axis. 
e = 0.00510 # Eccentricity. 
rc, thetac = calculate_radius(a,e)
ax.plot(thetac, rc, color=color_palete[3], linewidth=line_width, linestyle='solid')

# TRAPPIST-1f
a = 0.0371  # Semi-major Axis. 
e = 0.063 # Eccentricity. 
rc, thetac = calculate_radius(a,e)
ax.plot(thetac, rc, color=color_palete[4], linewidth=line_width, linestyle='solid')

# TRAPPIST-1g
a = 0.04687692  # Semi-major Axis. 
e = 0.00208 # Eccentricity. 
rc, thetac = calculate_radius(a,e)
ax.plot(thetac, rc, color=color_palete[5], linewidth=line_width, linestyle='solid')


# TRAPPIST-1h
a = 0.06193488 # Semi-major Axis. 
e = 0.00567 # Eccentricity. 
rc, thetac = calculate_radius(a,e)
ax.plot(thetac, rc, color=color_palete[6], linewidth=line_width, linestyle='solid')


#################
# Plot elements
ax.set_yticklabels([])
ax.yaxis.grid(False)
ax.xaxis.grid(False)
ax.xaxis.set_visible(False) 
ax.set_thetagrids([])
ax.spines['polar'].set_visible(False)
ax.set_facecolor('white')
#ax.set_edgecolor("black")
#edgecolor='none'

print(my_path+my_file)
fig.savefig(my_path+my_file, format='svg', dpi=1200)
plt.show()

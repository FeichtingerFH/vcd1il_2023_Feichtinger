#----
#copy code
#source: Vorgabe Example,
#Git clone https://github.com/altiharfh/vcvd2022_Altinger.git

__doc__ = "sample file for ploting method \
           based on \
           https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/"

#based on
#source: https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/

#required imports
import matplotlib.pyplot as plt
import numpy as np

#================================================
def exec_plot_speed_time_ind(file_name_out,v_start,µ):
  #define figure
    fig = plt.figure()
  #add one plot
    ax1 = fig.add_subplot(111)

  #define variables
    timestep = 0.01
    v = [v_start] #in km/h
    t = [0]
    g = 9.81 #in m/s²
  
  #calculate the data independent on timesteps
    while v[-1] > 0:
      t.append(t[-1] + timestep)
      v.append(v[-1] - µ * g * timestep)  

  #define plots
    ax1.plot(t, v, color ="green", lw = 2)

  #add axis label
    ax1.set_xlabel("time [s]")
    ax1.set_ylabel("speed [km/h]")

  # Add a grid
    ax1.grid(True)

  #add plot label
    fig.suptitle("speed to time on braking \n\n", fontweight ="bold")

  #export as PDF
    plt.savefig(file_name_out)
  
  #Ausgabe
    print("Calc finished of " + file_name_out)

#================================================
def exec_plot_distance_time_ind(file_name_out,v_start,µ,incline):
    #define figure
    fig = plt.figure()
  #add one plot
    ax1 = fig.add_subplot(111)

  #define variables
    timestep = 0.01
    s = [0]
    t = [0]
    v = [v_start/3.6] #Convert km/h into m/s
    g = 9.81
    braking_force = µ * g * np.cos(incline)

  #calculate the data independent on timesteps
    while v[-1] > 0:
      t.append(t[-1] + timestep)
      v.append(v[-1] - braking_force * timestep)
      s.append(s[-1] + v[-1] * timestep + 0.5 * (-braking_force) * (timestep ** 2))
  
  #calculate distance through rule of thumb
    s_thumb = (v_start/10)**2 /2

  #define plot
    ax1.plot(t, s, color ="green", lw = 1)
    ax1.axhline(s_thumb, color='red', linestyle='--', label='Rule of Thumb')

  #add axis label
    ax1.set_xlabel("time [s]")
    ax1.set_ylabel("distance [m]")

  # Add a grid
    ax1.grid(True)

  #add plot label
    fig.suptitle("braking distance \n\n", fontweight ="bold")

  #export as PDF
    plt.savefig(file_name_out)
  #Ausgabe
    print("Calc finished of " + file_name_out)
    print("\tcalc distance: " + str(s[-1]))
    print("\trule of thumb: " + str(s_thumb) )

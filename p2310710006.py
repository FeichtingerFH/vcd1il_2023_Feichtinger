#----
#code based from GIT
#source: Vorgabe Example
#Git clone https://github.com/altiharfh/vcvd2022_Altinger.git

#import system libs
import argparse
import sys

#import defined functions
from plot_example import exec_plot_distance_time_ind, exec_plot_speed_time_ind

#setup arg parser - Input von Terminal 
arg_parser_ = argparse.ArgumentParser(description="Process some integers.")
arg_parser_.add_argument("pdf_file_out", type=str, help="filename to plot")
arg_parser_.add_argument("--mass", type=int, help="mass_argument")
arg_parser_.add_argument("--velocity", type=int, help="velocity_argument")
arg_parser_.add_argument("--friction", type=float, help="friction_argument")
arg_parser_.add_argument("--incline", type=float, help="incline_argument")
cmd_call_args_ = arg_parser_.parse_args()

#Argparse controll and set if note done
if cmd_call_args_.pdf_file_out is None:
    cmd_call_args_.pdf_file_out = "p2310710006.pdf"

if cmd_call_args_.mass is None:
    cmd_call_args_.mass = 1000

if cmd_call_args_.velocity is None:
    cmd_call_args_.velocity = 100

if cmd_call_args_.friction is None:
    cmd_call_args_.friction = 0.85

if cmd_call_args_.incline is None:
    cmd_call_args_.incline = 0


#===============
# a method
def main_method():
    main_method.__doc__ = "sample main method"

#define Variables
    V_START = cmd_call_args_.velocity
    Incline = cmd_call_args_.incline #Steigung in RAD
    µ_dyn = cmd_call_args_.friction
    plot_filename = cmd_call_args_.pdf_file_out

    #create braking plots
    exec_plot_speed_time_ind("Plot_speed_time_" + plot_filename, V_START, µ_dyn )
    exec_plot_distance_time_ind("Plot_distance_time_" + plot_filename, V_START, µ_dyn, Incline)

#===============
# do work and call a methode
main_method()

#terminate program
sys.exit()

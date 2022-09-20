# coding=utf-8

"""
;*************************************************************************
author: franciscoaiglesias@gmail.com
Plots some basic signals for the lab reports
;*************************************************************************
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import math as m

# Output
REPO_PATH = os.getcwd()
PLOT_PATH = REPO_PATH + '/figures'
IMGFRMT = '.png'

# Sistema de audio
# plots
RNG = [-160, 160]
matplotlib.rc('font', size=17)
# format string for decimal numbers
STRFMT = '{:6.2f}'

# main

# 9.a
nval = 7  # number of values
x = np.zeros(nval)+5.  # real values
y = np.arange(m.pi/6, 8*m.pi/6, m.pi/6)  # imag values
nfun = 100  # number of points to plot the full function
fx = np.zeros(nfun)+5.  # real values
fy = np.arange(0, 2*m.pi, 2.*m.pi/nfun)  # imag values

# prepeares plot
matplotlib.rcParams.update({'font.size': 8})
fig, ax = plt.subplots()
# -- Set axis spines at 0
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')
# Hide the other spines...
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')
# -- Decorate the spins
arrow_length = 20  # In points
# X-axis arrow
ax.annotate('Re', xy=(1, 0), xycoords=('axes fraction', 'data'),
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black'))
# Y-axis arrow
ax.annotate('Im', xy=(0, 1), xycoords=('data', 'axes fraction'),
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

# plots
ax.annotate('   x  +  jy  ', (30, -20))
for i in range(nval):
    re = m.e**x[i]*m.cos(y[i])
    im = m.e**x[i]*m.sin(y[i])
    plt.scatter(re, im, marker='o')
    plt.arrow(0, 0, re, im, color='b')
    ax.text(re*1.05, im*1.05, STRFMT.format(re)+'+j'+STRFMT.format(im))
    ax.annotate(STRFMT.format(x[i])+' + j '+STRFMT.format(y[i]), (30, -i*15+-35))
    plt.ylim([-160, 160])
    plt.xlim([-160, 160])
    plt.axis('equal')
    if i == 0:
        plt.plot(np.power(m.e, fx) * np.cos(fy), np.power(m.e, fx) * np.sin(fy), color='none')  # plots fx
        plt.grid()
    if i == nval-1:
        plt.plot(np.power(m.e, fx) * np.cos(fy), np.power(m.e, fx) * np.sin(fy), color='r')  # plots fx
    plt.savefig(PLOT_PATH + '/9.a_'+str(i) + IMGFRMT, bbox_inches='tight')
plt.close()


# 9.b
nval = 8  # number of values
y = np.zeros(nval)+m.pi/4.  # real values
x = np.arange(0, 1.8, 0.2)  # imag values
nfun = 100  # number of points to plot the full function
fy = np.zeros(nfun)+m.pi/4.  # real values
fx = np.arange(0, 1.8, 0.2/nfun*9)  # imag values
# prepeares plot
matplotlib.rcParams.update({'font.size': 8})
fig, ax = plt.subplots()

# plots
ax.annotate('   x  +  jy  ', (0.7, 4.3))
# plt.ylim([0,5])
# plt.xlim([0,5])
# plt.axis('equal')
for i in range(nval):
    re = m.e**x[i]*m.cos(y[i])
    im = m.e**x[i]*m.sin(y[i])
    plt.scatter(re, im, marker='o')
    plt.arrow(0, 0, re, im, color='b')
    ax.text(re*1.05, im*1.05, STRFMT.format(re)+'+j'+STRFMT.format(im))
    ax.annotate(STRFMT.format(x[i])+' + j '+STRFMT.format(y[i]), (0.7, -i*0.2+4.1))
    if i == 0:
        plt.plot(np.power(m.e, fx) * np.cos(fy), np.power(m.e, fx) * np.sin(fy), color='none')  # plots fx
        plt.grid()
    if i == nval-1:
        plt.plot(np.power(m.e, fx) * np.cos(fy), np.power(m.e, fx) * np.sin(fy), color='r')  # plots fx
    plt.savefig(PLOT_PATH + '/9.b_'+str(i) + IMGFRMT, bbox_inches='tight')
plt.close()

# 9.c
nval = 9  # number of values
x = np.arange(0.2, 0.2*(nval+1), 0.2)  # imag values
y = np.arange(m.pi/6., (nval+1)*m.pi/6., m.pi/6.)  # imag values
nfun = 100  # number of points to plot the full function
fx = np.arange(0.2, 1.8, (1.8-0.2)/nfun)  # imag values
fy = np.arange(m.pi/6., 9.*m.pi/6, 8./6.*m.pi/nfun)  # imag values
# prepeares plot
matplotlib.rcParams.update({'font.size': 8})
fig, ax = plt.subplots()
# -- Set axis spines at 0
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')
# Hide the other spines...
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')
# -- Decorate the spins
arrow_length = 20  # In points
# X-axis arrow
ax.annotate('Re', xy=(1, 0), xycoords=('axes fraction', 'data'),
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black'))
# Y-axis arrow
ax.annotate('Im', xy=(0, 1), xycoords=('data', 'axes fraction'),
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

# plots
ax.annotate('   x  +  jy  ', (1, -1))
for i in range(nval):
    re = m.e**x[i]*np.cos(y[i])
    im = m.e**x[i]*np.sin(y[i])
    plt.scatter(re, im, marker='o')
    plt.arrow(0, 0, re, im, color='b')
    ax.text(re*1.20, im*1.20, STRFMT.format(re)+'+j'+STRFMT.format(im))
    ax.annotate(STRFMT.format(x[i])+' + j '+STRFMT.format(y[i]), (1, -i*0.5-1.5))
    plt.ylim([-160, 160])
    plt.xlim([-160, 160])
    plt.axis('equal')
    if i == 0:
        plt.plot(np.power(m.e, fx) * np.cos(fy), np.power(m.e, fx) * np.sin(fy), color='none')  # plots fx
        plt.grid()
    if i == nval-1:
        plt.plot(np.power(m.e, fx) * np.cos(fy), np.power(m.e, fx) * np.sin(fy), color='r')  # plots fx
    plt.savefig(PLOT_PATH + '/9.c_'+str(i) + IMGFRMT, bbox_inches='tight')
plt.close()

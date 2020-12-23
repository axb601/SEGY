# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:00:00 2020

@author: BIRCHHAWKINS

Tool for reading and diplaying standard SEGY data

"""

import segyio
import numpy as np
import matplotlib.pyplot as plt

filename="EBLIM3DMRG19_XLINE2849" #Name of SEGY file

#Insert path to SEGY file
with segyio.open('C:\\Users\\BIRCHHAWKINS\\Python\\data\\EBLIM3DMRG19_XLINE2849', strict=False, ignore_geometry=True) as f:
    # Get basic attributes
    n_traces = f.tracecount
    twt = f.samples
    data = f.trace.raw[:]  # Get all data into memory (could cause issues on big files, better to crop volumes)
    
#Get nth percentile of amplitudes - used to scale (adjust the gain of) the display 
clip_percentile = 98
vm = np.percentile(data, clip_percentile)    

#matplotlib Plot for displaying SEGY
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)
extent = [1, n_traces, twt[-1], twt[0]]  # define extent
ax.imshow(data.T, cmap="RdBu", vmin=-vm, vmax=vm, aspect='auto', extent=extent)
ax.ticklabel_format(axis='both', style='plain')
ax.set_xlabel('CDP number')
ax.set_ylabel('TWT [ms]')
ax.set_title(f'{filename}')
#%% Import libraries needed
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import os
import tkinter as tk
from tkinter import filedialog

# %% Ask the user to select the file containing the mesh bed level data
box_open = tk.Tk()
box_open.withdraw()

# Build a list of tuples for each file type the file dialog should display
my_filetypes = [('all files', '.*'), ('text files', '.txt'), ('Comma-separated files', '.csv')]

# Ask the user to select a single file name.
data_file = filedialog.askopenfilename(parent=box_open,
                                    initialdir=os.getcwd(),
                                    title="Please select the file containing the mesh bed level data",
                                    filetypes=my_filetypes)


# %% Read data from a csv
z_data = pd.read_table(data_file, delimiter= " ", skiprows = 0, skipinitialspace= "true"  )


# Get current time
now = datetime.now()
current_time = now.strftime("%d/%b/%y %H:%M:%S")
title_string = f'G29 Mesh data - {current_time}'

# Create surface figure
fig = go.Figure(data=[go.Surface(z=z_data.values)])


#%% Formatting
fig.update_layout(title= title_string, title_y = .9, autosize=False,
                  width=700, height=450,
                  margin=dict(l=50, r=10, b=10, t=20))

# Use per-axis property definition
fig.update_scenes(xaxis_range = [0, len(z_data.columns.values) ],
                  yaxis_range = [0, len(z_data.index.values) ],
                  zaxis_range=[-1, 1]  )

# Or pack the properties in dict format (more compact and clean)                                 
fig.update_scenes( aspectratio = {'x': .7, 'y': .7, 'z' : 0.5},
                    camera_eye = {'x': 0, 'y': -1, 'z' : 0.9},
                    camera_projection_type='perspective')

fig.update_traces(colorscale = 'Portland') #RdBu
fig.update_layout(plot_bgcolor='white')
fig.update_coloraxes(colorbar_lenmode='pixels', colorbar_len= 200)


# Export to html
box_save = tk.Tk()
box_save.withdraw()
# Build a list of tuples for each file type the file dialog should display
my_filetypes = [('all files', '.*'), ('text files', '.txt'), ('Comma-separated files', '.csv')]

# Ask the user to select a single file name.
save_name = filedialog.asksaveasfilename(parent=box_save,
                                    initialdir=os.getcwd(),
                                    title="Please type the name for the new file",
                                    filetypes=my_filetypes)

fig.show()                                  
fig.write_html(save_name)



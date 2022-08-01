# 3D printer mesh bed level data visualizer
This is a simple script to visualize the data output from Marlin's G29 command. It does not require you to have Octoprint set up. You can just use any host software compatible with your printer, with a command window to send commands and also read the data received from the printer. An excelent, free option is [Pronterface](https://www.pronterface.com/).


## Running the script

### Installing Python requirements
You will need to install some libraries using the command:

    pip install <library>

Just replace \<library> by the actual name of the following libraries:

**plotly**: Provides interactive visualization of the data. This is what makes the interactive plot

**pandas**: to read the data from the text file as a dataframe

**datetime**: to get the current date and time. Those get included in the plot title. I found it useful to track changes on the bed level over time.

**os**: needed to navigate directories when selecting the data files. Actually for now it's just used to get the current directory as star path for the browsing window.

**tkinter**: to get user input/select files and directories.


### Getting bed leveling data and running the script
Issue a G29 command to your printer, and copy the output data from the command window to a text file. The script will prompt you to select the file containing the data you want to visualize. Then, it will ask you to provide a filename to save the output plot as an html file. The plot will open automatically in your web browser.
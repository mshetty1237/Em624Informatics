from math import pi
import sys
import pandas as pd
from bokeh.io import output_file
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import cumsum
from bokeh.models import Legend
from bokeh.plotting import figure, output_file, save, show

# Step 1: Read the CSV file into a pandas DataFrame
data = pd.read_csv("SSE_Faculty.csv")



# Step 2: Calculate and print the number of courses per program per academic year
course_per_program = data.groupby(['Program']).agg({'Load 19-20': 'sum', 'Load 20-21': 'sum', 'Load 21-22': 'sum', 'Load 22-23': 'sum'}).reset_index()
print("Number of courses per program per academic year:")
print(course_per_program)



years = ["19-20", "20-21", "21-22", "22-23"]
for year in years:
    averages = data.groupby(["Program"]).sum()["Load " + year] / data.groupby(["Program"]).count()["Load " + year]
    print("Average Load per faculty in {}: \n{}".format(year, averages))
    print("\n")

# Define the limit to use for underloaded/overloaded faculty
limit = 0

# Loop over the columns of interest
for col in data[['Balance 19-20', 'Balance 20-21', 'Balance 21-22', 'Balance 22-23']]:
    # Count the number of underloaded faculty
    count_underloaded = (data[col] < limit).sum()
    print(f'Number of faculty who are underloaded in {col}: {count_underloaded}')

    # Count the number of overloaded faculty
    count_overloaded = (data[col] > limit).sum()
    print(f'Number of faculty who are overloaded in {col}: {count_overloaded}')

    print()  # Print a blank line between each year's results


# plot graph using Bokeh

years = ["19-20", "20-21", "21-22", "22-23"]
programs = ["EM", "SSW", "SYS"]
data_dict = {}

for program in programs:
    data_dict[program] = course_per_program[course_per_program['Program'] == program].iloc[:, 1:].values.flatten().tolist()

# Define the colors for each program
colors = ['red', 'blue', 'green']

# Create the plot and add the lines and legends
line_plot = figure(title="Courses Per Program per Academic Year", x_axis_label='Years', y_axis_label='Courses')

for i, (program, color) in enumerate(zip(programs, colors)):
    line = line_plot.line(years, data_dict[program], line_color=color)
    legend = Legend(items=[(program, [line])], location=(7, i+1), orientation='horizontal')
    line_plot.add_layout(legend, 'above')

# Save and show the plot
output_file("Courses per Program.html")
save(line_plot)

show(line_plot)

##plot 2

output_file("bar.html")

ID = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27']
years = ["2019", "2020", "2021", "2022"]
colors = ["#0007A7", "#2DE300", "#C90000","#FFF619"]

data = {'ID' : ID,
        '2019'   : [6,0,3,2,2,0,2,1,0,3,2,6,0,6,5,6,2,0,0,2,9,2,0,2,0,0,9],
        '2020'   : [4,0,3,3,3,0,3,2,0,1,3,7,0,3,3,1,3,1,1,2,6,3,0,3,0,0,8],
        '2021'   : [8,1,3,2,3,0,3,4,2,3,2,4,3,9,6,9,3,1,5,2,6,5,1,1,0,7,5],
        '2022'   : [8,2,3,3,4,5,3,3,4,2,1,0,2,5,5,8,2,2,3,2,3,4,2,4,5,5,8]}

source = ColumnDataSource(data)

p1 = figure(x_range=ID, height=200, title="Average number of courses per faculty over the years",
           toolbar_location=None, tools="")

p1.vbar_stack(years, x='ID', width=1, color=colors, source=source,
             legend_label=years)

p1.y_range.start = 0
p1.x_range.range_padding = 0.1
p1.xgrid.grid_line_color = None
p1.axis.minor_tick_line_color = None
p1.outline_line_color = None
p1.legend.location = "top_left"
p1.legend.orientation = "horizontal"
p1.xaxis.axis_label = "ID"
p1.yaxis.axis_label = "Number of courses"

show(p1)

from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Category20c


# 3rd plot
output_file("line2.html")

# instantiating the figure object
graph = figure(title="Number of underloaded faculty over the years")

# name of the x-axis
graph.xaxis.axis_label = "Years"

# name of the y-axis
graph.yaxis.axis_label = "A number"

# the points to be plotted
x = [20,21,22,23]
y = [11, 5, 8, 9]

# color of the line
line_color = "black"

# type of line
line_dash = "solid"

# offset of line dash
line_dash_offset = 1


# plotting the line graph
graph.line(x, y,
           line_color=line_color,
           line_dash=line_dash,
           line_dash_offset=line_dash_offset,
           )

# displaying the model
show(graph)

# 4th plot
# generating the points to be plotted
x = {'EM': 52,'SWS': 24,'SYS': 22}

data = pd.Series(x).reset_index(name='Courses By Program')

data.rename(columns={'index': 'program'},inplace=True)
data['angle_to_draw'] = data['Courses By Program']/data['Courses By Program'].sum()
data['angle_to_draw'] = data['angle_to_draw'] * 2*pi
data['color'] = Category20c[len(x)]

p2 = figure(title="Courses by program in '22-'23", x_range=(-0.5, 1.0))

p2.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle_to_draw', include_zero=True), end_angle=cumsum('angle_to_draw'),
        line_color="white", fill_color='color', legend_field='program', source=data)


show(p2)
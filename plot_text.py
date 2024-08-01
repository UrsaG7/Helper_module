import matplotlib.pyplot as plt

def get_text(ax, x_horz, y_vert, font_size):
    """
    Display value of vertical barplot
    ax = Variable where seaborn is assigned to (e.g ax_examp = sns.barplot)
    x_horz = Specific value (decimal or whole) to determine the position of displayed value along the x-axis (+ right), (- left)
    y_vert = Specific value (decimal or whole) to determine the position of displayed value along the y-axis (+ up), (- down)
    font_size = The size of the font
    """
    for p in ax.patches:
        percentage = f'{p.get_height() : .2f}%'
        x = p.get_x() + p.get_width() / x_horz
        y = p.get_y() + p.get_height() + y_vert
        ax.annotate(percentage, (x, y), size=font_size, ha='center', va='center')


def get_text_horz(ax, x_pos, y_pos, font_size, display):
    """
    Display value of horizontal barplot
    ax = Variable where seaborn is assigned to (e.g ax_examp = sns.barplot)
    x_pos = Specific value (decimal or whole) to determine the position of displayed value along the x-axis (+ right), (- left)
    y_pos = Specific value (decimal or whole) to determine the position of displayed value along the y-axis (+ up), (- down)
    font_size = The size of the font
    display = 'all' to display each of every bar value, 'partial' to display the first bar of every grouped bar category (hue).
    """
    if display == 'all':
        for p in ax.patches:
            percentage = f'{p.get_width() : .2f}%'
            x = p.get_width() + x_pos
            y = p.get_y() + p.get_height() / y_pos
            ax.text(x=x, y=y, s=percentage, size=font_size, ha='left', va='center')
        
    elif display == 'partial':
        i=0
        for p in ax.patches:
            x_val = p.get_width()
            first_cat = len(ax.patches)/2
            if i < first_cat:
                plt.text(x=x_val+x_pos, y=i+y_pos, s=f'{x_val : .2f}%')
                i += 1

def highest_highlight(measurement_axis, highest_color, other_color):
    """
    measurement_axis = Axis used as the measurement
    highest_color = Color used for the highest value. See seaborn.pydata.org for more color.
    highest_color = Color used for the other bar besides the highest.
    """
    palette = []
    
    for item in measurement_axis:
        if item == measurement_axis.max():
            palette.append(highest_color)
        else:
            palette.append(other_color)
    return palette

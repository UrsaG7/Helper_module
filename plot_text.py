import matplotlib.pyplot as plt

def get_text(ax, x_horz, y_vert, font_size):
    for p in ax.patches:
        percentage = f'{p.get_height() : .2f}%'
        x = p.get_x() + p.get_width() / x_horz
        y = p.get_y() + p.get_height() + y_vert
        ax.annotate(percentage, (x, y), size=font_size, ha='center', va='center')


def get_text_horz(ax, x_pos, y_pos, font_size, display):
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
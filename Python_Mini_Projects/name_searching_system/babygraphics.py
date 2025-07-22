

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    spacing = (width - 2 * GRAPH_MARGIN_SIZE) / (len(YEARS))
    return GRAPH_MARGIN_SIZE + year_index * spacing


def draw_fixed_lines(canvas):
    canvas.delete('all')  # delete all existing lines from the canvas

    # upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # lower line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.SW)


def draw_names(canvas, name_data, lookup_names):
    draw_fixed_lines(canvas)  # draw the fixed background grid

    i = 0
    for name in lookup_names:
        color = COLORS[i % len(COLORS)]
        if name in name_data:
            prev_x = None
            prev_y = None
            for j in range(len(YEARS)):
                year = YEARS[j]
                x = get_x_coordinate(CANVAS_WIDTH, j)
                year_str = str(year)
                if year_str in name_data[name]:
                    rank = int(name_data[name][year_str])
                    y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * rank / MAX_RANK
                    label = f"{name} {rank}"
                else:
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    label = f"{name} *"

                canvas.create_text(x + TEXT_DX, y, text=label, anchor=tkinter.NW, fill=color)

                if prev_x is not None and prev_y is not None:
                    canvas.create_line(prev_x, prev_y, x, y, fill=color, width=LINE_WIDTH)
                prev_x = x
                prev_y = y

        i += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

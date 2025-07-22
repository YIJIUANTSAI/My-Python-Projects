"""
File: my_drawing
Name: Christine
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine
from campy.graphics.gwindow import GWindow


def minions(window):
    body = GPolygon()
    body.add_vertex((330, 200))  # upper left
    body.add_vertex((465, 200))  # upper right
    body.add_vertex((450, 400))  # lower right
    body.add_vertex((350, 400))  # lower left
    body.filled = True
    body.fill_color = 'khaki'
    body.color = 'khaki'
    window.add(body)

    pants = GPolygon()
    pants.add_vertex((340, 315))  # upper left
    pants.add_vertex((458, 310))  # upper right
    pants.add_vertex((450, 400))  # lower right
    pants.add_vertex((350, 400))  # lower left
    pants.filled = True
    pants.fill_color = 'midnightblue'
    pants.color = 'midnightblue'
    window.add(pants)

    left_leg = GRect(15, 20, x=375, y=400)
    left_leg.filled = True
    left_leg.fill_color = 'midnightblue'
    left_leg.color = 'midnightblue'
    window.add(left_leg)

    left_shoe = GOval(17, 10, x=375, y=422)
    left_shoe.filled = True
    left_shoe.fill_color = 'midnightblue'
    left_shoe.color = 'midnightblue'
    window.add(left_shoe)

    right_leg = GRect(15, 20, x=415, y=400)
    right_leg.filled = True
    right_leg.fill_color = 'midnightblue'
    right_leg.color = 'midnightblue'
    window.add(right_leg)

    right_shoe = GOval(17, 10, x=416, y=422)
    right_shoe.filled = True
    right_shoe.fill_color = 'midnightblue'
    right_shoe.color = 'midnightblue'
    window.add(right_shoe)

    head = GArc(135, 300, 0, 180, x=330, y=115)
    head.filled = True
    head.fill_color = 'white'
    head.color = 'white'
    window.add(head)

    straw_bottom = GPolygon()
    straw_bottom.add_vertex((425, 75))  # upper left
    straw_bottom.add_vertex((415, 75))  # upper right
    straw_bottom.add_vertex((395, 140))  # lower right
    straw_bottom.add_vertex((405, 140))  # lower left
    straw_bottom.filled = True
    window.add(straw_bottom)

    straw_top = GPolygon()
    straw_top.add_vertex((460, 55))  # upper left
    straw_top.add_vertex((470, 55))  # upper right
    straw_top.add_vertex((425, 72))  # lower right
    straw_top.add_vertex((415, 72))  # lower left
    straw_top.filled = True
    window.add(straw_top)

    left_eye = GArc(50, 110, 0, -180, x=345, y=190)
    left_eye.filled = True
    left_eye.fill_color = 'white'
    left_eye.color = 'white'
    window.add(left_eye)

    right_eye = GArc(50, 110, 0, -180, x=400, y=190)
    right_eye.filled = True
    right_eye.fill_color = 'white'
    right_eye.color = 'white'
    window.add(right_eye)

    eyebrow = GLine(340, 215, 455, 215)
    window.add(eyebrow)

    left_pupil = GOval(8, 8, x=365, y=223)
    left_pupil.filled = True
    window.add(left_pupil)

    right_pupil = GOval(8, 8, x=423, y=223)
    right_pupil.filled = True
    window.add(right_pupil)

    mouth = GRect(13, 4, x=390, y=285)
    mouth.filled = True
    window.add(mouth)


def draw_background(window):
    background = GRect(800, 500)
    background.filled = True
    background.fill_color = 'gainsboro'
    window.add(background)


def main():
    """
    Title: Minions

    I think the way Minions look expressionless is really funny,
    so I tried to draw one using the commands I've learned.
    """
    window = GWindow(width=800, height=500, title='Minions')
    draw_background(window)
    minions(window)


if __name__ == '__main__':
    main()

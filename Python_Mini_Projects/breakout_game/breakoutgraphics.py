

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=window_height-PADDLE_OFFSET)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*BALL_RADIUS, 2*BALL_RADIUS)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - ball_radius) / 2, y=(window_height-ball_radius)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_falling = True

        # Initialize our mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.change_position)

        # Draw bricks
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = col * (brick_width + brick_spacing)
                y = brick_offset + row * (brick_height + brick_spacing)
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if row < 2:
                    brick.fill_color = 'red'
                elif row < 4:
                    brick.fill_color = 'orange'
                elif row < 6:
                    brick.fill_color = 'yellow'
                elif row < 8:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
                self.window.add(brick, x=x, y=y)

        # Count bricks
        self.brick_count = BRICK_ROWS * BRICK_COLS

    def change_position(self, mouse):
        new_x = mouse.x - self.paddle.width / 2
        if new_x < 0:  # don't let the paddle go beyond the left edge
            new_x = 0
        elif new_x + self.paddle.width > self.window.width:  # don't let the paddle go beyond the right edge
            new_x = self.window.width - self.paddle.width
        self.paddle.x = new_x

    def start(self, mouse):
        if self.__dx == 0 and self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
        self.ball_falling = False

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def set_vx(self, new_dx):
        self.__dx = new_dx

    def set_vy(self, new_dy):
        self.__dy = new_dy

    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0
        self.ball_falling = True

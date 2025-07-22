

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        # update
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics.ball.move(vx, vy)

        # check the wall edge
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:  # left or right
            graphics.set_vx(-vx)
        if graphics.ball.y <= 0:  # upper side
            graphics.set_vy(-vy)
        # lower side & avoid the ball stuck bouncing in the paddle
        if graphics.ball.y+graphics.ball.height >= graphics.window.height - graphics.paddle.height:
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:  # live = 0
                graphics.reset_ball()
                break

        # check the ball edge
        # upper left
        x1 = graphics.ball.x
        y1 = graphics.ball.y
        # upper right
        x2 = graphics.ball.x + graphics.ball.width
        y2 = graphics.ball.y
        # lower left
        x3 = graphics.ball.x
        y3 = graphics.ball.y + graphics.ball.height
        # lower right
        x4 = graphics.ball.x + graphics.ball.width
        y4 = graphics.ball.y + graphics.ball.height

        for (x, y) in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
            obj = graphics.window.get_object_at(x, y)
            if obj is not None:
                if obj is graphics.paddle:
                    graphics.set_vy(-vy)
                else:  # bricks
                    graphics.set_vy(-vy)
                    graphics.window.remove(obj)
                    graphics.brick_count -= 1

        # winning condition
        if graphics.brick_count == 0:
            graphics.reset_ball()
            break

        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

from __future__ import division
import curses
from curses import wrapper
'''
def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        try:
            z = 10 / v
        except ZeroDivisionError:
            v = 0
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, z))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
'''

stdscr = curses.initscr()
begin_x = 0; begin_y = 0
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
win.refresh()

pad = curses.newpad(100, 100)
#  These loops fill the pad with letters; this is
# explained in the next section
for y in range(0, 100):
    for x in range(0, 100):
        try:
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
        except curses.error:
            pass

#  Displays a section of the pad in the middle of the screen
pad.refresh(0,0, 5,5, 20,75)
stdscr.addstr(0, 0, "Current mode: Typing mode",
              curses.A_REVERSE)
stdscr.refresh()
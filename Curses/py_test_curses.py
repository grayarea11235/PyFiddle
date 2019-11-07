# import curses

# stdscr = curses.initscr()

# curses.noecho()

# curses.cbreak()

# stdscr.keypad(True)

# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()

# curses.endwin()




from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 10):
        print(i)
        v = i-10
        print(v)
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

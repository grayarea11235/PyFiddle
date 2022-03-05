import feedparser
import curses
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', 
        filename='rssticker.log', level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')
logging.info('Starting up rssticker...')

class NewsItem:
    def __init__(self, title):
        self.title = title


def load_feeds():
    pass

def scan_feeds():
    news_feed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
        
    entry = news_feed.entries[1]
    #print(entry.keys())

    for e in news_feed.entries:
        new_item = NewsItem(e['title'])

    return news_feed.entries


def update_screen():
    pass


def main():
    #scan_feeds()
    do_curses()
    

def refresh_screen(scr):
    entries = scan_feeds()

    i = 0
    for e in entries:
        scr.addstr(i, 0, e['title'])
        #scr.addstr('\n')

        i = i + 1

    scr.refresh()

def do_curses():
    scr = curses.initscr()

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    scr.keypad(0)

    refresh_screen(scr)

#    scr.addstr('hello world\n')
#    scr.addstr('hello world')
#    scr.addstr(0, 0, 'Chickens')

    try:
        done = False
        while done == False:
            c = scr.getch()

            if c == 114: # Lower case r
                refresh_screen(scr)
            else:
                done = True
    finally:
        curses.endwin()

    logging.info(c)


if __name__ == '__main__':
    main()

import curses
import time

def start_screen(screen):
    screen.clear()
    screen.addstr('welcome to speed test')
    screen.addstr('\npress any key to start')
    screen.refresh()

def display_text(screen, target_text, current_text, wpm=0):
    screen.addstr(target_text)
    screen.addstr(1,0, f'wpm : {wpm}')
    for i, char in enumerate(current_text):
        correct = target_text[i]
        color = curses.color_pair(1)
        if char != correct:
            color = curses.color_pair(2)
        screen.addstr(0, i, char, color)

def test(screen):
    target_text = 'abcdefghijklmnopqrstuvwxyz'
    current_text = []
    wpm = 0
    start = time.time()
    screen.nodelay(True)
    while True:
        time_elapsed = max(time.time() - start, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        screen.clear()
        display_text(screen, target_text, current_text)
        screen.refresh()

        if "".join(current_text) == target_text:
            screen.nodelay(False)
            break

        try:
            key = screen.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
        

def main(screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(screen)
    while True:
        test(screen)
        screen.addstr(2, 0, 'you have completed the text! press any key to continue ...')
        key = screen.getkey()
        if ord(key) == 27:
            break
curses.wrapper(main)

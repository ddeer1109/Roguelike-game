import sys
import os
from time import sleep
class Util:
    @staticmethod
    def key_pressed():
        try:
            import tty, termios
        except ImportError:
            try:
                # probably Windows
                import msvcrt
            except ImportError:
                # FIXME what to do on other platforms?
                raise ImportError('getch not available')
            else:
                key = msvcrt.getch().decode('utf-8')
                return key
        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    @staticmethod
    def clear_screen():
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def sleep(time=1):
        sleep(1)

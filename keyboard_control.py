from pynput.keyboard import Key, Controller

keyboard = None

def setup():
	global keyboard
	keyboard = Controller()

def press(c):
	keyboard.press(Key.shift)
	keyboard.press(Key.left)
	keyboard.release(Key.left)
	keyboard.release(Key.shift)
	keyboard.press(Key.backspace)
	keyboard.release(Key.backspace)
	keyboard.type(c)

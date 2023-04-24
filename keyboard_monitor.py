from pynput import keyboard
from threading import Thread
import keyboard_control as kc

# all except 0 and 3 : Anglo-Saxon runes
# 0 = z ('z'ero), 3 = e (thre'e')
rune_numbers = {
	'0' : 'ᛎ', '1' : 'ᚠ', '2' : 'ᛏ', '3' : 'ᛖ', '4' : 'ᚩ',
	'5' : 'ᚱ', '6' : 'ᚳ', '7' : 'ᚷ', '8' : 'ᚹ', '9' : 'ᚻ'
}

# a - w and y : Anglo-Saxon runes
# x, z : Medieval runes
rune_letters = {
	'a' : 'ᚪ', 'b' : 'ᛒ', 'c' : 'ᚳ', 'd' : 'ᛞ', 'e' : 'ᛖ', 'f' : 'ᚠ', 'g' : 'ᚷ',
	'h' : 'ᚻ', 'i' : 'ᛁ', 'j' : 'ᛡ', 'k' : 'ᛣ', 'l' : 'ᛚ', 'm' : 'ᛗ', 'n' : 'ᚾ',
	'o' : 'ᚩ', 'p' : 'ᛈ', 'q' : 'ᛢ', 'r' : 'ᚱ', 's' : 'ᛋ', 't' : 'ᛏ', 'u' : 'ᚢ',
	'v' : 'ᚡ', 'w' : 'ᚹ', 'x' : 'ᛉ', 'y' : 'ᚣ', 'z' : 'ᛎ'
}
numpad_0 = 96
numpad_9 = 105
num_0 = 48
num_9 = 57

def num_range(key_str, a, b):
	value = int(key_str.split('<')[1].split('>')[0])
	if (value >= a and value <= b): return True
	return False

def on_press(key):
	try:
		try:
			if (num_range(str(key), numpad_0, numpad_9)):
				value = int(str(key).split('<')[1].split('>')[0]) - numpad_0
				kc.press(rune_numbers[str(value)])
		except: pass
		if (key.char in rune_numbers): kc.press(rune_numbers[key.char])		
		else: kc.press(rune_letters[key.char])
	except: pass

def on_hotkey():
	main.MainWindow.hide()

def keyboard_listener():
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()

def hotkey_listener():
	with keyboard.GlobalHotKeys({"<ctrl>+<alt>+<shift>": on_hotkey}) as listener:
		listener.join()

def setup():
	kc.setup()
	
	th1 = Thread(target = keyboard_listener)
	th2 = Thread(target = hotkey_listener)
	th1.start()
	th2.start()

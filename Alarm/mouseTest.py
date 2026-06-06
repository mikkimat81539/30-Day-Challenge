from pynput import mouse

def on_move(x, y):
	print(f'Pointer moved to ({x},{y})')

listener = mouse.Listener(on_move=on_move)
listener.start()
listener.join()

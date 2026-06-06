from pynput import mouse

def on_click(x, y, button, pressed):
	print(f'Pressed')

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()

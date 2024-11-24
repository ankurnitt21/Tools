import pyautogui

print("Move the mouse to the top-left corner of the region you want to capture.")
print("Press 'Ctrl + C' to stop.")

try:
    while True:
        x, y = pyautogui.position()  # Get the current mouse position
        print(f"Mouse position: x={x}, y={y}")  # Output coordinates to the console
except KeyboardInterrupt:
    print("\nProgram terminated by user.")

import tkinter as tk
from threading import Thread
from pynput import keyboard
import pyautogui
import scrrenshot_ocr  # Assuming this module handles screenshot capture


class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Capture and OCR")
        self.root.geometry("450x250")

        # Initial coordinates state
        self.coordinates = {"start": None, "end": None}
        self.step = 0  # Track the step: 0 = waiting for start, 1 = waiting for end, 2 = reset

        # Label for instructions
        self.instructions = tk.Label(root, text="Press Num Lock to capture coordinates.\nFirst press: Start Coordinates\nSecond press: End Coordinates\nThird press: Reset.", font=("Arial", 10))
        self.instructions.pack(pady=5)

        # Text Entry for start and end coordinates (editable)
        self.start_entry = tk.Entry(root, font=("Arial", 12), width=40)
        self.start_entry.pack(pady=5)
        self.start_entry.insert(0, "Start Coordinates: Waiting...")
        self.start_entry.config(state='readonly')  # Initially read-only

        self.end_entry = tk.Entry(root, font=("Arial", 12), width=40)
        self.end_entry.pack(pady=5)
        self.end_entry.insert(0, "End Coordinates: Waiting...")
        self.end_entry.config(state='readonly')  # Initially read-only

        # Button to take a screenshot
        self.capture_button = tk.Button(root, text="Take Screenshot", command=self.capture_screenshot, font=("Arial", 14))
        self.capture_button.pack(pady=10)

        # Start the Num Lock listener in the background
        self.listen_thread = Thread(target=self.listen_for_numlock, daemon=True)
        self.listen_thread.start()

    def listen_for_numlock(self):
        """Listens for Num Lock key press and captures the cursor coordinates."""
        def on_press(key):
            try:
                # Check if the pressed key is Num Lock
                if key == keyboard.Key.num_lock:
                    print("Num Lock key pressed.")
                    self.capture_coordinates()
            except Exception as e:
                print(f"Error in Num Lock listener: {e}")

        # Start listening to keyboard events
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def capture_coordinates(self):
        """Captures start and end coordinates based on the current step (Num Lock presses)."""
        current_position = pyautogui.position()  # Get current mouse position

        if self.step == 0:  # Capture start coordinates
            self.coordinates["start"] = current_position
            print(f"Start Coordinates: {current_position}")
            self.update_entry_fields()
            self.step = 1  # Move to next step
        elif self.step == 1:  # Capture end coordinates
            self.coordinates["end"] = current_position
            print(f"End Coordinates: {current_position}")
            self.update_entry_fields()
            self.step = 2  # Move to reset step
        else:  # Reset and prepare for a new set of coordinates
            self.capture_screenshot()  # Automatically trigger screenshot on 3rd press
            self.coordinates = {"start": None, "end": None}
            self.update_entry_fields()
            print("Coordinates reset. Ready for new capture.")
            self.step = 0  # Reset step


    def update_entry_fields(self):
        """Updates the Entry fields with the current coordinates."""
        # Update start coordinates
        self.start_entry.config(state='normal')
        if self.coordinates["start"]:
            self.start_entry.delete(0, tk.END)
            self.start_entry.insert(0, f"Start Coordinates: {self.coordinates['start']}")
        self.start_entry.config(state='readonly')

        # Update end coordinates
        self.end_entry.config(state='normal')
        if self.coordinates["end"]:
            self.end_entry.delete(0, tk.END)
            self.end_entry.insert(0, f"End Coordinates: {self.coordinates['end']}")
        self.end_entry.config(state='readonly')

    def capture_screenshot(self):
        """Handles the screenshot capture based on the start and end coordinates in the entry boxes."""
        try:
            # Ensure we have both start and end coordinates
            if self.coordinates["start"] and self.coordinates["end"]:
                start_coords = self.coordinates["start"]
                end_coords = self.coordinates["end"]

                # Convert to the region format (x1, y1, x2, y2)
                region = (*start_coords, *end_coords)

                # Set the region and capture the screenshot
                scrrenshot_ocr.capture_region = region
                scrrenshot_ocr.capture_and_process()
                print(f"Screenshot captured for region: {region}")
            else:
                print("Coordinates are incomplete, please capture both start and end coordinates.")
        except Exception as e:
            print(f"Error during screenshot capture: {e}")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()

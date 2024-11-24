import tkinter as tk  # Import tkinter for GUI
import scrrenshot_ocr  # Import the screenshot OCR logic from the main script

def on_button_click():
    """
    This function is triggered when the button is clicked.
    It calls the `capture_and_process` function from `screenshot_ocr.py`.
    """
    print("Button clicked! Starting the process...")
    scrrenshot_ocr.capture_and_process()  # Call the function from the main script

# Set up the GUI window
def setup_gui():
    """
    Set up the GUI for the screenshot application with a button.
    """
    root = tk.Tk()
    root.title("Screenshot Capture and OCR")

    # Set window size
    root.geometry("300x150")

    # Add a button to trigger screenshot capture
    capture_button = tk.Button(root, text="Take Screenshot", command=on_button_click, font=("Arial", 14))
    capture_button.pack(expand=True)

    # Start the GUI event loop
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    setup_gui()

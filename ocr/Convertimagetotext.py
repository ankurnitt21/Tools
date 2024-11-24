import pytesseract
from PIL import Image
import pyautogui
import time

# Set the Tesseract executable path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your actual path

# Define the location and filename for the screenshot
screenshot_path = '/ocr/Capture_high_quality.jpg'

# Function to take a screenshot and save it
def capture_screenshot(save_path):
    """
    Capture the screen and save it to a specified file.
    :param save_path: Path to save the screenshot.
    """
    screenshot = pyautogui.screenshot()  # Capture the entire screen
    screenshot.save(save_path)  # Save the screenshot to the specified path

# Function to perform OCR on the saved image
def perform_ocr(image_path):
    """
    Perform OCR on the image specified by image_path.
    :param image_path: Path to the image file for OCR.
    :return: Extracted text as a string.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def main():
    print("Starting the process...")

    try:
        while True:
            # Capture screenshot and save it
            #capture_screenshot(screenshot_path)
            #print(f"Screenshot saved to {screenshot_path}")

            # Perform OCR on the saved screenshot
            extracted_text = perform_ocr(screenshot_path)
            print("\nExtracted Text:")
            print(extracted_text)

            # Pause briefly to reduce CPU load
            break  # Adjust the sleep time if needed

    except KeyboardInterrupt:
        print("Process Stopped by User.")

if __name__ == "__main__":
    main()

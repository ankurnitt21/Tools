import pytesseract
from PIL import Image
import mss
import cv2
import numpy as np
import time
import pyperclip  # Import the pyperclip library

# Set the Tesseract executable path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your actual path

# Define the region to capture (x, y, width, height)
capture_region = (470, 6, 1896, 962)  # Example region; adjust these values based on your needs

# Path to save the screenshot
screenshot_path = 'Capture_high_quality.jpg'  # Change to your desired path

def capture_screen(region):
    """
    Capture a specific region of the screen using mss with high resolution.
    :param region: Tuple (x, y, width, height) defining the screen area to capture
    :return: Processed image as a NumPy array
    """
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        frame = np.array(screenshot)

        # Convert to BGR format for saving with OpenCV (mss returns in RGB format)
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        return frame_bgr

def save_screenshot(frame, path):
    """
    Save the captured frame to a file with high quality.
    :param frame: The image to save
    :param path: Path where the image will be saved
    """
    cv2.imwrite(path, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])  # Save with 100% quality

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
            # Capture the region of the screen at high quality
            frame = capture_screen(capture_region)

            # Save the screenshot to the specified path
            save_screenshot(frame, screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

            # Perform OCR on the saved screenshot
            extracted_text = perform_ocr(screenshot_path)
            print("\nExtracted Text:")
            print(extracted_text)

            # Copy the extracted text to clipboard using pyperclip
            pyperclip.copy(extracted_text)
            print("\nText copied to clipboard!")

            # Pause briefly to reduce CPU load
            time.sleep(1)  # Adjust sleep time if needed
            break  # Remove or adjust for continuous operation

    except KeyboardInterrupt:
        print("Process Stopped by User.")

if __name__ == "__main__":
    main()

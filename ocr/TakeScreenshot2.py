import mss
import cv2
import numpy as np

# Define the region to capture (x, y, width, height)
# Adjust these values to your desired capture area
capture_region = (630, 6, 1896, 962)  # Example region; change as needed


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
    Save the captured frame to a file.
    :param frame: The image to save
    :param path: Path where the image will be saved
    """
    cv2.imwrite('Capture_high_quality.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
  # Save the screenshot


def main():
    # Path to save the screenshot
    screenshot_path = 'Capture_high_quality.png'  # Save with higher quality

    # Capture the region of the screen at the highest quality
    frame = capture_screen(capture_region)

    # Save the screenshot to the specified location with the same name
    save_screenshot(frame, screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")


if __name__ == "__main__":
    main()

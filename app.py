import cv2 as cv

def detect_scratches(path):
    print(path)
    # Load the image
    image = cv.imread(path)

    # Preprocess the image
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection
    edges = cv.Canny(blurred, threshold1=30, threshold2=150)

    # Thresholding
    _, thresholded = cv.threshold(
        edges, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Find contours
    contours, _ = cv.findContours(
        thresholded.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Loop through contours and identify scratches
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 100:  # Filter out small contours
            # Check for scratch-like properties (e.g., elongated shape)
            # You might want to add more sophisticated checks based on your specific needs
            x, y, w, h = cv.boundingRect(contour)
            # Draw rectangle around scratch
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display or save the result
    cv.imshow("Scratch Detection", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    path = "img/test.jpg"
    detect_scratches(path)

# detect_scratches('/img/test.jpg')
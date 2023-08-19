import cv2


def detect_scratches(path):
    print(path)

    image = cv2.imread(path)

    # Preprocess the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection
    edges = cv2.Canny(blurred, threshold1=30, threshold2=150)

    # Thresholding
    _, thresholded = cv2.threshold(
        edges, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(
        thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through contours and identify scratches
    for contour in contours:
        area = cv2.contourArea(contour)
        if 130 > area > 70:  # Filter out small contours
            # Check for scratch-like properties (e.g., elongated shape)
            # You might want to add more sophisticated checks based on your specific needs
            x, y, w, h = cv2.boundingRect(contour)
            # Draw rectangle around scratch
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.namedWindow('Preview', cv2.WINDOW_NORMAL)
    cv2.imshow("Preview", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path = "img/test.jpg"
    detect_scratches(path)

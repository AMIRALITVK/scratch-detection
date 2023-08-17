import cv2
import torch
from torchvision import transforms
from PIL import Image


def detect_scratches(image_tensor):
    # Convert PyTorch tensor to numpy array and then to OpenCV image format
    image_array = image_tensor.numpy().transpose(1, 2, 0)
    image_cv = (image_array * 255).astype('uint8')

    # Apply Canny edge detection to detect edges
    edges = cv2.Canny(image_cv, threshold1=100, threshold2=200)

    # You can further process the 'edges' result to identify scratches based on your criteria
    # For this example, we'll consider scratches as regions with a high density of edges

    # Calculate the ratio of edge pixels to total pixels
    total_pixels = edges.shape[0] * edges.shape[1]
    edge_pixels = cv2.countNonZero(edges)
    edge_density = edge_pixels / total_pixels

    if edge_density > 0.1:  # Adjust the threshold based on your needs
        return True  # Scratch detected
    else:
        return False  # No scratch detected


def resize_and_detect(image_path, new_width, new_height):
    # Load the image using PIL
    image = Image.open(image_path)

    # Define a transformation to resize the image and convert to a PyTorch tensor
    transform = transforms.Compose([
        transforms.Resize((new_height, new_width)),
        transforms.ToTensor()  # Converts the image to a PyTorch tensor
    ])

    # Apply the transformation to the image
    resized_image = transform(image)

    # Detect scratches in the resized image
    is_scratch_detected = detect_scratches(resized_image)

    if is_scratch_detected:
        print("Scratch detected in the resized image.")
    else:
        print("No scratch detected in the resized image.")


if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"
    new_width = 800  # Specify the new width in pixels
    new_height = 600  # Specify the new height in pixels

    resize_and_detect(image_path, new_width, new_height)

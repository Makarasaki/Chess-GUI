import os
import imageio
from datetime import datetime

def create_gif_from_images(image_folder, output_folder, fps=10):
    # Get a list of all PNG files in the folder
    filenames = [f for f in os.listdir(image_folder) if f.endswith('.png')]

    # Sort the filenames by their numeric value (e.g., '0.png' < '1.png' < '2.png', etc.)
    filenames.sort(key=lambda x: int(os.path.splitext(x)[0]))

    images = []
    for filename in filenames:
        file_path = os.path.join(image_folder, filename)
        images.append(imageio.imread(file_path))

    # Create a timestamped filename based on current date and time
    now = datetime.now()
    # e.g., "2023-05-30_14-32-45.gif"
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"{timestamp}.gif"
    output_path = os.path.join(output_folder, output_file)

    # Create the GIF
    imageio.mimsave(output_path, images, fps=fps)
    print(f"GIF saved as {output_path}")

if __name__ == "__main__":
    # Example usage:
    # Assumes the images are in a folder named 'screenshots'
    # and will produce a timestamped GIF in the 'gifs' folder
    create_gif_from_images('screenshots', 'gifs', fps=2)

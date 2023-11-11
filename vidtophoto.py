import cv2
import os

def video_to_frames(video_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the frames per second (fps) of the input video
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Get the width and height of the frames
    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))

    # Set the format for saving the frames
    file_format = '.jpg'

    # Counter for naming frames
    frame_count = 0

    while True:
        # Read the next frame
        success, frame = video_capture.read()

        if not success:
            break

        # Save the frame as an image file
        frame_filename = f"{output_folder}/frame_{frame_count:04d}{file_format}"
        cv2.imwrite(frame_filename, frame)

        # Increment the frame counter
        frame_count += 1

    # Release the video capture object
    video_capture.release()

    print(f"Frames extracted: {frame_count}")
    print(f"Frames per second (fps): {fps}")
    print(f"Frame dimensions: {frame_width}x{frame_height}")

def create_folder(folder_name):
    # Specify the path for the new folder
    folder_path = os.path.join(os.getcwd(), folder_name)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created successfully at {folder_path}")
    else:
        print(f"Folder '{folder_name}' already exists at {folder_path}")

if __name__ == "__main__":
    # Replace 'input_video.avi' with the path to your input video file
    folder_path = 'data/mTBI/video_sequence'

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the current item is a file (not a subdirectory)
        if os.path.isfile(file_path):
            # Your processing code goes here
            print(f"Processing file: {filename}")
            
            # Example: Print the contents of each file
            new_folder = "data/mTBI/video_frames/" + "output_" + filename
            create_folder(new_folder)
            video_to_frames(file_path, new_folder)
        
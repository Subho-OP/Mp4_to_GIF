import os
import moviepy.editor as mp
from tkinter import Tk, filedialog, Button, Label, StringVar


# Function to convert MP4 to GIF
def convert_mp4_to_gif(input_file, output_file, start_time, end_time):
    # Load the video
    video = mp.VideoFileClip(input_file)

    # Trim the video based on start and end time
    video = video.subclip(start_time, end_time)

    # Convert the video to a GIF and save
    video.write_gif(output_file)
    video.close()


# Function to browse the MP4 file
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
    if filename:
        input_path.set(filename)


# Function to choose the output directory
def browse_output():
    foldername = filedialog.askdirectory()
    if foldername:
        output_path.set(foldername)


# Function to start conversion
def start_conversion():
    input_file = input_path.get()
    output_folder = output_path.get()

    if not input_file or not output_folder:
        status.set("Please select both input and output paths!")
        return

    # Output file path
    output_file = os.path.join(output_folder, "output.gif")

    # Set the start and end time for the GIF (in seconds)
    start_time = 0  # Starting at the beginning
    end_time = 10  # End at 10 seconds (you can modify this)

    # Perform the conversion
    try:
        convert_mp4_to_gif(input_file, output_file, start_time, end_time)
        status.set(f"Conversion Successful! GIF saved at {output_file}")
    except Exception as e:
        status.set(f"Error: {e}")


# GUI Setup
root = Tk()
root.title("MP4 to GIF Converter")

# Increase the window size to 500x400
root.geometry("500x400")

# Optionally, make the window non-resizable
root.resizable(False, False)

input_path = StringVar()
output_path = StringVar()
status = StringVar()

# GUI Widgets
Label(root, text="Select MP4 file", font=("Arial", 12)).pack(pady=10)
Button(root, text="Browse MP4", font=("Arial", 12), command=browse_file).pack(pady=10)

Label(root, text="Select Output Folder", font=("Arial", 12)).pack(pady=10)
Button(root, text="Browse Output", font=("Arial", 12), command=browse_output).pack(pady=10)

Button(root, text="Start Conversion", font=("Arial", 14), bg="#4CAF50", fg="white", command=start_conversion).pack(
    pady=20)

Label(root, textvariable=status, font=("Arial", 10), fg="blue").pack(pady=10)

# Run the GUI event loop
root.mainloop()

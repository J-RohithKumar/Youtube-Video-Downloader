# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Widgets():

	head_label = Label(root, text="YouTube Video Downloader Using Tkinter",
					padx=15,
					pady=15,
					font="SegoeUI 14",
					bg="palegreen1",
					fg="red")
 
	head_label.grid(row=1,
					column=1,
					pady=10,
					padx=5,
					columnspan=3)

	link_label = Label(root,
					text="YouTube link :",
					bg="salmon",
					pady=5,
					padx=5)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=35,
						textvariable=video_Link,
						font="Arial 14")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)
	res_label = Label(root,
					text="  Resolution : ",
					bg="salmon",
					pady=5,
					padx=5)
	res_label.grid(row=4,
					column=0,
					pady=5,
					padx=5)

	root.resText = Entry(root,
						width=35,
						textvariable=video_res,
						font="Arial 14")
	root.resText.grid(row=4,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)
	foot_label = Label(root, text="*Enter any one of 144, 360, 720 in Resolution",
					padx=5,
					pady=5,
					font="SegoeUI 10",
					bg="palegreen1",
					fg="red")
	foot_label.grid(row=6,
					column=0,
					pady=10,
					padx=5,
					columnspan=3)

	destination_label = Label(root,
							text="Destination :",
							bg="salmon",
							pady=5,
							padx=9)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								font="Arial 14")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)


	browse_B = Button(root,
					text="Browse",
					command=Browse,
					width=10,
					bg="bisque",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(root,
						text="Download Video",
						command=Download,
						width=20,
						bg="thistle1",
						pady=5,
						padx=15,
						relief=GROOVE,
						font="Georgia, 13")
	Download_B.grid(row=5,
					column=1,
					pady=20,
					padx=20)
# Defining Browse() to select a destination folder to save the video
def Browse():
	# Presenting user with a pop-up for directory selection. initialdir
	# argument is optional Retrieving the  user-input destination directory and
	# storing it in download Directory
	download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video",)
	# Displaying the directory in the directory textbox
	download_Path.set(download_Directory)
# Defining Download() to download the video
def Download():

	# getting user-input Youtube Link
	Youtube_link = video_Link.get()
	# select the optimal location for saving file's
	download_Folder = download_Path.get()
	video_resolution = video_res.get()
	if video_resolution=="360":
		res=18
	elif video_resolution=="720":
		res=22
	elif video_resolution=="144":
		res=17
	# Creating object of YouTube()
	getVideo = YouTube(Youtube_link)
	# Getting all the available streams of the youtube video and selecting the first from the
	videoStream = getVideo.streams.get_by_itag(res)
	# Downloading the video to destination directory
	videoStream.download(download_Folder)

	# Displaying the message
	messagebox.showinfo("DOWNLOADED SUCCESSFULLY ",
						"SUCCESSFULLY DOWNLOADED AND SAVED IN\n"
						+ download_Folder)
# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and size of the tkinter window and disabling the resizing property
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="PaleGreen1")

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()
video_res = StringVar()
# Calling the Widgets() function
Widgets()
# Defining infinite loop to run application
root.mainloop()
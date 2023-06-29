import tkinter as tk
import serial

#print(serial.__version__)
arduino = serial.Serial(port = 'COM7', baudrate = 115200, timeout=1)

# Create a main window
root = tk.Tk()

# change window title
root.title("Gripper Control GUI V0.7")

# Set height and width variables
width = 500
height = 500

# create variable to keep track of servo angle
global servoAngle
servoAngle = 0


# Resize the window using geometry method
root.geometry(f"{width}x{height}")

# Make the window not resizable
root.resizable(False, False)

# Create a label widget with a title
label = tk.Label(root, text="Gripper Control GUI", pady=8, font=("Helvetica", 12, "bold"))

# Create a label to display the status message
varStatus = tk.StringVar()
varStatus.set("Gripper Ready.")
status = tk.Label(root, textvariable=varStatus, borderwidth=5, relief="sunken", font=("Helvetica", 17, "bold"))

varAngle = tk.StringVar()
varAngle.set("Servo Angle: " + str(servoAngle));
angleStatus = tk.Label(root, textvariable=varAngle, borderwidth=5, relief="sunken", font=("Helvetica", 15, "bold"))

# Place the label on the window using pack method
label.pack()

# Create a frame widget to hold the buttons
frame = tk.Frame(root)

# Place the frame on the window using pack method
frame.pack()

# Create a function to write to serial
def write_data(servo_value):
    delim = bytes(';', "utf-8")
    arduino.write(bytes(str(int(servo_value)), "utf-8"))    
    arduino.write(delim)

# Create a function to open gripper
def open_gripper():
    global servoAngle
    if (servoAngle == 0):
        varStatus.set("Gripper is aready open.")
    else:
        varStatus.set("Gripper Opening.")
        write_data(0)
        servoAngle = 0
        varAngle.set("Servo Angle: " + str(servoAngle))

# Create a function to close gripper
def close_gripper():
    global servoAngle
    if (servoAngle == 180):
        varStatus.set("Gripper is already closed.")
    else:
        varStatus.set("Gripper Closing.")
        write_data(180)
        servoAngle = 180
        varAngle.set("Servo Angle: " + str(servoAngle))

# Create a function to open gripper by 10 degrees
def open_10():
    global servoAngle
    if (servoAngle == 0):
        varStatus.set("Gripper is fully open.")
    else:
        varStatus.set("Gripper opening by 10 degrees.")
        write_data(-10)
        servoAngle -= 10
        varAngle.set("Servo Angle: " + str(servoAngle))

# Create a function to close gripper by 10 degrees    
def close_10():
    global servoAngle
    if (servoAngle == 180):
        varStatus.set("Gripper is fully closed.")
    else:
        varStatus.set("Gripper closing by 10 degrees.")
        write_data(10)
        servoAngle += 10
        varAngle.set("Servo Angle: " + str(servoAngle))

# Create a function to close gripper by 20 degrees
def close_20():
    global servoAngle
    if (servoAngle == 180):
        varStatus.set("Gripper is fully closed.")
    elif (servoAngle == 170):
        varStatus.set("Gripper closing by 10 degrees.")
        write_data(180)
        servoAngle = 180
        varAngle.set("Servo Angle: " + str(servoAngle))
    else:
        varStatus.set("Gripper closing by 20 degrees.")
        write_data(20)
        servoAngle += 20
        varAngle.set("Servo Angle: " + str(servoAngle))

# Create a function to open gripper by 20 degrees
def open_20():
    global servoAngle
    if (servoAngle == 0):
        varStatus.set("Gripper is fully open.")
    elif (servoAngle == 10):
        varStatus.set("Gripper opening by 10 degrees.")
        write_data(0)
        servoAngle = 0
        varAngle.set("Servo Angle: " + str(servoAngle))
    else:
        varStatus.set("Gripper opening by 20 degrees.")
        write_data(-20)
        servoAngle -= 20
        varAngle.set("Servo Angle: " + str(servoAngle))

# Create a function to open gripper halfway
def open_half():
    global servoAngle
    if (servoAngle == 90):
        varStatus.set("Gripper is aready half open.")
    else:
        varStatus.set("Gripper opening halfway.")
        write_data(0)
        write_data(90)
        servoAngle = 90
        varAngle.set("Servo Angle: " + str(servoAngle))
        
# Create a function to close serial when window closes   
def close():
    root.destroy() # Close the window
    arduino.close() # Then the connection

root.wm_protocol('WM_DELETE_WINDOW',close) # Assuming root = Tk()
   

# Create a button widget with some text and a command to open gripper
open_button = tk.Button(frame, text="Open Gripper", command=open_gripper, width=14, height=3, bg="lightGreen", font=("Helvetica", 17, "bold"))

# Place the button on the frame using pack method with side option
open_button.pack(side=tk.LEFT, padx=4)

# Create a button widget with some text and a command to close gripper
close_button = tk.Button(frame, text="Close Gripper", command=close_gripper, width=14, height=3, bg="#ff55a3", font=("Helvetica", 17, "bold"))

# Place the button on the frame using pack method with side option
close_button.pack(side=tk.RIGHT, padx=4)

# Create a button widget with some text and a command to open gripper
open_half = tk.Button(root, text="Open Gripper Halfway", command=open_half, width=23, height=1, bg="lightBlue", font=("Helvetica", 12, "bold"))

# Place the button on the frame using pack method with side option
open_half.place(relx=0.5, rely=0.34, anchor=tk.CENTER)

# Create a button widget with some text and a command to open gripper
open_10 = tk.Button(root, text="Open Gripper by 10 Degrees", command=open_10, width=23, height=1, bg="#f7e7ce", font=("Helvetica", 12, "bold"))

# Place the button on the frame using pack method with side option
open_10.place(relx=0.5, rely=0.43, anchor=tk.CENTER)

# Create a button widget with some text and a command to open gripper
close_10 = tk.Button(root, text="Close Gripper by 10 Degrees", command=close_10, width=23, height=1, bg="lightBlue", font=("Helvetica", 12, "bold"))

# Place the button on the frame using pack method with side option
close_10.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

# Create a button widget with some text and a command to open gripper
open_20 = tk.Button(root, text="Open Gripper by 20 Degrees", command=open_20, width=23, height=1, bg="#f7e7ce", font=("Helvetica", 12, "bold"))

# Place the button on the frame using pack method with side option
open_20.place(relx=0.5, rely=0.61, anchor=tk.CENTER)

# Create a button widget with some text and a command to open gripper
close_20 = tk.Button(root, text="Close Gripper by 20 Degrees", command=close_20, width=23, height=1, bg="lightBlue", font=("Helvetica", 12, "bold"))

# Place the button on the frame using pack method with side option
close_20.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

# Place status message
status.place(relx=0.5, rely=0.81, anchor=tk.CENTER, width=380)

# Place servo angle
angleStatus.place(relx=0.5, rely=0.92, anchor=tk.CENTER, width=250)

# Run the main loop
root.mainloop()

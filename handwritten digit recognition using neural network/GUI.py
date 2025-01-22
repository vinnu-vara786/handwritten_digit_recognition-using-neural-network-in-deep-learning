from tkinter import *
import numpy as np
from PIL import ImageGrab
from Prediction import predict

window = Tk()
window.title("Handwritten Digit Recognition")

# Label with new font and color
l1 = Label()

def MyProject():
    global l1

    widget = cv
    # Setting coordinates of canvas
    x = window.winfo_rootx() + widget.winfo_x()
    y = window.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()

    # Capture the image from canvas and resize to (28 X 28) px
    img = ImageGrab.grab().crop((x, y, x1, y1)).resize((28, 28))

    # Convert RGB to grayscale image
    img = img.convert('L')

    # Extract pixel matrix of image and convert it to a vector of (1, 784)
    x = np.asarray(img)
    vec = np.zeros((1, 784))
    k = 0
    for i in range(28):
        for j in range(28):
            vec[0][k] = x[i][j]
            k += 1

    # Load Thetas
    Theta1 = np.loadtxt('Theta1.txt')
    Theta2 = np.loadtxt('Theta2.txt')

    # Call the prediction function
    pred = predict(Theta1, Theta2, vec / 255)

    # Display the result with updated font and color
    l1 = Label(window, text="Predicted Digit: " + str(pred[0]), font=('Courier New', 20, 'bold'), fg="purple", bg="lightyellow")
    l1.place(x=180, y=420)

lastx, lasty = None, None

# Clears the canvas
def clear_widget():
    global cv, l1
    cv.delete("all")
    l1.destroy()

# Activate canvas for drawing
def event_activation(event):
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y

# Draw lines on canvas
def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width=30, fill='black', capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y

# Label with new font, color, and position
L1 = Label(window, text="Handwritten Digit Recognition", font=('Arial', 25, 'italic'), fg="darkgreen", bg="lightblue")
L1.place(x=50, y=10)

# Button to clear canvas with updated colors
b1 = Button(window, text="Clear Canvas", font=('Arial', 16), bg="lightcoral", fg="black", command=clear_widget)
b1.place(x=120, y=370)

# Button to predict drawn digit with new color scheme
b2 = Button(window, text="Predict Digit", font=('Arial', 16), bg="mediumseagreen", fg="white", command=MyProject)
b2.place(x=320, y=370)

# Setting properties for canvas with updated background color
cv = Canvas(window, width=350, height=290, bg='beige')
cv.place(x=120, y=70)

cv.bind('<Button-1>', event_activation)
window.geometry("600x500")
window.configure(bg="lightblue")  # Set a background color for the window
window.mainloop()

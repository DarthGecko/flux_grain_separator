# python3.8.2
import io
import PySimpleGUI as sg
from PIL import Image, ImageTk


# Practice with Event-Based Programming.
sg.theme('DarkAmber')
j_str = "Jester.png"

img = Image.open(j_str)
# First time opening of Image is tricky.
# This avoids RuntimeError: Too early to create image
bio = io.BytesIO()
img.save(bio, format="PNG")
j_img = bio.getvalue()
jester = sg.Image(data=j_img)
layout = [[sg.Text("Total Axis Manipulation")],
          [sg.Text("Axis 1"), sg.InputText()],
          [jester],
          [sg.Button('OK'), sg.Button('Cancel')]]
main_win = sg.Window('Inverted Dimension Multiplier', layout)

while True:
    event, values = main_win.read()
    if event in (None, 'Cancel'):
        break
    print('You entered ', values[0])
    if values[0] == 'x':
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        jester.update(data=ImageTk.PhotoImage(img))
        print('Here, have a horizontal flip.')
    if values[0] == 'y':
        # jester.Source = cv2.flip(j_img, 0)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        jester.update(data=ImageTk.PhotoImage(img))
        print('Here\'s a vertical flip.')

main_win.close()

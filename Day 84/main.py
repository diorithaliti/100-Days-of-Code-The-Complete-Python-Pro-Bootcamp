from tkinter import *
import tkinter
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import customtkinter

filetypes = (
    ('JPG files', '*.JPG'),
    ('All files', '*.*'),
)
def choose():
    filename = tkinter.filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,
    )
    print(filename)
    im = Image.open(filename)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    text = "DH Watermarked"

    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
 #   im.show()

    # Save watermarked image
    im.save(f'{filename}_watermarked.jpg')


# open-file dialog
customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green"

window = customtkinter.CTk()
window.title("DH Watermarker")
window.geometry("400x480")


# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 50, image=logo_img)


frame_1 = customtkinter.CTkFrame(master=window)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

# label = Label(text="Watermark Pictures For Free    ")
# label.grid(row=0, column=1)
label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Watermark Pictures For Free IMAGE")
label_1.pack(pady=10, padx=10)
# button = Button(text="ADD IMAGE", command=choose)
# button.grid(row=3, column=1)
button_1 = customtkinter.CTkButton(master=frame_1, command=choose, text="ADD IMAGE")
button_1.pack(pady=10, padx=10)


window.mainloop()
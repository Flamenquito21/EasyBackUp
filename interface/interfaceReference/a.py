
import io
import tkinter as tk
from PIL import Image,ImageTk

main=tk.Tk()

image_data = main.svg2png(url="example.svg")
image = Image.open(io.BytesIO(image_data))
tk_image = ImageTk.PhotoImage(image)

button=tk.Label(main, image=tk_image)
button.pack(expand=True, fill="both")
main.mainloop()
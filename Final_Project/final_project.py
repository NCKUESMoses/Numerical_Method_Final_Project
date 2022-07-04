# %%
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageFont, ImageDraw
import os

# %%
# create functions
def load():
    global img_path, img, imgg, print_path
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((500, 500))
    img1 = ImageTk.PhotoImage(img)
    canvas.create_image(325, 265, image=img1)
    canvas.image=img1
    print_path.set(img_path)

def blur(event):
    global img1, imgg
    for m in range(0, blur_val.get()+1):
        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg)
        canvas.create_image(325, 265, image=img1)
        canvas.image=img1

def bright(event):
    global img1, imgg
    for m in range(1, bright_val.get()+1):
        imgg = ImageEnhance.Brightness(img).enhance(m)
        img1 = ImageTk.PhotoImage(imgg)
        canvas.create_image(325, 265, image=img1)
        canvas.image=img1

def mosaic(event):
    global img1, imgg
    for m in range(1, mosaic_val.get()+1):
        w,h = img.size
        imgg = img.resize((int(w/(m)),int(h/(m))))
        imgg = imgg.resize((w,h), resample=Image.NEAREST)
        img1 = ImageTk.PhotoImage(imgg)
        canvas.create_image(325, 265, image=img1)
        canvas.image=img1

def save():
    global imgg
    w,h = img.size
    float_font = ImageFont.truetype('arial', 20)
    float_text = Image.new(mode='RGBA', size=(200, 150), color=(0,0,0,0))
    float_draw = ImageDraw.Draw(float_text)
    float_draw.text((0,0),'E94086131 STUDIO', fill=(255,255,255), font=float_font)
    float_text = float_text.rotate(5, expand=1)
    imgg.paste(float_text,(w-200,h-70), float_text)
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension =f".{ext}",filetypes=[("PNG file","*.png")])
    imgg.save(file)


# %%
# contrast border thumbnail 
win = Tk()
win.title("Image Editor")
win.geometry("750x700")

# -----load frame-----
load_frm = Frame(win, height=20)
load_frm.grid(row=0, column=0, sticky='nw')

load_button = Button(load_frm, text="Select Image", width=12, font=('Arial 14 bold'), command=load)
load_button.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

print_path = StringVar()
load_label = Label(load_frm, textvariable=print_path, font=('Arial 12'))
load_label.grid(row=0, column=1, padx=10, pady=15, sticky='nw')

# -----image-----
canvas = Canvas(win, width="650", height="520", relief=RIDGE, bd=2)
canvas.grid(row=1, column=0, padx=10)

# -----editor frame-----
edi_frm = Frame(win, height=20)
edi_frm.grid(row=2, column=0, sticky='nw')

blur_label = Label(edi_frm, text="Blur:", font=("Arial 14 bold"), width=9)
blur_label.grid(row=0, column=0, sticky=W)
blur_val = IntVar()
blur_scale = ttk.Scale(edi_frm, from_=0, to=10, variable=blur_val, orient=HORIZONTAL, command=blur) 
blur_scale.grid(row=0, column=1, sticky=W)

bright_label = Label(edi_frm, text="bright:", font=("Arial 14 bold"), width=9)
bright_label.grid(row=0, column=2, sticky=W)
bright_val = IntVar()
bright_scale = ttk.Scale(edi_frm, from_=0, to=10, variable=bright_val, orient=HORIZONTAL, command=bright) 
bright_scale.grid(row=0, column=3, sticky=W)

mosaic_label = Label(edi_frm, text="mosaic:", font=("Arial 14 bold"), width=9)
mosaic_label.grid(row=0, column=4, sticky=W)
mosaic_val = IntVar()
mosaic_scale = ttk.Scale(edi_frm, from_=1, to=30, variable=mosaic_val, orient=HORIZONTAL, command=mosaic) 
mosaic_scale.grid(row=0, column=5, sticky=W)

end_frm = Frame(win, width=700, height=30)
end_frm.grid(row=3, sticky=E)


save_button = Button(end_frm, text="save", width=8, font=('Arial 14 bold'), command=save)
save_button.grid(row=0, column=0, padx=5)

exit_button = Button(end_frm, text="leave", width=8, font=('Arial 14 bold'), command=win.destroy)
exit_button.grid(row=0, column=1, padx=5)

win.mainloop()

# %%




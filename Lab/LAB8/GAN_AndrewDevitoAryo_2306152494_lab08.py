'''
Nama    : Andrew Devito Aryo
NPM     : 2306152494
Kelas   : DDP1-C
Asdos   : GAN
'''
# Import Library Needed
from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT, HORIZONTAL, DoubleVar, ttk
from tkinter.colorchooser import askcolor

class Scribble(object):
    '''A simple pen drawing application'''
    def __init__(self):
        self.is_eraser_on = False

        self.master = Tk()
        self.master.title('Simple Pen (Finger) Scribble')
        self.master.geometry('1100x600')

        # Mouse coordinates and the drawing color are instanc variables
        self.oldx, self.oldy = 0, 0
        self.color = '#000000'

        # Create canvas 800 x 500
        self.canvas = Canvas(self.master, width=800, height=500, bg='#FFFFFF')
        # -- pressing the left mouse button
        self.canvas.bind('<Button-1>', self.begin)
        # -- moving the mouse while holding/pressing left mouse button
        self.canvas.bind('<Button1-Motion>', self.draw)

        self.canvas.pack(expand=True, fill=BOTH)

        # create a new frame for holding the button
        frame1 = Frame(self.master)
        frame1.pack(side=TOP)

        self.bt_clear = Button(master=frame1, text='Clear', command=self.delete)
        self.bt_clear.pack(side=LEFT, padx=5)

        self.bt_color = Button(master=frame1, text='Color', command=self.change_color, bg=self.color, fg='white')
        self.bt_color.pack(side=LEFT, padx=5)

        self.bt_erase = Button(master=frame1, text='Erase', command=self.eraser)
        self.bt_erase.pack(side=LEFT, padx=5)

        self.pen_width = DoubleVar()

        self.scale = ttk.Scale(frame1, orient=HORIZONTAL, length=220, variable=self.pen_width, from_=10.0, to=200.0)
        self.scale.pack(side=LEFT)

        self.message = Label(self.master, text='Press and drag the left mouse-button to draw')
        self.message.pack(side=BOTTOM)

        # start the event loop
        self.master.mainloop()
    
    def begin(self, event):
        '''handles left button click by recording mouse position 
        as the start of the curve'''

        self.oldx, self.oldy = event.x, event.y

    def eraser(self):
        '''handles eraser mechanism, erase is equal to pen with canvas color
        (in this case, the canvas color is white)'''

        self.is_eraser_on = not self.is_eraser_on
        if self.is_eraser_on:
            self.color = self.canvas['bg']
            self.bt_erase['bg'] = 'red'
        else:
            self.color = self.bt_color['bg']
            self.bt_erase['bg'] = 'white'

    def draw(self, event):
        '''handles mouse motion, while pressing left button, by
        connecting the previous mouse position to the new one'''

        self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color, width=self.pen_width.get(), capstyle='round')
        self.oldx, self.oldy = event.x, event.y

    def delete(self):
        '''Clear the canvas'''
        self.canvas.delete('all')

    def change_color(self):
        '''change the drawing color using the color chooser, 
        also change the background color of the color button'''
        self.color = askcolor()[-1]
        self.bt_color['bg'] = self.color

if __name__ == '__main__':
    Scribble()
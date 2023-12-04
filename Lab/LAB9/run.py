'''
Nama    : Andrew Devito Aryo
NPM     : 2306152494
Kelas   : DDP1 - C
Asdos   : GAN
'''

# Import the library needed
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox, ttk

class DrawRubberShapes(object):
    # Contruct the GUI
    def __init__(self):
        window = Tk()
        window.title('Lab 09: Drawing Rubber Shapes')
        frame1 = Frame(window)
        frame1.pack()

        # Create a button for choosing color using a color chooser
        self.fillcolor = StringVar()
        self.fillcolor.set('red')
        
        def colorCommand():
            (rgb, color) = askcolor()
            if color != None:
                self.fillcolor.set(color)
                colorButton['bg'] = color

        colorButton = Button(frame1, text='Color', command=colorCommand, bg=self.fillcolor.get())
        colorButton.grid(row=1, column=1, columnspan=2)

        # Create radio buttons for geometrical shapes
        self.v1 = StringVar()
        self.v1.set('R')
        rbRectangle = Radiobutton(frame1, text='Rectangle', variable=self.v1, value='R', command=self.processRadioButton)
        rbRectangle.grid(row=1, column=3)

        # Radiobutton for Oval
        rbOval = Radiobutton(frame1, text='Oval', variable=self.v1, value='O', command=self.processRadioButton)
        rbOval.grid(row=1, column=4)

        # Radiobutton for Line
        rbLine = Radiobutton(frame1, text='Line', variable=self.v1, value='L', command=self.processRadioButton)
        rbLine.grid(row=1, column=5)
        
        # Create a clear button
        clearButton = Button(frame1, text='Clear', command=self.clearCanvas, bg='yellow')
        clearButton.grid(row=1, column=6, columnspan=2)


        # TODO: Line Width Setup
        self.line_width = DoubleVar()
        
        self.message = Label(frame1, text=f'Pen Width: ')
        self.message.grid(row=2, column=1)

        # Create a scale for line width
        self.scale = Scale(frame1, orient=HORIZONTAL, length=220,variable=self.line_width, from_=1.0, to=200.0 )
        self.scale.set(20)
        self.scale.grid(row=2, column=2, columnspan=5)

        # Create a canvas, bound to mouse events
        self.canvas = Canvas(window, width=400, height=300)
        self.canvas.pack(expand=TRUE, fill=BOTH)

        # Create a label to display in canvas
        self.pressHmessage = Label(self.canvas, text='Press h for help')
        self.pressHmessage.place(x=0, y=0)

        # Setup all bind for the app
        self.canvas.bind('<ButtonPress-1>', self.onStart) # left-click
        self.canvas.bind('<B1-Motion>', self.onGrow) # and drag for drawing
        self.canvas.bind('<ButtonPress-3>', self.startMove) # right-click
        self.canvas.bind('<B3-Motion>', self.moving) # and drag for moving
        self.canvas.bind('<Key>', self.keyPressed) # press key 'd' to delete, and 'h' to show help
        self.canvas.focus_set()

        # for remembering the current object and shape
        self.object = None
        
        # Default Shape is Rectangle
        self.shape = self.canvas.create_rectangle
        
        window.mainloop()

    def setPenWidthMessage(self):
        # self.message['text'] = f'Pen Width: {self.line_width.get()}'
        print(f'Pen Width: {self.line_width.get()}')

    def processRadioButton(self):
        # Create shape based on radio button clicked
        if self.v1.get() == 'R':
            self.shape = self.canvas.create_rectangle
        elif self.v1.get() == 'O':
            self.shape = self.canvas.create_oval
        elif self.v1.get() == 'L':
            self.shape = self.canvas.create_line

    def onStart(self, event):
        self.start = event
        self.object = None

    def startMove(self, event):
        self.startMoving = event
        objectTuple = self.canvas.find_closest(event.x, event.y)
        if objectTuple != ():
            self.object = objectTuple[0]
            
    def moving(self, event):
        canvas = event.widget
        if self.object:
            canvas.move(self.object, event.x - self.startMoving.x,
                    event.y - self.startMoving.y)
            self.startMoving = event

    # elastic drawing: delete and redraw, repeatedly
    def onGrow(self, event):
        canvas = event.widget
        if self.object: canvas.delete(self.object)
        if self.v1.get() == 'L':
            objectId = self.shape(self.start.x, self.start.y, event.x, \
                                  event.y, fill=self.fillcolor.get(), width=self.line_width.get())
        else:
            objectId = self.shape(self.start.x, self.start.y, event.x, \
                    event.y, fill=self.fillcolor.get(), \
                    outline=self.fillcolor.get())
        self.object = objectId

    # Clear the canvas if clear button is clicked
    def clearCanvas(self):
        self.canvas.delete('all')

    def keyPressed(self, event):
        print(event.char)
        if event.char == 'd' or event.char == '':
            self.canvas.delete(self.object)
        elif event.char == 'h':
            messagebox.showinfo('Click & Move', \
                                'Mouse Commands:\n\
Left + Drag = Draw new rubber shape\n\
 Right = Select a Shape\n\
 Right + Drag = Drag the selected shape\n\
Keyboard Commands:\n\
    d = Delete the Selected Shape\n\
    h = Help')

if __name__ == '__main__':
    DrawRubberShapes()
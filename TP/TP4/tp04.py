# Import Necessary Library
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox

# Mainwindow Class
class MainWindow:
    def __init__(self, is_unit_test = False, barcode_inputs = '', eps_file_name = ''):
        # Window Setup
        self.window = Tk()
        self.window.title('EAN-13 [by Andrew D.A.]')
        self.window.geometry('500x600')
        self.window.resizable(False, False)

        frame1 = Frame(self.window)

        # Form 1 - EPS File Name Entry
        self.eps_file_name = StringVar()
        label1 = Label(frame1, text='Save barcode to PS file [eg: EAN13.eps]:', font='Helvetica 15 bold')
        eps_input = Entry(frame1, textvariable=self.eps_file_name)

        eps_input.bind('<Return>', self.enter_pressed)

        # Form 2 - 12 Decimal Digits Entry
        self.decimal_digits_input = StringVar()
        label2 = Label(frame1, text='Enter code (first 12 decimal digits):', font='Helvetica 15 bold')
        code_input = Entry(frame1, textvariable=self.decimal_digits_input)

        code_input.bind('<Return>', self.enter_pressed)

        # TODO: Extra Features
        # Color Chooser Function
        self.bar_color = StringVar()
        self.border_color = StringVar()

        self.bar_color.set('black')
        self.border_color.set('blue')
        def chooseBarColorCommand():
            (rgb, color) = askcolor()
            if color != None:
                self.bar_color.set(color)
                bar_color_button['bg'] = color
            self.barcode.enter(self.decimal_digits_input.get(), self.eps_file_name.get(), self.bar_color.get(), self.border_color.get(), bar_width=self.bar_width.get())

        def chooseBorderColorCommand():
            (rgb, color) = askcolor()
            if color != None:
                self.border_color.set(color)
                border_color_button['bg'] = color
            self.barcode.enter(self.decimal_digits_input.get(), self.eps_file_name.get(), self.bar_color.get(), self.border_color.get(), bar_width=self.bar_width.get())
        
        # Color Chooser Button for Bar Color and Border Color
        frame2 = Frame(frame1)
        bar_color_button = Button(frame2, text='Bar Color', command=chooseBarColorCommand, bg=self.bar_color.get(), fg='white')
        border_color_button = Button(frame2, text='Border Color', command=chooseBorderColorCommand, bg=self.border_color.get(), fg='white')

        # Bar Width Scale
        self.bar_width = DoubleVar()
        self.scale = Scale(frame2, orient=HORIZONTAL, length=80,variable=self.bar_width, from_=3.0, to=10.0 )
        self.scale.set(8)

        # Load and Positioning Features inside Frame2
        bar_color_button.grid(row=1, column=1, padx=5)
        border_color_button.grid(row=1, column=2, padx=5)
        self.scale.grid(row=1, column=3, columnspan=2)

        # Load and Positioning Element
        frame1.pack()
        label1.grid(row=1, column=1)
        eps_input.grid(row=2, column=1)

        label2.grid(row=3, column=1)
        code_input.grid(row=4, column=1)

        frame2.grid(row=5, column=1, pady=10)

        # Barcode Canvas Setup
        self.barcode = Barcode()

        self.barcode.pack(pady=10)

        # Unit test
        if is_unit_test and barcode_inputs != '' and eps_file_name != '':
            self.decimal_digits_input.set(barcode_inputs)
            self.eps_file_name.set(eps_file_name)

            self.barcode.enter(self.decimal_digits_input.get(), self.eps_file_name.get(), self.bar_color.get(), self.border_color.get(), bar_width=self.bar_width.get())
        
            self.barcode.after(1000, self.save_postscript)
        
        # MainWindow will closed if Escape is clicked
        self.window.bind('<Escape>', self.close_window)

        self.window.mainloop()

    def save_postscript(self):
        self.barcode.postscript(file=f'eps_folder/{self.eps_file_name.get()}', colormode='color')
    
    def close_window(self, event):
        self.window.withdraw()
        exit()

    def enter_pressed(self, event):
        # Check if 12 Digits Entry contains alphabet or the length of input is not equal to 12
        if not self.decimal_digits_input.get().isdigit() or \
            len(self.decimal_digits_input.get()) != 12:
            messagebox.showerror('Wrong Input!', 'Please enter correct input code')
        # Check if eps file name is valid (contains .eps and not)
        elif not self.eps_file_name.get().endswith('.eps') or self.eps_file_name.get().replace('.eps', '') == '':
            messagebox.showerror('Wrong Input!', 'EPS file name invalid')
        else:
            # Reset Canvas and Generate new Barcode
            self.barcode.enter(self.decimal_digits_input.get(), self.eps_file_name.get(), self.bar_color.get(), self.border_color.get(), bar_width=self.bar_width.get())

    def __str__(self):
        return "This is a barcode scanner built by Andrew Devito Aryo"

# Class Barcode inherited from Canvas
class Barcode(Canvas):
    def __init__(self):
        # Make a new Canvas Object
        super().__init__(width=400, height=500, bg='white')

        # Define the structure used to encode the input digits
        self.ean_13_structure       =  ('LLLLLLRRRRRR', 'LLGLGGRRRRRR', 'LLGGLGRRRRRR',
                                        'LLGGGLRRRRRR', 'LGLLGGRRRRRR', 'LGGLLGRRRRRR',
                                        'LGGGLLRRRRRR', 'LGLGLGRRRRRR', 'LGLGGLRRRRRR',
                                        'LGGLGLRRRRRR')
        self.encoding_ean_digits    =  (('0001101', '0100111', '1110010'), ('0011001', '0110011', '1100110'), 
                                        ('0010011', '0011011', '1101100'), ('0111101', '0100001', '1000010'),
                                        ('0100011', '0011101', '1011100'), ('0110001', '0111001', '1001110'),
                                        ('0101111', '0000101', '1010000'), ('0111011', '0010001', '1000100'),
                                        ('0110111', '0001001', '1001000'), ('0001011', '0010111', '1110100'))
        
        # Define default value of Input Entry, Bar Color, Border Color, Bar Height, and Bar Width
        self.input_digits = ''
        self.bar_color = 'black'
        self.border_color = 'blue'

        self.bar_height = 200
        self.bar_width = 2

    def enter(self, input_digits, eps_file_name, bar_color = 'black', border_color = 'blue', start_y = 100, bar_width = 2):
        # Clear Canvas and Clear Encoded List
        self.delete('all')
        self.encoded_digits_list = []

        # Start Position Setup
        # TODO: How to count start_x:
        # 95                        : Count of bar in an EAN Barcode
        # (bar_width / 10) * 4      : Determine the barwidth based on Bar Width Scale

        self.start_x = (int(self['width']) - (95 * (bar_width / 10) * 4)) / 2
        self.start_y = start_y

        # Instance Variable Setup
        self.input_digits   = input_digits
        self.bar_color      = bar_color
        self.border_color   = border_color
        self.bar_width      = bar_width

        # Draw barcode
        self.draw_barcode()

        # Create Checksum text
        self.create_text(int(self['width']) / 2, start_y + 280, text=f'Checksum: {self.calculate_check_digit()}', \
                         fill='orange', font='Helvetica 20 bold')

        # Save image to postscript file
        self.postscript(file=f'eps_folder/{eps_file_name}', colormode='color')

    def calculate_check_digit(self):
        check_sum = 0
        for index, digit in enumerate(self.input_digits):
            # If index is even, then weight = 1. Otherwise, if Index is odd, weight = 3
            weight = 1
            if index % 2 == 1:
                weight = 3
            
            # Add digit * weight to check_sum
            check_sum += int(digit) * weight
        
        # Calculate Check Digit
        check_digit = check_sum % 10
        if check_sum % 10 != 0:
            check_digit = 10 - check_sum%10
        
        return str(check_digit)
    
    def digits_conversion(self):
        # Choose what LGR composition will we use based on the first digit of 12 Decimal Entry
        chosen_ean_composition = self.ean_13_structure[int(self.input_digits[0])]

        # Iterate trought chosen LGR composition
        for index, encode_code in enumerate(chosen_ean_composition):
            # If current iteration is L, then lgr_index = 0
            lgr_index = 0

            # If current iteration is G, then lgr_index = 1
            if encode_code == 'G':
                lgr_index = 1

            # If current iteration is R, then lgr_index = 2
            elif encode_code == 'R':
                lgr_index = 2
            
            # Convert each digit based on LGR Composition
            converted_digit = self.encoding_ean_digits[int(self.digit_to_proceed[index + 1])][lgr_index]

            # Append to encoded_digits_list
            self.encoded_digits_list.append(converted_digit)

    # Function to draw each bar
    def draw_bar(self, group_of_binary, bar_height = 200, custom_color = '', num = '', start = False, gap=30):
        # Determine the color for each bar
        bar_count = 0
        for binary in group_of_binary:
            # Bar Color Setup
            bar_color = 'black'
            if binary == '0':
                bar_color = 'white'
            elif custom_color != '':
                bar_color = custom_color

            # Create line
            self.create_line(self.start_x, self.start_y, \
                             self.start_x, self.start_y + bar_height, \
                             fill=bar_color, width=(self.bar_width / 10) * 4)
            
            # Move the drawer to right based on scaled bar width)
            self.start_x += (self.bar_width / 10) * 4
            bar_count += 1
        
        # Create text under group of binary

        # If Start is False
        if not start:
            middle_position_x = self.start_x - (self.bar_width / 10) * 4 * bar_count / 2
            self.create_text(middle_position_x, self.start_y + self.bar_height + gap, text=num, font='Helvetica 18 bold')
        # If We want to draw display digit of start border
        else:
            self.create_text(self.start_x - 8*(self.bar_width / 10) * 4, self.start_y + self.bar_height + gap, text=num, font='Helvetica 18 bold')

    # Function to draw barcode
    def draw_barcode(self):
        # Add checkdigit to the most right part of input digits
        # self.input_digits += self.calculate_check_digit()
        self.digit_to_proceed = self.input_digits + self.calculate_check_digit()

        # Create EAN-13 Barcode title
        self.create_text(int(self['width']) / 2, 50, text="EAN-13 Barcode", font='Helvetica 20 bold')
        
        # Convert input digits to list of group of binary
        self.digits_conversion()

        # TODO: Create Bar
        # Start Bar - 101
        self.draw_bar('101', bar_height=210, custom_color=self.border_color, num=self.digit_to_proceed[0], start=True)

        # Content Bar
        for index, code in enumerate(self.encoded_digits_list):
            self.draw_bar(code, num=self.digit_to_proceed[index+1], custom_color=self.bar_color)
            # If index is 5, then we will draw middle border
            if index == 5:
                # Middle Bar - 01010
                self.draw_bar('01010', bar_height=210, custom_color=self.border_color)

        # End Bar - 101
        self.draw_bar('101', bar_height=210,  custom_color=self.border_color)

def main():
    MainWindow()

if __name__ == '__main__':
    main()
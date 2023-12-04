from tp04 import *

def unit_test(file_name, code, color= 'blue'):
    class TestBarcode(MainWindow):
        def __init__(self):
            super().__init__()
            self.eps_file_name.set(file_name)
            self.decimal_digits_input.set(code)
    TestBarcode()
            

if __name__ == "__main__":
    unit_test('vit.eps', '899275201140')
    unit_test('tessa.eps', '899293100511')
    unit_test('swana.eps', '899882455175')
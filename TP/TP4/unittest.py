from tp04 import *

# Barcode inputs include check sum (last digit included)
def unit_test(barcode_inputs_with_check_sum, file_name):
    # Aspect 1: Check if barcode inputs were correct
    if len(barcode_inputs_with_check_sum) != 13 or not barcode_inputs_with_check_sum.isdigit():
        print("Barcode Inputs are not valid!")
    else:
        # Aspect 2: Check if barcode generated successfully
        # Generate a window with already generated barcode based on input digits

        window = MainWindow(True, barcode_inputs_with_check_sum[:12], file_name)

        # Aspect 3: Check if checksum in barocode = check sum that calculated via the function
        # Check if our checksum is equal to generated checksum
        if window.barcode.calculate_check_digit() == barcode_inputs_with_check_sum[-1]:
            print(f"Checksum is safe! {window.barcode.calculate_check_digit()} == {barcode_inputs_with_check_sum[-1]}\
 is {window.barcode.calculate_check_digit() == barcode_inputs_with_check_sum[-1]}")
        else:
            print(f"Checksums dont match! {window.barcode.calculate_check_digit()} == {barcode_inputs_with_check_sum[-1]}\
 is {window.barcode.calculate_check_digit() == barcode_inputs_with_check_sum[-1]}")

# Here, just insert 13 digits of product barcode (include check sum)
unit_test('8997035563476', 'fitbar.eps')
unit_test('9789790339378', 'purcell_book.eps')
unit_test('8998866610124', 'nuvo_hand_sanitizer.eps')
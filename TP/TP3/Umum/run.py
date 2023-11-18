from tp3_template import *

data = read_csv('abalone.csv')
new_data = select_cols(data, ['Rings', 'Diameter'])

# scatter(data, "Length", "Diameter")
scatter(data, "Length", "Diameter")
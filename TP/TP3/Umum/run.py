from tp3 import *
import time

def main():
    start = time.time()
    dataframe = read_csv("abalone.csv")
    print(head(sorted_dataframe(dataframe, 'Sex'), 100))


    custom_plot(dataframe, 'Length', 'Diameter', 'Height')

    end = time.time()

    print(f"Done in {end - start:.3f} seconds")
if __name__ == '__main__':
    main()
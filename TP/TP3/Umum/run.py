from tp3 import *
import time

def main():
    start = time.time()
    dataframe = read_csv("test1.csv")
    print(to_list(dataframe))

    end = time.time()

    print(f"Done in {end - start:.3f} seconds")
if __name__ == '__main__':
    main()
#!/usr/bin/env python3


def main():
    row = 1
    maxx = 11
    col = 1
   
    for row in range(1,maxx):
        for col in range(1,maxx):
            print(f"{row*col} ",end="")
        print("")

if __name__ == "__main__":
    main()

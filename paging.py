# course: CSC3002F
# Assignment : OS1
# date: 29/05/2020
# StudentNo: THNGEO002
# name: Georgeo Thanathara
# description: Implemeting th Fifo,LRU & OPT algorithms
import sys
import random


def main():
    size = int(sys.argv[1])
    if((size<1) or (size>7)):
        print("Your frame size should be an integer between 1 and 7")
        exit()
    pages=""
    for x in range(9):
        pages=pages+str(random.randint(0,9))
    #print "FIFO", FIFO(size,pages), "page faults."
    #print "LRU", LRU(size,pages), "page faults."
    #print "OPT", OPT(size,pages), "page faults."


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python paging.py [number of pages]")
    else:
        main()
# course: CSC3002F
# Assignment : OS1
# date: 29/05/2020
# StudentNo: THNGEO002
# name: Georgeo Thanathara
# description: Implemeting th Fifo,LRU & OPT algorithms
import sys
import random

def FIFO(size,pages):
    pFaults=0
    queue=[]
    for page in pages:
        if(len(queue)!=size):
            queue.append(page)
            pFaults=pFaults+1
        else:
            if(page not in queue):
                queue.pop(0)
                queue.append(page)
                pFaults=pFaults+1
           
       

    return pFaults

def OPT(size,pages):
    pFault=0
    queue=[]
    for page in range(len(pages)):

        if(len(queue)!=size):
            queue.append(pages[page])
            pFault=pFault+1
        else:
            if(pages[page] not in queue):
                matches=[]
                rejects=[]
                check=False
                
                for i in queue:
                    innerC=False
                    for j in range(page,len(pages)):
                        if(i == pages[j]):
                            matches.append(j)
                            check=True
                            innerC=True
                            break
                    if(innerC==False):
                        rejects.append(i)
                        


                
                if(check and (len(matches)==size)):
                    switch=queue.index(pages[max(matches)])       
                    queue[switch]=pages[page]
                    pFault=pFault+1
                
                       
                else:
                    queue[queue.index(rejects[0])]=pages[page] 
                    pFault=pFault+1
            
        

    return pFault
def LRU(size,pages):
    pFault=0
    queue=[]
    for page in range(len(pages)):
        dict={}
        for ele in range(0,page):
            if pages[ele] not in dict.keys():
                dict[pages[ele]]=1
            else:
                dict[pages[ele]]+=1
        if(len(queue)!=size):
            queue.append(pages[page])
            pFault=pFault+1
        else:
            if(pages[page] in queue):
                continue
            else:
                max=100000
                replace=""
                for ay in queue:
                    if ay in dict.keys():
                        if dict[ay]<=max:
                            max=dict[ay]
                            replace=ay
                queue[queue.index(replace)]=pages[page]
                pFault+=1


                

                    
            
        

    return pFault

def main():
    size = int(sys.argv[1])
    if((size<1) or (size>7)):
        print("Your frame size should be an integer between 1 and 7")
        exit()
    pages=""
    for x in range(9):
        pages=pages+str(random.randint(0,9))
    pages="2748064263683623842273793235"
    print ("FIFO", FIFO(size,pages), "page faults.")
    print ("LRU", LRU(size,pages), "page faults.")
    print ("OPT", OPT(size,pages), "page faults.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python paging.py [number of pages]")
    else:
        main()
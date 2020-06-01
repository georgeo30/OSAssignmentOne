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
            if(page in queue):
                continue
            else:
                queue.append(page)
                pFaults+=1
        else:
            if(page not in queue):
                queue.pop(0)
                queue.append(page)
                pFaults+=1
           
       

    return pFaults

def OPT(size,pages):
    pFault=0
    queue=[]
    for page in range(len(pages)):
        if(len(queue)!=size):
            if(pages[page] in queue):
                continue
            else:
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
        
        if(len(queue)!=size):
            if(pages[page] in queue):
                
                queue.remove(pages[page])
                queue.append(pages[page])
            else:
                queue.append(pages[page])
                pFault=pFault+1
        else:
            if(pages[page] not in queue):
                queue.pop(0)
                queue.append(pages[page])
                
                pFault=pFault+1
            else:
                queue.remove(pages[page])

                queue.append(pages[page])
                
    return pFault

def main():
    size = int(sys.argv[1])
    length=int(sys.argv[2])
    if((size<1) or (size>7)):
        print("Your frame size should be an integer between 1 and 7")
        exit()
    pages=""
    for x in range(length):
       pages=pages+str(random.randint(0,9))

    print("random pages that are going to be swapped in and out",pages)
    print ("FIFO", FIFO(size,pages), "page faults.")
    print ("LRU", LRU(size,pages), "page faults.")
    print ("OPT", OPT(size,pages), "page faults.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ("Usage: python paging.py [number of frames in memory [1,7]] [number of pages in virtual memory to be swapped in]")
    else:
        main()
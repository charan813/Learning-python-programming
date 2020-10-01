import time, sys
indent=0 #how many spaces to indent
indentincreasing= True #whether the indentation is increasing or not

try:
    while True:
        print(' '*indent,end='')
        print('*******')
        time.sleep(0.2)
        
        if indentincreasing:
            #increasing the number of spaces.
            indent= indent+1
            if indent==20:
                #change direction
                indentincreasing= False
        
        else:
            #decreasing the number of spaces
            indent=indent-1
            if indent==0:
                #change direction
                indentincreasing= True
except KeyboardInterrupt():
    sys.exit()
            
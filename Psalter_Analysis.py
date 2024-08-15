# -*- coding: utf-8 -*-
"""
Analysis

@author: S D Francis
"""

def main():
    print('Initializing analysis mode')

    Command = input()
    command = Command.lower()
    
    running = True
    
    while running == True:
        
        if command == 'c':
            running = False
            continue
        
        else:
            print(ms.confusion)

if __name__ == '__main__':
    main()
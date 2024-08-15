# -*- coding: utf-8 -*-
"""
                                    Psalter
Author: S D Francis


This is the wrapper file for Psalter.
"""

import Psalter_Messages as ms
import Psalter_Strong as strong
import Psalter_Reader as reader
import Psalter_Analysis as analysis


def main():
    
    # Print intro message 
    print(ms.intro)
    
    Prunning = True
    
    while Prunning == True:
        # Print prompt
        print(ms.prompt)
    
        # Ask for input
        Command = input()
        command = Command.lower()
        
        # C to quit
        if command == 'c':
            print(ms.outro)
            Prunning = False
        
        if command == 'x':
            print(ms.outro)
            Prunning = False
        
        # Help message
        elif command == 'help':
            print(ms.help)
            
        # Send to analysis mode
        elif command == 'analysis':
            analysis.main()
    
        # Send to reader mode
        elif command == 'reader':
            reader.main()
        
        # Send to strongs mode
        elif command == 'strong' :
            strong.main()
            
        # If the prompt is unintelligable
        else:
            print(ms.confusion)
            
    




if __name__ == '__main__':
    main()


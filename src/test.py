#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    print ('Hello world')
    print ('おはよう世界')
    
    for i in range(5):
        print  (i)
        
    list = ['a','b','c','d']
    
    print ('len = ', len(list))
 
    for i in range(len(list)):
        print (list[i])
        
    for i in list:
        print (i, end='')

if __name__ == '__main__':
    main()
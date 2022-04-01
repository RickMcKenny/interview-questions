#!/usr/bin/env python
import re
'''
First technical interview -- Completed Mon, March 28 2022
Specifications:
must contain at least 8 characters, 
must contain at least one letter
must contain at least one digit, 
must contain at least one {!, ", #, $, %, &, ', , (, ), *, +, , -, ., / }
cannot contain four consecutive characters in a previous password

Test Cases:
Input 'G5%2@H#df', 'HS27hs5gd2!','abC123!@#'
'Tes$t1nG.', 'Te$t1ng','#&$!1*8.','Te$tinG.','A1b2C3d4','@hs5gD1.*A'

'''
def fourCons(pw, prev):
    '''
    inputs: string new password 
    prev: array of previous passwords
    Return: Boolean, true if the substring is not repeated, false if it is

    Uses sliding window tech to check four consecutive characters against previous passwords,

    '''

    for i in range(len(prev)):
        for j in range(len(pw) - 3):
            if pw[j: j+4] in prev[i]:
                return False
    return True
    
def checkPw(pw, prev):
    '''
    Param1: string: new password
    param2: array: last 3 passwords

    Utilizes happy path to validate pw. If all checks pass, password is accepted. 
    '''
    if len(pw) < 8:
        return False
    
    check = False

    for i in pw:
        if i in {'!', '"', '#', '$', '%', '&', '\'', ',', '(', ')', '*', '+', '-', '.', '/'}:
            check = True
            break

    if check:
        
        if re.search("[a-zA-Z]", pw):
            if re.search("[0-9]", pw):
                return fourCons(pw, prev)

    
    return False
    

if __name__ == '__main__':
    previous = ['G5%2@H#df', 'HS27hs5gd2!','abC123!@#']
    cases = ['Tes$t1nG.', 'Te$t1ng','#&$!1*8.','Te$tinG.','A1b2C3d4','@hs5gD1.*A']

    

    outcome = [True, False, False, False, False, False]
    for i in range(len(cases)):
        print(checkPw(cases[i], previous), "should be: ", outcome[i])


    


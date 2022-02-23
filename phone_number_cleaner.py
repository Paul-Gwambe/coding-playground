#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mobile_phone_cleaner(phone):
    """
    The function ``phone_cleaner`` cleans the input mobile phone number, ``phone``,
    into a desirable format that satisfies the following conditions:
    Removes all non-numeric characters from the string, phone.
    Add an initial zero if it is missing.
    Raises an error if the number provided is not the correct 
    length after adjusting for the initial zero.
    Returns the cleaned number.
    For simplicity, length of output is assumed to contain 10 digits.
    """
    
    try:
        #String is the variable in which we will append numeric values 
        #from input parameter, 'phone'.
        string = ''
        
        #We confirm if all characters present in input parameter, phone, 
        #are numeric, if not, loop through it to select numerics 
        if phone.isnumeric() != True:
            for character in phone:

                #Checks if each characteter from phone is numeric, if so, 
                #we select and append it to string
                if character.isnumeric() == True:
                    string = string + str(character)
        
        #Checks if input mobile number has all digits as non numeric
        if len(string) == 0:
            raise AssertionError('Can not have all characters as non numeric')
        
        #Now lets check if the leading digit is zero, if not, we add zero
        if string[0] != '0':
            string = str('0') + string

        #Confirms if the phone number, 'string', has the correct length of 10
        assert len(string) == 10, 'The mobile phone number does not contain correct length of numeric characters'
        
        #If string has the correct length and format, return it
        print("The cleaned phone number is: {num}".format(num = string))
        
    except AssertionError as msg:
            print(msg)
        


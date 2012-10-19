def right_justify(someString):
    strLen = len(someString)
    print(' '*(70-strLen)+someString)
    
right_justify("allan")
right_justify("a")
right_justify(" ")
right_justify("")
right_justify("1234567890123456789012345678901234567890123456789012345678901234567890")
right_justify("12345678901234567890123456789012345678901234567890123456789012345678901234567890")

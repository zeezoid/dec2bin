def dec2bin(n):
    remains=[] #open an array
    while True :
        r=n%2
        remains.append(r) #add each r to the array
        n=n//2
        if n ==1:
            remains.append(n) #add the last one to the array
            break
    #reverse the order of the array
    #remove the commas and take as a single string
    binary="".join(str(item) for item in list(reversed(remains)))
    #returns a string
    return binary



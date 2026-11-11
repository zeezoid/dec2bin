def main(n):
    remains=[] #open an array
    while True :
        r=n%2
        remains.append(r) #add each r to the array
        n=n//2
        print(int(n),f" and {r} remains")
        if n ==1:
            break
    print(remains , " (reversed order)") #print the array of the binary numbers in the reverse order
    #reverse the order
    correct_order=list(reversed(remains))
    print(correct_order)   #correct order
    #remove the commas and take as a single string
    binary="".join(str(item) for item in remains)
    print(binary)

main(30)

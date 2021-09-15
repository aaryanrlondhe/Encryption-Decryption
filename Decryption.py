def decrypt():
    var= input("Enter Your Text to Decrypt\n")
    g=0 
    sentence=[]
    for i in var:
        sentence.append(i)

    length=len(sentence)
    try:
        while(g!=length-1):
            sentence[g+1],sentence[g] = sentence[g],sentence[g+1]
            g=g+2
    except IndexError:
        while(g!=length):
            sentence[g+1],sentence[g] = sentence[g],sentence[g+1]
            g=g+2

    var2="".join(sentence)
    print("\n")
    print(" -------------Your Decrypted Text -------------")
    print("\n")
    print(var2.swapcase())


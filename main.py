## Zolix interpreter.
## By sahilgeorge
## URL to social media : https://www.beacons.ai/sahilgeorge

##defining some variables...
commands = ["exit", "help", "ver", "hash", "bta", "bintoascii" ]
hashes = ["sha1", "sha256", "sha384", "sha512", "md5", "md4"]
ver = "\n\nZolix Interpreter [Version.0.0.0]\n By sahilgeorge \n"

##NAME BANNER
print(ver)

##MAIN INTERPRETER LOGIC
while "zolix" == "zolix":
    console = input("zolix_terminal >> ")
    ##hasher function {will probably join most of this in the hsh file}
    if console[0:4] == "hash": 
        import hsh
        if console[6:] == "sha256":
            retirn = hsh.sha256(input("Enter the string to hash: "))
            print(retirn)
                    
        elif console[6:] == "md5":
            retirn = hsh.md5(input("Enter the string to hash: "))
            print(retirn)

        elif console[6:] == "sha1":
            retirn = hsh.sha1(input("Enter the string to hash: "))
            print(retirn)
        
        elif console[6:] == "sha384":
            retirn = hsh.md5(input("Enter the string to hash: "))
            print(retirn)
            
        elif console[6:] == "sha512":
            retirn = hsh.md5(input("Enter the string to hash: "))
            print(retirn)
            
        elif console[6:] == "md4":
            retirn = hsh.md5(input("Enter the string to hash: "))
            print(retirn)
            
        elif console[6:] != hashes:
            print("Currenty supports: -sha1 -sha256 -sha384 -sha512 -md5 -md4")
        

    elif console == "exit":
        print("\nExiting Zolix environment!!!")
        exit()
    
    elif console == "":
        continue
    
    elif console == "ver":
        print(ver)
    
    elif console == "bta" or console == "bintoascii":
        print("\n[WARNING!] \n[This function is currently a bit whack. Will try to fix any issues in the future.]\n\n")
        import bintoascii
        asc = bintoascii.bta(input("Enter the Binary with Every First bit of the byte removed: "))
        print(asc)
    
    elif console == "help":
        print("----------------------------------------------------------------------------")
        print("Zolix Help Menu: \nBelow are some commands(commands are case sensitive) and their uses:")
        print("----------------------------------------------------------------------------")
        print("     help       : Displays this help menu.\n")
        print("     hash       : Hashes the given string. More info can be seen when typed hash in the command line.\n")
        print("     ver        : Prints the given version.\n")
        print("     bta        : Converts entered binary string to its equivalent ascii character.\n")
        print("     bintoascii : Same as bta command.\n")
        print("     exit       : Quits the Zolix environment.\n")
    
    elif console != commands:
        print("No Such Commands. Available commands are:\n" + str(commands))
        
    continue


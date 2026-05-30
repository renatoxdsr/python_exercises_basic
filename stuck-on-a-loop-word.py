

palavra = str(input("Type a word: "))
while True:
    
    if palavra != "chupacabra":
        print("Wrong word")
        palavra = str(input("Type a word: "))
    else:
        print("You've successfully left the loop.")
        break

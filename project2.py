#encription programm(ceaser chiper)

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o', 'p','q',
           'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
def encription(plain_text,shift_key):
    chipertext=" "
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            chipertext+=alphabets[new_position]
        else:
            chipertext+=char
    print("the encription text is " ,{chipertext})
   
   
def discription(chipertext,shift_key):
    plain_text=" "
    for char in chipertext:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabets[new_position]
        else:
            plain_text+=char
    print("the encription text is ",{plain_text} )
        
wanna_end=False
while not wanna_end:
    what_to_do=input("type 'encript' for encription ,type 'discript' for discription:\n")
    text=input("enter a text: ")
    shift=int(input("enter shift: "))
    if what_to_do=='encript':
        encription(plain_text=text,shift_key=shift)
    elif what_to_do=="discript":
        discription(text,shift)
        play_again=input("type 'yes' to continue and type 'no' to exit ")
        if play_again=='no':
            wanna_end=True
            print("have a nice dayand Bye!...")
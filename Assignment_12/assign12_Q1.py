def checkvowel(char):
    if len(char)==1:
        if char.isalpha():
            vowel=["a","e","i","o","u"]
            Char=char.lower()
            if Char in vowel:
                return "vowel"
            else:
                return "Consonant"
        else:
            return "Not an alphabet character"
    else:
        return "Only one character needed"
 

char=input("Enter a character : ")
res=checkvowel(char)
print(res)
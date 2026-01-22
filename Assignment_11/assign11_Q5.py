def checkpalindrome(No):
    originalno=No
    reversedno=0
    while No>0:
        digit=No%10
        reversedno=reversedno * 10 + digit
        No//=10

    if originalno==reversedno:
        print("Palindrome")
    else:
        print("Not a Palindrome ")

No=int(input("Enter a number: "))
checkpalindrome(No)

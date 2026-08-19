# A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.



Comments = input("Enter the comments: ")

if("Make a lot of money" in Comments or "buy now" in Comments or "Subscribe this" in  Comments or "Click this" in Comments ):
    print("Spam detected")

else:
    print("Normal Comment")
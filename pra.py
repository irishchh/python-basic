text = input("Enter the text\n")

if ("Make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("Click this" in text):
    spam = True
elif("Subscribe this" in text):
    spam = True
elif("make money today for free" in text):
    spam = True
else:
    spam = False

if (spam):
    print("this text is spam")
else:
    print("this is not a spam")
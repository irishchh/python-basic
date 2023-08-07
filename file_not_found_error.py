# try is a function to handle the error in case of program crasses

file_name= 'pythons'

try:
    with open(file_name,"r")as f:
        content = f.read()
        
except FileNotFoundError:
    msg = "file not foung" + file_name + "doesn't exist"
    print(msg)

num = 1.23326362638
print("%.5f" %num)
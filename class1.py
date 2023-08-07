class Mobile:# first letter if mobile or other words must be capital in class
    def __init__(self, name, color):# self is needed in class function to run the program
        self.name = name
        self.color = color

    def receive_message(self):
        print(f"received message using mobile:-\t{self.name}")
    
    def send_message(self):
        print(f"Send message using mobile:-\t{self.name}")

samsung = Mobile("samsung s20 ultra", "white")

xaiomi = Mobile("xaiomi note20", "black")

samsung.send_message()
xaiomi.receive_message()


class Mobile:# first letter if mobile or other words must be capital in class
    def __init__(self):# self is needed in class function to run the program
        self.name = "nokia","samsung"
        self.color = "black","white"

    def receive_message(self):
        print(f"received message using mobile:-\t{self.name}")
    
    def send_message(self):
        print(f"Send message using mobile:-\t{self.name}")

samsung = Mobile()

xaiomi = Mobile()

samsung.send_message()
xaiomi.receive_message()

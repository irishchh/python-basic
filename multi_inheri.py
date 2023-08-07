class Chef:
    def __init__(self,chef_role):
        self.chef_role = chef_role

    def display_info(self):
        print(f"{self.chef_role} is involved in preparing meal")

class Entertainer:
    def __init__(self, entertainer_role):
        self.entertainer_role = entertainer_role

    def display_ent(self):
        print(f"{self.entertainer_role} is involved in doing dances")

class Yatch(Chef, Entertainer):
    def __init__(self, chef_role, entertainer_role):
        Chef.__init__(self, chef_role)# . is use to invoke the 
        Entertainer.__init__(self,entertainer_role)


    def invoke_base_methods(self):
        Chef.display_info(self)
        Entertainer.display_ent(self)

def main():
    y1 = Yatch("chou chef", "Micheal jackson")
    y1.invoke_base_methods()

if __name__=="__main__":
    main()
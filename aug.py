# multiple arg
def cheese_shop(kind,*args,**kwargs):
    print(f"Do you have any {kind}?")
    print("I'm sorry we are out of{kind}")

for arg in "args":
    print(arg)

print("__" *40)

for kw in "kwargs":
    print(kw,":", "kwargs[kw]")

def main():
    cheese_shop("Limburger","its very running,sir",
    "Its really very very running sir",
    shop_keeper = "micheal palin",
    client = "om",
    sketch = "chees shop")

if  __name__ == "__main__":
    main()


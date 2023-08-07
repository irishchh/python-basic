# use of the multiple *args and **kwargs
def chese_shop(kind,*args,**kwargs):
    print(f"Do you have any {kind}?")
    print(f"Im sorry, we're out of all {kind}")

    for arg in args:
        print(arg)
    print("__"40)

    for kw in kwargs:
        print(kw,":",kwargs[kw])

def main():
    chese_shop("burger", "its very popular sir",
    "its very really runny nowdays sir",
    shop_keeper="ishh",
    client="rahul",
    sketch = "chese shop")

    if __name__=="__main__":
        main()

      
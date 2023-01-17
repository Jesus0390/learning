def hi(name = ""):
    return "Hi {}".format(name)

def say_hello(name = "you"):
    return "Hello {}".format(name)

if __name__=="__main__":
    print(hi())
    print(hi("Python"))
    print(say_hello())
    print(say_hello("World"))
"""name=input("Hi buddy, what's your name? ")
print("HELLO", name)
print("Good!" + " Now we have you're name")"""

def main(): 
    name=input("whats your name")
    hello(name) 
    
def hello(to="world"): 
    print ("hello, ", to) 
        
main()
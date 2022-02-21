#Reverse the order of words in a given sentence (an array of characters). Take the “Hello World” string for example
def reverse(x):
    if len(x)!=0:
        y=x[::-1]
        return y
X="hello world"
Y=reverse(X)
print(Y)

#given a dictionary of words and a large input string. You have to find out whether the input string is present in the dictionary
#1 word inputs
def can_segment_string(s, dictionary):
  if (len(s))!=0:
    if s in dictionary:
      y=1
    else:
      y=0
  return (y==1)
my_dictionary="apple","pie","not","hi"
my_input="apple"
print(can_segment_string(my_input,my_dictionary))

##input> 1 word and incudes spaces
def can_segment_string(s, dictionary):
    quote = s
    clean_quote = quote.strip()
    print(clean_quote)
    s=clean_quote
    for i in range(1, len(s) + 1):
        
        first = s[0:i]
        #print(i,first)
        if first in dictionary:
            second = s[i:]
            print(i,first,second)
            if not second or second in dictionary or can_segment_string(second, dictionary):
                y= True
            else:
                y=False
            return y
  
my_dictionary="apple","pie","not","hi","be","gone","evil","witch","thou","art","not","welcome"
my_input="apple pie is not witch"
print(can_segment_string(my_input,my_dictionary))

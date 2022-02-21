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
        
        first_word = s[0:i]
        #print(i,first)
        if first_word in dictionary:
            second_word = s[i:]
            print(i,first_word,second_word)
            if not second_word or second_word in dictionary or can_segment_string(second_word, dictionary):
                y= "can segment"
            else:
                y= "cannot segment"
            return y
  
my_dictionary="apple","pie","not","hi","be","gone","evil","witch","thou","art","not","welcome"
my_input="apple pie is not witch"
print(can_segment_string(my_input,my_dictionary))

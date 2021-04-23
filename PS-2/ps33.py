# PS-33 WAP to read list of words and return the length of the longest one

def find_longest_word_in_li(li):
    longest_element = ''
    for element in li:
        if len(element) >= len(longest_element):
            longest_element = element
    return longest_element

li = ['Apple','Banana','Orange','Pear','Cherry','Strawberry','Mango']
print(find_longest_word_in_li(li))

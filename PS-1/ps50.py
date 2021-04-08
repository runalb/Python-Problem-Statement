# PS-50 WAP to accept number between 0 to 20 and display in words
# ex- If user enters 8 output should be "Eight"

num_in_words = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty']
c=0
while c!=1:
    num = int(input("Enter no. between 0 to 20: "))
    if num >= 0 and num <= 20:
        c = 1
        print(num_in_words[num])
    else:
        print("Invalid no.")
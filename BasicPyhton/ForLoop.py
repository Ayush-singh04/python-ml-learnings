
# for letter in "India is my country":
    # print(letter)



Names = ['Rohan' , 'Sohan', 'jhonny', 'Rohit', 'Sanju']

for name in Names:
# for name in Names[0] :
    print(name)

# Making exponential function in python

def exponent(Base_num , Power):
    
    result = 1

    for index in range(Power):
        result = result * Base_num
    return result
    

print(exponent(2 , 3))
import random

def compatability(name1, name2):
    letter_sum = 0
    total_sum = 0
    for letter in name1.lower().strip():
        if letter in name2.lower():
            letter_sum += 1
        total_sum += 1
    for letter in name2.lower().strip():
        if letter in name1.lower():
            letter_sum += 1
        total_sum += 1
    
    similarity = (letter_sum / total_sum) * 100
    random_addition = random.randint(0, int(100 - similarity))
    compatability = similarity + random_addition
                
    return compatability


    


def main():
    name1 = input("Enter a name: ")
    name2 = input( "enter another name: ")
    user_compatability = compatability(name1, name2)
    if user_compatability > 50:
        print(f"Your compatability is: {user_compatability:.2f}% Wooooo!")
    else:
        print("Womp Womp")
    
    
main()
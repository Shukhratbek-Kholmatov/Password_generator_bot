import random
upper_letters=list ("ABCDEFGHIJKLMNOPQRSTUVXYZ")
lower_letters=list("abcdefghijklmnopqrstuvxyz")
symbols=list("+-/*!$#?@=<>&")

def generate(password_degree,password_len):
    password=" "
    if password_degree=="easy":
        while len(password)<password_len:
                    random.shuffle(upper_letters)
                    random.shuffle(lower_letters)
                    choice=random.choice(lower_letters)
                    password+=choice
    elif password_degree=="middle":
                    while len(password)<password_len:
                        random.shuffle(upper_letters)
                        random.shuffle(lower_letters)
                        choice1=random.choice(upper_letters)
                        choice2=random.choice(lower_letters)
                        password+=choice1
                        password+=choice2
    elif password_degree=="strong":
                    while len(password)<password_len:
                        random.shuffle(upper_letters)
                        random.shuffle(lower_letters)
                        choice1=random.choice(upper_letters)
                        choice2=random.randint(1,100)
                        choice2=str(choice2)
                        choice3=random.choice(lower_letters)                       
                        choice4=random.choice(symbols)
                        password+=choice1
                        password+=choice2
                        password+=choice3
                        password+=choice4
    return password
        
        
                   
        
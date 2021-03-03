# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("Saved into database.")


username_input = input('Please enter your username: ')
save_into_db(username_input)
birth_year_input = int(input('Please enter your birth year: '))
age = 2020 - birth_year_input
print("You are",age, "years old.")
import random


# generate letters
def generate_password(length):
    letter = "abcdefghijklmnopqrstuvwxyz"
    big_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!££$%^&*()_+@'?/>.<,#~|¬`=-"
    # add everything
    generator = letter + big_letter + numbers + symbols
    # user prompt

    password = " "
    for i in range(length):
        password += random.choice(generator)

    return password


# Implement a password strength meter. You could add a function to calculate the strength of the
# password based on factors such as length, complexity, and uniqueness.
def password_strength(password):
    length_strength = min(len(password) / 20, 1)
    complexity_strength = min(len(set(password)) / 20, 1)
    uniqueness_strength = min(1 / len(password), 0.1)
    # calculate the overall   strength by the average of three:
    overall_strength = 0.4 * length_strength + 0.4 * complexity_strength + 0.2 * uniqueness_strength
    return overall_strength


#
# put policy on repetition and password strength
def password_policy(password):
    min_length = 10
    max_repetitions = 2
    while True:
        if len(password) < min_length:
            print("Password is too short: choose  a length of {}:".format(min_length))
            continue

    # check for repetitions
    for generator in set(password):
        if password.count(generator) >= max_repetitions:
            return False
        break
    return password


# Save password to a file
def save_password(username, password):
    filename = "passwords.txt"
    with open(filename, "a") as file:
        file.write(f"{username}: {password}\n")


# prompt user to tell you length of password
password_length = int(input("choose length of your password: "))

# check for the policy

password = generate_password(password_length)

# Prompt user for their name
username = input("Enter your name: ")

# Save the password to a file
save_password(username, password)

# print the password
print("Your password is: ", password)
print("Your password has been saved to the file.")


# display the strength of the password
strength = password_strength(password)
print("Password strength: {:.2f}/1.00".format(strength))

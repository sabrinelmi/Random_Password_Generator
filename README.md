# **Password Generator and Strength Evaluator**

This is a simple Python script that generates random passwords and evaluates their strength based on various factors such as length, complexity, and uniqueness. The script allows you to generate passwords of a specified length and provides an overall strength score for each password.
How it Works

### **The script consists of the following main functions:**

    generate_password(length): This function generates a random password of the specified length. It combines lowercase letters, uppercase letters, numbers, and symbols to create a diverse set of characters for the password.

    password_strength(password): This function evaluates the strength of a password based on three factors: length, complexity, and uniqueness. It calculates the strength score by taking the average of these factors.

    password_policy(password): This function enforces a policy on password repetition and strength. It checks if the password meets the minimum length requirement and does not contain excessive repetitions of characters.

**## Usage**

    Clone this repository or download the Python script to your local machine.

    Ensure you have Python installed on your system.

    Open a terminal or command prompt and navigate to the directory where the script is located.

    Run the script using the following command:

    shell

    python password_generator.py

    Follow the prompts to specify the length of the password.

    The script will generate a random password and display it on the screen.

    It will also provide an overall strength score for the password, indicating its strength level.

### **Customization**

    You can modify the character sets (letter, big_letter, numbers, and symbols) in the generate_password function to include or exclude specific characters based on your requirements.

    Adjust the min_length and max_repetitions variables in the password_policy function to customize the password policy according to your needs.

### **Contributing**

Contributions to this project are welcome. Feel free to suggest improvements or open issues for any bugs or feature requests.
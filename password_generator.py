import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordGenerator:
    def __init__(self):
        self.letter_length = random.randint(6, 8)
        self.num_length = random.randint(2, 5)
        self.sym_length = random.randint(2, 5)
        self.password = ""
        self.password_list = []

    def generate_password(self):

        pass_letters = [random.choice(letters) for _ in range(self.letter_length)]

        pass_numbers = [random.choice(numbers) for _ in range(self.num_length)]

        pass_symbols = [random.choice(symbols) for _ in range(self.sym_length)]

        self.password_list = pass_letters + pass_numbers + pass_symbols

        random.shuffle(self.password_list)

        return "".join(self.password_list)

import os

class PasswordGenerator:
    def __init__(self, length=12, lower=True, upper=True, digits=False, special=False):
        self.length = length
        self.is_lower = lower
        self.is_upper = upper
        self.is_digits = digits
        self.is_special = special
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digits = "0123456789"
        self.special = "!@#$*()-_[]{}"
    
    def validate(self, passwd):
        valid = True
        if self.is_lower and not any(c in self.lower for c in passwd):
            valid = False
        if self.is_upper and not any(c in self.upper for c in passwd):
            valid = False
        if self.is_digits and not any(c in self.digits for c in passwd):
            valid = False
        if self.is_special and not any(c in self.special for c in passwd):
            valid = False
        return valid

    def get_strength(self, passwd):
        used_chars = ""
        def chartype_in_pass(password, char_type):
            return any(c in char_type for c in password)
        if chartype_in_pass(passwd, self.lower):
            used_chars += self.lower
        if chartype_in_pass(passwd, self.upper):
            used_chars += self.upper
        if chartype_in_pass(passwd, self.digits):
            used_chars += self.digits
        if chartype_in_pass(passwd, self.special):
            used_chars += self.special
        possible_chars = pow(len(used_chars), len(passwd))
        strength = len(str(int(pow(possible_chars, .16))))
        return (self.strength_levels[strength-1], strength) if strength < len(self.strength_levels) else (self.strength_levels[-1], strength)

    def get_random_character(self, char_set):
        return char_set[os.urandom(1)[0] % len(char_set)]

    def useable_characters(self):
        useable_chars = ""
        if self.is_lower:
            useable_chars += self.lower
        if self.is_upper:
            useable_chars += self.upper
        if self.is_digits:
            useable_chars += self.digits
        if self.is_special:
            useable_chars += self.special
        return useable_chars

    def generate(self):
        passwd = ""
        while self.validate(passwd) is False:
            passwd = ''.join(self.get_random_character(self.useable_characters()) for _ in range(self.length))
        return passwd


if __name__ == "__main__":
    gen = PasswordGenerator(length=int(input("Length: ")), lower=True, upper=True, digits=True, special=True)
    password = gen.generate()
    print(password)

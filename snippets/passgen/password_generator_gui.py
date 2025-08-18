import tkinter as tk
from tkinter import ttk
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
        self.strength_levels = [["Very Weak", "#FF0000"], ["Weak", "#BB5500"], ["Moderate", "#FFFF00"], ["Strong", "#88AA00"], ["Very Strong", "#00FF00"], ["Unbreakable", "#000000"]]
    
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

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")

        self.password_label = tk.Label(self.root, text="", fg="black", font=("Arial", 12))
        self.password_label.grid(row=0, column=0, pady=10, sticky="w")

        copy_button = ttk.Button(self.root, text="Copy", command=self.copy_password)
        copy_button.grid(row=0, column=1, padx=5, pady=5)

        self.lower = tk.BooleanVar()
        self.upper = tk.BooleanVar()
        self.digit = tk.BooleanVar()
        self.special = tk.BooleanVar()
        checkbox1 = ttk.Checkbutton(self.root, text=f"Lower", variable=self.lower)
        checkbox1.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=2)
        checkbox2 = ttk.Checkbutton(self.root, text=f"Upper", variable=self.upper)
        checkbox2.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=2)
        checkbox3 = ttk.Checkbutton(self.root, text=f"Digits", variable=self.digit)
        checkbox3.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=2)
        checkbox4 = ttk.Checkbutton(self.root, text=f"Special", variable=self.special)
        checkbox4.grid(row=4, column=0, columnspan=2, sticky="w", padx=5, pady=2)

        self.length = tk.IntVar(value=8)
        self.slider = ttk.Scale(self.root, from_=4, to=24, orient="horizontal",
                                variable=self.length, command=self.update_slider_label)
        self.slider.grid(row=5, column=0, padx=5, pady=10, sticky="ew")

        self.slider_value_label = tk.Label(self.root, text="8")
        self.slider_value_label.grid(row=5, column=1, padx=5, pady=10)

        button = ttk.Button(self.root, text="Generate", command=self.generate)
        button.grid(row=6, column=0, columnspan=2, pady=10)

        self.strength_label = tk.Label(self.root, text="Strength", fg="black", font=("Arial", 12))
        self.strength_label.grid(row=7, column=0, columnspan=2, pady=10)

        self.root.mainloop()

    def generate(self):
        password = PasswordGenerator(length=self.length.get(), lower=self.lower.get(), upper=self.upper.get(), digits=self.digit.get(), special=self.special.get()).generate()
        strength = PasswordGenerator().get_strength(password)

        self.update_label("strength_label", strength[0][0], strength[0][1])
        self.update_label("password_label", password)

    def update_label(self, label_name, text, color="black"):
        label_map = {
            "password_label": self.password_label,
            "strength_label": self.strength_label,
            "slider_value_label": self.slider_value_label
        }
        if label_name in label_map:
            label_map[label_name].config(text=text, fg=color)

    def update_slider_label(self, value):
        self.update_label("slider_value_label", str(int(float(value))))

    def copy_password(self):
        text = self.password_label.cget("text")
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()


if __name__ == "__main__":
    MyApp()

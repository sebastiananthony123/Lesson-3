import random

def generate_password(length=12):

    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_char ="&!@£$%^*_[]+.#"
    extras = "☆►⇪Ω℗♧☻♙✈︎⚀♕⚁⚄✯☈"

    all_characters =  lower_case + upper_case + digits + special_char + extras

    password = random.choices(all_characters, k=length)
    random.shuffle = password
    return ''.join(password)

password = generate_password(12)

print("\nGenerated Pasword:")
print("------------------")
print(password,"\n")
      
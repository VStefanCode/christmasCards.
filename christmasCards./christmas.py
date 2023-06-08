import os

def read_templates(filename):
    with open(filename, 'r') as file:
        return file.read()

def generate_email(template, name):
    return template.replace('NAME', name)

def main():
    template = read_template('template.txt')
    with open('employees.txt', 'r') as file:
        names = file.readlines()

    if not os.path.exists('christmasCards'):
        os.makedirs('christmasCards')

    for name in names:
        name = name.strip()
        email = generate_email(template, name)
        with open(f'christmasCards/card_to_{name}.txt', 'w') as email_file:
            email_file.write(email)

        print(f'Card for {name} has been saved in christmasCards/card_to_{name}.txt')

if __name__ == "__main__":
    main()

#### Requirement: pip install cryptography
import json
import os
from feynman import *
import click
from cryptography.fernet import Fernet
from sympy.parsing.sympy_parser import parse_expr


def generate_new_key(saveto_filename):
    key = Fernet.generate_key()

    # string the key in a file
    with open(saveto_filename, 'wb') as filekey:
        filekey.write(key)


def encrypt_equation(equation, output_eq_file, key_filename):
    """
    {eq_name: "", n_vars: , eq_expression: {}}
    """
    # opening the key
    with open(key_filename, 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)
    # encrypting the Sympy Equation
    encrypted = fernet.encrypt(equation)
    with open(output_eq_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrpt_equation(eq_file, key_filename):
    with open(key_filename, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(eq_file, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)
    one_equation = json.loads(decrypted)
    one_equation['eq_expression'] = parse_expr(one_equation['eq_expression'])
    print("-" * 20)
    for key in one_equation:
        print(key, "\t", one_equation[key])
    print("-" * 20)


@click.command()
@click.option('--private_key_folder', default="./")
@click.option('--key_filename', default="feynman.private.key")
@click.option('--output_folder', default="./")
def main(private_key_folder, key_filename, output_folder):
    if os.path.isfile(os.path.join(private_key_folder, key_filename)):
        generate_new_key(key_filename)

    for eqname in EQUATION_CLASS_DICT:
        one_equation = get_eq_obj(eqname)

        equation = {"eq_name": one_equation._eq_name, "num_vars": one_equation.num_vars,
                    "function_ops": one_equation._function_ops,
                    "eq_expression": str(one_equation.sympy_eq)}
        user_encode_data = json.dumps(equation, indent=2).encode('utf-8')
        output_eq_file = os.path.join(output_folder, eqname + ".encypt")

        encrypt_equation(user_encode_data, output_eq_file, key_filename)

        decrpt_equation(output_eq_file, key_filename)


if __name__ == '__main__':
    main()

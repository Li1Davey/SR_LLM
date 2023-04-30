#### Requirement: pip install cryptography
import json
import os
import click
from cryptography.fernet import Fernet
from sympy.parsing.sympy_parser import parse_expr


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
@click.option('--key_filename', default="private.key")
@click.option('--output_folder', default="./")
def main(private_key_folder, key_filename, output_folder):


    for eqname in EQUATION_CLASS_DICT:
        output_eq_file = os.path.join(output_folder, eqname + ".encypt")

        decrpt_equation(output_eq_file, key_filename)


if __name__ == '__main__':
    main()

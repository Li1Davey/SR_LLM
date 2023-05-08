#### Requirement:
import json
import os
import xxhash
from typing import List, Dict, Set

from cryptography.fernet import Fernet
from sympy.parsing.sympy_parser import parse_expr
from sympy import preorder_traversal


def generate_new_key(saveto_filename):
    key = Fernet.generate_key()

    # string the key in a file
    with open(saveto_filename, 'wb') as filekey:
        filekey.write(key)


def encrypt_equation(equation, output_eq_file, key_filename=None, is_encrypted=0):
    """
    {eq_name: "", n_vars: , eq_expression: {}}
    """
    if is_encrypted == 1:
        # opening the key
        with open(key_filename, 'rb') as filekey:
            key = filekey.read()

        # using the generated key
        fernet = Fernet(key)
        # encrypting the Sympy Equation
        encrypted = fernet.encrypt(equation)
        with open(output_eq_file, 'wb') as encrypted_file:
            encrypted_file.write(b'1\n')
            encrypted_file.write(encrypted)
    else:
        with open(output_eq_file, 'wb') as encrypted_file:
            encrypted_file.write(b'0\n')
            encrypted_file.write(equation)


# def symbolic_equation_into_preorder_traversal(expr)-> List:
#     for arg in preorder_traversal(expr):
#         print(arg)
#     return []


def decrypt_equation(eq_file, key_filename=None):
    with open(eq_file, 'rb') as enc_file:
        encrypted = enc_file.readline()
        if encrypted == b'1\n':
            encrypted = enc_file.readline()
            fernet = Fernet(open(key_filename, 'rb').read())
            decrypted = fernet.decrypt(encrypted)
        elif encrypted == b'0\n':
            decrypted = enc_file.readline()
    one_equation = json.loads(decrypted)
    one_equation['eq_expression'] = parse_expr(one_equation['eq_expression'])
    print("-" * 20)
    for key in one_equation:
        print(key, "\t", one_equation[key])
    print("-" * 20)
    return one_equation


def main(private_key_folder='./', key_filename="private.key", output_folder="./"):
    if not os.path.isfile(os.path.join(private_key_folder, key_filename)):
        print('A new key is generated!')
        generate_new_key(key_filename)

    for eqname in EQUATION_CLASS_DICT:
        one_equation = get_eq_obj(eqname)

        equation = {"eq_name": one_equation._eq_name,
                    "num_vars": one_equation.num_vars,
                    "function_set": one_equation._function_set,
                    "eq_expression": str(one_equation.sympy_eq_preorder_traversal)}
        print(equation)
        user_encode_data = json.dumps(equation).encode('utf-8')
        print(user_encode_data)
        # exit()
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)
        hashed_name = xxhash.xxh128(eqname, seed=42).intdigest()
        print(hashed_name)
        output_eq_file = os.path.join(output_folder, str(hashed_name) + ".encypt.in")

        encrypt_equation(user_encode_data, output_eq_file, key_filename, is_encrypted=1)
        decrypt_equation(output_eq_file, key_filename)
        output_eq_file = os.path.join(output_folder, str(hashed_name) + ".unencypt.in")

        encrypt_equation(user_encode_data, output_eq_file, is_encrypted=0)

        decrypt_equation(output_eq_file)


if __name__ == '__main__':
    # from equations_srsd_benchmark import *
    #
    # main(output_folder='./equations_srsd_benchmark')
    # from equations_DSOs import *
    #
    # main(output_folder='./equations_DSOs')

    from equations_trigometric import *

    main(output_folder='./equations_trigometric')

#

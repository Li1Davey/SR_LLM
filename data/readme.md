# Data Expression Input File Format

The input expression file are of two types: un-encrypted file and encrypted file. See below for details.

## Un-encrypted file format


### Example
```txt
'{  "eq_name": "sample_equation",  "num_vars": 2,  "function_set": [  "sqrt",    "add",    "sub",    "mul",    "div",    "inv",    "sin",    "cos",    "const"  ],  "eq_expression": "[('+','binary'), ('*', 'binary'), ('0.1', 'const'), ('X1', 'var'), ('sin', 'unary'), ('X2', 'var')]"\n}'
```
The second line represents a dictinary:
```python
{
    'num_vars': 2, 
    'function_set': ['sqrt', 'add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const'], 
    'eq_expression': [('+','binary'), ('*', 'binary'), ('0.1', 'const'), ('X1', 'var'), ('sin', 'unary'), ('X2', 'var')]
}
```
- `num_vars`: number of varaibles in the symbolic expression.
- `function_set`: it represent the set of mathemetical operators. The symbolic expression will use subset of the operators.
- `eq_expression`: The defintion can be found at [expression defintion](/file-formats/expression-format/).

## Encrypted File Format


### Example
```txt
1
gAAAAABkTgSd8j6HB8Od-AXaD44-RgVbuxmIKZuSWpAvfcYYWOTkpUrMFuXxhtXjAHRlIrqRk0bjOfAHT-CdkfkyZzOPX17ky5uY0px-IIhlmAdIV8VXfOy-kiwvyxM7mqwRspxwHoIGOFY0g9cr-HF9-Ogmo0Z9hXipHdxDZYGdTUvkUVM-rDflVlJjTEH5Wgj6oL_yR4Vf5K_ZXwJJAfsaPFQEndESQw6MATjzJh7w9ChCDoDOhpPlyNZQTk2zfTlYtDJ4-KC2ghS_r2k1G1Rv44fNkRY4z4QVbc3qT1Av-qpMLqMOL8RVdwgEfGvXAswqJ2Pqk-nIn0fLomfRMOBNSYAJnHoIwA==
```
The second line represents the same dictionary as the above one, but a crypto function is adopted.

## Note

The above format definition is illustated for the user and is handled by our proposed [data protocel](/data-query-protocol/). The user does not need to worries about this format.
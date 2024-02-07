# Data Expression Input File Format



## File format


### Example

The second line is a json formated expression:
```python
{
    'num_vars': 2, 
    'function_set': ['sqrt', 'add', 'sub', 'mul', 'div', 'inv', 'sin', 'cos', 'const'], 
    'eq_expression': [('+','binary'), ('*', 'binary'), ('0.1', 'const'), ('X1', 'var'), ('sin', 'unary'), ('X2', 'var')]
}
```
- `num_vars`: number of variables in the symbolic expression.
- `function_set`: it represent the set of mathematical operators. The symbolic expression will use subset of the operators.
- `eq_expression`: The preorder traversal of the expression.





## Note

The above format definition is illustrated for the user and is handled by our proposed [data protocel](/data-query-protocol/). The user does not need to worries about this format.
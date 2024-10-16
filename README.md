# MyPasswordPackage

A secure password hashing package using PyNaCl.

## Installation

Install the package using pip:

```bash
pip install hash_maker
```

## Usage

Import the package and use the `hash_password` and `verify_password` functions:

```python
from hash_maker import hash_password, verify_password

password = 'my_password'
hashed_password = hash_password(password)

if verify_password(hashed_password, password):
    print('Password is correct!')
else:
    print('Password is incorrect.')
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Thanks to [PyNaCl](https://github.com/pyca/pynacl) for providing a secure password hashing library.   

## Contact

If you have any questions or suggestions, please feel free to contact me at [mariswarycharan@gmail.com](mailto:mariswarycharan@gmail.com).  

## Disclaimer

This project is not affiliated with or endorsed by PyNaCl or any of its contributors. It is a personal project and is not intended for commercial use. Use at your own risk.    

## References

1. [PyNaCl Documentation](https://pynacl.readthedocs.io/en/stable/)
2. [PyNaCl GitHub Repository](https://github.com/pyca/pynacl)
3. [PyNaCl PyPI Package](https://pypi.org/project/pynacl/)          

## Author

**Charan A A**

- [GitHub](https://github.com/mariswarycharan/)
- [LinkedIn](https://www.linkedin.com/in/charanaa/)
 



# test_print.py

def test_print():
    output = capture_console_output(main)
    expected_output = """Hello, world!
The value of x is: 10 and the value of y is: 20
My name is Alice and I am 30 years old.
The sum of 5 and 7 is 12
Hello world!
This is on the same line.
apple, banana, cherry
Binary: 0b101010
Octal: 0o52
Hexadecimal: 0x2a
Value of pi (rounded to 2 decimal places): 3.14
Numbers from 1 to 5:
1
2
3
4
5
Fruits: ['apple', 'banana', 'cherry']
Person details: {'name': 'John', 'age': 30, 'city': 'New York'}
My name is Bob and I am 25 years old.
HaHaHaHaHa"""
    assert output.strip() == expected_output.strip(), "Output doesn't match expected output"

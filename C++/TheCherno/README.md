# The Cherno

## Variables

- `char` 1 byte of data.
- `bool` 1 byte of data.
- `short` 2 bytes of data.
- `int` 4 bytes of data.
- `long` 4 bytes of data depending of the compiler.
    - How to use it?
            
            float variable = 5.5f;
            
- `long long` 8 bytes of data.
- `double` 8 bytes of data.

You also can use `unsigned`

### How to know the size of the data type?

Use `sizeof({dataType})`:

    sizeof(int) // Returns 4
    sizeof(bool) // Returns 1

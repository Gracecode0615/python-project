# examples of built-in-function
# sum(iterable[, start]
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # total will be 15 (1 + 2 + 3 + 4 + 5)

# print()
myName = "Habeeb"
print(myName)

# help([object])
help(print)  # Displays documentation about the print function

# range([start], stop[, step])
# range([start], stop[, step])
numbers = list(range(1, 6))  # numbers will be [1, 2, 3, 4, 5]

# int([x])
numbers = list(range(1, 6))  # numbers will be [1, 2, 3, 4, 5]

# float([x])

num = float("3.14")  # num will be 3.14

str([object])
s = str(42)  # s will be "42"



    # - `len(iterable)`: Returns the number of items in an iterable.
    My_list = [1, 2, 3, 4, 5]
    print(len(my_list))  # Output: 5
   

    # - `max(iterable)`: Returns the maximum value in an iterable.
    
    My_list = [10, 20, 30, 40, 50]
    print(max(my_list))  # Output: 50
    

    # - `min(iterable)`: Returns the minimum value in an iterable.

        my_list = [10, 20, 30, 40, 50]
        print(min(my_list))  # Output: 10
        

    # - `abs(x)`: Returns the absolute value of a number `x`.
        num = -10
        print(abs(num))  # Output: 10
     

    # - `sorted(iterable, key=None, reverse=False)`: Returns a new sorted list from the elements of the iterable.
   
        my_list = [3, 1, 4, 1, 5, 9, 2]
        sorted_list = sorted(my_list)
        print(sorted_list)  # Output: [1, 1, 2, 3, 4, 5, 9]
     

    # - `enumerate(iterable, start=0)`: Returns an iterator that yields tuples containing a count and the values from the iterable.
    #     ```python
        my_list = ['apple', 'banana', 'cherry']
        for index, value in enumerate(my_list):
            print(index, value)
        # Output:
        # 0 apple
        # 1 banana
        # 2 cherry
      

    # - `any(iterable)`: Returns `True` if any element in the iterable is `True`, otherwise `False`.
       
        my_list = [False, False, True, False]
        print(any(my_list))  # Output: True
     

    # - `all(iterable)`: Returns `True` if all elements in the iterable are `True`, otherwise `False`.
      
        my_list = [True, True, True, True]
        print(all(my_list))  # Output: True
     

    # - `filter(function, iterable)`: Constructs an iterator from elements of the iterable for which the function returns `True`.
      
        def is_positive(x):
            return x > 0

        numbers = [-1, 2, -3, 4, -5]
        positive_numbers = list(filter(is_positive, numbers))
        print(positive_numbers)  # Output: [2, 4]

    # - `map(function, iterable, ...)`: Applies the function to all elements of the iterable and returns an iterator of the results.
        def square(x):
            return x * x

        numbers = [1, 2, 3, 4, 5]
        squared_numbers = list(map(square, numbers))
        print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
  

# 2. **Functions Related to Functions:**

    # - `lambda arguments: expression`: Creates an anonymous function.
         
         add = lambda x, y: x + y
        print(add(3, 5))  # Output: 8

    # - `def`: Keyword used to define user-defined functions in Python.
        
        def greet(name):
            print("Hello, " + name)

        greet("Alice")  # Output: Hello, Alice
     

    # - `return`: Statement used inside a function to exit the function and optionally return a value.
      def square(x):
            return x * x

        result = square(4)
        print(result)  # Output: 16
 

    # - `global`: Keyword used inside a function to declare a variable as global.
    #     ```python
        x = 10

        def func():
            global x
            x += 5
            print(x)

        func()  # Output: 15
        ```

    # - `nonlocal`: Keyword used inside a nested function to indicate that a variable is not local to the innermost function.
    #     ```python
        def outer():
            x = 10
            def inner():
                nonlocal x
                x += 5
                print(x)
            inner()

        outer()  # Output: 15
        ```

These examples demonstrate the usage of various built-in functions and functions related to functions in Python.
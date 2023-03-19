"""
Global variables confusion

    def outer():
        x = 10
        print(x) #first print
        
        def inner():
            global x 
            x = 20
            print(x) #second print
    
        inner()
    outer()
    print(x) #third print

Expected output:

    10
    10
    20

Actual output:

    10
    20
    20

Thought process:

`global x` says to assign the `x` variable defined in `inner()` to the global scope. `x = 20` is thus defined in the global scope.  When we do `print(x)` in `inner()`,  x is looked for in the local scope, which does not exist. Then, Python searches the nonlocal scope, and finds `x = 10` in `outer()`. Therefore, the second print statement should output `x = 10`. Why is `inner()` printing `x = 20`, when the variable is only defined in the global scope, which is 1 level above the nonlocal one?

&#x200B;

For example, this code 

    x = 20
    
    def outer():
        x = 10
        print(x) #first print
        
        def inner():
            print(x) 
    
        inner()
    
    outer()
    print(x) #third print
    
    

would obviously output

    >> 10
    >> 10
    >> 20 

not 

    >> 10
    >> 20
    >> 20

for the same reasons given in my thought process section.
"""
print(f"x in module globals(): {'x' in globals()}")
print(f"x in module locals(): {'x' in locals()}")
print("define x = 20")
x = 20
print(f"x in module globals(): {'x' in globals()}")
print(f"x in module locals(): {'x' in locals()}")

def outer():
    print(f"x in outer globals(): {'x' in globals()}")
    print(f"x in outer locals(): {'x' in locals()}")
    print("define x = 10")
    x = 10
    print(f"x in outer globals(): {'x' in globals()}")
    print(f"x in outer locals(): {'x' in locals()}")
    print(x) #first print

    def inner():
        print(f"x in inner globals(): {'x' in globals()}")
        print(f"x in inner locals(): {'x' in locals()}")
        #global x 
        x = 30
        print(x)

    inner()

outer()
print(x) #third print



"""
Page up
x in module globals(): False
x in module locals(): False
define x = 20
x in module globals(): True
x in module locals(): True
x in outer globals(): True
x in outer locals(): False
define x = 10
x in outer globals(): True
x in outer locals(): True
10
x in inner globals(): True
x in inner locals(): False
30
30
"""

"""
Page up
x in module globals(): False
x in module locals(): False
define x = 20
x in module globals(): True
x in module locals(): True
x in outer globals(): True
x in outer locals(): False
define x = 10
x in outer globals(): True
x in outer locals(): True
10
x in inner globals(): True
x in inner locals(): False
30
20
"""
# general-utils
A selection of general utilities created while learning python and selenium.

## temp_conversion.py
This util prompts the user for a temperature and degrees in either C, F, or K then converts it into the other two degrees.
The input is checked for the first instance of the letters C, F, or K to determine the temperature scale entered. This means if the user enters "-10 CelFerKel" or "-10 abc", the util will interpret the input as -10 Celsius. Conversely, "-10 FKC" would be interpreted as -10 Fahrenheit.
### Example
> Enter the temperature and degrees you want to convert from (e.g., -10 C or 14 F or 263.15 K): -10 C  
> -10.0 Celsius (C) is 14.0 Fahrenheit (F) and 263.2 Kelvin (K)

## calculator-cli.py
This basic calculator prompts the user for a simple operator (+, -, *, /) followed by two numbers. The util is designed to support including more operators by adding them to the ops dictionary.
### Example
> Simple Calculator CLI  
> Available operations:  
> \+  -> add  
> \-  -> sub  
> \*  -> mul  
> \/  -> truediv  
> Type 'q' or 'quit' to exit.  
>   
> Enter operation: +  
> Enter first number: 2  
> Enter second number: 3  
> Result: 2.0 + 3.0 = 5.0

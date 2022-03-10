def convert_temp(unit_in, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    if unit_in == 'c':
      return (temp * 9/5) + 32

    if unit_in == 'f':
      return (temp - 32) * 5/9

    if unit_in != 'c' or 'f':
      return f'invalid unit {unit_in}'


print("c", "f", 0, convert_temp("c", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", 32), "should be Invalid unit z")

#you don't need to specify unit out if you're not including kelvin as a possible output. that just wastes code. 


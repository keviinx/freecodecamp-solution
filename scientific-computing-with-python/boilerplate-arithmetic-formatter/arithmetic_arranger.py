def arithmetic_arranger(lists, answer = False):

  # variables
  top_string = ""
  bottom_string = ""
  dashes_string = ""
  answer_string = ""

  # Print error if too many problems
  if len(lists) > 5:
    return("Error: Too many problems.")

  # go through the list individually
  for list in lists:
    first_number, operator, second_number = list.split()

    # check if number is more than 4 digits
    if len(first_number) > 4 or len(second_number) > 4:
      return("Error: Numbers cannot be more than four digits.")

    # return error if is not numeric
    if first_number.isnumeric() != True or second_number.isnumeric() != True:
      return("Error: Numbers must only contain digits.")

    # check if operator is other than + or -
    if operator == "+":
      sum =str(int(first_number) + int(second_number))
    elif operator == "-":
      sum = str(int(first_number) - int(second_number))
    else:
      # return error if operator other than + or - is used
      return("Error: Operator must be '+' or '-'.")
    
    # check to see whether the last formula to determine the trailing spaces
    if list == lists[-1]:
      trailing_spaces =""
    else:
      trailing_spaces = "    "

    # the longest with is the maximum between the 2 numbers + 2 spaces
    longest_width = 2 + max(len(first_number), len(second_number))

    # arrange the printing in lines
    top_string += first_number.rjust(longest_width) + trailing_spaces
    bottom_string += operator + second_number.rjust(longest_width - 1) + trailing_spaces
    dashes_string += "".rjust(longest_width, "-") + trailing_spaces
    answer_string += sum.rjust(longest_width) + trailing_spaces

  # determine how to print the output based on the argument given
  if answer:
    return(top_string + "\n" + bottom_string + "\n" + dashes_string + "\n" + answer_string)
  else:
    return(top_string + "\n" + bottom_string + "\n" + dashes_string)

"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():

    question_list = ["num"]

    while question_list[0] != "q":

        question = raw_input("> ")
# TO DO
# question != "q" enables ability to quit, but removes ability to do math
# removing question != "q" stops text from being entered but results in user can't quit
        if question.isdigit() == False and question != "q":
            print "That's dumb."
            continue

        question_list = question.split()
        question_list.extend([0, 0])
    
        first = int(question_list[1])
        second = int(question_list[2])

        if question_list[0] == "+":
            print arithmetic.add(first, second)

        if question_list[0] == "-":
            print arithmetic.subtract(first, second)

        if question_list[0] == "*":
            print arithmetic.multiply(first, second)

        if question_list[0] == "/":
            print arithmetic.divide(first, second)

        if question_list[0] == "**2" or question_list[0] == "square":
            print arithmetic.square(first)    

        if question_list[0] == "**3" or question_list[0] == "cube":
            print arithmetic.cube(first)

        if question_list[0] == "pow":
            print arithmetic.power(first, second)

        if question_list[0] == "%" or question_list[0] == "mod":
            print arithmetic.mod(first, second)

if __name__ == '__main__':
    main()
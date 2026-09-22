# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"

    # the following lines of code indicate the math needed to turn seconds into hours, minutes, and seconds

    hours = total_seconds // 3600
    remaining_seconds = total_seconds%3600
    minutes = remaining_seconds //60
    seconds = remaining_seconds % 60

    return f"{hours}:{minutes:02d}:{seconds:02d}"
    


def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age

    if (age<5):
        return 0.0
    elif (age<=12):
        return 8.0
    elif (age<=64):
        return 15.0
    else:
        return 10.0
    


def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    #sum_multiples(10)
    total =0 #needed for for loop 

    for n in range (limit):
        if n % 3==0 or n % 5 ==0:
            total+=n

    return total


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    #total_of_positives([1,2,3,5,6,7,9])

    # same idea as sum_multiples function but checks if number is greater than 0 (a positive number)

    total =0

    for number in numbers: 
        if number >0:
            total += number 

    return total


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(3661))            # 1:01:01
    print (admission_price(10))            # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4
    return 


if __name__ == "__main__":
    print(admission_price(10))    
    print("hello")
    main()


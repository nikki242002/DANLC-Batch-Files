#Q3.Python program to display all numbers within a range except the prime numbers.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_numbers(start, end, current):
    if current > end:
        return
    if not is_prime(current):
        print(current, end=" ")
    display_numbers(start, end, current + 1)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
display_numbers(start, end, start)

def solution(number):
    total = 0
    for num in range(0, number):
       if num % 3 == 0 or num % 5 == 0:
           total += num
    return total

#Another way write this is

def new_solution(number):
    return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)

print(new_solution(10))
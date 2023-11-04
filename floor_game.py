#this game is about the players choosing  the mode of reaching a certian floor wiht the available possibilities
print("the score will be based on the floor you choose",end = "\n\n")
print("if the user chooses 1 that is the elevator the score will be the increased with a even number and the next time the user choose this path the score increases with the next even number ",end = '\n \n')
print("if the user chooses 2 that is the escalator then the score will increase with the odd numebrs and the nexr time the iser chooses this path the score will be increased with the nenxt odd number", end= '\n \n')
print("if the user chooses 3 that is 'walk' then the score will increase with the prime numbers and the next time the user chooses this path the score will be increased with the next prime number", end = '\n \n')

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

m = 2
j = 1
k = 2
score = 0
floor = int(input("Enter the number of floors: "))

for i in range(floor):
    choice = int(input("Enter the facility (1 for elevator, 2 for escalator, 3 for walk): "))
    
    if choice == 1:
        # Elevator (1): Score increments to the next even number
        score += m if m % 2 == 0 else m +1
        m += 2
    elif choice == 2:
        # Escalator (2): Score increments to the next odd number
        score += j if j % 2 != 0 else j
        j += 2
    elif choice == 3:
        # Walk (3): Score increments to the next prime number
        while not is_prime(k):
            k += 1
        score += k
        k += 1
    else:
        print("Invalid choice")
    
    print("Current score:", score, end = '\n')

print("Total score:", score)


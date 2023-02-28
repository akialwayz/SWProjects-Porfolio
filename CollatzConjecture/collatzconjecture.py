def collatz(count,number,lists):
    if number == 1:
        lists.append(number)
        return count,lists
    elif number == 4:
        count += 2
        lists.extend([4,2,1])
        return count, lists
    elif number == 2:
        count += 1
        lists.extend([2,1])
        return count,lists
    elif number % 2 == 0:
        lists.append(number)
        number = number // 2
        count += 1
        return collatz(count,number,lists)
    elif number % 2 == 1:
        lists.append(number)
        number = 3 * number + 1
        count += 1
        return collatz(count,number,lists)

def main():
    count = 0
    lists = []
    print("This Program is to find the Collatz Conjecture")
    print("\n Please enter a positive integer above:")
    number = int(input())
    while number != 1 or number != 0:
        lists = []
        count, lists=collatz(count,number,lists)
        print(f"The number of steps to reach {number} is: ", count)
        print(f"The path taken by the {number} is: ", lists)
        break
    print("Do you wish to continue? (Y/N)")
    answer = input()
    if answer == "Y" or answer == "y":
        main()
    else:
        print("Goodbye")
        exit()

if __name__ == "__main__":
    main()
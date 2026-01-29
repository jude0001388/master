def summarise_numbers(numbers_list):
    total = sum(numbers_list)
    count = len(numbers_list)
    average = total/count
    count if count > 0 else 0
    return (total, count, average)

def main():
    numbers_list = []
    while True:
        num = int(input("Enter a the next number: "))
        if num == 0:
            break
        numbers_list.append(num)
    total, count, average = summarise_numbers(numbers_list)
    print("The average is", average)
    print("The total is", total)
    print("The count is", count)

main()
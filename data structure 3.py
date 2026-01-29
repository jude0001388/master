def summarise(numbers_list):
    total = sum(numbers_list)
    count = len(numbers_list)
    average = total/count
    return (total, count, average)

numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12]
print(summarise(numbers_list))
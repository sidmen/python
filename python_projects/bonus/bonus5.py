waiting_list = ['sidharth', 'revathy', 'vihaan']
waiting_list.sort()               # to sort in ascending order
# waiting_list.sort(reverse=True) # to sort in descending order

for index, item in enumerate(waiting_list):
    row = f"{index + 1}-{item.capitalize()}"
    print(row)


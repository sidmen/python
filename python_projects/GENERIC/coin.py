# while True:
#     user_input = input("Throw the coin and enter head or tail here: ")
#     filename = 'files/coin_input.txt'
#     match user_input:
#         case 'head' | 'tail':
#             with open(filename, 'r') as file:
#                 file_contents = file.readlines()
#             with open(filename, 'w') as file:
#                 file.writelines(file_contents)
#                 file.write(f"{user_input}\n")
#             with open(filename, 'r') as file:
#                 file_contents = file.readlines()
#                 file_contents = [file_content.strip('\n') for file_content in file_contents]
#             head_count = file_contents.count('head')
#             total_count = len(file_contents)
#             head_percent = float(100*head_count/total_count)
#             print(f"Heads: {head_percent}%")
#         case 'exit':
#             break

##############
while True:

    user_input = input("Throw the coin and enter head or tail here: ")
    filename = '../files/coin_input.txt'

    match user_input:
        case 'head' | 'tail':
            with open(filename, 'r') as file:
                file_contents = file.readlines()

            file_contents.append(f"{user_input}\n")

            with open(filename, 'w') as file:
                file.writelines(file_contents)

            file_contents = [file_content.strip('\n') for file_content in file_contents]

            head_count = file_contents.count('head')
            total_count = len(file_contents)
            head_percent = float(100*head_count/total_count)

            print(f"Heads: {head_percent}%")

        case 'exit':
            break

################


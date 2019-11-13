import datetime
print(datetime.datetime.now().date())

def go_back_to_menu():
    option = ""
    while (option != "q"):
        entry = input("Please press q to go back to menu: ")
        option = entry
    start_page()

def about_page():
    print(
        "Cryptor encrypts and decrypt a file that used Cryptor encryption. The program is created fully in python. People who might use this range from the illuminati, president of the United States and people like you. This code for cryptor is fully open source and you can modify it to better suit your needs. Hope you find Cryptor helpful!. "
    )
    go_back_to_menu()

def find_file():
    file = ""
    while True:
        try:
            file_name = open(input("Please enter a filename or path = "), "r")
            file = file_name
            return file
            break
        except:
            print("File not found please try again")


def encryption_key():
    file = ''
    while True:
        try:
            encryption_key = float(
                input("ENTER ANY FLOAT NUMBER TO BE USED AS KEY: "))
            file = encryption_key
            break
        except ValueError:
            print("invalid input, please make a number selection")
    return file


# alphabet list
alfa = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','\n','.','0','1','2','3','4','5','6','7','8','9','!',',','|','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encryptor():
    print("==================================")
    print("Encrypt a text file")
    print("------------------------")
    crypted_list = []
    crypted_string = ""
    file = find_file()
    key = encryption_key()
    for line in file:
        for i in line:
            index = alfa.index(i)
            cryptconvert = (index / 3)**0.25 + 5
            crypted_list.append(cryptconvert)
    number = key
    for i in range(len(crypted_list)):
        final_addition = crypted_list[i] + i**number
        crypted_string = crypted_string + str(final_addition) + " "
    time = datetime.datetime.now()
    new_encrypted_file = open(file.name + "_encrypted_" + str(time), "a")
    new_encrypted_file.write(crypted_string)
    print("Encrypted text file" + new_encrypted_file.name +
          " has been created")
    new_encrypted_file.close()
    go_back_to_menu()



def decryptor():
    print("==================================")
    print("Decrypt a text file")
    print("------------------------")
    decrypted_string = ""
    decrypted_list = []
    file = find_file()
    key = encryption_key()
    crypted_message = file.readline().split()  #Find a simpler way
    index = 0
    for num in crypted_message:
      step_1_decryption = float(num) - index**key
      decrypted_list.append(step_1_decryption)
      index += 1
    for num in decrypted_list:
      step_2_decryption = round(((num - 5)**4)*3)
      decrypted_string = decrypted_string + alfa[step_2_decryption]
    print(decrypted_string)
    time = datetime.datetime.now()
    new_decrypted_file = open(file.name + "_decrypted_" + str(time), "a")
    new_decrypted_file.write(decrypted_string)
    print("Decrypted text file" + new_decrypted_file.name +
          " has been created")
    new_decrypted_file.close()
    go_back_to_menu()


def start_page():
    print("==================================")
    print("Welcome to cryptor 1.0")
    print("A python based text file encryptor")
    print("================================== ")
    print("\n MENU")
    print("-------")
    print("1. About")
    print("2. Encrypt a text file")
    print("3. Decrypt a file")
    print("----------------------------------")
    while True:
        try:
            entry = int(
                input(
                    "Please enter a number corresponding to menu selection: "))
            if (entry <= 3):
              break
            else:
              print("Invalid option, please make a valid selection")
        except ValueError:
            print("invalid input, please make a number selection")
    if (entry == 3):
        decryptor()
    if (entry == 1):
        about_page()
    if (entry == 2):
        encryptor()


start_page()

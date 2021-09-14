from simple_scrapping import habr_simple_scrapping
from full_scrapping import habr_full_scrapping

if __name__ == '__main__':
    print("'1' для основной части задания.\n'2' для необязательной части задания")
    my_input = input("Ваш выбор: ")
    if my_input == '1':
        habr_simple_scrapping()
    if my_input == '2':
        habr_full_scrapping()

import sys
import random
import time

#   ZMIENNE GLOBALNE OKREŚLAJĄCE WYMAGANIA DOTYCZĄCE LOSOWANIA ORAZ STAŁE WYKORZYSTYWANE W PROGRAMIE

LIST_SIZE = 6  # Ilość losowanych liczb
MAX_NUM = 49  # Maksymalna losowana liczba
MIN_NUM = 1  # Minimalna losowana liczba
ALLOTMENT = 40 * '-'  # Podział wiersza ---------------------


#  Funkcja welcome() nie przyjmująca argumentów. Pojawiająca się na samym początku programu, opisująca
#  zasady wprowadzania danych.

def welcome():
    print(ALLOTMENT)
    print("---------------          ---------------")
    print("------------                ------------")
    print("----------     LOSOWANIE      ----------")
    print("----------       LOTTO        ----------")
    print("------------                ------------")
    print("---------------          ---------------")
    print(ALLOTMENT)
    print('WCIŚNIJ PRZYCISK ENTER ABY PRZEJŚĆ DALEJ', end='')
    input()

    print(ALLOTMENT)
    print("1. WYBIERZ", LIST_SIZE, " LICZB, Z PRZEDZIAŁU", MIN_NUM, 'DO', MAX_NUM)
    print("2. WYBRANE LICZBY NIE MOGĄ SIĘ POWTARZAĆ")
    print("                                        ")
    print("    KOMPUTER WYLOSUJE SWOJE LICZBY I    ")
    print("        SPRAWDZIMY CZY WYGRAŁEŚ   ")
    print("              POWODZENIA   \n")
    print('WCIŚNIJ PRZYCISK ENTER ABY PRZEJŚĆ DALEJ')


#   Funkcja congrat(num) przyjmuje argument w postaci liczby. Wyświetla się wyłącznie w przypadku trafienia wszyskich
#   liczb wylosowanych przez komputer. Wyświetlenie uzależnione jest również od zmiennej globalnej LIST_SIZE.

def congrat(num):
    print("---------------          ---------------")
    print("------------   GRATULACJE   ------------")
    print("----------      TRAFIŁEŚ      ----------")
    print("----------        ", num, "         ----------")
    print("------------                ------------")
    print("---------------          ---------------")


#   Funkcja make_int(nums_str) przyjmuje argumenty w postaci listy z ciągiem znaków string,
#   obcina białe znaki przed i po wprowadzonej wartości, następnie każdy z elementów String w liście strs_list,
#   zmienia na Integer i dodaje do nowej listy o nazwie int_nums_list, którą zwraca po zakończeniu pętli

def make_int(nums_str):
    strs_list = nums_str.split()
    int_nums_list = []
    for str_num in strs_list:
        int_nums_list.append(int(str_num))
    return int_nums_list


#   Funkcja check_size(nums_list) pobiera argumenty w postaci listy liczb. Sprawdza wiekość listy. Jeżeli ilość
#   liczb w liście jest nieprawidłowa ze zmienną globalną zwraca wartość False. Jeżeli ilość elementów listy
#   jest prawidłowa zwraca wartość True

def check_size(nums_list):
    if len(nums_list) > LIST_SIZE:
        print(ALLOTMENT)
        print('Wprowadzono za dużą ilość liczb')
        print(ALLOTMENT)
        return False
    elif len(nums_list) < LIST_SIZE:
        print(ALLOTMENT)
        print('Wprowadzono zbyt małą ilość liczb')
        print(ALLOTMENT)
        return False
    else:
        return True


#   Funkcja chech_replic(nums_list) pobiera argument listy i sprawdza jej wartości pod względem powtórzeń wysępujących
#   w liście. Funkcja zwraca wartość True w przypadku braku powtórzeń lub wartość False w przypadku występujących
#   powtórzeń w liście.


def check_replic(nums_list):
    #   pobrana lista jest kopiowana do listy uniq_nums, następnie lista uniq_nums zostaje przesortowana

    uniq_nums = nums_list.copy()
    uniq_nums.sort()

    #   w tym miejsu jest wykonywana pętla i sprawdzane są powtórzenia danych w liście uniq_nums
    #   w przypadku wystąpienia powtórzeń liczby te appendowane są do listy rep_nums

    rep_nums = []
    for num, uniq in zip(uniq_nums, uniq_nums[1:]):
        if num == uniq:
            rep_nums.append(num)

    #   jeżeli długość listy rep_nums jest większa niż 0 funkcja zwraca wartość False, w przeciwnym razie True

    if len(rep_nums) > 0:
        return False
    else:
        return True


#   Funkcja show_replic(nums_list) ma podobne zadanie jak funkcja check_replic. Używana jest ona przede
#   wszystkim do wyświetlenia powtarzających się liczb. Funkcja nie zwraca wartości.

def show_replic(nums_list):
    uniq_list = [] + nums_list
    uniq_list.sort()
    rep_nums = []
    for i in range(len(uniq_list) - 1):
        if uniq_list[i] == uniq_list[i + 1]:
            rep_nums.append(uniq_list[i])
    for rep in rep_nums:
        uniq_list.remove(rep)
    if len(rep_nums) != 0:
        print(ALLOTMENT)
        print('Wprowadzone liczby powtarzają się')
        print(ALLOTMENT)
        print('Ilość poprawnie wprowadzonych liczb:', len(uniq_list), '\nLiczby poprawne:', end=' ')
        print(uniq_list)
        print('Ilość liczb powtarzających się to:', len(rep_nums), '\nLiczby do poprawy: ', end=' ')
        print(rep_nums)
        print(ALLOTMENT)


#   Funkcja check_num_range(nums_list) sprawdza czy wprowadzone przez użytkowanika liczby są poza zakresem
#   wprowadzonym zakresem liczb dozwolonych w zmiennej globalnej MIN_NUM i MAX_NUM. Zwraca wartość False w przypadku
#   błędnie wprowadzonych danych lub wartość True

def check_num_range(nums_list):
    out_range = []
    for num in nums_list:
        if num > MAX_NUM or num < MIN_NUM:
            out_range.append(num)
    if len(out_range) > 0:
        print(ALLOTMENT)
        print('Wprowadzono liczby spoza zakresu:', out_range)
        print(ALLOTMENT)
        return False
    else:
        return True


#   Funkcja chose_num() prosi użytkowanika o podanie liczb, sprawdza poprawność wprowadzonych danych typu integer
#   w przypadku wprowadzenia błędnych danych pyta użytkowanika o wykonanie ponownej próby.
#   jeżeli użytkownik nie potwierdzi chęci ponownej próby, program kończy działanie.
#   W przypadku wprowadzenia poprawnych danych, funkcja zwraca listę wybranych liczb.

def chose_num():
    while True:
        chosen_nums = input('Podaj liczby ')
        try:
            nums_list = make_int(chosen_nums)
        except ValueError:
            print(ALLOTMENT)
            print(ALLOTMENT)
            print('WPROWADZONO BŁĘDNE DANE\n')
            again()
        else:
            return nums_list


#   Funcja draw() losuje ilość liczb zgodną ze zmienną globalną LIST_SIZE w zakresie wskazanym w zmiennych
#   globalnych MIN_NUM i MAX_NUM i zwraca wylosowane liczby

def draw():
    draw_nums = []
    for num in range(LIST_SIZE):
        draw_nums.append(random.randint(MIN_NUM, MAX_NUM))
    return draw_nums


def user_chose():
    while True:
        user_nums = chose_num()
        if check_size(user_nums) and check_num_range(user_nums) is True:
            if check_replic(user_nums) is True:
                return user_nums
            else:
                show_replic(user_nums)


#   Funkcja comp_draw() odpowiedzialna jest za wylosowanie liczb i sprawdzenie powtórzeń podczas losowania. W przypadku
#   powtórzeń wykonywane jest ponowne losowanie do momentu braku powtarzających się liczb. Funkcja zwraca
#   liczby unikalne w postaci listy.

def comp_draw():
    while True:
        draw_list = draw()
        if check_replic(draw_list) is True:
            return draw_list
        else:
            continue


#   Funkcja show_results(user_nums, draw_list) przyjmuje argumenty w postaci list. Wyświetla listę pierwszą i drugą

def show_results(user_nums, draw_list):
    #   W tej części wyświetlane są liczby wprowadzone przez użytkowanika

    print(ALLOTMENT)
    print('Twoje liczby to:')
    for num_user in user_nums:
        print(num_user, end=' ')
    print()
    print(ALLOTMENT)

    #   ta część wyświetla wylosowane liczby przez komputer

    print('TRWA LOSOWANIE')
    for num_comp in draw_list:
        print(num_comp, end=' ')
        time.sleep(0.6)
    print()
    print(ALLOTMENT)

    # w tej części sprawdzane są obie listy pod względem powtarzania się liczb w liscie liczb użytkowanika i
    # liście wylosowanych liczb przez komputer

    end_list = []
    for num_draw in draw_list:
        for num_chose in user_nums:
            if num_draw == num_chose:
                end_list.append(num_draw)

    # Ta część odpowiedzialna jest za wyświetlenie wyników

    if len(end_list) == LIST_SIZE:
        congrat(len(end_list))
    elif len(end_list) == 0:
        print(ALLOTMENT)
        print('!!!! NIE TRAFIłEŚ, SPRÓBUJ PONOWNIE !!!!')
        print(ALLOTMENT)
    elif 0 < len(end_list) < LIST_SIZE:
        print(ALLOTMENT)
        print('!!!!!!!!!!!!!! TRAFIłEŚ', len(end_list), '!!!!!!!!!!!!!!')
        end_list.sort()
        print('TRAFIONE LICZBY TO', end_list)
        print(ALLOTMENT)


#   Funkcja again() ma za zadanie zapytać użytkownika czy chce zagrać jeszcze raz i w zależności od wykonanej akcji
#   przeprowadzić odpowietnią operację.

def again():
    while True:
        print('Czy chcesz zagrać jeszcze raz - t/n :', end=" ")
        agree = input()
        if agree.lower() == 'n':
            print(ALLOTMENT)
            print('DZIĘKUJEMY I ZAPRASZAMY PONOWNIE')
            print(ALLOTMENT)
            sys.exit(0)
        elif agree.lower() == 't':
            break
        else:
            print(ALLOTMENT)
            print('Błędny wybór!')
            print('Spróbuj jeszcze raz')
            print(ALLOTMENT)


# Funkcja main() łączy ze sobą wszystkie funkcje i jest odpowiedzialna za ich wywołanie.

def main():
    welcome()
    while True:
        user_list = user_chose()
        comp_list = comp_draw()
        show_results(user_list, comp_list)
        again()

#   Wywoładnie funkcji main()


main()

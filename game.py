import time

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def introduction():
    print_slow("Sveicināts, drosmīgais piedzīvojumu meklētāj!")
    print_slow("Tu stāvi pie tumša meža malas. Leģenda vēsta par dārgumiem, kas paslēpti dziļi tajā.")
    print_slow("Lai tos iegūtu, tev nāksies saskarties ar briesmām, pieņemt lēmumus un pārbaudīt savu drosmi.")
    print_slow("Kā tevi sauc, ceļotāj?")
    name = input("Ievadi savu vārdu: ")
    print_slow(f"Labi tevi satikt, {name}. Tavs ceļojums sākas tagad...")
    return name

def first_choice(inventory):
    print_slow("Tu ieej mežā. Ir pārāk kluss...")
    print_slow("Priekšā ceļš sadalās divos virzienos.")
    print_slow("Pa kreisi tu dzirdi ūdens čalošanu.")
    print_slow("Pa labi mežs kļūst tumšāks un biedējošāks.")
    choice = input("Vai tu ej PA KREISI vai PA LABI? ").strip().lower()

    if choice == "pa kreisi":
        print_slow("Tu seko ūdens skaņām un atrod upi.")
        print_slow("Tur, ūdenī, tu pamani spožu priekšmetu. Tā ir zobens!")
        inventory.append("zobens")
        print_slow("Tu paņem zobenu un jūties daudz drošāk.")
    elif choice == "pa labi":
        print_slow("Tumsa tevi ieskauj. Tu dzirdi rūcienu tuvumā...")
        print_slow("Pēkšņi no krūmiem izlec vilks!")
        if "zobens" in inventory:
            print_slow("Tu izvelc zobenu un aizbaidi vilku!")
        else:
            print_slow("Tev nav ar ko aizstāvēties. Vilks tevi uzbrūk!")
            print_slow("Tu knapi izglābies, bet esi ievainots.")
            inventory.append("ievainots")
    else:
        print_slow("Vilcināšanās mežā ir bīstama. Koks uzkrīt tev virsū. Tu knapi izglābies, bet zaudē laiku.")

    print_slow("Tu turpini dziļāk mežā.")
    return inventory

def second_choice(inventory):
    print_slow("Ceļojot tālāk, tu atrod vecu vīru, kas sēž pie ugunskura.")
    print_slow("'Sveiks,' viņš saka. 'Vai pievienosies man uz brīdi?'")
    choice = input("Vai tu RUNĀSI ar veco vīru vai IGNORĒSI viņu? ").strip().lower()

    if choice == "runāsi":
        print_slow("Vecais vīrs pasmaida un dalās ar gudrībām.")
        print_slow("'Ņem šo karti,' viņš saka. 'Tā tevi aizvedīs pie dārgumiem.'")
        inventory.append("karte")
        print_slow("Tu viņam pateicies un turpini savu ceļu.")
    elif choice == "ignorēsi":
        print_slow("Tu aizej garām vecajam vīram, bet viņš kaut ko nomurmina zem deguna.")
        print_slow("Tu sajūti dīvainu vēsumu gaisā. Vai tu tikko sadusmoji burvi?")
    else:
        print_slow("Tava vilcināšanās kaitina veco vīru. Viņš pazūd dūmu mutulī, atstājot tevi tukšām rokām.")

    print_slow("Tu turpini savu ceļojumu.")
    return inventory

def final_challenge(inventory):
    print_slow("Beidzot tu sasniedz alas ieeju.")
    print_slow("Dārgumi ir iekšā, bet tos sargā pūķis.")

    if "karte" in inventory:
        print_slow("Izmantojot karti, tu atrod slepenu eju alā.")
        print_slow("Tu nemanāmi apies pūķi un iegūsti dārgumus!")
        print_slow("Apsveicu, tu esi uzvarējis!")
    elif "zobens" in inventory:
        print_slow("Tu izvelc zobenu un stājies pretī pūķim.")
        print_slow("Cīņa ir sīva, bet tu iznāc kā uzvarētājs!")
        print_slow("Tu iegūsti dārgumus un slavu.")
    else:
        print_slow("Tev nav ne ieroču, ne plāna. Pūķis pamostas un...")
        print_slow("Tavs piedzīvojums šeit arī beidzas.")
        print_slow("SPĒLE BEIGTA")

# Galvenā spēles cilpa
if __name__ == "__main__":
    inventory = []
    name = introduction()
    inventory = first_choice(inventory)
    inventory = second_choice(inventory)
    final_challenge(inventory)

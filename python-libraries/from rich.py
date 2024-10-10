from rich.console import Console

console = Console()

def introduction():
    console.print("Hello!", style="bold cyan")
    console.print("This program will prompt you to enter information about your favorite foods!", style="bold yellow")
    questions()

def questions():
    data_entries = []#continuous list

    while True:
        food = input("Enter a food you enjoy: ")
        loc = input("Do you typically enjoy this food at home or at a restaurant?: ")
        side = input("Enter a food or drink that would accompany it as a side: ")

        db = [food, loc, side]
        console.print(f"You entered: {db}", style="bold magenta")

        confirm = input('Is this information correct? Type "y" for yes, type "n" for no: ')
        if confirm.lower() == 'y':
            data_entries.append(db) #add continious
            console.print("Data added.", style="bold green")
        else:
            console.print("That's okay!", style="bold red")
            continue

        repeater = input('Would you like to add another set? Type "y" for yes and "n" for no: ')
        if repeater.lower() != 'y':
            break

    if data_entries:
        save_to_file(data_entries)

def save_to_file(data_entries):
    file_path = "favorite_foods.txt"
    with open(file_path, 'w') as file:
        for entry in data_entries:
            file.write(', '.join(entry) + '\n')

    console.print(f"Your information has been saved to: {file_path}", style="bold green")

def main():
    introduction()

if __name__ == '__main__':
    main()
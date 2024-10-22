# import libraries
from rich.console import Console
from rich.table import Table
import os
import json

# Create a console object
console = Console()

# Create a table to display the data
table = Table(title="Steps per Day")
table.add_column("Date", style="green", no_wrap=True)
table.add_column("Miles Walked", style="blue")
table.add_column("Steps Walked per Day", justify="right", style="purple")
table.add_row("Oct 1, 2024", "3.85 mi", "8,795")
table.add_row("Oct 2, 2024", "3.61 mi", "8,317")
table.add_row("Oct 3, 2024", "4.89 mi", "11,066")
table.add_row("Oct 4, 2024", "2.05 mi", "4,798")
console.print(table)



# Ask the user for the number of steps walked per day
while True:
        steps = []
        console.print("\n[bold cyan]Please enter how many steps you walked per day!:[/bold cyan]")
        date = console.input("Please enter the date of when you walked: ")
        miles_walked = console.input("Please enter the amount of miles you walked: ")
        steps_walked = console.input("Please enter the number of steps that you walked: ")
        console.print(f"\n[blue]What you entered was:[/blue]{date}, {miles_walked}, {steps_walked}")

        # Confirm the data entered
        confirm = console.input("Is the information you entered correct? (yes or no?)")
        if confirm == 'yes':
            steps.append((miles_walked, steps_walked, date))
            console.print(f"\Information added!: {date}, {miles_walked}, {steps_walked}")
            table.add_row(date, miles_walked, steps_walked)
        else:
              console.print("[bold yellow] No worries, please re-enter the data![/bold yellow]")

        # Ask the user if they want to add more data
        add_more = console.input("Would you like to add another day? (yes or no?)")
        if add_more != "yes":
            break

console.print(table)

# Save the data to a file
file_path = os.path.join(os.getcwd(), "steps_per_day.json")
with open(file_path, "w") as file:
    json.dump(steps, file, indent=4)
console.print(f"\n[bold yellow]Your data has been saved to {file_path}![/bold yellow]")
# Tada!


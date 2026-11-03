# Name: Angeline Vanhaltren | Student ID: 0324635 | Group A
# What goes in: The scenario file 'scenarios_A.csv' is a comma-separated file with 14 columns:
#ID, Scenario, OptionA, OptionB, OptionC, BudgetA, BudgetB, BudgetC,ReputationA, ReputationB, ReputationC, FeedbackA, FeedbackB, FeedbackC. Numbers (budget and reputation changes) are read as text and converted to integers.
# Process: Each of the 10 days: Displays the day number, current budget, and reputation. Shows the scenario and options A, B, and C.Prompts the player for a valid choice (A, B, or C). Updates budget and reputation, caps reputation at 100, and displays feedback. Checks if budget or reputation <= 0 (Game Over).
# Output: At the end, displays survival status, final budget, reputation, score, title, best move, and worst move. Appends one summary line to 'results.csv'.
# Error: Invalid key entered: Loop keeps prompting until valid input (A, B, or C) is given. Gauge drops to 0 or below: Game stops immediately with Fired status. Missing scenario file: Caught using a try/except block.
# Feature Unicorn (B): The algorithm - on one random day during the game, the reputation change of the chosen option is doubled!

import csv
import random
from datetime import datetime

def load_scenarios(filename="scenarios_A.csv"):
# loading scenarios from CSV into github dictionary
    scenarios = []
    try:
        with open(filename, mode = "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                scenarios.append(row)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Is it in the dictionary?")
    return scenarios

def get_player_choice():
# ask player for choice and return in uppercase
    while True:
        choice = input("Your choice (A, B, C): ").strip().upper()
        if choice in ["A", "B", "C"]:
            return choice
        print("Type A, B, or C: ")

def apply_choice(budget, reputation, option, row, is_doubled):
    # applying changes based on choice
    if option == "A":
        budget_change = int(row["BudgetA"])
        reputation_change = int(row["ReputationA"])
        feedback = row["FeedbackA"]
    elif option == "B":
        budget_change = int(row["BudgetB"])
        reputation_change = int(row["ReputationB"])
        feedback = row["FeedbackB"]
    else:
        budget_change = int(row["BudgetC"])
        reputation_change = int(row["ReputationC"])
        feedback = row["FeedbackC"]

    # (below) Feature Unicorn: reputation changes twice

    if is_doubled and reputation_change != 0:
        reputation_change *= 2
        feedback += "[Algorithm bonus: reputation impact doubled!]"
    new_budget = budget + budget_change
    new_reputation = min(100, reputation + reputation_change)
    return new_budget, new_reputation, feedback, reputation_change
def save_result(name, budget, reputation, title):
    date_str = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("results.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, budget, reputation, title, date_str])

def main():
    name = input("Enter your name: ").strip()
    if not name:
        name = "Anon"

    scenarios = load_scenarios()
    if not scenarios:
        print("No scenarios loaded. Exiting...")
        return
    
    random.shuffle(scenarios)
    game_scenarios = scenarios[:10]
    # any 10 scenarios at random

    budget = 10000
    repuation = 50
    history = []
    # to save history - required acc. to doc

    # (below) to pick a random day (1-10) for Feature Unicorn

    doubled_day = random.randint(1,10)
    print("\n=== SURVIVE THE QUARTER ===")
    print("May your budget stay positive and your rep viral.\n")
    
    survived = True

    for day_num in range(1, 11):
        row = game_scenarios[day_num - 1]
        print(f"Day {day_num}")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(row["Scenario"])
        print(f"A: {row["OptionA"]}")
        print(f"B: {row["OptionB"]}")
        print(f"C: {row["OptionC"]}")

        choice = get_player_choice()
        is_doubled = (day_num == doubled_day)

        budget, reputation, feedback, reputation_change = apply_choice(budget, reputation, choice, row, is_doubled)
        print(feedback)

        # the top lines take the real changes in budget, rep, etc. and 1. display the latest version, 2. prints the funny feedback sentence

        if choice == "A":
            opt_text = row["OptionA"]
        if choice == "B":
            opt_text = row["OptionB"]
        if choice == "C":
            opt_text = row["OptionC"]

        history.append((reputation_change, day_num, opt_text))
        print("===============")

        if budget <= 0 or reputation <= 0:
            print("Too bad, game over. Either your reputation or your budget hit zero.")
            survived = False
            break

    if survived:
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
        score = reputation + budget // 200
        print(f"Final score: {score}")

        if score < 95:
            title = "Eternal Intern"
        elif score <=119:
            title = "Growth Hacker"
        elif score <= 139:
            title = "Next CMO"
        else:
            title = "Viral Legend"

        print(f"{name}, your title: {title}")

        #(below) finding player's best and worst moves

        history.sort(key=lambda x: x[0])
        worst_move = history [0]
        best_move = history[-1]

        print (f"Best move: day {best_move[1]}, \"{best_move[2]}\" ({"+" if best_move[0]> 0 else "" }{best_move[0]} rep)")
        print(f"Worst move: day {worst_move[1]}, \"{worst_move[2]}\" ({worst_move[0]} rep)")
        save_result(name, budget, reputation, title)
        print("Saved in results.csv")
    else:
        title = "Fired"
        print(f"{name}, you were fired!")
        save_result(name, budget, reputation, title)
        print("Saved in results.csv")

    if __name__ == "__main__":
        main()




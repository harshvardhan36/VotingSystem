import random
import time
import json  # For saving data as JSON

# File to store voting data
file_name = "voting_data.json"

# Initialize candidates and votes
def load_data():
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data.get("candidates", []), data.get("votes", {})
    except FileNotFoundError:
        # If file doesn't exist, start with default values
        candidates = ['BJP', 'CONGRESS', 'TMC', 'AAP', 'NDA', 'JDU']
        votes = {candidate: 0 for candidate in candidates}
        return candidates, votes

def save_data(candidates, votes):
    with open(file_name, "w") as file:
        json.dump({"candidates": candidates, "votes": votes}, file)

# Load existing data
candidates, votes = load_data()

admin_password = "harsh_vardhan3656"  # Predefined admin password

while True:
    print("\nWelcome to HARSH VOTING SYSTEM\nThis system is hosted by HVM")
    print("Choose 'portal' from the given options:")
    print("\n1. Voters Registration")
    print("2. General Instructions")
    print("3. View Votes (Admin Only)")
    print("4. Add a New Party")
    print("5. Exit")
    user_choice = int(input("::> "))

    if user_choice == 1:
        name = input("Enter your name below:\n> ")
        age = int(input("Enter your age:\n> "))
        
        if age < 18:
            print("Not Eligible to vote.")
        else:
            captcha = random.randint(1000, 9999)
            print(f"Please Enter the captcha shown below:\n'{captcha}'")
            user_captcha = int(input("> "))
            
            if user_captcha == captcha:
                print("Registration successful!")
                time.sleep(1)  # Wait for 1 second
                
                print("\nParties available for voting:")
                for party in candidates:
                    print(party)
                    
                user_vote = input("\nPlease Enter the name of the party you want to vote for:\n> ")
                user_vote = user_vote.strip().upper()
                
                if user_vote in votes:
                    votes[user_vote] += 1
                    print(f"Thank you for voting for {user_vote}!")
                else:
                    print("Invalid party name! Your vote was not counted.")
            else:
                print("Incorrect captcha. Please try again.")
                
    elif user_choice == 2:
        print("""
        General Instructions:
        1. Only individuals aged 18 and above are eligible to vote.
        2. Please ensure you enter the correct captcha to complete registration.
        3. You can vote only once.
        4. Choose from the available parties listed during the voting process.
        """)

    elif user_choice == 3:
        password = input("Enter the admin password to view vote counts:\n> ")
        if password == admin_password:
            print("\nVote Count Summary:")
            for candidate, count in votes.items():
                print(f"{candidate}: {count} votes")
        else:
            print("Access Denied! Incorrect password.")
    
    elif user_choice == 4:
        print("\nWelcome to Party Registration!")
        new_party = input("Enter the name of the new party to register:\n> ").strip().upper()
        if new_party in votes:
            print(f"The party '{new_party}' is already registered!")
        else:
            votes[new_party] = 0
            candidates.append(new_party)
            print(f"The party '{new_party}' has been successfully registered!")
    
    elif user_choice == 5:
        save_data(candidates, votes)  # Save data before exiting
        print("Thank you for using HARSH VOTING SYSTEM. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")

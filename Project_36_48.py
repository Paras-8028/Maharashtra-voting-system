# Voting system for Maharashtra Elections 

maharashtra_parties = [
    "Shiv Sena",
    "BJP",
    "NCP",
    "Congress",
    "MNS",
    "AAP"
]

votes = {party: 0 for party in maharashtra_parties}
voter_details = {party: [] for party in maharashtra_parties}
total_votes = 0  

def display_parties():
    print("\nAvailable Parties:")
    for idx, party in enumerate(maharashtra_parties, start=1):
        print(f"{idx}. {party}")

def is_valid_name(name):
    return any(char.isalpha() for char in name)

def vote(candidate_name):
    global total_votes
    display_parties()

    while True:
        try:
            choice = input("Select party number to vote for: ").strip()

            if not choice.isdigit():
                raise ValueError("Please enter a valid number between 1 and 6.")

            choice = int(choice)

            if choice < 1 or choice > len(maharashtra_parties):
                raise IndexError("Invalid party number. Please choose a number from the list.")

            selected_party = maharashtra_parties[choice - 1]
            votes[selected_party] += 1
            voter_details[selected_party].append(candidate_name.title())
            total_votes += 1

            print(f"\nVote recorded for {candidate_name.title()} to {selected_party}.")
            print(f"Total votes so far: {total_votes}\n")
            break  

        except ValueError as ve:
            print(f"Input Error: {ve}\n")
        except IndexError as ie:
            print(f"Selection Error: {ie}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")

def show_results():
    print("\n--- Final Election Results ---")
    for party, count in votes.items():
        print(f"{party}: {count} votes")

    print(f"\nTotal Votes Cast: {total_votes}")

    if total_votes == 0:
        print("No votes were cast.")
        return

    max_votes = max(votes.values())
    winners = [party for party, count in votes.items() if count == max_votes]

    if len(winners) == 1:
        winning_party = winners[0]
        print(f"\n{winning_party} wins the Maharashtra elections!")

        print(f"\nVoters who voted for {winning_party}:")
        for name in voter_details[winning_party]:
            print(f" - {name}")

        print("\nOther Parties & Voters:")
        for party, names in voter_details.items():
            if party != winning_party and votes[party] > 0:
                print(f"\n{party}: {votes[party]} votes")
                for name in names:
                    print(f" - {name}")
    else:
        print(f"\nIt's a tie between: {', '.join(winners)}")
        for tied_party in winners:
            print(f"\n{tied_party}: {votes[tied_party]} votes")
            print("Voters:")
            for name in voter_details[tied_party]:
                print(f" - {name}")

def main():
    print("Maharashtra State Election Voting System")
    print("Type 'result' to view the result or 'exit' to quit without result.\n")

    while True:
        try:
            name = input("Enter candidate name: ").strip()
            if name.lower() == 'exit':
                print("\nVoting ended.")
                break
            elif name.lower() == 'result':
                show_results()
                break
            elif not is_valid_name(name):
                print("Invalid name. Must contain letters (not just symbols). Try again.\n")
            else:
                vote(name)
        except KeyboardInterrupt:
            print("\nVoting interrupted by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

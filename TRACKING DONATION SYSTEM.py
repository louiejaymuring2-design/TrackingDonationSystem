donations = []
fundraising_goal = 0

while True:
    print("\n--- Login ---")
    print("1. Treasurer")
    print("2. Organization Leader")
    print("3. Exit")

    role = input("Choose your role: ")

    if role == "1":
        while True:
            print("\n--- Treasurer Menu ---")
            print("1. Add Donation")
            print("2. Track Total Collected")
            print("3. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                donor = input("Enter Donor Name: ")

                amount_input = input("Enter Donation Amount: ₱")
                if amount_input.replace('.', '', 1).isdigit():
                    amount = float(amount_input)
                    donations.append({"donor": donor, "amount": amount})
                    print("\nDonation added successfully!")
                else:
                    print("Invalid amount. Please enter numbers only.")

            elif choice == "2":
                total = sum(d["amount"] for d in donations)
                print(f"\nTotal Collected: ₱{total:.2f}")

            elif choice == "3":
                print("Logging out Treasurer...")
                break

            else:
                print("Invalid choice. Try again.")

    
    elif role == "2":
        while True:
            print("\n--- Organization Leader Menu ---")
            print("1. View All Donations")
            print("2. Set/Update Fundraising Goal")
            print("3. Monitor Funds Raised")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                if not donations:
                    print("No donations recorded yet.")
                else:
                    print("\n--- Donations Summary ---")
                    for d in donations:
                        print(f"Donor: {d['donor']} | Amount: ₱{d['amount']:.2f}")

            elif choice == "2":
                goal_input = input("Enter new fundraising goal: ₱")
                if goal_input.replace('.', '', 1).isdigit():
                    fundraising_goal = float(goal_input)
                    print("\nFundraising goal updated successfully!")
                else:
                    print("Invalid amount. Please enter numbers only.")

            elif choice == "3":
                if fundraising_goal == 0:
                    print("No fundraising goal set yet.")
                else:
                    total = sum(d["amount"] for d in donations)
                    progress = (total / fundraising_goal) * 100

                    print("\n--- Fundraising Progress ---")
                    print(f"Goal: ₱{fundraising_goal:.2f}")
                    print(f"Collected: ₱{total:.2f}")
                    print(f"Progress: {progress:.2f}%")

                    if total >= fundraising_goal:
                        print("Goal reached or exceeded!")
                    else:
                        print(f"₱{fundraising_goal - total:.2f} more needed.")

            elif choice == "4":
                print("Logging out Organization Leader...")
                break

            else:
                print("Invalid choice. Try again.")

    elif role == "3":
        print("\nExiting system... Goodbye!")
        break

    else:
        print("Invalid role. Choose 1, 2, or 3.")
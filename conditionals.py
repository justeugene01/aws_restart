"""A simple post office menu that shows how if / elif / else works."""


def ask(prompt):
    """Ask a question and return the answer in lowercase without extra spaces."""
    return input(prompt).strip().lower()


def main():
    ship_reply = ask("Do you need to ship a package? (Enter yes or no): ")

    if ship_reply == "yes":
        print("We can help you ship that package!")
    elif ship_reply == "no":
        print("Please come back when you need to ship a package. Thank you.")
        return  # end the program here
    else:
        print("Sorry, please enter yes or no.")
        return

    menu_reply = ask(
        "Would you like to buy stamps, buy an envelope, or make a copy? "
        "(Enter stamps, envelope, or copy): "
    )

    if menu_reply == "stamps":
        print("We have many stamp designs to choose from.")
    elif menu_reply == "envelope":
        print("We have many envelope sizes to choose from.")
    elif menu_reply == "copy":
        copies = ask("How many copies would you like? (Enter a number): ")
        if copies.isdigit() and int(copies) > 0:
            print(f"Here are {copies} copies.")
        else:
            print("Please enter a whole number greater than 0.")
    else:
        print("Sorry, we don't have that option.")

    print("Thank you, please come again.")


main()

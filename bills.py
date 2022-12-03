

import json
import getpass
import os
from datetime import datetime
import requests

today = datetime.today()
NAME = getpass.getuser()


# with open(f"/Users/{NAME}/.data.json", "r") as data_file:
print('''  ╔╗ ╦╦  ╦  ╔═╗
  ╠╩╗║║  ║  ╚═╗
  ╚═╝╩╩═╝╩═╝╚═╝''')
print("**********************************************************")
print("new = New bill entry.")
print("query = List all the bill entries + bitcoin current price.")
print("delete = Delete a bill entry.")
print("total = List the total amount of all the bills.")
print("due = Displays the date that a bill is due.")
print("quit = Quit the application.")
print("**********************************************************")


def total():
    total = 0
    try:
        with open(f"/home/{NAME}/.data.json", "r") as data_file:
            data = json.load(data_file)

        for i in data:
            amounts = data[i]["amount"]
            amounts = float(amounts)
            total += amounts
        return (f"${format(total,'.2f')}")
    except FileNotFoundError:
        print("There are no bills entered.")


def lets_get_started():
    while True:
        user = input("What would you like to do? ")
        if user == "quit":
            break
        elif user == "new":
            company = input("Company name: ")
            amount = input("Amount Due: ")
            due_date = input("Due date: ")
            new_data = {
                company: {
                    "amount": amount,
                    "due_date": due_date,
                }
            }
            if len(company) == 0:
                print("Please make sure you haven't left any fields empty.")
            else:
                try:
                    with open(f"/home/{NAME}/.data.json", "r") as data_file:
                        # Reading old data
                        data = json.load(data_file)

                except FileNotFoundError:
                    with open(f"/home/{NAME}/.data.json", "w") as data_file:
                        # date_file is the location of where I will dump the new data
                        json.dump(new_data, data_file, indent=4)
                else:
                    # Updating old data with new data
                    data.update(new_data)

                    with open(f"/home/{NAME}/.data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)

        if user == "total":

            print(total())

        if user == "due":
            try:
                name = input("Please enter the company name: ")
                if len(name) == 0:
                    print("Please make sure you haven't left any fields empty.")
                else:

                    with open(f"/home/{NAME}/.data.json", "r") as data_file:
                        data = json.load(data_file)

                    due_dates = data[name]["due_date"]

                    print(
                        f"Your {name} payment is due on\n {today.month}/{due_dates}/{today.year}.")
            except FileNotFoundError:
                print("There are no bills entered.")
            except KeyError:
                print("Company name not found.")

        if user == "query":
            try:
                response = requests.get(
                    url="https://api.coindesk.com/v1/bpi/currentprice.json")
                response.raise_for_status()

                data_bitcoin = response.json()
                bitcoin = data_bitcoin['bpi']['USD']['rate_float']
                string = ''

                #name = company_e.get()
                with open(f"/home/{NAME}/.data.json", "r") as data_file:
                    data = json.load(data_file)
                for i in data:
                    string += f"{i} ${data[i]['amount']} on {today.month}/{data[i]['due_date']}/{today.year}\n"

                # \nBitcoin Price: ${round(bitcoin,2)}
                print(
                    f"{string}Total: {total()}\nBitcoin Price: ${round(bitcoin,2)}")
            except FileNotFoundError:
                print("There are no bills entered.")
        if user == "delete":
            wt_delete = input("Enter the company to be deleted: ")
            if len(wt_delete) == 0:
                print("Please make sure you haven't left any fields empty.")
            else:
                try:
                    with open(f"/home/{NAME}/.data.json", "r") as data_file:
                        # Reading old data
                        data = json.load(data_file)

                        data.pop(f"{wt_delete}")
                    with open(f"/home/{NAME}/.data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)

                except FileNotFoundError:
                    print("There is nothing to delete.")
                except KeyError:
                    print("Company name not found.")


def main():
    lets_get_started()


if __name__ == '__main__':
    main()

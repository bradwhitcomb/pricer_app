""" This is the quote app for acapella-design"""


import tkinter as tk
from tkinter import Canvas, END
import smtplib
import datetime
import cred
from widgets import create_widgets
import sqlite3

"""
Creates a global dictionary.  Data from the entry boxes populate the dict.
Data from the price table also populates the dict.  The dict provides the info
for the quote email and the quote DB in sqlite3
"""

global quote_dict
quote_dict = {}


class Root(tk.Tk):

    def __init__(self):
        super().__init__()
        """ Create Canvas """

        a = "#7a871e"
        b = "#104210"
        c = "#e55b13"
        d = "#f6a21e"
        self.quote_canvas = Canvas(height=55, width=450, bg=a)
        self.quote_canvas.grid(row=0, column=0)

        self.output_canvas = Canvas(height=120, width=450, bg=b)
        self.output_canvas.grid(row=1, column=0)

        self.input_canvas = Canvas(height=420, width=450, bg=c)
        self.input_canvas.grid(row=2, column=0)

        self.button_canvas = Canvas(height=100, width=450, bg=d)
        self.button_canvas.grid(row=3, column=0)

        self.iconbitmap('bike.png', False)

        self.title("Quote Machine")
        # self.geometry("450x300")
        create_widgets(self)

    def create_quote(self):
        """ Get inputs from entry boxes """
        x = int(self.entry_quantity.get())
        price = float(self.price_var.get())
        front_colors = int(self.front_var.get())
        back_colors = int(self.back_var.get())
        markup = int(self.markup_var.get())
        art = float(self.art_var.get())
        flash = float(self.flash_var.get())
        setup = int(self.setup_var.get())
        customer = self.customer_var.get()
        brand = self.vendor.get()
        product = self.product.get()
        comments = self.description.get("1.0", END).strip()

        """In the pricer_a dict the keys are the number of colors to print.
           In the values x represents the quantity to print.
           The conditional calculates price based on number of colors and x
        """
        pricer_a = {
            0:0,
            1: .6 if x >= 1200 else .7 if x >= 480 else .75 if x >= 240 else .85 if x >= 180 else .95
             if x >= 120 else 1.05 if x >= 60 else 1.2 if x >= 36 else 1.6 if x >= 12 else None,

            2: .75 if x >= 1200 else .85 if x >= 480 else .95 if x >= 240 else 1.05 if x >= 180 else 1.1
             if x >= 120 else 1.45 if x >= 60 else 1.60 if x >= 36 else 1.90 if x >= 12 else None,

            3: .8 if x >= 1200 else .9 if x >= 480 else 1.05 if x >= 240 else 1.15 if x >= 180 else 1.35
             if x >= 120 else 1.75 if x >= 60 else 2 if x >= 36 else 2.25 if x >= 12 else None,

            4: 1.1 if x >= 1200 else 1.1 if x >= 480 else 1.25 if x >= 240 else 1.4 if x >= 180 else 1.75
             if x >= 120 else 2.15 if x >= 60 else 2.5 if x >= 36 else 2.65 if x >= 12 else None,

            5: 1.1 if x >= 1200 else 1.2 if x >= 480 else 1.3 if x >= 240 else 1.55 if x >= 180 else 1.85
             if x >= 120 else 2.45 if x >= 60 else 2.9 if x >= 36 else None if x >= 12 else None,

            6: 1.35 if x >= 1200 else 1.45 if x >= 480 else 1.7 if x >= 240 else 1.85 if x >= 180 else 2.2
             if x >= 120 else None if x >= 60 else None if x >= 36 else None if x >= 12 else None

        }

        # print(x, price, front_colors, back_colors, setup, markup, art, flash)
        front_cost = pricer_a[front_colors]
        back_cost = pricer_a[back_colors]
        total_cost = (x * (price + front_cost + back_cost + flash)) + setup + art
        margin = total_cost * (markup/100)
        total_quote = total_cost + margin
        quote_per_unit = total_quote/x

        """Creates output labels"""
        self.label_totalquote["text"] = f"TOTAL QUOTE: ${total_quote:,.2f}"
        self.label_itemquote["text"] = f"QUOTE PER ITEM: ${quote_per_unit:,.2f}"
        self.label_totalcost["text"] = f"Cost:  ${total_cost:,.2f}"
        self.label_cost["text"] = f"Cost per unit:  ${total_cost/x:,.2f}"
        self.label_profit["text"] = f"Profit per Unit:  ${margin/x:,.2f}"
        self.label_totalprofit["text"] = f"Total Profit: ${margin:,.2f}"
        self.label_frontcost["text"] = f"Front Print Charge: ${front_cost:,.2f}"
        self.label_backcost["text"] = f"Back Print Charge: ${back_cost:,.2f}"

        quote_date = datetime.datetime.today()
        quote_date = str(quote_date)
        quote_date = quote_date[0:16]
        quote_dict["Total_Quote"] = total_quote
        quote_dict["Quote_per_Item"] = quote_per_unit
        quote_dict["Cost_per_Unit"] = total_cost/x
        quote_dict["Profit_per_Unit"] = margin/x
        quote_dict["Cost"] = total_cost
        quote_dict["Total_Profit"] = margin
        quote_dict["Front_Print_Charge"] = front_cost
        quote_dict["Back_Print_Charge"] = back_cost
        quote_dict["Client_Name"] = customer
        quote_dict["Quantity_to_Print"] = x
        quote_dict["Price_of_Item"] = price
        quote_dict["Front_Colors"] = front_colors
        quote_dict["Back_Colors"] = back_colors
        quote_dict["Markup"] = markup
        quote_dict["Setup"] = setup
        quote_dict["Art"] = art
        quote_dict["Flash"] = flash
        quote_dict["Time_Stamp"] = quote_date
        quote_dict["Brand"] = brand
        quote_dict["Product"] = product
        quote_dict["Comments"] = comments

        return quote_dict

# #         """ to create app 
# #         pyinstaller --onefile --add-binary="/System/Library/Frameworks/Tk.framework/Tk":"tk" --add-binary="/System/Library/Frameworks/Tcl.framework/Tcl":"tcl" name_of_file.py """
    def save_quote(self):

        password = cred.password

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            """Creates email from the quote_dict"""

            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login('acapella.design670@gmail.com', password)
            subject = f"This is the quote for: {quote_dict['Client_Name']}"
            body = f"""
            TIME STAMP: {quote_dict['Time_Stamp']}
            CLIENT: {quote_dict['Client_Name']}

            TOTAL QUOTE: ${quote_dict['Total_Quote']:,.02f}
            QUOTE PER ITEM: ${quote_dict['Quote_per_Item']:,.02f}

            Cost per Unit: ${quote_dict['Cost_per_Unit']:,.02f}
            Profit per Unit: ${quote_dict['Profit_per_Unit']:,.02f}
            Cost: ${quote_dict['Cost']:,.02f}
            Total Profit: ${quote_dict['Total_Profit']:,.02f}
            Front Print Charge: ${quote_dict['Front_Print_Charge']:,.02f}
            Back Print Charge: ${quote_dict['Back_Print_Charge']:,.02f}

            Quantity to Print: {quote_dict['Quantity_to_Print']} pcs
            Price of Item: ${quote_dict['Price_of_Item']:,.02f}
            Front: Number of Colors: {quote_dict['Front_Colors']}
            Back: Number of Colors: {quote_dict['Back_Colors']}
            Mark-up: {quote_dict['Markup']}%
            Set-Up Charge: ${quote_dict['Setup']}
            Art-Charge: ${quote_dict['Art']}
            Flash-Charge: ${quote_dict['Flash']}

            Brand: {quote_dict['Brand']}
            Product: {quote_dict['Product']}

            Comments:{quote_dict['Comments']}
            """
            msg = f"Subject:  {subject}\n\n{body}"
            smtp.sendmail('EMAIL_ADDRESS', 'marty@acapella-design.com', msg)
        """Sets up the sqlite3 object"""
        conn = sqlite3.connect('quoteapp.db')

        c = conn.cursor()

        with conn:
            c.execute("""CREATE TABLE IF NOT EXISTS acapella (
                        Date text,
                        Client text,
                        Quantity integer,
                        Price real,
                        Quote real,
                        Cost real,
                        Profit real,
                        Item_quote real,
                        Item_cost real,
                        Item_profit real,
                        Front_charge real,
                        Back_charge real,
                        Front_colors integer,
                        Back_colors integer,
                        Markup real,
                        Art real,
                        Setup real,
                        Flash real,
                        Brand text,
                        Product text,
                        Comments text

                        )""")
        with conn:
            c.execute(f"""INSERT INTO acapella (Date, Client, Quantity, Price, Quote, Cost, Profit, Item_quote, Item_cost, 
                          Item_profit, Front_charge, Back_charge, Front_colors, Back_colors, Markup, Art, Setup, Flash, Brand, Product, Comments) 
                          VALUES { quote_dict["Time_Stamp"], quote_dict["Client_Name"], f'{quote_dict["Quantity_to_Print"]}', f'${quote_dict["Price_of_Item"]:,.02f}',
                          f'${quote_dict["Total_Quote"]:,.02f}', f'${quote_dict["Cost"]:,.02f}', f'${quote_dict["Total_Profit"]:,.02f}', f'${quote_dict["Quote_per_Item"]:,.02f}',
                          f'${quote_dict["Cost_per_Unit"]:,.02f}', f'${quote_dict["Profit_per_Unit"]:,.02f}', f'${quote_dict["Front_Print_Charge"]:,.02f}', 
                          f'${quote_dict["Back_Print_Charge"]:,.02f}', quote_dict["Front_Colors"], quote_dict["Back_Colors"], f'{quote_dict["Markup"]:,.02f}%', f'${quote_dict["Setup"]:,.02f}',
                          f'${quote_dict["Art"]:,.02f}', f'${quote_dict["Flash"]:,.02f}', f'{quote_dict["Brand"]}', f'{quote_dict["Product"]}', f'{quote_dict["Comments"]}'

                      }""")


if __name__ == "__main__":
    root = Root()
    root.mainloop()

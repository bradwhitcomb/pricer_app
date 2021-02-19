<<<<<<< HEAD
from tkinter import Label, Entry, Button, StringVar, Text, ttk
=======
from tkinter import Label, Entry, Button, StringVar, OptionMenu, Text, ttk
>>>>>>> e4151c20420bbac9b04fbf4811f07232aba3ceb9
import smtplib
import cred


global quote_dict
quote_dict = {}

<<<<<<< HEAD

=======
>>>>>>> e4151c20420bbac9b04fbf4811f07232aba3ceb9
def create_widgets(self):
        x = 120
        y = 30

        h = 1
        w = 20

        px = 2
        py = 1
<<<<<<< HEAD
=======


        
        
>>>>>>> e4151c20420bbac9b04fbf4811f07232aba3ceb9
       
        """ Create input boxes """

        self.label_client = Label(self.input_canvas, text="CLIENT NAME", height=h,
                                  width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y, window=self.label_client)

        self.label_quantity = Label(self.input_canvas, text="Quantity to Print", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y+30, window=self.label_quantity)

        self.label_price = Label(self.input_canvas, text="Price of Item", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y+60, window=self.label_price)


        self.label_front = Label(self.input_canvas, text="Front: Number of Colors", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y+90, window=self.label_front)

        self.label_back = Label(self.input_canvas, text="Back: Number of Colors", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y+120, window=self.label_back)

        self.label_markup = Label(self.input_canvas, text="Mark-Up %", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y+150, window=self.label_markup)

        self.label_setup = Label(self.input_canvas, text="Set-Up Charge", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y+180, window=self.label_setup)

        self.label_art = Label(self.input_canvas, text="Art-Charge", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y+210, window=self.label_art)

        self.label_flash = Label(self.input_canvas, text="Flash-Charge", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.input_canvas.create_window(x, y+240, window=self.label_flash)

        vendors =[
          "Select a Brand",
          "Augusta Sportswear",
          "Badger",
          "Bella+Canvas",
<<<<<<< HEAD
          "Champion",
=======
          "Champion" ,
>>>>>>> e4151c20420bbac9b04fbf4811f07232aba3ceb9
          "Columbia",
          "Comfort Colors",
          "Core",
          "Gildan",
          "Harriton",
          "Headsweats",
          "Next Level",
          "Nike",
          "Port Authority",
          "Russell",
          "Sport-Tek",
          "Team 365",
          "The Game",
          "Under Armour",
          "Yupoong",
          "OTHER"
          ]
        self.vendor = StringVar()
        self.drop = ttk.OptionMenu(self.input_canvas, self.vendor, *vendors, direction='flush')
        self.input_canvas.create_window(x, y+270, window=self.drop)
        self.vendor.set(vendors[0])

        products = [
                "Select a Product",
                "1/4 zip",
                "Backpack",
                "Beanie",
                "Blanket",
                "Booney",
                "Cap",
                "Crewneck",
                "Duffle",
                "Fullzip",
                "Hat",
                "Hoodie",
                "Jacket",
                "LS Tee",
                "Polo",
                "Mask",
                "Shirt",
                "Shorts",
                "SS Tee",
                "Sweatpants",
                "Sweatshirt",
                "Vest",
                "Visor",
                "V-neck",
                "Warm-up",
<<<<<<< HEAD
                "Other"

=======
                "Other"   
     
>>>>>>> e4151c20420bbac9b04fbf4811f07232aba3ceb9
        ]

        self.product = StringVar()
        self.drop2 = ttk.OptionMenu(self.input_canvas, self.product, *products, direction='flush')
        self.input_canvas.create_window(x+220, y+270, window=self.drop2)
        self.product.set(products[0])

        self.description = Text(self.input_canvas, width=45, height=4, wrap="word", bd=10, bg='black', fg='white',
        font="courier 12 bold", highlightbackground='green', highlightcolor='blue', insertbackground='red')
        self.input_canvas.create_window(x+75, y+340, window=self.description)
        self.description.insert('1.0', 'Comments:')

<<<<<<< HEAD
=======


>>>>>>> e4151c20420bbac9b04fbf4811f07232aba3ceb9
        """ Create entry input boxes """
        self.customer_var = StringVar()
        self.entry_client = Entry(self.input_canvas, bg = "white", fg = "black", textvariable=self.customer_var)
        self.input_canvas.create_window(x+200, y, window=self.entry_client)

<<<<<<< HEAD
=======
       
>>>>>>> e4151c20420bbac9b04fbf4811f07232aba3ceb9
        self.quantity_var = StringVar()
        self.entry_quantity = Entry(self.input_canvas, bg = "white", fg = "black", textvariable=self.quantity_var)
        self.input_canvas.create_window(x+200, y+30, window=self.entry_quantity)
        self.entry_quantity.insert(0,0)

        self.price_var = StringVar()
        self.entry_price = Entry(self.input_canvas, bg = "white", fg = "black", textvariable=self.price_var)
        self.input_canvas.create_window(x+200, y+60, window=self.entry_price)
        self.entry_price.insert(0,0)

        self.front_var = StringVar()
        self.entry_front = Entry(self.input_canvas, bg = "white", fg = "black",textvariable=self.front_var)
        self.input_canvas.create_window(x+200, y+90, window=self.entry_front)
        self.entry_front.insert(0,0)

        self.back_var = StringVar()
        self.entry_back = Entry(self.input_canvas, bg = "white", fg = "black", textvariable=self.back_var)
        self.input_canvas.create_window(x+200, y+120, window=self.entry_back)
        self.entry_back.insert(0,0)

        self.markup_var = StringVar()
        self.entry_markup = Entry(self.input_canvas, bg = "white", fg = "black", textvariable=self.markup_var)
        self.input_canvas.create_window(x+200, y+150, window=self.entry_markup)
        self.entry_markup.insert(0,45)

        self.setup_var = StringVar()
        self.entry_setup = Entry(self.input_canvas, bg = "white", fg = "black", textvariable=self.setup_var)
        self.input_canvas.create_window(x+200, y+180, window=self.entry_setup)
        self.entry_setup.insert(0,20)

        self.art_var = StringVar()
        self.entry_art = Entry(self.input_canvas, bg = "white", fg = "black", textvariable=self.art_var)
        self.input_canvas.create_window(x+200, y+210, window=self.entry_art)
        self.entry_art.insert(0,0)

        self.flash_var = StringVar()
        self.entry_flash = Entry(self.input_canvas, bg = "white", fg = "black", textvariable=self.flash_var)
        self.input_canvas.create_window(x+200, y+240, window=self.entry_flash)
        self.entry_flash.insert(0,.6)

        """ Output Quote """
        self.label_totalquote = Label(self.quote_canvas, text="TOTAL QUOTE:", height=h,
                                      width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.quote_canvas.create_window(x, y, window=self.label_totalquote)
       

        self.label_itemquote = Label(self.quote_canvas, text="QUOTE PER ITEM:", height=h,
                                     width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.quote_canvas.create_window(x+220, y, window=self.label_itemquote)
        
        """ Output Quote Economics"""

        self.label_cost = Label(self.output_canvas, text="Cost per unit", height=h,
                                  width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.output_canvas.create_window(x+220, y, window=self.label_cost)

        self.label_profit = Label(self.output_canvas, text="Profit", height=h,
                                  width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.output_canvas.create_window(x+220, y+30, window=self.label_profit)

        self.label_totalcost = Label(self.output_canvas, text="Total Cost", height=h,
                                  width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.output_canvas.create_window(x, y, window=self.label_totalcost)

        self.label_totalprofit = Label(self.output_canvas, text="Total Profit", height=h,
                                  width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.output_canvas.create_window(x, y+30, window=self.label_totalprofit)

        self.label_frontcost = Label(self.output_canvas, text="Front Cost", height=h,
                                  width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.output_canvas.create_window(x, y+60, window=self.label_frontcost)

        self.label_backcost = Label(self.output_canvas, text="Back Cost", height=h,
                                    width=w, bg="black", fg="white", padx=px, pady=py, anchor="w")
        self.output_canvas.create_window(x+220, y+60, window=self.label_backcost)

        """ Create Button """
        self.quote_button = Button(self.button_canvas, bd=5, padx=50, fg="red", bg="black", text="QUOTE", font=("Ariel", 20, "bold"), command=self.create_quote,
        activebackground='blue', activeforeground='blue')
        # self.quote_button.grid(row=0, column=0)
        self.quote_button.config(relief="sunken")
        self.button_canvas.create_window(225, y+10, window=self.quote_button)

        self.save_quote_button = Button(self.button_canvas, padx=10, fg="red", text="Save", font=("Ariel", 15), command=self.save_quote)
        # self.save_quote_button.grid(row=0, column=1)
        self.save_quote_button.config(relief="sunken")
        self.button_canvas.create_window(115, y+50, window=self.save_quote_button)

        self.reset_button = Button(self.button_canvas, padx=10, fg="red", text="Exit", font=("Ariel", 15), command=self.destroy)
        # self.save_quote_button.grid(row=0, column=1)
        self.save_quote_button.config(relief="sunken")
        self.button_canvas.create_window(340, y+50, window=self.reset_button)



        # self.save_button = Button(self.button_canvas, bd=50, fg="yellow", text="SAVE QUOTE", font=("Ariel", 20), command=self.save_info)
        # self.save_button.grid(row=0, column=1)
        # self.save_button.config(relief="sunken")

# from tkinter import Label, Entry, Button, StringVar

# global quote_dict
# quote_dict = {}

def create_quote(self):
        """ Find Quantity Price """
        x = int(self.entry_quantity.get())
        price = float(self.price_var.get())
        front_colors = int(self.front_var.get())
        back_colors = int(self.back_var.get())
        markup = int(self.markup_var.get())
        art = float(self.art_var.get())
        flash = float(self.flash_var.get())
        setup = int(self.setup_var.get())
        customer = self.customer_var.get()

        
        
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
        print(x, price, front_colors, back_colors, setup, markup, art, flash)
        
        front_cost = pricer_a[front_colors]
        back_cost = pricer_a[back_colors]
        total_cost = (x * (price + front_cost + back_cost + flash)) + setup + markup + art
        margin = total_cost * (markup/100)
        total_quote = total_cost + margin
        quote_per_unit = total_quote/x

        

        self.label_totalquote["text"] = f"TOTAL QUOTE: ${total_quote:,.2f}"
        self.label_itemquote["text"] = f"QUOTE PER ITEM: ${quote_per_unit:,.2f}"
        self.label_totalcost["text"] = f"Cost:  ${total_cost:,.2f}"
        self.label_cost["text"] = f"Cost per unit:  ${total_cost/x:,.2f}"
        self.label_profit["text"] = f"Profit per Unit:  ${margin/x:,.2f}"
        self.label_totalprofit["text"] = f"Total Profit: ${margin:,.2f}"
        self.label_frontcost["text"] = f"Front Print Charge: ${front_cost:,.2f}"
        self.label_backcost["text"] = f"Back Print Charge: ${back_cost:,.2f}"

        import datetime
        quote_date = datetime.datetime.now()

        quote_dict = {
            
                      "Total_Quote": total_quote,
                      "Quote_per_Item": quote_per_unit,
                      "Cost_per_Unit": total_cost/x,
                      "Profit_per_Unit": margin/x,
                      "Cost": total_cost,
                      "Total_Profit": margin,
                      "Front_Print_Charge": front_cost,
                      "Back_Print_Charge": back_cost,
                      "Client_Name": customer,
                      "Quantity_to_Print": x,
                      "Price_of_Item": price,
                      "Front_Colors": front_colors,
                      "Back_Colors": back_colors,
                      "Markup": markup,
                      "Setup": setup,
                      "Art": art,
                      "Flash": flash
                      }
        quote_dict["Total_Quote"] =  total_quote
        quote_dict["Quote_per_Item"] =  quote_per_unit
        quote_dict["Cost_per_Unit"] =  total_cost/x
        quote_dict["Profit_per_Unit"] =  margin/x
        quote_dict["Cost"] =  total_cost
        quote_dict["Total_Profit"] =  margin
        quote_dict["Front_Print_Charge"] =  front_cost
        quote_dict["Back_Print_Charge"] =  back_cost
        quote_dict["Client_Name"] =  customer
        quote_dict["Quantity_to_Print"] =  x
        quote_dict["Price_of_Item"] =  price
        quote_dict["Front_Colors"] =  front_colors
        quote_dict["Back_Colors"] =  back_colors
        quote_dict["Markup"] =  markup
        quote_dict["Setup"] =  setup
        quote_dict["Art"] =  art
        quote_dict["Flash"] =  flash
        quote_dict["Time_Stamp"] = quote_date



        return quote_dict
        # quote_per_unit, front_cost, back_cost, 
        # total_cost, margin)



        
        
        # print(f"The total cost is ${total_cost:,.2f}, The margin is {margin:,.2f} so the quote is {total_quote:,.2f}")

       

        
       
        

#         """ to create app 
#         pyinstaller --onefile --add-binary="/System/Library/Frameworks/Tk.framework/Tk":"tk" --add-binary="/System/Library/Frameworks/Tcl.framework/Tcl":"tcl" name_of_file.py """

#     def save_info(self):

#         import datetime
#         quote_date = datetime.datetime.now()
#         # datetime(2009, 1, 6, 15, 8, 24, 78915)
#         quote_date = str(quote_date)
#         print(quote_date)


#         # And just the time:

#         # datetime.datetime.time(datetime.datetime.now())
#         client=self.client
#         # quantity = self.entry_quantity.get()
#         # lastname_info = lastname.get()
#         # age_info = age.get()
#         # age_info = str(age_info)
#         print(self.quantity)
 
#         file = open(f"{client+quote_date}.txt", "w")
#         file.write(f"Client: {self.client}\nQuantity: {self.quantity}\n")
#         file.close()
#         print("User  has been registered successfully")
 
# #   firstname_entry.delete(0, END)
# #   lastname_entry.delete(0, END)
# #   age_entry.delete(0, END)

# def create_quote(self):
#         """ Find Quantity Price """
#         x = int(self.entry_quantity.get())
#         price = float(self.price_var.get())
#         front_colors = int(self.front_var.get())
#         back_colors = int(self.back_var.get())
#         markup = int(self.markup_var.get())
#         art = float(self.art_var.get())
#         flash = float(self.flash_var.get())
#         setup = int(self.setup_var.get())
#         customer = self.customer_var.get()

        
        
#         pricer_a = {
#             0:0,
#             1: .6 if x >= 1200 else .7 if x >= 480 else .75 if x >= 240 else .85 if x >= 180 else .95
#              if x >= 120 else 1.05 if x >= 60 else 1.2 if x >= 36 else 1.6 if x >= 12 else None,

#             2: .75 if x >= 1200 else .85 if x >= 480 else .95 if x >= 240 else 1.05 if x >= 180 else 1.1
#              if x >= 120 else 1.45 if x >= 60 else 1.60 if x >= 36 else 1.90 if x >= 12 else None,

#             3: .8 if x >= 1200 else .9 if x >= 480 else 1.05 if x >= 240 else 1.15 if x >= 180 else 1.35
#              if x >= 120 else 1.75 if x >= 60 else 2 if x >= 36 else 2.25 if x >= 12 else None,

#             4: 1.1 if x >= 1200 else 1.1 if x >= 480 else 1.25 if x >= 240 else 1.4 if x >= 180 else 1.75
#              if x >= 120 else 2.15 if x >= 60 else 2.5 if x >= 36 else 2.65 if x >= 12 else None,

#             5: 1.1 if x >= 1200 else 1.2 if x >= 480 else 1.3 if x >= 240 else 1.55 if x >= 180 else 1.85
#              if x >= 120 else 2.45 if x >= 60 else 2.9 if x >= 36 else None if x >= 12 else None,

#             6: 1.35 if x >= 1200 else 1.45 if x >= 480 else 1.7 if x >= 240 else 1.85 if x >= 180 else 2.2
#              if x >= 120 else None if x >= 60 else None if x >= 36 else None if x >= 12 else None

            
#         }
#         print(x, price, front_colors, back_colors, setup, markup, art, flash)
        
#         front_cost = pricer_a[front_colors]
#         back_cost = pricer_a[back_colors]
#         total_cost = (x * (price + front_cost + back_cost + flash)) + setup + art
#         margin = total_cost * (markup/100)
#         total_quote = total_cost + margin
#         quote_per_unit = total_quote/x

        

#         self.label_totalquote["text"] = f"TOTAL QUOTE: ${total_quote:,.2f}"
#         self.label_itemquote["text"] = f"QUOTE PER ITEM: ${quote_per_unit:,.2f}"
#         self.label_totalcost["text"] = f"Cost:  ${total_cost:,.2f}"
#         self.label_cost["text"] = f"Cost per unit:  ${total_cost/x:,.2f}"
#         self.label_profit["text"] = f"Profit per Unit:  ${margin/x:,.2f}"
#         self.label_totalprofit["text"] = f"Total Profit: ${margin:,.2f}"
#         self.label_frontcost["text"] = f"Front Print Charge: ${front_cost:,.2f}"
#         self.label_backcost["text"] = f"Back Print Charge: ${back_cost:,.2f}"

#         import datetime
#         quote_date = datetime.datetime.now()

#         # quote_dict = {
            
#         #               "Total_Quote": total_quote,
#         #               "Quote_per_Item": quote_per_unit,
#         #               "Cost_per_Unit": total_cost/x,
#         #               "Profit_per_Unit": margin/x,
#         #               "Cost": total_cost,
#         #               "Total_Profit": margin,
#         #               "Front_Print_Charge": front_cost,
#         #               "Back_Print_Charge": back_cost,
#         #               "Client_Name": customer,
#         #               "Quantity_to_Print": x,
#         #               "Price_of_Item": price,
#         #               "Front_Colors": front_colors,
#         #               "Back_Colors": back_colors,
#         #               "Markup": markup,
#         #               "Setup": setup,
#         #               "Art": art,
#         #               "Flash": flash
#         #               }
#         quote_dict["Total_Quote"] =  total_quote
#         quote_dict["Quote_per_Item"] =  quote_per_unit
#         quote_dict["Cost_per_Unit"] =  total_cost/x
#         quote_dict["Profit_per_Unit"] =  margin/x
#         quote_dict["Cost"] =  total_cost
#         quote_dict["Total_Profit"] =  margin
#         quote_dict["Front_Print_Charge"] =  front_cost
#         quote_dict["Back_Print_Charge"] =  back_cost
#         quote_dict["Client_Name"] =  customer
#         quote_dict["Quantity_to_Print"] =  x
#         quote_dict["Price_of_Item"] =  price
#         quote_dict["Front_Colors"] =  front_colors
#         quote_dict["Back_Colors"] =  back_colors
#         quote_dict["Markup"] =  markup
#         quote_dict["Setup"] =  setup
#         quote_dict["Art"] =  art
#         quote_dict["Flash"] =  flash
#         quote_dict["Time_Stamp"] = quote_date



#         return quote_dict
#         # quote_per_unit, front_cost, back_cost, 
#         # total_cost, margin)



        
        
#         print(f"The total cost is ${total_cost:,.2f}, The margin is {margin:,.2f} so the quote is {total_quote:,.2f}")

       

        
       
        

# #         """ to create app 
# #         pyinstaller --onefile --add-binary="/System/Library/Frameworks/Tk.framework/Tk":"tk" --add-binary="/System/Library/Frameworks/Tcl.framework/Tcl":"tcl" name_of_file.py """

# #     def save_info(self):

# #         import datetime
# #         quote_date = datetime.datetime.now()
# #         # datetime(2009, 1, 6, 15, 8, 24, 78915)
# #         quote_date = str(quote_date)
# #         print(quote_date)


# #         # And just the time:

# #         # datetime.datetime.time(datetime.datetime.now())
# #         client=self.client
# #         # quantity = self.entry_quantity.get()
# #         # lastname_info = lastname.get()
# #         # age_info = age.get()
# #         # age_info = str(age_info)
# #         print(self.quantity)
 
# #         file = open(f"{client+quote_date}.txt", "w")
# #         file.write(f"Client: {self.client}\nQuantity: {self.quantity}\n")
# #         file.close()
# #         print("User  has been registered successfully")
 
# # #   firstname_entry.delete(0, END)
# # #   lastname_entry.delete(0, END)
# # #   age_entry.delete(0, END)

def save_quote(self):

        # import datetime
        # quote_date = datetime.datetime.now()
        
        
    password = cred.password

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

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
        
        """

            
        msg = f"Subject:  {subject}\n\n{body}"
        smtp.sendmail('EMAIL_ADDRESS', 'whitco670@icloud.com', msg)

    

        
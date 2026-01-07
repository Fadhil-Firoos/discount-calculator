from tkinter import Tk, Label, Button, Entry


def calculate_discount():

    try:
        # Get user inputs for original price
        original_price = float(entry_original_price.get())

        # Get user inputs for discount percentage
        discount_percentage = float(entry_discount_percentage.get())

        # Calculate discount amount
        discount_amount = original_price * (discount_percentage / 100)
        
        # Calculate final price after discount
        final_price = original_price - discount_amount
        
        # Update and replace label_result with final price
        label_result.config(text=f"Final Price: Rp. {final_price:.2f}")

    except ValueError:

        # Handle invalid input and replace label_result with error message
        label_result.config(text="Please enter valid numbers.")

# Create the main window
window = Tk()

# Set window title and size
window.title("Discount Calculator")
window.geometry("500x300")

# Create a label for original price
label_original_price = Label(window, text="Original Price:")
# show the label on the window
label_original_price.pack()

# Create an entry for original price
entry_original_price = Entry(window)
# show the entry on the window
entry_original_price.pack()

# Create a label for discount percentage
label_discount_percentage = Label(window, text="Discount (%):")
# show the label on the window
label_discount_percentage.pack()

# Create an entry for discount percentage
entry_discount_percentage = Entry(window)
# show the entry on the window
entry_discount_percentage.pack()

# Create a button to calculate discount and set it to running method calculate_discount
button_calculate = Button(window, text="Calculate", command=calculate_discount)
# show the button on the window and define external margin to 10 pixels
button_calculate.pack(pady=10)

# Create a label to display the result
label_result = Label(window, text="Final Price: Rp. 0.00")
# show the label on the window
label_result.pack()

# Run the main event loop
window.mainloop()

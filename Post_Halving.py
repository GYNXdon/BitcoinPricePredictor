import tkinter as tk 

# Define function to estimate price based on historical data 
def estimate_price(halving_year, max_price, target_year): 
    # Calculate the annual growth rate 
    years_since_halving = target_year - halving_year 
    annual_growth_rate = (max_price / halving_year) / (len(halving_dates) - 1) 

    # Estimate price for the target year 
    estimated_price = max_price + (annual_growth_rate * years_since_halving) 
    return estimated_price 

# Define function to run the script and display results 
def predict_price(): 
    # Project prices for every four years until 2140 
    target_year = 2140 
    result_text = "" 
    for i in range(len(halving_dates)): 
        halving_year = halving_dates[i] 
        max_price = max_prices[i] 
        for year in range(halving_year, target_year + 1, 4): 
            estimated_price = estimate_price(halving_year, max_price, year) 
            result_text += f"Estimated price for {year} based on halving in {halving_year}: ${estimated_price:.2f}\n" 

    # Update result label with the calculated results 
    result_label.config(text=result_text) 

# Create Tkinter window 
root = tk.Tk() 
root.title("Bitcoin Price Predictor") 

# Define historical halving events and corresponding maximum prices 
halving_dates = [2012, 2016, 2020] # Add more years as needed 
max_prices = [12.25, 1150, 6500] # Corresponding maximum prices in USD 

# Create a button to run the prediction 
predict_button = tk.Button(root, text="Let's Price Predict!", command=predict_price) 
predict_button.pack(pady=10) 

# Create a label to display the results 
result_label = tk.Label(root, text="") 
result_label.pack() 

# Run the Tkinter event loop 
root.mainloop()

#CodeAlpha - Task 2
#Stock Portfolio Tracker 
#Hardcoded stock prices
stock_prices = {
    "AAPL" : 160,
    "TSLA" : 280,
    "AMZN" : 140,
    "GOOGL" : 320,
    "MSFT" : 300
}
#store total investment
total_investment = 0
print("================================")
print("   STOCK PORTFOLIO TRACKER")
print("================================")
while True:

    stock = input("\nEnter Stock name (or 'done) to finish): ").upper()
    #stop th program
    if stock == "DONE":
        break


    #check stock availability
    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue
    #get quantity
    quantity = int(input("Enter quantity: "))

    #calculate investment 
    price = stock_prices[stock]
    investment = price * quantity

    #Add to total
    total_investment += investment

    print("Stock price:", price)
    print("Investment:", investment)

#Display final total
print("\n===============================")
print("Total Investment:",total_investment)
print("===============================")


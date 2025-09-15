def main():
    cost_per_item = 19.99
    quantity = 5 
    subttotal_cost = 99.95
    tax = 12.99
    total_cost = 112.94

    # YOUR CODE FOR PART 1 GOES HERE 
    # cost_per_item * quantity = subtotal_cost
    # tax = subtotal_cost * 0.13
    # total_cost = subtotal + tax


    # YOUR CODE FOR PART 2 GOES HERE
    print(f'cost_per_item = ${19.99:0.2f}')
    print(f'quantity = 5')
    print(f'subtotal_cost = ${99.95:0.2f}')
    print(f'tax = ${12.99:0.2f}')
    print(f'total_cost = ${112.94:0.2f}')



    # THIS IS THE CODE FOR PART 3
    # initial_investment = 1000
    # interest_rate = 0.035
    # investment = initial_investment
    # investment += investment * interest_rate
    # investment += investment * interest_rate
    # investment += investment * interest_rate
    # investment += investment * interest_rate
    # investment += investment * interest_rate
    # print('After 5 years, your investment will be worth ' + investment + ' dollars.')
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.

if __name__ == "__main__":
    main()
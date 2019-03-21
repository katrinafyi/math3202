from gurobipy import * 

def portfolio_optimisation():
    # multiplier for investments in each product.
    Returns = {
        'Cars (Germany)': 10.3/100 + 1,
        'Cars (Japan)': 10.1/100 + 1,
        'Computers (USA)': 11.8/100 + 1,
        'Computers (Singapore)': 11.4/100 + 1,
        'Appliances (Europe)': 12.7/100 + 1,
        'Appliances (Asia)': 12.2/100 + 1,
        'Insurance (Germany)': 9.5/100 + 1,
        'Insurance (USA)': 9.9/100 + 1,
        'Short-term bonds': 3.6/100 + 1,
        'Medium-term bonds': 4.2/100 + 1
    }
    Products = list(Returns.keys())

    filter_products = lambda p: [prod for prod in Products if p in prod]

    Cars = filter_products('Cars')
    Computers = filter_products('Computers')
    Appliances = filter_products('Appliances')
    Insurance = filter_products('Insurance')
    Bonds = filter_products('bonds')
    Germany = filter_products('Germany')
    USA = filter_products('USA')

    m = Model('Portfolio Optimisation')
    
    # dollars to invest into each product.
    X = m.addVars(Products, obj=Returns)

    # total amount to invest.
    m.addConstr(X.sum('*') == 100000)

    investment_in = lambda products_list: quicksum(X[p] for p in products_list)

    # investment requirements (1-9)
    m.addConstr(investment_in(Cars) <= 30000)
    m.addConstr(investment_in(Computers) <= 30000)
    m.addConstr(investment_in(Appliances) <= 20000)
    m.addConstr(investment_in(Insurance) >= 20000)
    m.addConstr(investment_in(Bonds) >= 25000)
    m.addConstr(X['Short-term bonds'] >= 0.4*X['Medium-term bonds'])
    m.addConstr(investment_in(Germany) <= 50000)
    m.addConstr(investment_in(USA) <= 40000)

    m.modelSense = GRB.MAXIMIZE
    m.optimize()

    print()
    print('Objective:')
    print(m.objVal)
    print()
    for name, variable in X.items():
        name_padded = "{:<21}".format(name)
        print(f'{name_padded}    {variable.x}')

if __name__ == "__main__":
    portfolio_optimisation()
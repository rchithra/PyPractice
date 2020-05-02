def state_tax(gross_income, state):
    """
    Calculate the net income after deducting federal and state tax
    :param state: State name
    :param gross_income: Gross income value
    :return: Net income
    """
    states_list = {'CA': 10, 'NJ': 8, 'NY': 12, 'TX': 4}

    # Calculate net income by deducting federal tax 10% from gross income
    net_income = gross_income - (gross_income * 0.1)

    # Calculate net income after deducting state tax
    if state in states_list:
        net_income = net_income - (gross_income * states_list[state] / 100)
        print("Your net income after all the tax deduction is: " + str(net_income))
        return net_income
    else:
        print("State not in the list")
        return None


state_tax(100000, 'NY')



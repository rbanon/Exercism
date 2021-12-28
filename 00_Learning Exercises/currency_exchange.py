# This function should return the value of the exchanged currency.
def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget/exchange_rate

# This function should return the amount of money that is left from the budget.
def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget-exchanging_value

# This function should return the total value of the given bills.
def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return denomination*number_of_bills

# This function should return the number of bills that you can get using the budget.
# You can only receive whole bills, not fractions of bills, so remember to divide accordingly.
def get_number_of_bills(budget, denomination):
    """
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget/denomination)

# This function should return the maximum value of the new currency after calculating the exchange rate plus the spread.
# Remember that the currency denomination is a whole number, and cannot be sub-divided.
# Note: Returned value should be int type.
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_rate = exchange_rate * (1.0 + spread / 100)

    total_money = exchange_money(budget, spread_rate)
    total_bills = get_number_of_bills(total_money, denomination)

    return get_value_of_bills(denomination, total_bills)

def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    spread_rate = exchange_rate * (1.0 + spread / 100)

    total_money = exchange_money(budget, spread_rate)
    to_exchange = exchangeable_value(budget, exchange_rate, spread, denomination)

    return int(total_money-to_exchange)

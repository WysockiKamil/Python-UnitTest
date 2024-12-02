def calc_tax(amount, tax_rate, age):

    if not (isinstance(amount, (int, float))):
        raise TypeError('Ammount must be type of int of float')
    if not (amount >= 0):
        raise ValueError('Amount must be positive or 0')

    if not (isinstance(tax_rate, float)):
        raise TypeError('Tax rate must be type of float')
    if not (0 < tax_rate < 1):
        raise ValueError('Tax rate must be in range from 0 to 1')

    if not (isinstance(age, int)):
        raise TypeError('The age value must be int')
    if not (age > 0):
        raise ValueError('The age value must be positive')

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount*tax_rate, 8000))
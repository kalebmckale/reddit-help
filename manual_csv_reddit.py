with open('sc_rent_prices.csv') as file:
    content = file.read().strip().split('\n')

content = [row.split(',') for row in content]
data = {col[0]: [*col[1:]] for col in zip(*content)}

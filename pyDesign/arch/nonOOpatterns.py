"""  Small procedural pattern
    (-1) for looking up 'owner' twice
    (-1) requires four lines and an indent
"""
roledict = {}
admin = 'admin'

## Standard
if 'owner' in roledict:
    owner = roledict['owner']
else:
        owner = admin

## Pythonic
owner = roledict.get('owner', admin)


"""  Bigger procedural pattern
    (-1) actual buy() is buried 2 levels deep
"""

## Standard
for item in items:
    if is_for_sale(item):
        cost = compute_cost(item)
        if cost <= wallet.money:
            buy(item)

## Pythonic
for item in items:
    if not is_for_sale(item):
        continue
    cost = compute_cost(item):
    if cost > wallet.money:
        continue
    buy(item)




"""  Bigger procedural pattern
    (-1) actual buy() is buried 2 levels deep
"""

## Standard

## Pythonic
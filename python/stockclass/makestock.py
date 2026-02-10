import stock

try:
    shares = stock.Stock('TCKT', 100, 18.02, 20.21, 380)
except:
    try:
        shares = stock.Stock('TCKT', 100, 18.02)
    except:
        try:
            shares = stock.Stock('TCKT', 18.02, 100)
        except:
            shares = stock.Stock('TCKT', 100)

print(shares)
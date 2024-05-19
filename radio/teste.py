def calculate_maximum_fo():
    max_fo = 0
    best_st, best_lx = 0, 0
    for ST in range(25):  # ST vai de 0 a 24
        for LX in range(17):  # LX vai de 0 a 16
            if ST + 2 * LX <= 40:
                FO = 30 * ST + 40 * LX
                if FO > max_fo:
                    max_fo = FO
                    best_st, best_lx = ST, LX
    return best_st, best_lx, max_fo

best_st, best_lx, max_fo = calculate_maximum_fo()
print(f"ST: {best_st}, LX: {best_lx}, FO: {max_fo}")

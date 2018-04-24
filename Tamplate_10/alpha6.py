
def run_formula(dv):
    alpha6 = dv.add_formula('alpha6', 
               "-Rank(Abs(high- low))/Rank(vwap)", is_quarterly=False, add_data=True)
    return alpha6   

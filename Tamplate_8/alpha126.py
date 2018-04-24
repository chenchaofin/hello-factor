

def run_formula(dv):
    alpha126 = dv.add_formula('alpha126', 
               "(close+high+low)/3", is_quarterly=False, add_data=True)
    return alpha126   

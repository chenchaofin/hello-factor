def run_formula(dv):
    OperatingRevenuePS = dv.add_formula('OperatingRevenuePS_J', 
               "oper_rev/total_share ", is_quarterly=False, add_data=True)
    return OperatingRevenuePS

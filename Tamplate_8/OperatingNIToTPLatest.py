def run_formula(dv):
    OperatingNIToTPLatest = dv.add_formula('OperatingNIToTPLatest_J', 
               "net_cash_flows_oper_act/tot_profit ", is_quarterly=False, add_data=True)
    return OperatingNIToTPLatest

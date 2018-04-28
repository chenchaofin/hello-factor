def run_formula(dv, param = None):
    defult_param = {'t1':3}
    if not param:
        param = defult_param


    alpha2 = dv.add_formula('alpha2', 
               "-If(empl_ben_payable>Ts_Max(empl_ben_payable,%s),turnover_ratio/net_profit,turnover_ratio/tot_oper_cost)"%(param['t1'])
               , is_quarterly=False, add_data=True)

    return alpha2

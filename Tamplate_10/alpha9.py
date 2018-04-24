def run_formula(dv, param = None):
    defult_param = {'t1':12,'t2':12}
    if not param:
        param = defult_param
    

    alpha9 = dv.add_formula('alpha9', 
            "-(vwap*12-Ts_Sum(close,%s))/Ts_Sum(close,%s)*100-close"%(param['t1'],param['t2'])
             , is_quarterly=False, add_data=True)
    return alpha9

def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':1,'t3':5}
    if not param:
        param = defult_param
        


    alpha1 = dv.add_formula('alpha1', 
                         "-If(net_profit>Delay(net_profit,%s),Delay(turnover_ratio,%s),Ts_Max(turnover_ratio,%s))"%(param['t1'],param['t2'],param['t3'])
                        , is_quarterly=False, add_data=True)


    return alpha1

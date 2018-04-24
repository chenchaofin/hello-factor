def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':10,'t3':20}
    if not param:
        param = defult_param
    

    alpha4 = dv.add_formula('alpha4',
                        " (Ts_Mean(vwap,%s)+Ts_Min(close,%s)+Ts_Max(close,%s))/(4*close)"%(param['t1'],param['t2'],param['t3'])
                        , is_quarterly=False, add_data=True)
    return alpha4

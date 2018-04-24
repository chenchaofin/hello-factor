def run_formula(dv, param = None):
    defult_param = {'t1':6,'t2':3,'t3':6}
    if not param:
        param = defult_param

    alpha2 = dv.add_formula('alpha2', 
               "-Ts_Mean(Abs(volume-Ts_Mean(volume,%s)+Pow(vwap,%s)),%s)"%(param['t1'],param['t2'],param['t3'])
               , is_quarterly=False, add_data=True)
    return alpha2

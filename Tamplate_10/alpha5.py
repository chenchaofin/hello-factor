def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':20,'t3':1}
    if not param:
        param = defult_param
    

    alpha5 = dv.add_formula('alpha5', 
                        "-Abs(close-Delay(close,%s))/Abs(Delay(close,%s))-Delay(close,%s)"%(param['t1'],param['t2'],param['t3'])
                        , is_quarterly=False, add_data=True)
    return alpha5

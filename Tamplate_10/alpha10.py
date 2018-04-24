def run_formula(dv, param = None):
    defult_param = {'t1':15,'t2':5}
    if not param:
        param = defult_param
    
    alpha10 = dv.add_formula('alpha10', 
            "-Abs(close-Delay(close,%s))/Sqrt(Delay(close,%s))"%(param['t1'],param['t2'])
             , is_quarterly=False, add_data=True)
    return alpha10

def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':5}
    if not param:
        param = defult_param
    

    alpha8 = dv.add_formula('alpha8', 
            "-(close-(Delay(vwap,%s)/Delay(close,%s)))*volume"%(param['t1'],param['t2'])
             , is_quarterly=False, add_data=True)
    return alpha8

def run_formula(dv, param = None):
    defult_param = {'t1':10,'t2':10}
    if not param:
        param = defult_param
    
    alpha7 = dv.add_formula('alpha7', 
            "-Correlation(Log(volume),vwap,%s)-(high+open-close-low)*%s"%(param['t1'],param['t2'])
             , is_quarterly=False, add_data=True)
    return alpha7

def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':5}
    if not param:
        param = defult_param
    
    alpha1 = dv.add_formula('alpha1', 
                        '(-1 * Ts_Product(close,%s)/Ts_Product(high,%s))*close'%(param['t1'],param['t2'])
                        , is_quarterly=False, add_data=True)
    
    return alpha1

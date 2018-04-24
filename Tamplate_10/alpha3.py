def run_formula(dv, param = None):
    defult_param = {'t1':5}
    if not param:
        param = defult_param
    

    alpha3 = dv.add_formula('alpha3', 
                        "-Ts_Product(high-low,%s)-close"%(param['t1'])
                        , is_quarterly=False, add_data=True)
    return alpha3

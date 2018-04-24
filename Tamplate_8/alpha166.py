def run_formula(dv, param = None):
    defult_param = {'t1':1.5,'t2':20,'t3':20,'t4':2,'t5':20,'t6':1.5}
    if not param:
        param = defult_param
    
    alpha166 = dv.add_formula('alpha166', 
               "20*Pow((20-1),%s)*Ts_Sum(close/Delay(close,1)-1-Ts_Mean(close/Delay(close,1)-1,%s),%s)/((20-1)*(20-2)*Pow(Ts_Sum(Pow(close/Delay(close,1),%s),%s),%s))"%(param['t1'],param['t2'],param['t3'],param['t4'],param['t5'],param['t6']) 
             , is_quarterly=False, add_data=True)
    
    return alpha166

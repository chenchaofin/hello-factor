def run_formula(dv):
    Volatility = dv.add_formula('Volatility_J', 
               "StdDev(turnover_ratio,20)/Ts_Mean(turnover_ratio,20) "
               , is_quarterly=False, add_data=True)
    return Volatility   


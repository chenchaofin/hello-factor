def run_formula(dv):
    CurrentAssetsRatio = dv.add_formula('CurrentAssetsRatio_J', 
               "tot_non_cur_assets/tot_assets ", is_quarterly=False, add_data=True)
    return CurrentAssetsRatio



def run_formula(dv):
    IntangibleAssetRatio = dv.add_formula('IntangibleAssetRatio_J', 
               "(intang_assets+goodwill)/tot_assets ", is_quarterly=False, add_data=True)
    return IntangibleAssetRatio   

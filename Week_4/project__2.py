import pandas as pd
cadbury = {'Refeshment' : ['CABUJRY BOURNVITA', 'CADBURY 3-IN-1 HOT CHOLATE'],
            'Confectionery' : ['TOMROM CLASSIC', 'TOMTOM STRAWBERRRY'],
            'Intermediate' : ['COCOA POWDER', 'COCOA BUTTER']}
df = pd.DataFrame(cadbury)
df.to_csv("Cadbury Nigeria.csv")
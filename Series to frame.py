import pandas as pd

emp = ["Parker", "John", "Smith", "William"]
id = [102, 107, 109, 114]   
emp_series = pd.Series(emp)
id_series = pd.Series(id)
details = {'Emp':emp_series, 'ID':id_series}
result = pd.DataFrame(details)
print(result)

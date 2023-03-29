import pandas as pd

tabela = pd.read_excel("Teste.ods")
tabela.loc[tabela["MultiplicadorImposto"] == 1.3, "MultiplicadorImposto"] = 1.5

tabela["PreçoBaseReais"] = tabela["MultiplicadorImposto"] * tabela["PreçoBaseOriginal"]
order = tabela.sort_values("PreçoBaseReais")

for i, row in tabela.iterrows():
    #print(f'{row.Produtos} - {row.PreçoBaseReais:.2f} - {row.MultiplicadorImposto:.2f}')
    if row['MultiplicadorImposto'] == 1.3:
        print(tabela)
tabela.to_excel("NovoImposto.ods", index=False)
print(tabela)
print(order)

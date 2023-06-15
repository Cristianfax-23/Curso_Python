import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

def graficando_3():
    df = pd.read_csv("/home/cristian/proyect/imitando el code/data_d4a3e41a-c8c7-423a-9929-8fb55502600e.csv")
    grafica = sns.catplot(
    data=df
    )
    plt.savefig("grafica-barra.jpg")
    plt.close()

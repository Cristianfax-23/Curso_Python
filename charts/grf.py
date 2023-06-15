import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

sns.set_style("whitegrid")

def grafica(): 
    labels = ["Colombia","Peru","Brazil"]
    value = [50000,46000,60000]

    fig, ax = plt.subplots()
    sns.barplot(
        x=labels,
        y=value
    )
    plt.title("poblacion")
    plt.savefig("graficando-pratica-.jpg")
    plt.close()

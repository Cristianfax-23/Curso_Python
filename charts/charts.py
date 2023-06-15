import matplotlib.pyplot as plt

def grafice_pie():
    labels = ["A","B","C"]
    values = [200,34,120]

    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig(".pie.jpg")
    plt.close()

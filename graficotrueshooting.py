import matplotlib.pyplot as plt

jogadores = ["Kauan Raymundo", "Betinho", "Pinheiros", "Corinthians"]
aproveitamento = [90.53, 76.6, 55.93, 56.3]

cores = ["orange", "red", "blue", "black"]

plt.figure(figsize=(8, 5))

barras = plt.bar(
    jogadores,
    aproveitamento,
    color=cores
)

plt.title("Aproveitamento de True Shooting")
plt.ylabel("True Shooting (%)")

plt.ylim(0, 100)
plt.yticks([0, 25, 50, 75, 100])

for barra, valor in zip(barras, aproveitamento):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        valor + 1,
        f"{valor:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()

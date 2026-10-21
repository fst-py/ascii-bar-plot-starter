from rich.console import Console

values = [
    ("A", 2.16),
    ("B", 4.33),
    ("C", 6.57),
    ("D", 8.71),
]


def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)

def render_bar_chart(values, width=40):
    console = Console()
    maximum = max(value for name, value in values)

    colors = ["red", "green", "blue", "yellow"]

    for i, (name,value) in enumerate(values):
        length = scale_bar(value, maximum, width)
        bar = "█" * length

        console.print(f"{name}: {bar} {value:.2f}", style=colors[i])

if __name__ == "__main__":
    render_bar_chart(values)
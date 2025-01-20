from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(
    "🤓 [link=https://www.ragibalasad.me]Ragib Al Asad", guide_style="bold cyan"
)
python_tree = tree.add("🐍 Python enthusiast", guide_style="green")
python_tree.add(
    "⭐ [link=https://github.com/ragibalasad/ragib-portfolio]ragib-portfolio"
)
python_tree.add("⭐ [link=https://github.com/ragibalasad/gocloudy]gocloudy")
python_tree.add(
    "⭐ [link=https://github.com/ragibalasad/DEVELEVEN-io/develeven-io]DEVELEVEN-io/develeven-io"
)
full_stack_tree = tree.add("🔧 Full-stack developer")
tree.add("📘 Author")

about = """\
I'm a freelance software developer, living in [link=https://www.google.com.bd/maps/place/Rangpur/@25.7497964,89.2208095,13z]Rangpur[/], Bangladesh. Other than open source software development, my passion would be [link=https://en.wikipedia.org/wiki/Livestock]Livestock[/].

[green]Follow me on twitter [bold link=https://twitter.com/RagibAlAsad]@RagibAlAsad[/]"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)

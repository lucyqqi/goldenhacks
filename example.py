from taipy import Gui

# Add a navbar to switch from one page to the other
root_md = """
<|navbar|>
# eduscribe.ai
"""
page1_md = "## Upload your file"
page2_md = "## transcript and/or translation"

pages = {
    "/": root_md,
    "page1": page1_md,
    "page2": page2_md
}
Gui(pages=pages).run(use_reloader=True)


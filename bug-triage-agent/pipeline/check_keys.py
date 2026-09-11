import solari_core.desktop as d
print([x for x in dir(d) if not x.startswith("_")])
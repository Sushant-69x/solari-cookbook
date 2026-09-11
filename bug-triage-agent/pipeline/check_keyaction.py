from solari_core.desktop import KeyAction
print(KeyAction)
print(list(KeyAction) if hasattr(KeyAction, "__iter__") else vars(KeyAction))
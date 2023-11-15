from Inventory import Inventory

invent = Inventory("store.db", "inventory")
invent.viewInventory()
invent.searchInventory()
invent.decreaseStock(1)
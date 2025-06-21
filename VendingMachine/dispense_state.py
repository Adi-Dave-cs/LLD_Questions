from vending_machine_state import VendingMachineState
from Product import Product
from coin import Coin
from note import Note

class DispenseState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
    
    def select_product(self, product):
        print("Product Already Selected. Please collect the product")
    
    def insert_coin(self, coin):
        print("Payment done. Please collect the product")
    
    def insert_note(self, note):
        print("Payment already done. Please collect the product")
    
    def dispense_product(self):
        self.vending_machine.set_state(self.vending_machine.ready_state)
        product = self.vending_machine.selected_product
        self.vending_machine.inventory.update_quantity(product,self.vending_machine.inventory.get_quantity(product)-1)
        print(f"Product dispensed: {product.name}")
        self.vending_machine.set_state(self.vending_machine.return_change_state)
    
    def return_change(self):
        print("Please collect the dispensed product first")
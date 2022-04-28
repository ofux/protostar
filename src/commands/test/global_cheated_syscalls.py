from collections import defaultdict
from typing import Dict

AddressType = int
SelectorType = int


class GlobalCheatedSyscalls:
    custom_caller_address_per_contracts: Dict[AddressType, AddressType] = defaultdict(dict)

    def set_caller_address_for_contract(self, contract_addr: AddressType, caller_addr: AddressType):
        self.custom_caller_address_per_contracts[contract_addr] = caller_addr

    def get_caller_address_for_contract(self, contract_addr: AddressType):
        return self.custom_caller_address_per_contracts[contract_addr]

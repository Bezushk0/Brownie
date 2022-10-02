from lib2to3.pgen2.literals import simple_escapes
from brownie import SimpleStorage, accounts

def test_deploy():
    account = accounts[0]

    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    assert starting_value == expected

def test_updating_store():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    
    expected = 15
    simple_storage.store(expected, {"from": account})

    assert expected == simple_storage.retrieve()

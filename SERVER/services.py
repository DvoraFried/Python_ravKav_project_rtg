import sqlite3 as sqlite_library
from collections import namedtuple
import json

database = sqlite_library.connect(database="./ravKav_DB.sqlite")
cursor = database.cursor()

Card = namedtuple('Card', ['card_id', 'user_id', 'contract', 'wallet'])
Contract = namedtuple('Contract', ['name', 'price'])

#create new rav-kav
def createCard(personId, wallet=0, contract="NONE"):
    if personId == '' or not personId.isdigit():
        return -1
    # checks contract validate
    contract_det = get_contract_by_name(contract)
    if contract == -1:
        return -1
    # add card
    add_card = '''INSERT OR REPLACE INTO cards
                   (user_id, name_contract, wallet) VALUES (?, ?, ?);
    '''
    cursor.execute(add_card, (personId, contract_det.name, wallet))
    database.commit()
    return json.dumps({"card_id": get_card_by_person_id(personId).card_id})


#get rav-ka data: person's id, contract & wallet
def getDataCard(cardId):
    get_card = '''SELECT * FROM cards
                    WHERE card_id = ?
    '''
    cursor.execute(get_card, (cardId, ))
    records = cursor.fetchall()
    if records == []:
        return -1

    card = Card(card_id=records[0][0], user_id=records[0][1], contract=records[0][2], wallet=records[0][3])
    return json.dumps({"card_id": card.card_id, "user_id": card.user_id, "contract_name": card.contract, "wallet": card.wallet})


#pay for ride
def payRide(cardId, destination):
    #checks if card exist
    card = getDataCard(cardId)
    if card == -1:
        return -1

    if destination == json.loads(card)["contract_name"]:
        return 0

    # gets destination details
    destination = get_contract_by_name(destination)
    if fillWallet(cardId, 0 - destination.price) == -1:
        return -1
    return 0


def fillWallet(cardId, sum):
    # checks if card exist
    card = getDataCard(cardId)
    if card == -1:
        return -1

    if json.loads(card)["wallet"] + sum < 0 or sum > 9999:
        return -1

    set_wallet = '''UPDATE cards
                     SET wallet = ?
                     WHERE card_id = ?
    '''
    cursor.execute(set_wallet, (json.loads(card)["wallet"] + sum, cardId))
    database.commit()
    return 0


def changeContract(cardId, newContract):
    # checks if card exist
    card = getDataCard(cardId)
    if card == -1:
        return -1

    contract = get_contract_by_name(newContract)
    if contract == -1:
        return -1

    set_contract = '''UPDATE cards
                      SET name_contract = ?
                      WHERE card_id = ?
    '''
    cursor.execute(set_contract, (contract.name, cardId))
    database.commit()
    return 0


def get_card_by_person_id(personId):
    get_card = '''SELECT * FROM cards
                        WHERE user_id = ?
            '''
    cursor.execute(get_card, (personId, ))
    records = cursor.fetchall()
    if records == []:
        return -1
    return Card(card_id=records[0][0], user_id=records[0][1], contract=records[0][2], wallet=records[0][3])


def get_contract_by_name(name):
    get_contract = '''SELECT * from contracts
                       WHERE name_contract = ?
    '''
    cursor.execute(get_contract, (name, ))
    records = cursor.fetchall()
    if records == []:
        return -1
    return Contract(name=records[0][0], price=records[0][1])


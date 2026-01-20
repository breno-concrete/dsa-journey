#revision from last day

phonebook = {}

phonebook["Breno"] = "61982744166"
phonebook["Lusiana"] = "61984749629"
phonebook["Francisco"] = "61984033326"


def find(nome):
    if phonebook.get(nome):
        print(phonebook[nome])
    else:
        print("Não encontraddo")

while True:
    src = input('Nome: ')
    find(src)
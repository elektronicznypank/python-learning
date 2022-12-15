import inspect


class MedicineDrugs:
    def __init__(self, name, nlpz, no_pain, no_fever, no_inflamation):
        self.name = name
        self.nlpz = nlpz
        self.no_pain = no_pain
        self.no_fever = no_fever
        self.no_inflamation = no_inflamation


print(inspect.signature(MedicineDrugs.__init__))
print()

paracetamol = MedicineDrugs('paracetamol', False, True, True, False)
ibuprofen = MedicineDrugs('ibuprofen', True, True, True, True)
metamizol = MedicineDrugs('metamizol', True, True, True, True)
naproxen = MedicineDrugs('naproxen', True, True, True, True)
diclofenac = MedicineDrugs('diklofenak', True, True, True, True)
tramadol = MedicineDrugs('tramadol', False, True, False, False)
nimesulid = MedicineDrugs('nimesulid', True, True, True, False)

medicine_list = [
    paracetamol,
    ibuprofen,
    metamizol,
    naproxen,
    diclofenac,
    tramadol,
    nimesulid
]

for i in medicine_list:
    if i.nlpz:
        print(f'{i.name.capitalize()} należy do grupy niesteroidowych leków przeciwzapalnych.')
    if i.no_pain:
        if i.name in ['tramadol', 'metamizol']:
            print(f'{i.name.capitalize()} działa silnie przeciwbólowo.')
        else:
            print(f'{i.name.capitalize()} działa przeciwbólowo.')
    if i.no_fever:
        print(f'{i.name.capitalize()} działa przeciwgorączkowo.')
    if i.no_inflamation:
        print(f'{i.name.capitalize()} działa przeciwzapalnie.')
    print('-' * 50)

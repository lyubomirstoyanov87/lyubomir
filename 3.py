def validate_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}

while key_materials['shards'] < 250 and key_materials['fragments'] < 250 and key_materials['motes'] < 250:
    command = input()
    materials = command.lower().split()
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1]
        if material in key_materials.keys():
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                winner = material
                break

        else:
            validate_existing(junk_materials, material)
            junk_materials[material] += quantity

key_materials[winner] -= 250
winning_item = legendary_items[winner]
key_material = dict(sorted(key_materials.items(), key=lambda el: (-el[1], el[0])))
junk_material = dict(sorted(junk_materials.items()))

print(f'{winning_item} obtained!')
print_dict(key_material, '{}: {}')
print_dict(junk_material, '{}: {}')

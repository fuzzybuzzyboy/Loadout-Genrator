from colorama import Fore, Style # Fore, Style # styles: BRIGHT, NORMAL, DIM. Fore.WHITE, Style.RESET_ALL (EXAMPLE: Fore.GREEN + Style.BRIGHT + "a")
import random, colorama
colorama.init(autoreset=True)
hammer_pump_options, frenzy_auto_options, assault_rifle_options, thunder_burst_options, ranger_pistol_options, reaper_sniper_options, nothing_options, mythic_attachment_map = (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag',), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake')), (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake')), (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake')), (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake')), (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake')), (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip'), ('None', 'Suppressor', 'Muzzle Brake')), ((), (), (), ()), {"Peter Griffin's Hammer Pump Shotgun": ('Holo-13 Optic', 'Speed Mag', 'Angled Foregrip', 'Muzzle brake'), "Oscar's Frenzy Auto Shotgun": ('Red Eye Sight', 'Drum Mag', 'Vertical Foregrip', 'Muzzle brake'), "Nisha\'s Striker AR": ('Red Eye Sight', 'Speed Mag', 'Angled Foregrip', 'Suppressor'), "Montague\'s Nemesis AR": ('P2X Optic', 'Drum Mag', 'Vertical Foregrip', 'Muzzle brake'), "Valeria\'s Hyper SMG": ('Holo-13 Optic', 'Drum Mag', 'Vertical Foregrip', 'Suppressor')}
weapon_types=['Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other', 'Health']
weapons, weapon_rarity_options= {'Shotgun': ['Hammer Pump Shotgun', 'Frenzy Auto Shotgun'], 'SMG': ['Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol', 'Lock On Pistol'], 'Assault-Rifle': ['Striker AR', 'Nemesis AR', 'Enforcer AR'], 'Sniper': ['Reaper Sniper Rifle'], 'Other': ['Grapple Blade', 'Ballistic Shield'], 'Health': ['Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit']}, {'Hammer Pump Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'], 'Frenzy Auto Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'], 'Striker AR': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'], 'Nemesis AR': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'], 'Enforcer AR': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Thunder Burst SMG': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Hyper SMG': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'], 'Ranger Pistol': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Lock On Pistol': ['Rare',], 'Reaper Sniper Rifle': ['Uncommon', 'Rare', 'Epic', 'Legendary'], 'Ballistic Shield': ['Epic',], 'Grapple Blade': ['Epic',], 'Shield Potion': ['Rare',], 'Flowberry Fizz': ['Rare',], 'Small Shield Potion': ['Uncommon',], 'Medkit': ['Uncommon',], 'Flowberry': ['Uncommmon',]}

slotone_weapon=slotone_rarity=slottwo_weapon=slottwo_rarity=slotthree_weapon=slotthree_rarity=slotfour_weapon=slotfour_rarity=slotfive_weapon=slotfive_rarity=None

def generator():
    weapon_type = random.choice(weapon_types)
    weapon = random.choice(weapons[weapon_type])
    rarity_options = weapon_rarity_options.get(weapon, [])
    if rarity_options: rarity = random.choice(rarity_options)
    else: rarity = 'idk wtf happened here but something happened and i dont care.'
    return weapon, rarity
slotone_weapon, slotone_rarity = generator()
slottwo_weapon, slottwo_rarity = generator()
slotthree_weapon, slotthree_rarity = generator()
slotfour_weapon, slotfour_rarity = generator()
slotfive_weapon, slotfive_rarity = generator()

print(Fore.CYAN + Style.BRIGHT + 'Loadout generated!\n' + Fore.WHITE + Style.RESET_ALL + f'Slot 1: {slotone_weapon}, Rarity: {slotone_rarity}\nSlot 2: {slottwo_weapon}, Rarity: {slottwo_rarity}\nSlot 3: {slotthree_weapon}, Rarity: {slotthree_rarity}\nSlot 4: {slotfour_weapon}, Rarity: {slotfour_rarity}\nSlot 5: {slotfive_weapon}, Rarity: {slotfive_rarity}')

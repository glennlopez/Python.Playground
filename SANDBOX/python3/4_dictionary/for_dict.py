npc_bob = {
    'npc_id': 11234,
    'npc_events': ['buy', 'sell', 'chat'],
    'npc_health': 100
}

for key, value in npc_bob.items():
    print("Key: {} \t Value: {}".format(key, value))
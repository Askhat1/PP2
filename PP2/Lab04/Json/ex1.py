import json

try:
    data = json.load(open('PP2\Lab04\Json\sample-data.json'))
    print("Interface Status")
    print("=" * 120)
    print(f"{'DN':<60} {'Description':<25} {'Speed':<15} {'MTU':<8}")
    print("-" * 120)
    for i in data['imdata']:
        l1_phys_if = i['l1PhysIf']['attributes']
        dn = l1_phys_if['dn']
        desc = l1_phys_if['descr']
        speed = l1_phys_if['speed']
        mtu = l1_phys_if['mtu']
        print(f"{dn:<60} {desc:<25} {speed:<15} {mtu:<8}")
except Exception as e:
    print(f"An error occurred: {e}")

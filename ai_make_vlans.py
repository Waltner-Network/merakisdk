
from meraki import DashboardAPI


dashboard = DashboardAPI(log_path="logs/")

# Get first organization
orgs = dashboard.organizations.getOrganizations()
org_id = orgs[0]['id']

# Find the network and device named "switch1"
networks = dashboard.organizations.getOrganizationNetworks(org_id)
target_net = None
switch_serial = None

for net in networks:
    devices = dashboard.networks.getNetworkDevices(net['id'])
    for dev in devices:
        if dev['model'].startswith('MS') and dev.get('name') == 'switch1':
            target_net = net
            switch_serial = dev['serial']
            break
    if target_net:
        break

if not target_net or not switch_serial:
    print("❌ Could not find switch1 in any network.")
    exit()

# Create VLANs
# vlans_to_create = [
#     {"id": 30, "name": "IT", "subnet": "192.168.30.0/24", "applianceIp": "192.168.30.1"},
#     {"id": 40, "name": "Finance", "subnet": "192.168.40.0/24", "applianceIp": "192.168.40.1"},
# ]

# for vlan in vlans_to_create:
#     print(f"Creating VLAN {vlan['id']} - {vlan['name']}")
#     dashboard.appliance.createNetworkApplianceVlan(
#         networkId=target_net['id'],
#         id=vlan['id'],
#         name=vlan['name'],
#         subnet=vlan['subnet'],
#         applianceIp=vlan['applianceIp']
#     )

# Assign ports to VLANs
# Example: ports 1–5 to VLAN 30, ports 6–10 to VLAN 40
for port_num in range(1, 6):
    dashboard.switch.updateDeviceSwitchPort(
        serial=switch_serial,
        portId=str(port_num),
        vlan=10,
        name=f"IT-Port{port_num}"
    )

for port_num in range(6, 11):
    dashboard.switch.updateDeviceSwitchPort(
        serial=switch_serial,
        portId=str(port_num),
        vlan=20,
        name=f"Finance-Port{port_num}"
    )

print("✅ VLANs created and ports assigned.")
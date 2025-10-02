import meraki

dashboard = meraki.DashboardAPI(log_path="logs/")



# Get first organization
orgs = dashboard.organizations.getOrganizations()
org_id = orgs[0]['id']

# Find the network and device named "switch1"
network = dashboard.organizations.getOrganizationNetworks(org_id)[0]

#get netwpork vlan profile, need this top get iname
# response = dashboard.networks.getNetworkVlanProfiles(network['id'])
# print(response)


#update network vlan profile
payload = {
    "networkId": network['id'],
    "name": "Default Profile",
    "iname" : "Default",
    "vlanNames" : [
        {'name': 'Data', 'vlanId': '10', 'adaptivePolicyGroup': {'id': '', 'name': None}},
        {'name': 'Voice', 'vlanId': '20', 'adaptivePolicyGroup': {'id': '', 'name': None}},
        {'name': 'Management', 'vlanId': '30', 'adaptivePolicyGroup': {'id': '', 'name': None}}
        ],
    "vlanGroups" : []
}

response = dashboard.networks.updateNetworkVlanProfile(**payload)

devices = dashboard.networks.getNetworkDevices(network['id'])
for dev in devices:
    if dev['model'].startswith('MS') and dev.get('name') == 'switch1':
        switch_serial = dev['serial']

for port_num in range(1, 6):
    dashboard.switch.updateDeviceSwitchPort(
        serial=switch_serial,
        portId=str(port_num),
        type='access',
        vlan=10,
        voiceVlan=20,
        name=f"Access Port-{port_num}"
    )

for port_num in range(6, 11):
    dashboard.switch.updateDeviceSwitchPort(
        serial=switch_serial,
        portId=str(port_num),
        type='access',
        vlan=30,
        voiceVlan=None,
        name=f"Managment Port-{port_num}"
    )
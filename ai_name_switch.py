from meraki import DashboardAPI


# Initialize dashboard connection
dashboard = DashboardAPI(log_path="logs/")

# Get organizations
orgs = dashboard.organizations.getOrganizations()
org_id = orgs[0]['id']  # Use the first org (or select one explicitly)

# Get all networks in the organization
networks = dashboard.organizations.getOrganizationNetworks(org_id)

switch_counter = 1

for net in networks:
    net_id = net['id']
    devices = dashboard.networks.getNetworkDevices(net_id)

    for device in devices:
        if device['model'].startswith('MS'):  # MS = Meraki Switch
            new_name = f"switch{switch_counter}"
            print(f"Renaming {device.get('name', device['serial'])} → {new_name}")
            dashboard.devices.updateDevice(device['serial'], name=new_name)
            switch_counter += 1
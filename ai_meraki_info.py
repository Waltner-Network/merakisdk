from meraki import DashboardAPI

# Initialize dashboard connection
dashboard = DashboardAPI(log_path="logs/", print_console=False)

# Get organizations
orgs = dashboard.organizations.getOrganizations()

print("\n📦 Organizations:")
for org in orgs:
    print(f"- Name: {org['name']}")
    print(f"  ID: {org['id']}")
    print(f"  URL: https://dashboard.meraki.com/o/{org['id']}/overview\n")

    # Get networks for this organization
    networks = dashboard.organizations.getOrganizationNetworks(org['id'])

    print("🌐 Networks:")
    for net in networks:
        print(f"- Name: {net['name']}")
        print(f"  ID: {net['id']}")
        print(f"  Type: {net.get('productTypes', 'Unknown')}")
        print(f"  Timezone: {net.get('timeZone', 'N/A')}")
        print(f"  Tags: {net.get('tags', [])}\n")

        # Get devices in this network
        devices = dashboard.networks.getNetworkDevices(net['id'])

        print("🔌 Devices:")
        for dev in devices:
            print(f"- Name: {dev.get('name', 'Unnamed')}")
            print(f"  Model: {dev['model']}")
            print(f"  MAC: {dev['mac']}")
            print(f"  Serial: {dev['serial']}")
            print(f"  IP: {dev.get('lanIp', 'N/A')}")
            print(f"  Address: {dev.get('address', 'N/A')}\n")

    print("="*50)
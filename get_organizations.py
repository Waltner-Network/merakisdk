import meraki

dashboard = meraki.DashboardAPI(suppress_logging=True)


my_orgs = dashboard.organizations.getOrganizations()

print("Organizations")
print("-" * 50)
for org in my_orgs:
    print(f"- Name: {org['name']}")
    print(f"  ID: {org['id']}")
    print(f"  URL: https://dashboard.meraki.com/o/{org['id']}/overview\n")
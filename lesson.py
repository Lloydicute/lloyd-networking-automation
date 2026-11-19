from netmiko import ConnectHandler
from router_config import get_router_device


try:
    print("Connecting to the router...")

    router_device = get_router_device()
    net_connect = ConnectHandler(**router_device)

    print("Connected successfully!")

    net_connect.enable()

    commands_to_run = [
        "show version",
        "show ip interface brief",
        "show running-config",
        "show ip route"
    ]

    for cmd in commands_to_run:
        print(f"\n--- Output for: {cmd} ---")

        output = net_connect.send_command(cmd)

        print(output)

    net_connect.disconnect()

    print("\nDisconnected successfully!")

except Exception as e:
    print(f"Connection failed: {e}")

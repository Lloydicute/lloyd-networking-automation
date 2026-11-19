from netmiko import ConnectHandler
from router_config import get_router_device


try:
    print("Connecting to the router...")
    router_device = get_router_device()
    net_connect = ConnectHandler(**router_device)
    net_connect.enable()
    commands_to_run = [
        "show running-config",
        "show ip interface brief",
        "show version",
    ]
    for cmd in commands_to_run:
        print(f"\nExecuting command: {cmd} ---")
        output = net_connect.send_command(cmd)
        print(output)


    net_connect.disconnect()
    print("\nDisconnected successfully.")
except Exception as e:
    print(f"Connection failed: {e}")
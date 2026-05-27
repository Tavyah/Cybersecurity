import subprocess, argparse

#TODO: Need to implement command injection prevention. Currently able to pass interface;ls.... Not good.

def main() -> None:
    args = get_arguments()
    for_linux(args.network_interface, args.new_mac_address)   

def get_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--network_interface', help= 'Name of the interface to change it\'s MAC address')
    parser.add_argument('-m', '--new_mac_address', help='The new MAC address that you want to change to. Format: 00:11:22:33:44:55')
    return parser.parse_args()

def for_linux(network_device_name: str, new_mac_address: str) -> None:
    print(f'[+] Changing MAC address for {network_device_name} to {new_mac_address}')
    subprocess.call(["ifconfig", network_device_name, "down"])
    subprocess.call(["ifconfig", network_device_name,'hw', "ether", new_mac_address])
    subprocess.call(["ifconfig", network_device_name, "up"])
    print(subprocess.check_output(['ifconfig', network_device_name]))

if __name__ == "__main__":
    main()
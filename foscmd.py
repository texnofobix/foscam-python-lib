import argparse
import sys
import ConfigParser
from foscam import FoscamCamera
import json


Config = ConfigParser.ConfigParser()
Config.read("./camera.cfg")

myCams=[]
for section in Config.sections():
    hostname = Config.get(section,'hostname')
    port = Config.getint(section,'port')
    username = Config.get(section,'username')
    password = Config.get(section,'password')
    myCams.append(FoscamCamera(hostname, port, username, password, verbose=False))

def main():
    for cam in myCams:
        if args.get_ip_info:
            print cam.get_ip_info()
        if args.get_system_time:
            print cam.get_system_time()
        if args.get_dev_name:
            print cam.get_dev_name()
        if args.enable_motion_detection:
            print cam.enable_motion_detection()
        if args.disable_motion_detection:
            print cam.disable_motion_detection()
        if args.get_dev_state:
            print(json.dumps(cam.get_dev_state()[1]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--get_ip_info", action="store_true", help="Gets camera info")
    group.add_argument("-t", "--get_system_time", action="store_true", help="Gets camera time")
    group.add_argument("-n", "--get_dev_name", action="store_true", help="Gets camera name")
    group.add_argument("-M", "--enable_motion_detection", action="store_true", help="Turns on motion detection")
    group.add_argument("-m", "--disable_motion_detection", action="store_true", help="Turns off motion detection")
    group.add_argument("-s", "--get_dev_state", action="store_true", help="Gets dev state")
    args = parser.parse_args()
    sys.exit(main())

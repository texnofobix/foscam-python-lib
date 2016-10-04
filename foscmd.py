#!/usr/bin/env python
import argparse
import sys
import ConfigParser
from foscam import FoscamCamera
import json

def connectCamera(section):
    hostname = Config.get(section,'hostname')
    port = Config.getint(section,'port')
    username = Config.get(section,'username')
    password = Config.get(section,'password')
    return FoscamCamera(hostname, port, username, password, verbose=False)

if __name__ == '__main__':
    Config = ConfigParser.ConfigParser()
    Config.read("./camera.cfg")
    myCams=[]
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--get_ip_info", action="store_true", help="Gets camera info")
    group.add_argument("-t", "--get_system_time", action="store_true", help="Gets camera time")
    group.add_argument("-n", "--get_dev_name", action="store_true", help="Gets camera name")
    group.add_argument("-M", "--enable_motion_detection", action="store_true", help="Turns on motion detection")
    group.add_argument("-m", "--disable_motion_detection", action="store_true", help="Turns off motion detection")
    group.add_argument("-s", "--get_dev_state", action="store_true", help="Gets dev state",)
    group.add_argument("-L", "--enable_infra_led", action="store_true", help="Turns on Infrared LED")
    group.add_argument("-l", "--disable_infra_led", action="store_true", help="Turns off Infrared LED")
    group.add_argument("-a", "--get_product_all_info", action="store_true", help="Gets all info")
    parser.add_argument("-c", "--config", default=False, type=str, help="Config file")
    parser.add_argument('cameraname', nargs="?", default=False, type=str, help='Sets individual camera')
    args = parser.parse_args()
    #print args

    Config = ConfigParser.ConfigParser()
    if args.config:
        Config.read(args.config)
    else:
        Config.read("./camera.cfg")

    myCams=[]
    
    for section in Config.sections():
        if args.cameraname == section:
            # If only one camera called, no need to connect to all
            myCams.append(connectCamera(section))
            break

        if args.cameraname is False:
            myCams.append(connectCamera(section))

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
        if args.enable_infra_led:
            print cam.enable_infra_led()
        if args.disable_infra_led:
            print cam.disable_infra_led()
        if args.get_product_all_info:
            print cam.get_product_all_info()

    #sys.exit(0)


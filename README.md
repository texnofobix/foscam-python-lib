foscam-python-lib
=================

Foscam Python Library for H.264 IP Cameras (FI9821W/P,HD816W/P,C2)

TODO
----
1. Package setup.py and upload to pypi.
2. Support more camera models.

Getting Started
---------------
### Simple example:
Here is a simple example to move camera lens up and stop after 1s.
```python
    from foscam import FoscamCamera
    from time import sleep

    mycam = FoscamCamera('192.168.0.110', 88, 'admin', 'foscam')
    mycam.ptz_move_up()
    sleep(1)
    mycam.ptz_stop_run()
```

### Asynchronous feature:
This example uses the asynchronous feature provided by ``FoscamCamera``.
Normally, a command is sent synchronously, waiting for results and blocking the main thread.
By initializing ``FoscamCamera`` with `daemon=True` (defaults to False), commands are sent asynchronously.
```python
    mycam = FoscamCamera('192.168.0.110', 88, 'admin', 'foscam', daemon=True)
    mycam.get_ip_info()
    mycam.get_port_info()
    mycam.refresh_wifi_list()
```

### Send command with callback:
This example illustrates the use of a callback function when the command completes.
```python
    from foscam import FoscamCamera, FOSCAM_SUCCESS
    def print_ipinfo(returncode, params):
        if returncode != FOSCAM_SUCCESS:
            print 'Failed to get IPInfo!'
            return
        print 'IP: %s, Mask: %s' % (params['ip'], params['mask'])

    mycam = FoscamCamera('192.168.0.110', 88, 'admin', 'foscam', daemon=False)
    mycam.get_ip_info(print_ipinfo)
```

### foscmd usage:
You can call this library by creating a camera.cfg file
```
[camera0]
hostname: 192.168.9.30
port: 443
username: admin
password: password

```
 

```
python foscmd.py -h
usage: foscmd.py [-h] [-i | -t | -n | -M | -m | -s] [cameraname]

positional arguments:
  cameraname            Sets individual camera

optional arguments:
  -h, --help            show this help message and exit
  -i, --get_ip_info     Gets camera info
  -t, --get_system_time
                        Gets camera time
  -n, --get_dev_name    Gets camera name
  -M, --enable_motion_detection
                        Turns on motion detection
  -m, --disable_motion_detection
                        Turns off motion detection
  -s, --get_dev_state   Gets dev state

```

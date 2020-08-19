import datetime
import os
import time

import serial


class Device:
    def __init__(self, uhub_location, uhub_port, arduino_serial):
        self.uhub_location = uhub_location
        self.uhub_port = uhub_port
        self.arduino_serial = arduino_serial
        self.serial = serial.Serial(arduino_serial, 9600)

    def run_trezorctl(self, cmd: str):
        full_cmd = "trezorctl "
        full_cmd += cmd
        print("[software/trezorctl] Running '{}'".format(full_cmd))
        os.system(full_cmd)

    def check_version(self):
        self.run_trezorctl("get-features | grep version")

    def reboot(self):
        self.power_off()
        self.power_on()

    def power_on(self):
        self.now()
        print("[hardware/usb] Turning power on...")
        os.system(
            "uhubctl -l {} -p {} -a on > /dev/null".format(
                self.uhub_location, self.uhub_port
            )
        )
        self.wait(3)

    def power_off(self):
        self.now()
        print("[hardware/usb] Turning power off...")
        os.system(
            "uhubctl -l {} -p {} -r 100 -a off > /dev/null".format(
                self.uhub_location, self.uhub_port
            )
        )
        self.wait(3)

    def touch(self, location, action):
        raise NotImplementedError

    @staticmethod
    def wait(seconds):
        Device.now()
        print("[software] Waiting for {} seconds...".format(seconds))
        time.sleep(seconds)

    @staticmethod
    def now():
        print("\n[timestamp] {}".format(datetime.datetime.now()))

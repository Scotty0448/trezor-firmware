from .device import Device


class TrezorT(Device):
    def update_firmware(self, file=None):
        if file:
            trezorctlcmd = "firmware-update -s -f {} &".format(file)
            print("[software] Updating the firmware to {}".format(file))
        else:
            trezorctlcmd = "firmware-update &"
            print("[software] Updating the firmware to latest")

        self.wait(5)
        self.run_trezorctl(trezorctlcmd)
        # upgrading to 2.3.2 toook about 80s - let's give a bit extra to be sure
        self.wait(120)
        self.check_version()

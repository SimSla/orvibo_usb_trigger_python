import subprocess

# DEVICE_NAME = "USB PnP Sound Device"

def usb_connected(device_name):
    """Checks whether a USB device by that name is connected.
    @param  device_name The exact and complete name of the USB device.
    @return True if a connected USB device exactly matches device_name.
            False otherwise.
    """
    try:
        # ioreg -p IOUSB shows connected USB interfaces.
        response = subprocess.check_output("ioreg -p IOUSB | grep '+-o %s@'" % device_name, shell=True) 
        return response != ""  # Just in case.
    except:
        # Grep may exit with nonzero exit code if no lines match.
        return False 
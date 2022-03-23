from utils.devices_utils import generate_mac_addr,get_dev_type
from utils.db import create_db, add_device, get_device, add_endpoint

async  def add_10_devices():
    try:
        for i in range(0, 10):
            dev_id = generate_mac_addr()
            dev_type = get_dev_type()
            add_device(dev_id, dev_type)
            device = get_device(dev_id,dev_type)[-1]

            if i<5:
                add_endpoint(device[0], f"Endpoint for device {device[0]}" )
        return "ok"
    except Exception as e:
        return str(e)
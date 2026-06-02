def mask_ip(ip):
    parts = ip.split('.')
    if len(parts) == 4:
        parts[-1] = '0'
        return '.'.join(parts)
    return ip

class FilterModule(object):
    def filters(self):
        return {'mask_ip': mask_ip}

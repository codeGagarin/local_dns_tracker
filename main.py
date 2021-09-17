import dns.resolver

from keys import Keys


class Alarmer:
    def alarm(self, name: str):
        print(f'Follow name as not resolved: {name}')

    def send(self):
        pass


def resolve(name: str):
    try:
        dns.resolver.query(name, dns.rdatatype.A)
    except dns.resolver.NXDOMAIN:
        return False
    return True


def main():
    alarmer = Alarmer()
    for sub_name in Keys.SRV_LIST:
        full_name = f'{sub_name}.{Keys.DOMAIN}'
        if not resolve(full_name):
            alarmer.alarm(full_name)
        alarmer.send()





if __name__ == '__main__':
    main()

import dns.resolver

def main():
    answers = dns.resolver.query('station-hotels.ru', dns.rdatatype.A)
    for rdata in answers:
        print('Host', 'has preference', rdata)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

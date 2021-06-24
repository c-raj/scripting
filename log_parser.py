def parser(lines, filter='robots.txt'):
    for line in lines:
        if filter in line:  # we only process lines that match with filter
           fields = line.split(' ')
           # field 1 is client IP
           client_ip = fields[0]
           # field 9 is response status code
           status_code = fields[8]
           print(f'{client_ip} {status_code}')


if __name__ == "__main__":
    lines = []
    with open('access.log', 'r') as f:
        lines = f.readlines()
    parser(lines)
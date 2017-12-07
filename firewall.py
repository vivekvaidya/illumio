import csv

class Firewall:
    'Firewall class for rules'
    def __init__(self, path, res, ranges):
        self.path = path
        self.res = res
        self.ranges = ranges

        buffer = []
        ip_return = []
        concat_string = ""

        def expand_ip(ip1, ip2):

            ip1 = map(int, ip1)
            ip2 = map(int, ip2)
            ip_list = []

            while ip1 < ip2:
                ip1[3] += 1
                if ip1[3] == 256:
                    ip1[3] = 0
                    ip1[2] += 1
                    if(ip1[2]) == 256:
                        ip1[2] = 0
                        ip1[1] += 1
                        if(ip1[3]) == 256:
                            ip1[1] = 0
                            ip1[0] += 1 

                ip1_str = map(str, ip1)
                ip_list.append(ip1_str)

            for i in range(0, len(ip_list)):
                ip_list[i] = '.'.join(ip_list[i])
            
            return ip_list

        with open(path, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                concat_string = row[0] + row[1] + row[2] + row[3]
                if '-' not in concat_string:
                    res[concat_string] = 1
                else:
                    buffer.append(row)
                    for x in buffer:
                        if '-' in x[2]:
                            split_buffer = x[2].split('-')
                            for i in range(int(split_buffer[0]), int(split_buffer[1])):
                                buffer.append([x[0], x[1], str(i), x[3]])
                        if '-' in x[3]:
                            split_buffer = x[3].split('-')
                            ip_return = expand_ip(split_buffer[0].split('.'), split_buffer[1].split('.'))
                            for i in range(0, len(ip_return)):
                                buffer.append([x[0], x[1], x[2], ip_return[i]])
                        concat_range_string = ''.join(x)
                        ranges[concat_range_string] = 2

    def accept_packet(self, direction, protocol, port, ip_address):
        concat_input = direction + protocol + str(port) + ip_address
        if(concat_input in res.keys() or concat_input in ranges.keys()):
            return True
        return False

res = {}
ranges = {}
fw = Firewall("file.csv", res, ranges)
print(fw.accept_packet("outbound", "udp", 200, "192.168.1.5"))
print(fw.accept_packet("inbound", "udp", 65520, "192.168.8.255"))
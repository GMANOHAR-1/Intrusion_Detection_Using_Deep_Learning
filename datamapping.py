import json

data = "30,udp,private,SF,172,0,0,0,0,0,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00"
data_list = data.split(',')

# Mappings for the columns
protocol_type_mapping = {'icmp': 0, 'tcp': 1, 'udp': 2}
service_mapping = {'IRC': 0, 'X11': 1, 'Z39_50': 2, 'auth': 3, 'bgp': 4, 'courier': 5, 'csnet_ns': 6, 'ctf': 7, 'daytime': 8, 'discard': 9, 'domain': 10, 'domain_u': 11, 'echo': 12, 'eco_i': 13, 'ecr_i': 14, 'efs': 15, 'exec': 16, 'finger': 17, 'ftp': 18, 'ftp_data': 19, 'gopher': 20, 'hostnames': 21, 'http': 22, 'http_443': 23, 'http_8001': 24, 'imap4': 25, 'iso_tsap': 26, 'klogin': 27, 'kshell': 28, 'ldap': 29, 'link': 30, 'login': 31, 'mtp': 32, 'name': 33, 'netbios_dgm': 34, 'netbios_ns': 35, 'netbios_ssn': 36, 'netstat': 37, 'nnsp': 38, 'nntp': 39, 'ntp_u': 40, 'other': 41, 'pm_dump': 42, 'pop_2': 43, 'pop_3': 44, 'printer': 45, 'private': 46, 'red_i': 47, 'remote_job': 48, 'rje': 49, 'shell': 50, 'smtp': 51, 'sql_net': 52, 'ssh': 53, 'sunrpc': 54, 'supdup': 55, 'systat': 56, 'telnet': 57, 'tim_i': 58, 'time': 59, 'urh_i': 60, 'urp_i': 61, 'uucp': 62, 'uucp_path': 63, 'vmnet': 64, 'whois': 65}
flag_mapping = {'OTH': 0, 'REJ': 1, 'RSTO': 2, 'RSTOS0': 3, 'RSTR': 4, 'S0': 5, 'S1': 6, 'S2': 7, 'S3': 8, 'SF': 9, 'SH': 10}

# Convert to integers based on mappings
protocol_type = protocol_type_mapping[data_list[1]]
service = service_mapping[data_list[2]]
flag = flag_mapping[data_list[3]]

# Create a dictionary with column names as keys and corresponding values
json_data = {
    'duration': float(data_list[0]),
    'protocol_type': protocol_type,
    'service': service,
    'flag': flag,
    'src_bytes': int(data_list[4]),
    'dst_bytes': int(data_list[5]),
    'land': int(data_list[6]),
    'wrong_fragment': int(data_list[7]),
    'urgent': int(data_list[8]),
    'hot': int(data_list[9]),
    'srv_count': int(data_list[10]),
    'serror_rate': float(data_list[11]),
    'srv_serror_rate': float(data_list[12]),
    'rerror_rate': float(data_list[13]),
    'srv_rerror_rate': float(data_list[14]),
    'same_srv_rate': float(data_list[15]),
    'diff_srv_rate': float(data_list[16]),
    'srv_diff_host_rate': float(data_list[17]),
    'dst_host_count': int(data_list[18]),
    'dst_host_srv_count': int(data_list[19]),
    'dst_host_same_srv_rate': float(data_list[20]),
    'dst_host_diff_srv_rate': float(data_list[21]),
    'dst_host_same_src_port_rate': float(data_list[22]),
    'dst_host_srv_diff_host_rate': float(data_list[23]),
    'dst_host_serror_rate': float(data_list[24]),
    'dst_host_srv_serror_rate': float(data_list[25]),
    'dst_host_rerror_rate': float(data_list[26]),
    'dst_host_srv_rerror_rate': float(data_list[27])
}

# Convert to JSON
json_output = json.dumps(json_data)
print(json_output)

#!/usr/bin/env python3

import struct
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(5)
# s.connect(('ModBus', 8899))
# s.sendall(b'\x55\xAA\x55\x00\x25\x80\x03\xA8') # For USR initialize
# s.close()

client = ModbusClient(host='ModBus', port=8899, framer=ModbusFramer)

kwargs = {'unit': 1}
result = client.read_input_registers(6, 1, **kwargs)

byte_string = b''.join([x.to_bytes(2, byteorder='big') for x in result.registers])
value = struct.unpack('>H', byte_string)[0]

print(value)

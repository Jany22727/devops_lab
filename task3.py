import json
import psutil
from config import interval
from config import output
from config import output_file_name
from datetime import datetime
from time import sleep
from prettytable import PrettyTable


def system_state():
    ''' Show system information'''
    t = str(datetime.strftime(datetime.now(), "%H:%M:%S"))
    d = str(datetime.strftime(datetime.now(), "%d.%m.%Y"))
    cpu = str(psutil.cpu_percent(interval=1))
    memory = (psutil.virtual_memory().total/(1024*1024))
    memory = str(format(memory, '.8f'))
    v_memory = str(psutil.virtual_memory().percent)
    io_read = psutil.disk_io_counters()[2]/(1024*1024)  # (read_bytes )
    io_read = str(format(io_read, '.8f'))
    io_write = psutil.disk_io_counters()[3]/(1024*1024)  # (write_bytes)
    io_write = str(format(io_write, '.8f'))
    net_l = str((psutil.net_connections()[1]).laddr[0])
    net_r = str((psutil.net_connections()[1]).laddr[1])
    net_s = str((psutil.net_connections()[1]).status)
    return [count, t, d, cpu, memory, v_memory,
            io_read, io_write, net_l, net_r, net_s]


def PT(x):
    '''Create pretty tabble'''
    mpt = PrettyTable()
    mpt.field_names = [
                      "Snpsh#", "Time", "Date", "CPU",
                      "Memory MB", "Memory %", "IO read MB",
                      "IO write MB", "local IP", "PORT", "Status"
                      ]
    mpt.add_row(x)
    return mpt.get_string()


def write_txt(z):
    '''Write information in txt file'''
    out_file = open(output_file_name, "a")
    out_file.write(z + '\n')
    out_file.close()


def write_json(y):
    '''Write  information in json file'''
    out_file = open(output_file_name, "a")
    out_file.write(json.dumps(y + '\n'))
    out_file.close()


count = 0

if output == "txt":
    while True:
        write_txt(PT(system_state()))
        count += 1
        sleep(interval)


if output == "json":
    while True:
        write_json(PT(system_state()))
        count += 1
        sleep(interval)

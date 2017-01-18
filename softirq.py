# -*- coding:utf-8 -*-
#    author    :   丁雪峰
#    time      :   2017-01-17 10:22:22
#    email     :   fengidri@yeah.net
#    version   :   1.0.1
import time

def proc_softirqs():
    SOFTIRQS = {}

    lines = open('/proc/softirqs').readlines()

    cpus = lines[0].split()

    for line in lines[1:]:
        line = line.strip()
        irq, value = line.split(':')


        value = value.split()

        SOFTIRQS[irq] = T = {}

        for i, cpu in enumerate(cpus):
            T[cpu] = value[i]
    return SOFTIRQS

def show_diff(old, new):
    valuelen = 5
    table = []

    cpuslist = old.values()[0].keys()
    cpuslist.sort(key = lambda key: int(key[3:]))

    irqlist = old.keys()
    irqlist.sort()

    table.append(cpuslist)

    for irq in irqlist:
        cpus = old[irq]
        line = [irq.rjust(12)]
        table.append(line)
        for cpu in cpuslist:
            value = cpus[cpu]
            value = int(new[irq][cpu]) - int(value)
            value = str(value).rjust(valuelen)
            line.append(value)

    table[0] = [x.rjust(valuelen) for x in cpuslist]
    table[0].insert(0, ' ' * 12)
    for line in table:
        print ' '.join(line)
    print ''



def main():
    softirqs = proc_softirqs()
    while True:
        time.sleep(1)

        _softirqs = proc_softirqs()
        show_diff(softirqs, _softirqs)
        softirqs = _softirqs




main()

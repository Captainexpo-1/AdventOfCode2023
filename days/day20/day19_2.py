import queue

import AOC_Helpers as util
import cProfile
from collections import deque

profiler = cProfile.Profile()
profiler.enable()

LOW = 0x00
HIGH = 0xFF
NO_VAL = -1

f = util.read_file("../data/20.txt")
fm = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
f = f.split("\n")

broadcaster = [i for i in f if i.find("broadcast") != -1]
broadcaster = {"src": "broad", "broad": None, "sig": [i.replace(",", "") for i in broadcaster[0].split(" ")[2:]],
               "val": LOW}
print(broadcaster)

# parsing
flip_flops = {
    i.split(" ")[0][1:]: {"src": i.split(" ")[0][1:], "sig": [j.replace(",", "") for j in i.split(" ")[2:]], "val": LOW}
    for i in f if
    i[0] == '%'}
conjunctors = {
    i.split(" ")[0][1:]: {"src": i.split(" ")[0][1:], "sig": [j.replace(",", "") for j in i.split(" ")[2:]], "val": {}}
    for i in f if
    i[0] == '&'}
all_lbls = []
all_lbls.extend([i for i in flip_flops.keys()])
all_lbls.extend([i for i in conjunctors.keys()])
conjunctor_memories = {i: {} for i in conjunctors.keys()}
print(flip_flops)
print(conjunctors)
print(all_lbls)
print(conjunctor_memories, type(conjunctor_memories))
pulse_queue = deque()


def init_conjunctors() -> None:
    for cur_conj in conjunctors.keys():
        for other_conj in conjunctors.keys():
            if cur_conj != other_conj:
                if cur_conj in conjunctors[other_conj]["sig"]:
                    conjunctor_memories[cur_conj][other_conj] = LOW

        for cur_flop in flip_flops.keys():
            if cur_conj in flip_flops[cur_flop]["sig"]:
                conjunctor_memories[cur_conj][cur_flop] = LOW


init_conjunctors()
print(conjunctor_memories)


def get_mod(lbl):
    if lbl in list(flip_flops.keys()):
        return {"type": "flp", "val": flip_flops[lbl]}
    elif lbl in list(conjunctors.keys()):
        return {"type": "con", "val": conjunctors[lbl]}
    else:
        return broadcaster


def inv_val(val):
    return HIGH if val == LOW else LOW


def send_individual(source, val, dest: str):
    if dest in conjunctors.keys():
        conjunctor_memories[dest][source] = val # CORRECT
        do_low = True
        for val in conjunctor_memories[dest].values():
            if val == LOW:
                do_low = False
        conjunctors[dest]["val"] = LOW if do_low else HIGH
        #if dest == "con": print(conjunctor_memories["con"])
        pulse_queue.append(conjunctors[dest])
    elif dest in flip_flops.keys():
        if val == LOW:
            pulse_queue.append(flip_flops[dest])
            flip_flops[dest]["val"] = inv_val(flip_flops[dest]["val"])


def send_pulse(pulse: dict):
    #print("SIG",pulse["sig"])
    for i in pulse["sig"]:  # for every output
        if "broad" in list(pulse.keys()):  # if pulse is sent by broadcast
            # is broadcast
            print("broadcaster", ("-low" if pulse["val"] == LOW else "-high")+"->",i)
            send_individual(pulse["src"], pulse["val"], i)
        elif pulse["val"] == HIGH or pulse["val"] == LOW:
            print(pulse["src"], ("-low" if pulse["val"] == LOW else "-high")+"->",i)
            send_individual(pulse["src"], pulse["val"], i)
        else:
            pass


low_pulses = 1000
high_pulses = 0
print("button", "-low"+"->","broadcaster")

def push_button():
    global low_pulses
    global high_pulses
    pulse_queue.append(broadcaster)

    while pulse_queue:
        pulse = pulse_queue.popleft()
        if pulse["val"] == HIGH: high_pulses += len(pulse["sig"])
        if pulse["val"] == LOW: low_pulses += len(pulse["sig"])
        send_pulse(pulse)
        # print("PULSE", pulse)
    print(low_pulses * high_pulses)


for i in range(1000):
    push_button()
profiler.disable()
#profiler.print_stats(sort="cumulative")

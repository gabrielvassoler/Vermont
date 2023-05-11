import json
import numpy as np
from datetime import datetime


for i in range(0,35):

    senders = {}
    results = {}
    receivers = []
    last_sender = ''
    last_receiver = ''
    dtimes = []

    with open('Outcomes-1000/Reachability/Exp{}/results/sender.json'.format(i)) as f:
        senders = json.load(f)

    with open('Outcomes-1000/Reachability/Exp{}/results/1result.json'.format(i)) as f:
        results = json.load(f)
    c = 0
    for x in results:
        for a in results[x]:
            if a["processing_times"] != []:
                receivers.append(datetime.strptime(a["processing_times"][0], "%H:%M:%S.%f"))
            else:
                c += 1
    print(c)

    last_sender = datetime.strptime(senders["0"][len(senders["0"])-1], "%H:%M:%S.%f")

    receivers.sort()

    last_receiver = receivers[len(receivers)-1]
    print((last_receiver-last_sender).total_seconds())

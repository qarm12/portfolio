from scapy import IP, TCP
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def generate_ipv4():
    return '.'.join([str(random.randint(0, 255)) for _ in range(4)])

# Example packet generation
packet_ = IP(dst=generate_ipv4()) / TCP()
packet_.show()

def Model(packet):
    data = pd.read_csv('log2.csv')
    print(data.head(10))
    print(data.info())
    print(data.describe())

    # Transforming 'Action' to numeric values
    data = data.replace({'Action': {'allow': 1, 'deny': 2, 'drop': 3, 'reset-both': 4}})

    # Dropping unnecessary columns
    columns_to_drop = ['Bytes', 'Bytes Received', 'Elapsed Time (sec)', 'pkts_sent', 'pkts_received']
    data1 = data.drop(labels=columns_to_drop, axis=1, errors='ignore')

    x = data1[['Source Port', 'Destination Port', 'Bytes Sent', 'NAT Source Port', 'NAT Destination Port']]
    y = data1['Action']
    train_data, test_data, train_labels, test_labels = train_test_split(x, y, random_state=42)

    # Using Logistic Regression for multi-class classification
    firewall = LogisticRegression(multi_class='multinomial', solver='lbfgs')
    firewall.fit(train_data, train_labels)

    # Packet DataFrame
    packet_data = pd.DataFrame({
        'Source Port': [packet.sport],
        'Destination Port': [packet.dport],
        'Bytes Sent': [len(packet)],
        'NAT Source Port': [packet.sport],
        'NAT Destination Port': [packet.dport]
    })

    # Make a prediction
    f_prediction = firewall.predict(packet_data)
    f_prediction_proba = firewall.predict_proba(packet_data)

    # Ensuring prediction validity
    #print(f"Predicted class: {f_prediction}")
    print(f"Class probabilities: {f_prediction_proba}")

    for x in f_prediction:
        if x == 1:
            print('Firewall: allow')
        elif x == 2:
            print('Firewall: deny')
        elif x == 3:
            print('Firewall: drop')
        elif x == 4:
            print('Firewall: reset-both')
        else:
            raise ValueError('Unknown action predicted')

Model(packet=packet_)

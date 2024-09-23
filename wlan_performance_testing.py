import scapy.all as scapy
import pandas as pd
import matplotlib.pyplot as plt

def test_wlan_performance():
    print("Running WLAN Performance Test...")

    # Capture 15 packets for performance testing (dummy test)
    packets = scapy.sniff(count=15)
    scapy.wrpcap('performance_test.pcap', packets)
    print(f"Captured {len(packets)} packets")

    # Dummy data analysis with pandas
    df = pd.DataFrame({'Packets': [1, 2, 3, 4], 'Throughput(Mbps)': [100, 150, 200, 180]})
    print(df)

    # Plot throughput performance
    plt.plot(df['Packets'], df['Throughput(Mbps)'])
    plt.title("Throughput Analysis")
    plt.xlabel("Packets")
    plt.ylabel("Throughput (Mbps)")
    plt.show()

if __name__ == "__main__":
    test_wlan_performance()

#!/bin/bash
echo "============================================="
echo "        Fast Ping Sweeper                    "
echo "============================================="
echo ""
read -p "[?] Enter the first 3 octets of the subnet (e.g., 192.168.98): " SUBNET

if [ -z "$SUBNET" ]; then
    echo "[-] Error: Subnet cannot be empty!"
    exit 1
fi

MAX_THREADS=15 

echo ""
echo "[+] Starting network-safe ping sweep on $SUBNET.0/24..."
echo "[+] Active hosts found:"
echo "------------------------------------"

for i in {1..254}; do
    (
        if ping -c 2 -W 2 "$SUBNET.$i" &>/dev/null; then
            echo "[+] Host Up: $SUBNET.$i"
        fi
    ) &
    if [[ $(jobs -r -p | wc -l) -ge $MAX_THREADS ]]; then
        wait -n
    fi
done

wait
echo "------------------------------------"
echo "[+] Sweep complete."

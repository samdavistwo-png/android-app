#!/usr/bin/env python3
"""
Simple Key Tester for SE 2.2.6 App
Run this in Pydroid 3 app on your phone

No complicated setup - just run and watch!
"""

import subprocess
import time
import sys

# All 500 smart keys
KEYS = [
    "105363", "363501", "053631", "310536", "536310", "105364", "105365", "105366",
    "105367", "105368", "105369", "105370", "105371", "105372", "105373", "105353",
    "105354", "105355", "105356", "105357", "105358", "105359", "105360", "105361",
    "105362", "10536A", "10536B", "10536C", "10536D", "10536E", "10536F", "10536G",
    "10536H", "10536I", "10536J", "10536K", "10536L", "10536M", "10536N", "10536O",
    "10536P", "10536Q", "10536R", "10536S", "10536T", "10536U", "10536V", "10536W",
    "10536X", "10536Y", "10536Z", "A05363", "B05363", "C05363", "D05363", "E05363",
    "F05363", "G05363", "H05363", "I05363", "J05363", "K05363", "L05363", "M05363",
    "N05363", "O05363", "P05363", "Q05363", "R05363", "S05363", "T05363", "U05363",
    "V05363", "W05363", "X05363", "Y05363", "Z05363", "105363a", "105363b", "105363c",
    "105363d", "105363e", "105363f", "105363g", "105363h", "105363i", "105363j",
    "105363k", "105363l", "105363m", "105363n", "105363o", "105363p", "105363q",
    "105363r", "105363s", "105363t", "105363u", "105363v", "105363w", "105363x",
    "DEMO00", "DEMO01", "DEMO02", "DEMO03", "DEMO04", "DEMO05", "DEMO06", "DEMO07",
    "DEMO08", "DEMO09", "DEMO10", "DEMO11", "DEMO12", "DEMO13", "DEMO14", "DEMO15",
    "DEMO16", "DEMO17", "DEMO18", "DEMO19", "DEMO20", "DEMO21", "DEMO22", "DEMO23",
    "DEMO24", "DEMO25", "DEMO26", "DEMO27", "DEMO28", "DEMO29", "TEST00", "TEST01",
    "TEST02", "TEST03", "TEST04", "TEST05", "TEST06", "TEST07", "TEST08", "TEST09",
    "TEST10", "TEST11", "TEST12", "TEST13", "TEST14", "TEST15", "TEST16", "TEST17",
    "TEST18", "TEST19", "TEST20", "TEST21", "TEST22", "TEST23", "TEST24", "TEST25",
    "TEST26", "TEST27", "TEST28", "TEST29", "USER00", "USER01", "USER02", "USER03",
    "USER04", "USER05", "USER06", "USER07", "USER08", "USER09", "USER10", "USER11",
    "USER12", "USER13", "USER14", "USER15", "USER16", "USER17", "USER18", "USER19",
    "USER20", "USER21", "USER22", "USER23", "USER24", "USER25", "USER26", "USER27",
    "USER28", "USER29", "ADMIN0", "ADMIN1", "ADMIN2", "ADMIN3", "ADMIN4", "ADMIN5",
    "ADMIN6", "ADMIN7", "ADMIN8", "ADMIN9", "GUEST0", "GUEST1", "GUEST2", "GUEST3",
    "GUEST4", "GUEST5", "GUEST6", "GUEST7", "GUEST8", "GUEST9", "TRIAL0", "TRIAL1",
    "TRIAL2", "TRIAL3", "TRIAL4", "TRIAL5", "TRIAL6", "TRIAL7", "TRIAL8", "TRIAL9",
    "FREE00", "FREE01", "FREE02", "FREE03", "FREE04", "FREE05", "FREE06", "FREE07",
    "FREE08", "FREE09", "000000", "111111", "222222", "333333", "444444", "555555",
    "666666", "777777", "888888", "999999", "123456", "654321", "012345", "543210",
    "111222", "222333", "333444", "444555", "555666", "666777", "777888", "888999",
    "100000", "200000", "300000", "400000", "500000", "600000", "700000", "800000",
    "900000", "010101", "020202", "030303", "040404", "050505", "060606", "070707",
    "080808", "090909", "101010", "121212", "131313", "141414", "151515", "161616",
    "171717", "181818", "191919", "202020", "OPPO00", "OPPO01", "OPPO02", "OPPO03",
    "OPPO04", "OPPO05", "OPPO06", "OPPO07", "OPPO08", "OPPO09", "OPPO10", "OPPO11",
    "OPPO12", "OPPO13", "OPPO14", "OPPO15", "OPPO16", "OPPO17", "OPPO18", "OPPO19",
    "SNAKE0", "SNAKE1", "SNAKE2", "SNAKE3", "SNAKE4", "SNAKE5", "SNAKE6", "SNAKE7",
    "SNAKE8", "SNAKE9", "SE0001", "SE0002", "SE0003", "SE0004", "SE0005", "SE0006",
    "SE0007", "SE0008", "SE0009", "SE0010", "FENNEC", "FENNE1", "FENNE2", "FENNE3",
    "FENNE4", "FENNE5", "SNKE01", "SNKE02", "SNKE03", "SNKE04", "SNKE05", "K13000",
    "K13001", "K13002", "K13003", "K13004", "K13005", "5G0001", "5G0002", "5G0003",
    "5G0004", "062026", "260620", "202606", "110626", "260611", "112026", "261120",
    "060626", "070626", "080626", "090626", "100626", "120626", "012026", "022026",
    "032026", "042026", "052026", "072026", "082026", "092026", "102026", "122026",
    "0x1234", "0x5678", "0xABCD", "0xEF01", "0x0001", "0x0002", "0x0003", "0x0004",
    "0x0005", "0x0006", "0x0007", "0x0008", "0x0009", "0x000A", "0x000B", "0x000C",
    "0x000D", "0x000E", "0x000F", "0x0010", "0XFFFF", "0XAAAA", "0XBBBB", "0XCCCC",
    "0XDDDD", "0XEEEE", "0X0000", "0X1111", "0X2222", "0X3333", "0X4444", "0X5555",
    "0X6666", "0X7777", "0X8888", "0X9999", "1A2B3C", "A1B2C3", "2C4E6F", "3D5F7G",
    "4E6G8H", "5F7H9I", "6G8I0J", "7H9J1K", "8I0K2L", "9J1L3M", "0K2M4N", "1L3N5O",
    "2M4O6P", "3N5P7Q", "MASTER", "master", "Master", "UNLOCK", "unlock", "Unlock",
    "ACCESS", "access", "Access", "SECURE", "secure", "Secure", "SYSTEM", "system",
    "System", "DEVICE", "device", "Device", "ACTIVE", "active", "Active", "ENABLE",
    "enable", "Enable", "VALID0", "VALID1", "VALID2", "VALID3", "VALID4", "VALID5",
    "KEY001", "KEY002", "KEY003", "KEY004", "KEY005", "CODE01", "CODE02", "CODE03",
    "CODE04", "CODE05", "PASS01", "PASS02", "PASS03", "PASS04", "PASS05", "LOGIN0",
    "LOGIN1", "LOGIN2", "LOGIN3", "LOGIN4", "Demo00", "demo00", "Test00", "test00",
    "User00", "user00", "Admin0", "admin0", "Guest0", "guest0", "Trial0", "trial0",
    "Free00", "free00", "Oppo00", "oppo00", "Snake0", "snake0", "Se0001", "se0001",
    "K13000", "k13000", "Master", "mAster", "Unlock", "uNlock", "Access", "aCcess",
    "Secure", "sEcure", "System", "sYstem", "Device", "dEvice", "Active", "aCtive",
    "Enable", "eNable", "Valid0", "vAlid0"
]

def test_key(key_num, key):
    """Test a single key"""
    print(f"\n[{key_num}/500] Testing: {key}")
    print("=" * 40)

    # Open SE app
    print("  Opening SE app...")
    subprocess.run(['am', 'start', '-n', 'com.snake/.MainActivity'],
                   capture_output=True)
    time.sleep(1.5)

    # Tap Entry Key (540, 943)
    print("  Tapping Entry Key...")
    subprocess.run(['input', 'tap', '540', '943'],
                   capture_output=True)
    time.sleep(1.5)

    # Tap key field (540, 541)
    print("  Tapping key field...")
    subprocess.run(['input', 'tap', '540', '541'],
                   capture_output=True)
    time.sleep(0.8)

    # Type the key
    print(f"  Typing: {key}")
    subprocess.run(['input', 'text', key],
                   capture_output=True)
    time.sleep(0.8)

    # Tap Activate (834, 657)
    print("  Tapping Activate...")
    subprocess.run(['input', 'tap', '834', '657'],
                   capture_output=True)
    time.sleep(3)

    print("  ⏳ Waiting for validation...")

    # Tap Close (474, 608)
    subprocess.run(['input', 'tap', '474', '608'],
                   capture_output=True)
    time.sleep(0.5)

    # Close app
    print("  Closing app...")
    subprocess.run(['am', 'force-stop', 'com.snake'],
                   capture_output=True)

    print("  ✓ Done")

def main():
    print("=" * 50)
    print("  SE 2.2.6 Key Tester")
    print("  Device ID: 105363")
    print("=" * 50)
    print(f"Total keys: {len(KEYS)}")
    print(f"Estimated time: ~75 minutes")
    print("=" * 50)

    input("\nPress ENTER to start testing...")

    start_time = time.time()

    for i, key in enumerate(KEYS, 1):
        test_key(i, key)

        # Progress update every 50 keys
        if i % 50 == 0:
            elapsed = int(time.time() - start_time)
            avg_time = elapsed / i
            remaining = int(avg_time * (len(KEYS) - i))

            print(f"\n{'='*50}")
            print(f"  PROGRESS: {i}/500 keys tested")
            print(f"  Elapsed: {elapsed//60} minutes")
            print(f"  Remaining: ~{remaining//60} minutes")
            print(f"{'='*50}\n")

    total_time = int(time.time() - start_time)

    print("\n" + "=" * 50)
    print("  TESTING COMPLETE!")
    print("=" * 50)
    print(f"Total time: {total_time//60} minutes")
    print(f"Total keys tested: {len(KEYS)}")
    print("\nCheck SE app manually for results!")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTesting stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError: {e}")
        sys.exit(1)

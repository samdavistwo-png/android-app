#!/usr/bin/env python3
"""
EXHAUSTIVE Key Tester for SE 2.2.6 App
Tests ALL 56.8 BILLION possible keys (62^6 combinations)

⚠️ WARNING: This will take approximately 16+ YEARS to complete
   at 9 seconds per key (56,800,235,584 keys × 9 seconds)

Character Set:
- Numbers: 0-9 (10 options)
- Uppercase: A-Z (26 options)
- Lowercase: a-z (26 options)
Total per position: 62 options
Total keys: 62^6 = 56,800,235,584

Run this in Pydroid 3 app on your phone.
Keep phone charging and screen on.
"""

import subprocess
import time
import sys
import itertools
import os

# Character set: 0-9, A-Z, a-z (62 characters)
CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
TOTAL_KEYS = 62 ** 6  # 56,800,235,584
CHECKPOINT_FILE = '/storage/emulated/0/key_tester_checkpoint.txt'
LOG_FILE = '/storage/emulated/0/key_tester_log.txt'

def save_checkpoint(key_num, key):
    """Save progress to resume later"""
    try:
        with open(CHECKPOINT_FILE, 'w') as f:
            f.write(f"{key_num}\n{key}")
    except:
        pass  # Continue even if can't save

def load_checkpoint():
    """Load last checkpoint to resume testing"""
    try:
        if os.path.exists(CHECKPOINT_FILE):
            with open(CHECKPOINT_FILE, 'r') as f:
                lines = f.read().strip().split('\n')
                return int(lines[0]), lines[1]
    except:
        pass
    return 0, None

def log_result(key_num, key, message="Tested"):
    """Log each tested key"""
    try:
        with open(LOG_FILE, 'a') as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] Key #{key_num}: {key} - {message}\n")
    except:
        pass  # Continue even if can't log

def test_key(key_num, key):
    """Test a single key"""
    print(f"\n[{key_num:,}/{TOTAL_KEYS:,}] Testing: {key}")
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

    # Save checkpoint every key
    save_checkpoint(key_num, key)
    log_result(key_num, key)

def generate_keys(start_key=None):
    """Generate all 56.8 billion keys in order"""
    # Generate all 6-character combinations
    all_combinations = itertools.product(CHARS, repeat=6)

    # If resuming, skip to start_key
    if start_key:
        print(f"Resuming from key: {start_key}")
        for combo in all_combinations:
            current_key = ''.join(combo)
            if current_key == start_key:
                yield current_key
                break

    # Continue generating
    for combo in all_combinations:
        yield ''.join(combo)

def format_time(seconds):
    """Convert seconds to human readable format"""
    years = seconds // (365 * 24 * 3600)
    seconds %= (365 * 24 * 3600)
    months = seconds // (30 * 24 * 3600)
    seconds %= (30 * 24 * 3600)
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60

    parts = []
    if years > 0: parts.append(f"{years} years")
    if months > 0: parts.append(f"{months} months")
    if days > 0: parts.append(f"{days} days")
    if hours > 0: parts.append(f"{hours} hours")
    if minutes > 0: parts.append(f"{minutes} minutes")

    return ", ".join(parts) if parts else "0 minutes"

def main():
    print("=" * 60)
    print("  EXHAUSTIVE SE 2.2.6 Key Tester")
    print("  Device ID: 105363")
    print("=" * 60)
    print(f"Total possible keys: {TOTAL_KEYS:,}")
    print(f"Character set: {CHARS}")
    print(f"Key format: 6 characters (any combination)")
    print("=" * 60)

    # Calculate estimated time
    time_per_key = 9  # seconds
    total_seconds = TOTAL_KEYS * time_per_key

    print(f"\n⚠️  ESTIMATED TIME: {format_time(total_seconds)}")
    print(f"⚠️  (~{total_seconds / (365 * 24 * 3600):.1f} years at 9 seconds/key)")
    print("\n💡 TIP: Keep phone charging and screen on")
    print("💡 Progress saved every key - can resume anytime")
    print(f"💡 Checkpoint file: {CHECKPOINT_FILE}")
    print(f"💡 Log file: {LOG_FILE}")
    print("=" * 60)

    # Check for existing checkpoint
    start_num, start_key = load_checkpoint()
    if start_key:
        print(f"\n✅ Found checkpoint! Resuming from key #{start_num:,}: {start_key}")
        resume = input("Press ENTER to resume, or type 'restart' to start over: ")
        if resume.lower() == 'restart':
            start_num = 0
            start_key = None
            try:
                os.remove(CHECKPOINT_FILE)
            except:
                pass
    else:
        input("\nPress ENTER to start exhaustive testing...")

    start_time = time.time()
    key_num = start_num

    try:
        for key in generate_keys(start_key):
            key_num += 1
            test_key(key_num, key)

            # Progress update every 1000 keys
            if key_num % 1000 == 0:
                elapsed = int(time.time() - start_time)
                avg_time = elapsed / (key_num - start_num)
                remaining = int(avg_time * (TOTAL_KEYS - key_num))

                print(f"\n{'='*60}")
                print(f"  PROGRESS: {key_num:,}/{TOTAL_KEYS:,} keys tested")
                print(f"  Percentage: {(key_num/TOTAL_KEYS)*100:.6f}%")
                print(f"  Elapsed: {format_time(elapsed)}")
                print(f"  Remaining: ~{format_time(remaining)}")
                print(f"  Current key: {key}")
                print(f"{'='*60}\n")

    except KeyboardInterrupt:
        print("\n\n⏸️  Testing paused by user.")
        print(f"Progress saved at key #{key_num:,}: {key}")
        print(f"Run script again to resume from this point.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error at key #{key_num}: {e}")
        print(f"Progress saved. Run script again to resume.")
        sys.exit(1)

    total_time = int(time.time() - start_time)

    print("\n" + "=" * 60)
    print("  🎉 TESTING COMPLETE!")
    print("=" * 60)
    print(f"Total time: {format_time(total_time)}")
    print(f"Total keys tested: {TOTAL_KEYS:,}")
    print(f"\nCheck log file: {LOG_FILE}")
    print("=" * 60)

if __name__ == "__main__":
    main()

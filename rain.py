import cv2
import hashlib
import numpy as np
import time
from scipy.stats import chisquare

def capture_entropy(duration=5):
    cap = cv2.VideoCapture(0)
    prev = None
    bits = []
    thresh = None
    start = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)

        if prev is not None:
            diff = cv2.absdiff(gray, prev)
            _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
            count = np.count_nonzero(thresh)
            bits.append(count % 2)

        prev = gray

        # live display
        if thresh is not None:
            cv2.imshow("Leakage Feed", thresh)
        else:
            cv2.imshow("Leakage Feed", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time.time() - start >= duration:
            break

    cap.release()
    cv2.destroyAllWindows()
    return bits

def analyze_bits(bits):
    bits_arr = np.array(bits)
    ones = np.sum(bits_arr)
    zeros = len(bits_arr) - ones
    p_value = chisquare([ones, zeros])[1]
    return ones, zeros, p_value

def hash_bits(bits):
    bits_str = ''.join(str(b) for b in bits)
    byte_chunks = [bits_str[i:i+8] for i in range(0, len(bits_str), 8)]
    byte_array = bytearray(int(chunk, 2) for chunk in byte_chunks)
    return hashlib.sha256(byte_array).hexdigest()

results = []
for i in range(5):  # number of runs
    print(f"Run {i+1} starting. Press 'q' to abort early.")
    bits = capture_entropy(5)
    digest = hash_bits(bits)
    ones, zeros, p_value = analyze_bits(bits)
    results.append((ones, zeros, p_value, digest))
    print(f"Run {i+1}: ones={ones}, zeros={zeros}, p={p_value:.5f}, hash={digest[:16]}...")

p_values = [r[2] for r in results]
print("\nAverage p-value:", np.mean(p_values))
print("Std deviation:", np.std(p_values))

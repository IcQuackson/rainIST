# rainIST
<img width="1175" height="637" alt="image" src="https://github.com/user-attachments/assets/7a8846fb-47b1-4ebd-b0fb-375c50b0e343" />


A small experiment in physical randomness extraction using a real-world entropy source — a ceiling leak at **Instituto Superior Técnico**.

## Overview

Water droplets from a ceiling leak were used as a **physical entropy source**. A standard webcam captured video frames, and **OpenCV** was used to detect motion and brightness changes caused by splashing droplets. These variations were converted into binary sequences, which were then hashed using **SHA-256**.

## Method

1. **Data Capture:**  
   A webcam recorded the leaking ceiling. Each frame was processed to detect pixel-level motion.

2. **Bitstream Generation:**  
   Frame-to-frame changes were mapped to binary values based on motion intensity thresholds.

3. **Hashing:**  
   Generated sequences were hashed using SHA-256 to normalize distribution and mitigate direct bias.

4. **Statistical Evaluation:**  
   Randomness was tested using **Chi-square frequency analysis** over multiple runs.

## Results

| Metric | Value |
|---------|--------|
| Mean p-value | 0.2168 |
| Standard deviation | 0.3928 |

The output shows partial randomness with noticeable bias fluctuations. Environmental sensitivity—such as lighting and camera stability—introduced measurable drift.

## How to Install and Run

### 1. Clone the repository
```bash
git clone https://github.com/IcQuackson/rainIST.git
cd rainIST
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate        # On Windows
```

### 3. Install dependencies

```bash
pip install opencv-python numpy scipy
```

### 4. Run the experiment

```bash
python rain.py
```

The webcam feed will open in a window. The script detects motion differences caused by droplets and converts them into a binary entropy stream.

* Press **'q'** to stop any run early.
* After all runs, the script prints per-run statistics and final averages.

### 5. Example Output

```
Run 1 starting. Press 'q' to abort early.
Run 1: ones=1423, zeros=1378, p=0.37210, hash=f9a3a12b87c19e4a...
...
Average p-value: 0.2168
Std deviation: 0.3928
```

## Dependencies

* Python 3.x
* OpenCV (`cv2`)
* NumPy
* SciPy
* hashlib (standard library)

## Conclusions

* Visual entropy harvesting is feasible but unstable with low-quality sensors.
* Environmental consistency is critical to maintain entropy reliability.
* Future iterations require a higher-resolution camera and controlled lighting conditions.

## Notes

Entropy can leak faster than ceilings.

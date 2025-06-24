# Image Segmentation

This repository contains two scripts demonstrating fundamental image segmentation techniques:

1. **Global thresholding** with Otsu’s method after adding Gaussian noise.
2. **Region-growing** segmentation based on pixel similarity and user-defined seeds.

---

## 📂 Folder Structure

```plaintext
TakeHome2/
├── .gitignore                 # Files/directories to ignore in Git
├── README.md                  # Project overview and instructions
├── requirements.txt           # Python dependencies
├── data/
│   └── synthetic.png          # Generated 3-level input image
├── results/
│   ├── noisy.png              # After adding Gaussian noise
│   ├── otsu_result.png        # Binary mask from Otsu’s threshold
│   └── region_growing.png     # Segmentation via region-growing
└── src/
    ├── noise_and_otsu.py      # Create synthetic image, add noise, apply Otsu
    └── region_growing.py      # Perform region-growing on noisy image
```

---

## 🚀 Prerequisites

* Python 3.7 or higher
* Virtual environment tool (venv or conda)

---

## ⚙️ Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/mhdmusharraf/Image-Segmentation-Assignment.git
   cd Image-Segmentation-Assignment
   ```
2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows (PowerShell)
   .\\venv\\Scripts\\Activate.ps1
   ```
3. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### 1. Noise Injection & Otsu’s Thresholding

Run:

```bash
python src/noise_and_otsu.py
```

* **Generates:**

  * `data/synthetic.png`
  * `results/noisy.png`
  * `results/otsu_result.png`

### 2. Region-Growing Segmentation

Then run:

```bash
python src/region_growing.py
```

* **Generates:**

  * `results/region_growing.png`






# 🔒 Encrypted BMI Calculator (Zama FHE Demo)

A simple privacy-preserving BMI calculator built using **Fully Homomorphic Encryption (FHE)** via Zama's [Concrete](https://zama.ai/concrete) library.

## 🚀 Features
- Compute BMI without revealing height or weight.
- Built with Concrete FHE + Streamlit UI.
- Lightweight and deployable on any platform.

## 🧠 How It Works
1. User inputs height and weight.
2. Both values are encrypted locally.
3. Computation runs on encrypted data: `BMI = weight / (height^2)`
4. Result is decrypted only by the user.

## 🛠️ Tech Stack
- **Python**
- **Zama Concrete**
- **Streamlit**

## ▶️ Run Locally
```bash
git clone https://github.com/<your-username>/encrypted-bmi.git
cd encrypted-bmi
pip install -r requirements.txt
python fhe_bmi.py   # build model
streamlit run app.py
```

---

### 🧾 Credits
Built by **Halo** — inspired by Zama’s vision for open-source privacy-preserving computation.

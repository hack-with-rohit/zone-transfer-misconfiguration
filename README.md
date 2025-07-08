# AXFR Zone Scanner

A simple Python-based tool to automate **AXFR (Zone Transfer)** vulnerability checks against domain nameservers.

---

## 🚀 Features

- Automatically retrieves NS (Name Server) records for a given domain.
- Attempts AXFR zone transfers on each nameserver.
- Highlights successful transfers with results.
- Clean and color-coded terminal output.

---

## ⚙️ Pre-installation Requirements

Before running the tool, make sure the following are installed:

### ✅ Dependencies

- `Python 3.x`
- `dig` command-line tool (usually comes with `dnsutils`)

### 🛠 Install on Debian/Kali/Ubuntu:
```bash
sudo apt update
sudo apt install dnsutils -y

💻 Usage

python3 axfr_scanner.py <domain>

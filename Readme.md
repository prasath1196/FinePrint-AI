# 🔥 FinePrint-AI  

## 📌 Project Description  
The **FinePrint-AI** is a Python-based application that scrapes **Terms of Service agreements** from specified URLs and generates structured reports highlighting **key privacy insights**. It utilizes **Firecrawl for web scraping** and **OpenAI's language model** to extract actionable information from the scraped content.  

### ✨ Features  
✅ Scrapes **Terms of Service agreements** from user-provided URLs  
✅ Extracts **important insights** related to **data privacy, hidden fees, content ownership, and account risks**  
✅ Generates a **well-styled HTML report** with **actionable insights**  
✅ Provides **AI-powered analysis** to detect **red flags** in Terms of Service  

## DEMO
https://fineprint-ai-2025.streamlit.app/
---

## 🛠️ Installation Instructions  

### 1️⃣ **Clone the Repository**  
```bash
git clone <repository-url>
cd firecrawl_basics
```

### 2️⃣ **Create a Virtual Environment** (Optional but Recommended)  
```bash
python -m venv myenv
```
Activate the virtual environment:  
- **On macOS/Linux:**  
  ```bash
  source myenv/bin/activate
  ```
- **On Windows:**  
  ```bash
  myenv\Scripts\activate
  ```

### 3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**  
Create a `.env` file in the project root directory and add your API keys:  
```env
OPENAI_API_KEY="your_openai_api_key"
FIRECRAWL_API_KEY="your_firecrawl_api_key"
```

### 5️⃣ **Run the Application**  
Start the **Streamlit UI**:  
```bash
streamlit run report_ui.py
```

### 6️⃣ **Access the Application**  
Once the server starts, open your browser and go to:  
🔗 **[http://localhost:8501](http://localhost:8501)**  

---

## 🚀 **Usage Instructions**  

### **🔹 Step 1: Enter the Terms of Service URL**  
- Copy and paste the **URL of the website’s Terms of Service page** into the input field.  

### **🔹 Step 2: Click "Generate Report"**  
- The app will **scrape the Terms of Service**, analyze it using **AI**, and generate a **privacy insights report**.  

### **🔹 Step 3: Review the Report**  
- The report will highlight:  
  - **💰 Hidden fees & subscription traps**  
  - **🔐 Data collection & sharing policies**  
  - **📝 Content ownership terms**  
  - **⛔ Account bans & user rights**  
  - **⚖️ Legal dispute policies**  

### **🔹 Step 4: Take Action**  
- Use the insights to **make informed decisions** before agreeing to Terms of Service.  

---

## 📜 Example Output  

### **Example Company: Spotify**  
| Category          | Insights |
|------------------|----------------------------------------------------------------|
| **Hidden Fees**  | Auto-renews subscriptions without explicit confirmation.       |
| **Data Privacy** | Collects personal and behavioral data for targeted ads.       |
| **Account Ban Risk** | Can terminate your account without notice or refund.     |
| **Legal Disputes** | Users waive rights to sue, must go through arbitration.      |

---

## 🎨 **HTML Report View**  
The generated **HTML report** is **visually appealing**, structured for easy readability, and highlights key risks.  

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service Report</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: #ffffff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #d9534f;
            border-bottom: 3px solid #d9534f;
            padding-bottom: 12px;
            margin-bottom: 20px;
        }
        .insight {
            background-color: #fdf7f7;
            border-left: 6px solid #d9534f;
            padding: 12px;
            margin: 15px 0;
            border-radius: 5px;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .insight:hover {
            transform: scale(1.02);
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📜 Terms of Service Insights</h1>
        <div class="insight"><strong>Company:</strong> Spotify</div>
        <div class="insight"><strong>Hidden Fees:</strong> Auto-renews subscriptions.</div>
        <div class="insight"><strong>Data Privacy:</strong> Collects personal data.</div>
        <div class="insight"><strong>Account Ban Risk:</strong> Can terminate accounts without refund.</div>
        <div class="insight"><strong>Legal Disputes:</strong> Users waive right to sue.</div>
    </div>
</body>
</html>
```

💡 **This clean, structured HTML makes reports visually appealing & easy to read!**  

---

## 🤖 **Tech Stack**  
🖥 **Backend:** Python, OpenAI API, Firecrawl API  
🎨 **Frontend:** Streamlit  
📊 **AI Processing:** GPT-4 / DeepSeek API  
📡 **Web Scraping:** Firecrawl  

---

## 📢 **Contributing**  
Want to improve the Firecrawl Privacy Report Generator? Feel free to contribute!  
1. **Fork the repo**  
2. **Create a new branch**  
3. **Commit your changes**  
4. **Submit a pull request** 🚀  

---

## 🛡️ Disclaimer  
This tool provides AI-generated insights and should **not be considered legal advice**. Always consult official **legal documents** before making decisions.  

---

## 💡 **Future Enhancements**  
🔹 **Chrome Extension** for quick privacy analysis  
🔹 **AI-powered Terms of Service comparison**  
🔹 **Privacy Score Rating System**  
🔹 **Automated Subscription Cancelation Alerts**  

---

## 🔗 **Contact & Support**  
📩 Email: `your-email@example.com`  
🐙 GitHub: [GitHub Repository](https://github.com/prasath1196/FinePrint-AI/)  
🚀 Built with ❤️ using **AI & Web Scraping**  

---

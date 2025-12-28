Here’s a **clean, professional, and GitHub-ready `README.md`** for your project.
You can **copy–paste this directly** into your repository.

---

```md
# 🧾 Multilanguage Invoice Extractor (LangChain + Gemini)

An intelligent **Multilanguage Invoice Extraction system** built using **LangChain**, **Google Gemini Vision**, and **Streamlit**.  
This app extracts structured invoice data (JSON) from invoice images across different languages and formats.

---

## 🚀 Features

- 📸 Upload invoice images (JPG / PNG)
- 🌍 Supports **multilingual invoices**
- 🧠 Uses **Gemini Vision (gemini-2.5-flash)**
- 🔗 Powered by **LangChain** for clean prompt orchestration
- 📊 Extracts structured data:
  - Invoice Number
  - Invoice Date
  - Vendor Details
  - Customer Name
  - Subtotal, Tax, Total
  - Currency & Payment Method
- 📄 Outputs **valid JSON**
- ⚡ Simple Streamlit UI

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Google Gemini Vision**
- **Pillow**
- **python-dotenv**

---

## 📂 Project Structure

```

invoice-extractor/
│
├── app.py                # Main Streamlit app
├── .env                  # Environment variables
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kishankumar1047/multilanguage-invoice-extractor.git
cd multilanguage-invoice-extractor
````

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser 🚀

---

## 🧠 How It Works

1. User uploads an invoice image
2. Image is sent to **Gemini Vision** via **LangChain**
3. Prompt template enforces structured extraction
4. Model returns **JSON-only output**
5. Data is displayed in the UI

---

## 📌 Example Output

```json
{
  "invoice_number": "INV-1023",
  "invoice_date": "2024-05-12",
  "vendor_name": "ABC Traders",
  "vendor_address": "Mumbai, India",
  "customer_name": "XYZ Pvt Ltd",
  "subtotal": 5000,
  "tax": 900,
  "total_amount": 5900,
  "currency": "INR",
  "payment_method": "UPI"
}
```

---

## 🔮 Future Enhancements

* 📄 PDF invoice support
* 📤 Export to CSV / Excel
* 🧾 GST & VAT auto-calculation
* 📦 Batch invoice processing
* 📊 Confidence score per field
* 🗄️ Database integration

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 👨‍💻 Author

**Kishan Kumar**
GitHub: [https://github.com/kishankumar1047](https://github.com/kishankumar1047)

---

## ⭐ Support

If you find this project helpful, please consider giving it a ⭐ on GitHub!

```

---

If you want, I can also:
- Generate `requirements.txt`
- Add badges (stars, license, Python version)
- Create a **professional GitHub repo description**
- Add screenshots section

You’re building something solid—this README already puts you at a **production-ready level** 🚀
```

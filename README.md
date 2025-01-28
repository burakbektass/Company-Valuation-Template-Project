# Company Valuation Tool 📊 💹

⚠️ **IMPORTANT NOTICE** ⚠️
> The formulas and financial information used in this tool were provided by Management Engineering students in 2021. The methodologies and calculations reflect academic research and market conditions from that period.

A powerful web application for company valuation using multiple methodologies including DCF (Discounted Cash Flow), Residual Income, and Enterprise Value methods.

## 🌟 Features

- 📈 Multiple valuation methods:
  - Discounted Cash Flow (DCF)
  - Residual Income Method
  - Enterprise Value Method
  - Weighted Average of all methods
  
- 🏢 Pre-loaded company data for:
  - Tech giants (Google, Apple, Microsoft)
  - Beverage companies (Coca-Cola, PepsiCo, Monster)
  - Retail chains (Walmart, Dollar General, Target)
  - Turkish energy companies (Aksa Enerji, Odaş Elektrik, Ak Enerji)
  - Turkish retail companies (Migros, Carrefour SA, BIM)
  - Turkish electronics companies (Arcelik, Vestel, Bosch)

- 📁 Custom company analysis through file upload
- 📊 Sector-specific comparisons
- 💡 Clear buy/sell recommendations
- 🔄 Real-time stock price integration

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/company-valuation-tool.git
cd company-valuation-tool
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### 🏃‍♂️ Running the Application

1. Start the Streamlit server:
```bash
streamlit run main.py
```

2. Open your browser and navigate to `http://localhost:8501`

## 📊 Using the Tool

### 1. Pre-loaded Company Analysis
- Select a company from the dropdown menu
- Click "Calculate" to view the valuation results
- Review the results in three expandable sections:
  - DCF Analysis
  - Enterprise Value Analysis
  - Weighted Average Results

### 2. Custom Company Analysis
- Prepare your financial data in Excel format (template available)
- Click "Upload" and select your Excel file
- Review the results in the same format as pre-loaded companies

## 📑 Financial Data Format

Your Excel file should include:
- Balance Sheet data (2013-2021)
- Income Statement data (2013-2021)
- Cash Flow Statement data (2013-2021)

Template structure:
- Sheet name should match company name
- Specific cell references for key financial metrics
- Currency in thousands (×1000)

## 🔍 Valuation Methods Explained

### DCF Method
Calculates future cash flows and discounts them to present value using:
- Historical growth rates
- WACC (Weighted Average Cost of Capital)
- Terminal value estimation

### Residual Income Method
Evaluates company value based on:
- Book value of equity
- Future residual income
- Cost of equity

### Enterprise Value Method
Compares company metrics with sector averages:
- EV/EBITDA ratios
- Market capitalization
- Debt and cash positions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Financial data provided by Yahoo Finance
- Streamlit for the web interface
- OpenPyXL for Excel handling

## ⚠️ Disclaimer

This tool is for educational purposes only. Always conduct thorough research and consult financial professionals before making investment decisions.

---
Made with ❤️ by [Bahcesehir University Students (software Engineering and Management Engineering)]

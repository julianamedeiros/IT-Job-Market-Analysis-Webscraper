# 📊 Web Scraper & EDA of the Job Market for Data Analysis   

## Overview  
This project **scrapes job postings from Pracuj.pl** to analyze the **most in-demand technologies** for a given role.  
For this analysis, I focused on **Data Analyst** positions, but **you can customize it for any job title** by modifying the script!  

The project includes:  
:heavy_check_mark: **Web scraping with Python, Selenium & BeautifulSoup** 🕵️‍♂️  
:heavy_check_mark: **Data cleaning & analysis with Pandas** 📊  
:heavy_check_mark: **An interactive Power BI report** 📈  

---

## How It Works  

### **Web Scraping**   
- The script extracts **job titles, required experience levels, and technologies** from job postings.  
- It **iterates through job offer URLs**, collecting relevant details.  
- Data is **cleaned and stored in a structured format** for analysis.  

### **Data Analysis (EDA)**  
- Cleans & processes the scraped data using **Pandas**.  
- Identifies **the most in-demand technologies** for Data Analysts.  
- Analyzes **job levels (junior/mid/senior)**.  
- Checks **missing data & distributions**.  

### **Power BI Report**  
- Visualizes trends in tech demand across job levels.  
- Provides insights into required skills in the job market.  
- Can be **adapted for other roles**!  

---

## 📂 Project Structure  

```
📁 IT-Job-Market-Analysis-Webscraper
│── 📄 README.md                            # Project documentation  
│── 📄 pracujpl                             # Folder refered to the scraped job board
│────📄 scraper.py                          # Web scraping script (Selenium & BeautifulSoup)  
│── 📄 EDA_job_market_Data_Analysts.pbix    # Power BI report  
│── 📄 EDA_job_market_Data_Analysts.pdf     # Summary of findings with visuals  
│── 📄 dataanalysis.py                      # Data cleaning & Exploratory Data Analysis (pandas)
│── 📄 tech_jobs.csv                        # File for scraped job data (CSV)  
```

---

## 🔍 Key Insights  

📊 **Top 5 Most In-Demand Technologies for Data Analysts**  
1. **SQL** 
2. **Jira**
3. **Python**   
4. **Confluence**
5. **Power BI**   

🎯 **Senior roles are more in demand.**  

---


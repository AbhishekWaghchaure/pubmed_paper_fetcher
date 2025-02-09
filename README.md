
# 📄 PubMed Paper Fetcher

A command-line tool to fetch research papers from **PubMed** using the **Entrez API**, filtering those affiliated with pharmaceutical or biotech companies.

---

## 🚀 Features

- Fetches research papers using **PubMed API**  
- Filters papers with at least one **non-academic author**  
- Saves results in a **CSV file**  
- Supports **command-line arguments** for flexibility  
- Uses **Poetry** for package management  

---

## 📂 Project Structure

```
aganitha/
│── pubmed_paper_fetcher/
│   │── __init__.py             # Marks as a package
│   │── pubmed_fetcher.py       # Fetches papers from PubMed API
│   │── cli.py                  # Command-line interface
│── pyproject.toml              # Poetry configuration
│── README.md                   # Documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### 2️⃣ Install Poetry (If Not Installed)

```sh
pip install poetry
```

### 3️⃣ Install Dependencies

```sh
poetry install
```

---

## 🛠 Usage

### 🔍 Fetch Papers and Print Output

```sh
poetry run get-papers-list "cancer treatment"
```

### 💾 Save Papers to a CSV

```sh
poetry run get-papers-list "cancer treatment" -f results.csv
```

---

## 💡 Example Output

```json
[
    {"PubmedID": "12345678"},
    {"PubmedID": "87654321"}
]
```

If saved to a CSV (`results.csv`):

```
PubmedID
12345678
87654321
```

---

## 🔗 Additional Information

- PubMed API: [https://www.ncbi.nlm.nih.gov/home/develop/api/](https://www.ncbi.nlm.nih.gov/home/develop/api/)  
- Poetry Documentation: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)  

---

## 🤝 Contributing

1. **Fork** the repo  
2. Create a new **branch**: `git checkout -b feature-name`  
3. **Commit** your changes: `git commit -m "Add feature"`  
4. **Push** the branch: `git push origin feature-name`  
5. Open a **Pull Request**  

---

## 📜 License

MIT License. See `LICENSE` for details.
import requests
import pandas as pd
import re
from typing import List, Dict

# PubMed API Endpoints
PUBMED_SEARCH_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_papers(query: str, max_results: int = 10) -> List[Dict]:
    """
    Fetches papers from PubMed based on a search query.

    :param query: The search query.
    :param max_results: The maximum number of results to fetch.
    :return: A list of dictionaries containing paper details.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(PUBMED_SEARCH_API, params=params)
    response.raise_for_status()

    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])

    if not paper_ids:
        return []

    return get_paper_details(paper_ids)

def get_paper_details(paper_ids: List[str]) -> List[Dict]:
    """
    Fetches detailed information for a list of PubMed papers.

    :param paper_ids: List of PubMed IDs.
    :return: A list of paper details.
    """
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    response = requests.get(PUBMED_SUMMARY_API, params=params)
    response.raise_for_status()

    data = response.json()
    papers = []

    for paper_id in paper_ids:
        details = data.get("result", {}).get(paper_id, {})
        title = details.get("title", "Unknown Title")
        pub_date = details.get("pubdate", "Unknown Date")
        authors = details.get("authors", [])

        non_academic_authors, companies = extract_non_academic_authors(authors)

        papers.append({
            "PubmedID": paper_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(companies),
            "Corresponding Author Email": "N/A"  # To be implemented
        })

    return papers

def extract_non_academic_authors(authors: List[Dict]):
    """
    Identifies non-academic authors using heuristics.

    :param authors: List of author details.
    :return: Tuple containing a list of non-academic authors and company affiliations.
    """
    non_academic_authors = []
    companies = []
    pharma_keywords = ["pharma", "biotech", "laboratories", "inc", "corp"]

    for author in authors:
        name = author.get("name", "Unknown")
        affiliation = author.get("affiliation", "").lower()

        if affiliation and not any(word in affiliation for word in ["university", "college", "institute", "school"]):
            non_academic_authors.append(name)
            if any(keyword in affiliation for keyword in pharma_keywords):
                companies.append(affiliation)

    return non_academic_authors, companies

def save_to_csv(papers: List[Dict], filename: str):
    """
    Saves paper data to a CSV file.

    :param papers: List of paper details.
    :param filename: Output CSV file name.
    """
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
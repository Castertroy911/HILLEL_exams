from save_urls import SaveUrls
from parser import Parser
from analyze_urls import UrlAnalyzer

if __name__ == "__main__":
    page = SaveUrls()
    page.save_urls(Parser(), UrlAnalyzer())

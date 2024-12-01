import json
from newspaper import Article
from dateutil import parser
import re
import asyncio
from text_summary import TextSummary
from image_summary import ImageSummary
from logger import logging
from content_analysis import check_offensive_content

class ArticleExtractor:
    def __init__(self):
        """
        Initialize the ArticleExtractor with the article URL and Gemma API key.
        """
        self.url=None
        self.article=None
        self.article_data=None
        self.text_summariser = TextSummary()
        self.image_summariser = ImageSummary()

    async def __call__(self, article_url):
        self.set_article(article_url)
        self.download_and_parse()
        await self.extract_details()
        return self.article_data["summary"]

    def set_article(self, article_url):
        self.url = article_url
        self.article = Article(article_url)
        self.article_data = {}

    def download_and_parse(self):
        """
        Download and parse the article.
        """
        self.article.download()
        self.article.parse()

    @staticmethod
    def parse_relative_time(time_string):
        """
        Handle relative time formats (e.g., '8 hours ago').
        """
        try:
            return parser.parse(time_string)
        except (ValueError, TypeError):
            return None

    def extract_publish_date(self):
        """
        Extract the published date or relative time.
        """
        if self.article.publish_date:
            return self.article.publish_date

        # Search for relative time
        relative_time_match = re.search(r'updated\s*(.*)', self.article.text, re.IGNORECASE)
        if relative_time_match:
            return self.parse_relative_time(relative_time_match.group(1))
        return None

    def extract_authors(self):
        """
        Extract authors or infer from text patterns.
        """
        if self.article.authors:
            return self.article.authors

        # Attempt to find potential author names
        author_matches = re.findall(r'By\s+([A-Za-z\s]+)', self.article.text)
        return author_matches if author_matches else None

    async def summarize_with_gemma(self):
        """
        Summarize the article text using Google's Generative AI (Gemma).
        """


        try:
            # Configure Gemma
            # genai.configure(api_key=self.gemma_api_key)
            # model = genai.GenerativeModel("gemini-1.5-flash")

            # Generate summary
            image_summary = await self.image_summariser(self.article_data["main_image"])
            text_summary = await self.text_summariser(f"Text: {self.article.text} \n Image description: {image_summary}")
            logging.info(f"Summary of the full article is: {text_summary}")
            shield_on = await check_offensive_content(text_summary)
            logging.info(f"Shield on: {shield_on}")
            if shield_on is False:
                return "This news does not contain dangerous content and protected by Gemma Shield: " + text_summary
            else:
                return "This news may contain dangerous content: " + text_summary

        except Exception as e:
            print(f"Error during Gemma summarization: {e}")
            return None

    async def extract_details(self):
        """
        Extract details including title, authors, publish date, text, and summary.
        """
        publish_date = self.extract_publish_date()
        authors = self.extract_authors()

        main_image = self.article.top_image if self.article.top_image else None  # selects main image # Extract the main image (top image)

        self.article_data = {
            'title': self.article.title,
            'authors': authors,
            'publish_date': publish_date.strftime('%Y-%m-%d %H:%M:%S') if publish_date else None,
            'text': self.article.text,
            'main_image': main_image,
            'images': list(self.article.images),  # Convert set to list
        }
        # Summarize the article
        summary = await self.summarize_with_gemma()

        self.article_data["summary"] = summary

    def save_to_json(self, filename):
        """
        Save the extracted article data to a JSON file.
        """
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(self.article_data, json_file, indent=4, ensure_ascii=False)



# Main Script
if __name__ == "__main__":
    # Replace with your target article URL and Gemma API key
    url = "https://www.bbc.co.uk/news/articles/c0rgkkpl0dno"
    gemma_api_key = "AIzaSyCmXk4kUNLC2UriyuYcpkhkT3KoSBf97ts"  # Replace with your actual API key

    extractor = ArticleExtractor()
    asyncio.run(extractor(url))

    print("Article data extracted and saved to article_data_with_summary.json")

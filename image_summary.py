import os
from logger import logging
from dotenv import load_dotenv
from utils import timing
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
from openai import OpenAI

class ImageSummary():

    @timing
    def __init__(self):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY)

    @timing
    async def __call__(self, url):
        try:
            summary = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                                "url": url,
                                            }
                            },
                            {
                                "type": "text",
                                "text": "Please describe the image in a short sentence.",
                            },
                        ],
                    }
                ],
                max_tokens=256,
            )
            logging.info(f"Summary of the image: {summary.choices[0].message.content}")
            return summary.choices[0].message.content
        except Exception as e:
            logging.error(e)





if __name__ == "__main__":
    urls = ["https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/cd43/live/0dfaae30-ae6f-11ef-93a6-9fd2d3586a96.jpg",
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/a003/live/dc55dd90-ae56-11ef-a4be-fb03c4435021.jpg"
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/25b4/live/4237aa80-aeb6-11ef-9026-3f684a99c959.jpg",
            "https://ichef.bbci.co.uk/news/1024/branded_news/fec4/live/79733480-ae73-11ef-8ab9-9192db313061.jpg",
            "https://ichef.bbci.co.uk/images/ic/240x135/p0jpdjgy.jpg",
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/cd43/live/0dfaae30-ae6f-11ef-93a6-9fd2d3586a96.jpg",
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/f876/live/00907960-aefa-11ef-bdf5-b7cb2fa86e10.jpg",
            "https://ichef.bbci.co.uk/ace/standard/385/cpsprodpb/8090/live/cb3f89c0-ae6a-11ef-bdf5-b7cb2fa86e10.jpg",
            "https://sb.scorecardresearch.com/p?c1=2&c2=17986528&cs_ucfr=0&cv=2.0&cj=1",
            ]
    import asyncio
    image_summary = ImageSummary()
    from speak import speak
    for i, url in enumerate(urls):

        summary = image_summary(url)
        asyncio.run(speak(f"Image {str(i+1)}"))
        asyncio.run(speak(summary))

# ByteTheNews
Get bite-sized news summaries of online news stories, read aloud to you, so that you can stay informed on-the-go, save time, save your eyes and never miss out on important updates!

# ⚙️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/llama-hackathon.git
   cd ByteTheNews_Hackathon
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.10+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Copy the `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

   - `GROQ_API_KEY`: Your Groq API key.
   - `ELEVENLABS_API_KEY`: Your ElevenLabs API key.
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `KAGGLE_KEY`: Your Kaggle key for Gemma Access.
   - `KAGGLE_USERNAME`: Your Kaggle Username for Gemma Access.
   - `HF_ACCESS_TOKEN`: Your HuggingFace token for **google/shieldgemma-2b** access
   

4. **Run server**:
   Give it some time to download the big ShieldGemma model. If it takes too long, try to rerun the server.py
    ```bash
   python server.py
   ```
   
# 📑 Run the Extension
   1. Open Chrome browser.
   2. Type `chrome://extensions/` in the search bar.
   3. Switch **Developer Mode** to On.
   4. Press **Load Unpacked** on the top left.
   5. Choose the **browser_extension** folder located in the project.
   6. Open a new Chrome Tab and direct to a news page.
   7. Find the extension and click **Hear Summary**.
   8. Give it a few seconds as some models are running locally


# 🚀 About the Project
- **What**: ByteTheNews delivers bite-sized reads out summaries of online news stories while you are not looking.

- **Problem**: ByteTheNews addresses the needs of busy professionals with limited time, enhances accessibility for individuals with visual impairments, and provides a screen-free, customizable way to consume news, perfect for unwinding after a long day.

- **Business Impact**: With the potential to reach millions of news readers worldwide, ByteTheNews promotes inclusivity and accessibility, creating a positive social impact for diverse audiences.

# 🏆 Hackathon Details

- **Hackathon Name**: Gemma 2 AI Challenge
- **Challenge**: Build intelligent AI solutions that harness the power of Gemma 2 models to transform processes and enhance productivity.

Team Members:
- **Ying Liu** - https://github.com/sophia172
- **Joenam Coutinho** - https://github.com/joenamcoutinho
- **Tanuj Guha Thakurta** - https://github.com/hexcodeblaster
- **Rekha Mathew** - https://github.com/RekhaMathew-Product

# 🎯 Key Features
- **Article Scraper**: Instantly condenses long news articles from your browser into clear, bite-sized summaries using the Newspaper Python package.
- **Text Summarizer**: Utilizes the Gemma API through Groq to transform lengthy text into concise, digestible summaries, making news easier to read.
- **Image Summarizer**: Leverages OpenAI's API to detect and summarize visual content.
- **Content Analyzer**: Scans and notifies users when sensitive content is present, ensuring they are informed before proceeding with the summarized news, powered by ShieldGemma.
- **Audio Output**: Converts text summaries into natural-sounding audio using ElevenLab's API, with automatic warnings for sensitive content.
- **Web Browser Extension**: Seamlessly integrates into your browser with a user-friendly interface, allowing easy control to start, pause, or resume audio.

# 🛠️ Tech Stack

- Frontend: Javascript
- Backend: Python
- AI Models: Gemma2, GemmaShield, ElevenLabs, OpenAI



# 🎥 Demo
Demo Link: 

# 🔥 Screenshots

# 🔗 Links
- GitHub Repository: [Github](https://github.com/sophia172/ByteTheNews_Hackthon) 
- Live Demo: 
- Presentation Deck: 

# 💡 Future Enhancements
- Select voice as male or female as per users preference 
- Implemented on mobile phone device 

# 📧 Contact
Name - sophia.j.liu@gmail.com
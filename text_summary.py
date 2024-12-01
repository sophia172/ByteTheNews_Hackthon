
import os
from openai import OpenAI
from dotenv import load_dotenv
import asyncio
from utils import timing
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
from logger import logging

class TextSummary():
    def __init__(self, model="gemma2-9b-it"):
        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=GROQ_API_KEY,
        )
        self.model = model

    @timing
    async def __call__(self, article):
        chat_completion = self.client.chat.completions.create(
                                    messages=[
                                        {
                                            "role": "user",
                                            "content": "Read this news article and summarise it in less than 3 sentences"
                                                       f"{article}"
                                                       f"Summary:",

                                        }
                                    ],
                                    model=self.model,
                                )
        summary = chat_completion.choices[0].message.content
        logging.info(f"Summary of the text is: {summary}")
        # await speak(chat_completion.choices[0].message.content, speed=1.5)
        return summary

if __name__ == "__main__":
    summary = TextSummary(model="gemma2-9b-it")
    # summary = TextSummary(model="llama3-8b-8192")
    text = """While completing his residency in anesthesiology at Massachusetts General Hospital in the mid-2000s, Jon Bloom saw his fair share of foot amputations among patients with diabetes. The culprit: infected foot ulcers.

“Some days, I would spend the entire day doing nothing but amputations,” Bloom says. “It’s a major problem we haven’t really moved forward on.”

Now Bloom’s startup, Podimetrics, has developed a smart mat that can detect early warning signs before foot ulcers form, which may drastically reduce amputations and cut medical costs. The startup was additionally co-founded by Brian Petersen SM ’13, MBA ’13, who is Podimetrics’ chief data scientist; David Linders SM ’13, MBA ’13, who is Podimetrics’ chief technology officer; and Harvard Business School graduate Jeff Engler.

Conceived at an MIT Hacking Medicine hackathon, the smart mat is equipped with sensors that detect minute spikes in temperature around the foot, which precede the formation of ulcers. A patient stands on the mat for about 20 seconds per day, and the measurements are sent to the cloud. If an ulcer is suspected, the startup shoots an alert to the patient’s physician, who can help the patient start a treatment plan.

Currently, the mat is in more than 500 homes. In a paper published by the startup recently in Diabetes Care, the mat detected 97 percent of incipient ulcers about five weeks before they were diagnosed at the doctor’s office. “That’s an enormous jump in time, where patients and physicians can put a plan in place with the goal of preventing the foot ulcer from occurring,” Bloom says.

The other promising statistic from the study, Bloom adds, was that 86 percent of the test subjects used the system at least three days per week over the duration of the nine-month trial. “That was the most exciting statistic,” he says, “because we know it’s a challenge [for patients] to incorporate these technologies into daily workflow.”

Tracking heat

Once formed, foot ulcers have a high probability of infection. According to the Mayo Clinic, more than 80 percent of amputations from diabetic patients are due to infected foot ulcers.

They’re also costly for public and private payers: Medical costs are estimated to be about $15,000 to $20,000 per patient per ulcer. According to a 2014 study published in Diabetes Care, ulcer care adds around $9 billion to $13 billion to the direct annual costs associated with diabetes, “making it one of most expensive complications in all of medicine and one that nobody really knows about,” Bloom says.

Podimetrics relies on a decades-old discovery: Wounds heat up before they break down. Foot ulcers take weeks to develop, usually from the force of walking or friction from shoes. When ulcers begin to form, the tissue breaks down, causing inflammation, leading to minute spikes in temperature.

In 2007, a National Institutes of Health study used infrared temperature monitoring as an early warning sign of foot ulcers. If patients with diabetes stayed off their feet when they saw temperature spikes of about 2.2 degrees Celsius, the study found, incidents of foot ulcers dropped 70 percent.

Podimetrics uses that threshold, programming its mat to monitor the whole foot and note areas that are 2.2 C hotter than other areas. Once alerted, physicians call the patient, telling them to keep off their feet until the temperature dies down. Or they can set up an appointment.

Foot ulcers are traditionally diagnosed visually by patients or physicians, once an open sore has developed. By then they are potentially dangerous, and costly in terms of time and money: Patients must stay off their feet, sometimes for months, in order to heal. They also have to go back to clinic once a week.

“[Physicians and patients] don’t find [ulcers] until after fact, and then they’re going down the wound-care path,” Bloom says. “We’re saying let’s identify them before they’re open, so we can do simple, brief preventative interventions.”

A common concern with such diagnostic technologies is the rate of false positives. But those haven’t been an issue, Bloom says. Each mat can be remotely customized for a higher or lower temperature threshold. A lower threshold means greater sensitivity but more potential for false positives; a higher threshold means less sensitivity but also less potential for false positives. “Not surprisingly, every clinician has it on the most sensitive setting, so they don’t miss anything,” Bloom says.

Moreover, false positives for foot ulcers aren’t as disruptive as those for other diseases and conditions. With false positives for cancers, for instance, patients may get an unnecessary biopsy or blood test. “With foot ulcers, you may get an extra phone call or need to walk less for short period of time,” Bloom says. “It’s fairly benign.”

Leveraging the innovation ecosystem

In 2011, Bloom attended MIT’s first Hacking Medicine hackathon at the invitation of an organizer. “The idea was to get 100 people in a room to hack any medical idea, winner take all. It sounded like an interesting event. I had no idea it was going to change my life,” says Bloom, who is a former student in the MIT Sloan School of Management.

During the hackathon, the co-founders teamed up to tackle a major, yet relatively unknown issue that Bloom knew all too well. “[Foot ulcers] are so costly and have high mortality rates, yet all innovation has been on the treatment side,” Bloom says. “We wanted to prevent them from occurring.”

After talking to many doctors and patients, the team developed various concepts, including an insole system that continuously monitored foot pressures and sent real-time data to mobile phones. For their concept, the team was named one of the hackathon’s two winners.

Momentum from the victory carried the team to the 2011 pitch contest for the MIT $100K Entrepreneurship Competition, where they came in second place and earned the audience choice award. The following year, they won the life science track at the $100K Launch finale.

Classes Bloom took as a student on the Entrepreneurship and Innovation track, such as 15.3901 (New Enterprises), and events organized through MIT Sloan helped shape the startup further and attract funding. A trip to Silicon Valley, for instance, attracted an angel investor. “I can’t imagine Podimetrics without the MIT environment,” Bloom says. “It was such an unbelievable place to be.” Linders and Petersen were part of the Leaders for Global Operations program.

In fall 2012, Podimetrics entered Rock Health — a major digital-health startup accelerator — and then the now-defunct Beehive incubator, joining many other MIT spinouts. Among those there at the time were Ecovent, Pillpack, Bevi, and Ministry of Supply. “We fed off each other, motivated each other. If something needed marketing or engineering, you’d find someone down the hall,” Bloom says.

In the incubator, Podimetrics created an early prototype — a mat with large sensors and a circuit board sticking out, all held together with electric tape — and took it through a series of clinical trials. The startup then relocated to its current headquarters in Somerville, Massachusetts, where it refined the prototype into its commercial iteration. In the past five years, the startup has raised more than $8 million in funding.  

The startup is scaling up and aiming to get into many more homes in the coming year. It’s also starting a new set of studies to measure the cost and health outcomes associated with the mat. “Now we’re focused on gathering more data, continuing to build on data we have, and learning the best environment where we can help,” Bloom says."""
    asyncio.run(summary(text))
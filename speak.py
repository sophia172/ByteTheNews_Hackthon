
from elevenlabs.client import ElevenLabs, Voice, VoiceSettings
from dotenv import load_dotenv
from logger import logging
import os
import asyncio
from utils import timing
import io

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")


@timing
async def speak(text: str):
    try:
        client = ElevenLabs(
            api_key=ELEVENLABS_API_KEY
        )

        audio = client.generate(
            text=text,
            voice=Voice(
                voice_id="onwK4e9ZLuTAKqWW03F9",
                settings=VoiceSettings(
                    stability=0.5,
                    similarity_boost=0.75,
                    output_format="pcm_44100",
                    style=0.0,
                    use_speaker_boost=False,
                ),
            ),
            model="eleven_turbo_v2_5",
        )
        logging.info(f"Within speak function, audio is {audio}")
        # Check if play returns a coroutine
        if audio is not None:
            audio_bytes = b''.join(audio)
            audio_bytes = io.BytesIO(audio_bytes)
            logging.info(f"Within speak function, audio bytes created with {audio_bytes}")
            return audio_bytes
        else:
            logging.info("No audio was generated")

    except Exception as e:
        logging.error(f"Error in speak function: {e}")


if __name__ == "__main__":
    asyncio.run(speak("e money \"derived substantially the whole of its value from the activities of Mr Grint\", which was \"otherwise realised\" as income.\n\nHe previously lost another, separate court case in 2019 that involved a £1m tax refund.\n\nGrint appeared in all eight Harry Potter films from 2001 until 2011.\n\nSince then, he has appeared in the films Into the White and Knock at the Cabin, and also appeared on TV and in theatre.\n\nHe has starred in Apple TV series Servant for the last four years.",))
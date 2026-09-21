import asyncio
import os
import logging
from typing import Optional
from dotenv import load_dotenv
from speechmatics.rt import Microphone
from speechmatics.voice import VoiceAgentClient, VoiceAgentConfigPreset, AgentServerMessageType

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SovereignAgent")

class SovereignVoiceAgent:
    def __init__(self, api_key: Optional[str] = None, sample_rate: int = 16000, chunk_size: int = 320):
        self.api_key = api_key or os.getenv("SPEECHMATICS_API_KEY")
        if not self.api_key:
            raise ValueError("SPEECHMATICS_API_KEY is missing from environment variables.")
        
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.config = VoiceAgentConfigPreset.load("adaptive")
        self.client = VoiceAgentClient(api_key=self.api_key, config=self.config)
        self.mic = Microphone(sample_rate=self.sample_rate, chunk_size=self.chunk_size)
        self._register_handlers()

    def _register_handlers(self) -> None:
        @self.client.on(AgentServerMessageType.ADD_SEGMENT)
        def on_segment(message):
            for segment in message.get("segments", []):
                speaker = segment.get("speaker_id", "S1")
                text = segment.get("text", "")
                logger.info(f"[{speaker}]: {text}")

        @self.client.on(AgentServerMessageType.END_OF_TURN)
        def on_turn_end(message):
            logger.info("[END OF TURN DETECTED]")

    async def run(self) -> None:
        if not self.mic.start():
            logger.error("Failed to initialize microphone via PyAudio.")
            return

        try:
            await self.client.connect()
            logger.info("MySovereignVOIP_Agent online. Streaming active...")

            while True:
                audio_chunk = await self.mic.read(self.chunk_size)
                await self.client.send_audio(audio_chunk)
        except asyncio.CancelledError:
            logger.info("Agent task cancelled.")
        finally:
            self.mic.stop()
            await self.client.disconnect()
            logger.info("Agent session safely closed.")

if __name__ == "__main__":
    agent = SovereignVoiceAgent()
    try:
        asyncio.run(agent.run())
    except KeyboardInterrupt:
        logger.info("Interrupted by user. Shutting down.")

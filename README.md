<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./logo/speechmatics-dark-theme-logo.png">
  <source media="(prefers-color-scheme: light)" srcset="./logo/speechmatics-light-theme-logo.png">
  <img alt="Speechmatics Logo" src="./logo/speechmatics-light-theme-logo.png" width="70%">
</picture>

<br/>

# MySovereignVOIP_Agent

**An enterprise-grade, high-performance Sovereign Voice AI & Real-Time Telephony Agent built on modern async Python patterns, advanced VAD turn-detection, and low-latency speech architectures.**

[![PyPI - batch](https://img.shields.io/pypi/v/speechmatics-batch?label=batch)](https://pypi.org/project/speechmatics-batch/)
[![PyPI - rt](https://img.shields.io/pypi/v/speechmatics-rt?label=rt)](https://pypi.org/project/speechmatics-rt/)
[![PyPI - agent-stt](https://img.shields.io/pypi/v/speechmatics-agent-stt?label=agent-stt)](https://pypi.org/project/speechmatics-agent-stt/)
[![PyPI - voice](https://img.shields.io/pypi/v/speechmatics-voice?label=speechmatics-voice)](https://pypi.org/project/speechmatics-voice/)
[![Python Versions](https://img.shields.io/pypi/pyversions/speechmatics-batch.svg)](https://pypi.org/project/speechmatics-batch/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/AnticipatedD/MySovereignVOIP_Agent/blob/main/LICENSE)
[![Build Status](https://github.com/AnticipatedD/Vane-Guard-Sovereign-RAG/actions/workflows/test.yaml/badge.svg)](https://github.com/AnticipatedD/Vane-Guard-Sovereign-RAG)

**Fully typed** request parameters and response schemas. Built with **async/await**, strict type hints, and production context managers for zero-latency streaming pipelines.

[Portfolio](https://anticipatedd.github.io/mdhossain) • [Project Framework](https://anticipatedd.github.io/VANE-SPACE-SLA) • [Credly Badges](https://credly.com/users/mdahossain) • [Microsoft Learn](https://learn.microsoft.com/en-gb/users/mdahossain/)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Quick Start](#-quick-start)
- [Architecture & Core Pipeline](#-architecture--core-pipeline)
- [Production Voice Agent Implementation](#-production-voice-agent-implementation)
- [Deployment & Sovereign Infrastructure](#-deployment--sovereign-infrastructure)
- [Author & Credentials](#-author--credentials)

---

## 🚀 Overview

**MySovereignVOIP_Agent** represents the next generation of autonomous conversational AI infrastructure. Designed from the ground up to eliminate conversational lag, manage complex multi-speaker diarization, and execute robust server-side turn detection without heavy local machine-learning runtimes.

---

<h2 id="quick-start">⚡ Quick Start</h2>

### Installation
Clone the repository and install the required core packages:
```bash
git clone [https://github.com/AnticipatedD/MySovereignVOIP_Agent.git](https://github.com/AnticipatedD/MySovereignVOIP_Agent.git)
cd MySovereignVOIP_Agent
```
```python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
---
# Install essential dependencies
```bash
pip install speechmatics-rt speechmatics-voice speechmatics-batch python-dotenv pyaudio
```
- Set up your environment variables by creating a `.env` file in the root directory: 
```env
SPEECHMATICS_API_KEY=your_api_key_here
```
---
🛠️**Production Voice Agent Implementation**: 
​The core asynchronous entrypoint implementing adaptive smart turn detection, real-time segment parsing, and speaker tracking for production voice deployments: 
```
import asyncio
import os
from dotenv import load_dotenv
from speechmatics.rt import Microphone
from speechmatics.voice import VoiceAgentClient, VoiceAgentConfigPreset, AgentServerMessageType

load_dotenv()

async def main():
    api_key = os.getenv("SPEECHMATICS_API_KEY")
    if not api_key:
        raise ValueError("SPEECHMATICS_API_KEY environment variable not set.")

    # Load adaptive sovereign voice configuration preset
    config = VoiceAgentConfigPreset.load("adaptive")

    client = VoiceAgentClient(
        api_key=api_key,
        config=config
    )

    @client.on(AgentServerMessageType.ADD_SEGMENT)
    def on_segment(message):
        for segment in message.get("segments", []):
            speaker = segment.get('speaker_id', 'S1')
            text = segment.get('text', '')
            print(f"[{speaker}]: {text}")

    @client.on(AgentServerMessageType.END_OF_TURN)
    def on_turn_end(message):
        print("[END OF TURN DETECTED]")

    mic = Microphone(sample_rate=16000, chunk_size=320)
    if not mic.start():
        print("Error: PyAudio initialization failed.")
        return

    try:
        await client.connect()
        print("MySovereignVOIP_Agent online. Speak into your microphone...")

        while True:
            audio_chunk = await mic.read(320)
            await client.send_audio(audio_chunk)
    except KeyboardInterrupt:
        print("\nShutting down agent...")
    finally:
        mic.stop()
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```
---
📐**Architecture & Core Pipeline** 
```
sequenceDiagram
    participant Mic as Audio Input / Mic
    participant Client as MySovereignVOIP_Agent
    participant Engine as Speechmatics Voice Service
    participant LLM as LLM / Execution Core

    Mic->>Client: Stream PCM Chunks (16kHz)
    Client->>Engine: WebSocket Audio Binary Transmission
    Engine->>Client: Add Segment (Speaker ID & Text)
    Engine->>Client: End Of Turn Trigger
    Client->>LLM: Process Conversational Intent
    LLM->>Client: Generate Response Pipeline
```
---

🔐**Deployment & Sovereign Infrastructure**: 
- ​**Cloud & On-Premises Ready**: Deploy seamlessly via global SaaS endpoints or orchestrate locally inside isolated Kubernetes clusters.

-**​Security & Compliance**: Fully aligned with enterprise requirements, ensuring secure memory-buffered handling and strict data governance. 

---

​🏆**Author & Credentials ​Architect, Refined and maintaining by MD ABUL HOSSAIN (AnticipatedD)**:
*SVP & Head of Strategic Partnerships* TARU Global Access (IBM Business Partner Plus & Microsoft Business Partner)
# ​European Commission Designation: 
- **Category B Senior Researcher & European F&T Expert**
- ​AlphaNova Tech Global Leaderboard: **Rank #28 (Individual Rank 57/873).**
- **​AMD ROCm Certified Associate** & Official Contributor (3000+ points pool).
- ​Certifications: **87 Advanced/Enterprise Certifications (19 IBM Badges, 140 Microsoft Badges & 30 Trophies, Level 11).**

---
​📄 **License**
​Licensed under the MIT License - see the [LICENSE](license.md) file for details.

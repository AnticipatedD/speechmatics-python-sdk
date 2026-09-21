import pytest
from unittest.mock import MagicMock, patch
from sovereign_agent.agent import SovereignVoiceAgent

def inquisitive_env_setup():
    return "test_mock_api_key_12345"

@patch.dict("os.environ", {"SPEECHMATICS_API_KEY": "test_mock_api_key_12345"})
def test_agent_initialization():
    agent = SovereignVoiceAgent()
    assert agent.api_key == "test_mock_api_key_12345"
    assert agent.sample_rate == 16000
    assert agent.chunk_size == 320

def test_missing_api_key():
    with patch.dict("os.environ", {}, clear=True):
        with pytest.raises(ValueError, match="SPEECHMATICS_API_KEY is missing"):
            SovereignVoiceAgent(api_key=None)

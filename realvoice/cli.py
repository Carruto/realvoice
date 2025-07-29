
import argparse
import asyncio
from .tts_engine import synthesize

def main():
    parser = argparse.ArgumentParser(description="Portable Edge TTS Wrapper")
    parser.add_argument("--text", required=True, help="Text to synthesize")
    parser.add_argument("--voice", required=True, help="Voice name")
    parser.add_argument("--output", required=True, help="Output MP3 path")
    parser.add_argument("--version", action="store_true", help="Show version info")
    args = parser.parse_args()

    if args.version:
        try:
            import edge_tts
            print("portable_edge_tts 1.0.0, edge-tts", edge_tts.__version__)
        except:
            print("portable_edge_tts 1.0.0, edge-tts not available")
        return

    asyncio.run(synthesize(args.text, args.voice, args.output))

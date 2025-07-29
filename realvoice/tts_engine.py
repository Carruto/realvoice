
import edge_tts

async def synthesize(text, voice, output):
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output)

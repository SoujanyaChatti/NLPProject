import wave
import audioop

def create_silent_wav(filename, duration=1, framerate=16000, nchannels=1, sampwidth=2):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(nchannels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(framerate)

        # Create silent audio data
        num_frames = duration * framerate
        silent_frame = audioop.lin2lin(b'\x00\x00', sampwidth, sampwidth)
        silent_data = silent_frame * num_frames

        wf.writeframes(silent_data)

if __name__ == "__main__":
    create_silent_wav("ai-english-learning-platform/tests/backend/test.wav")

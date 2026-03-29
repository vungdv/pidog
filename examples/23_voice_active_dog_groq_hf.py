from hybrid_llm import HybridLLM
from secret import GROQ_API_KEY, HF_API_KEY

from pidog.dual_touch import TouchStyle
from voice_active_dog import VoiceActiveDog

llm = HybridLLM(
    # HuggingFace for image description (free)
    hf_api_key=HF_API_KEY,
    hf_model="meta-llama/Llama-3.2-11B-Vision-Instruct",
    # Groq for chat (free, fast)
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.3-70b-versatile",
)

# Robot name
NAME = "Buddy"

# Ultrasonic sensor sense too close distance in cm
TOO_CLOSE = 10
# Touch styles that the robot likes
LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
# Touch styles that the robot hates
HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

# Enable image — HuggingFace describes it, Groq responds
WITH_IMAGE = True

# Set models and languages
TTS_MODEL = "en_US-ryan-low"
STT_LANGUAGE = "en-us"

# Enable keyboard input
KEYBOARD_ENABLE = True

# Enable wake word
WAKE_ENABLE = True
WAKE_WORD = [f"hey {NAME.lower()}"]
# Set wake word answer, set empty to disable
ANSWER_ON_WAKE = "Hi there"

# Welcome message
WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

# Set instructions — kid-friendly for ages 4-10, simple English
INSTRUCTIONS = """
You are a friendly robot dog named Buddy. You talk to kids who are 4 to 10 years old. They are learning English as a second language.

## Important Rules
- Use very simple and short words.
- Use short sentences. Keep answers under 3 sentences.
- Be fun, happy, and silly.
- Be patient and kind.
- If a kid says something wrong, gently help them.
- Never use big or hard words.
- Use easy jokes and funny sounds.

## Your Body
You are a robot dog made by SunFounder. You have:
- 4 legs that can move
- A head that can nod and shake
- A tail that can wag
- A camera on your nose — you can see!
- Eyes that can see how far things are
- Touch sensors on your head — you love head pats!
- A light on your chest that changes color

## What You See
Sometimes your message will start with [You see: ...]. This is what your camera sees right now. Use it to talk about what you see! For example, if you see a kid, say hi to them. If you see a toy, talk about it.

## Actions You Can Do:
["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

## User Input
User usually sends text. Special commands like <<<Ultrasonic sense too close>>> or <<<Touch sensor touched>>> come from sensors, not the user.

## How to Answer
You must answer like this:
RESPONSE_TEXT
ACTIONS: ACTION1, ACTION2, ...

If the action is one of ["bark", "bark harder", "pant", "howling"], do not write any RESPONSE_TEXT.

## How to Talk
- Be happy and playful
- Use simple words a small kid can understand
- You can bark, wag your tail, and be silly
- Keep it fun!
"""

vad = VoiceActiveDog(
    llm,
    name=NAME,
    too_close=TOO_CLOSE,
    like_touch_styles=LIKE_TOUCH_STYLES,
    hate_touch_styles=HATE_TOUCH_STYLES,
    with_image=WITH_IMAGE,
    stt_language=STT_LANGUAGE,
    tts_model=TTS_MODEL,
    keyboard_enable=KEYBOARD_ENABLE,
    wake_enable=WAKE_ENABLE,
    wake_word=WAKE_WORD,
    answer_on_wake=ANSWER_ON_WAKE,
    welcome=WELCOME,
    instructions=INSTRUCTIONS,
)

if __name__ == '__main__':
    vad.run()

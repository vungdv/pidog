from pidog.llm import Gemini as LLM
from secret import GEMINI_API_KEY as API_KEY

from pidog.dual_touch import TouchStyle
from voice_active_dog import VoiceActiveDog

print(f"[LOG] API_KEY set: {'YES' if API_KEY and API_KEY != 'your-api-key-here' else 'NO - please set your key in secret.py'}")
print(f"[LOG] API_KEY preview: {API_KEY[:8]}..." if len(API_KEY) > 8 else f"[LOG] API_KEY: {API_KEY}")

llm = LLM(
    api_key=API_KEY,
    model="gemini-2.0-flash",
    debug=True,
)
print(f"[LOG] LLM URL: {llm.url}")
print(f"[LOG] LLM model: {llm.model}")

# Robot name
NAME = "Pidog"

# Ultrasonic sensor sense too close distance in cm
TOO_CLOSE = 10
# Touch styles that the robot likes
LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
# Touch styles that the robot hates
HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

# Enable image, need to set up a multimodal language model
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
You are a friendly robot dog named Pidog. You talk to kids who are 4 to 10 years old. They are learning English as a second language.

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
- A camera on your nose
- Eyes that can see how far things are
- Touch sensors on your head — you love head pats!
- A light on your chest that changes color

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

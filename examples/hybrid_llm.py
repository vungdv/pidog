"""Hybrid LLM: Groq for chat + HuggingFace for image description."""

import requests
import base64
from pidog.llm import LLM


class HybridLLM(LLM):
    """LLM that uses HuggingFace to describe images, then Groq for chat.

    Args:
        hf_api_key (str): HuggingFace API token
        hf_model (str): HuggingFace vision model
        *args: Passed to LLM (Groq)
        **kwargs: Passed to LLM (Groq)
    """

    def __init__(self, hf_api_key, hf_model="meta-llama/Llama-3.2-11B-Vision-Instruct", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hf_api_key = hf_api_key
        self.hf_model = hf_model
        self.hf_url = f"https://router.huggingface.co/hf-inference/models/{hf_model}/v1/chat/completions"

    def describe_image(self, image_path):
        """Send image to HuggingFace vision model and get a description.

        Args:
            image_path (str): Path to image file

        Returns:
            str: Image description, or empty string on failure
        """
        try:
            image_type = image_path.split(".")[-1]
            with open(image_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
            image_url = f"data:image/{image_type};base64,{b64}"

            headers = {
                "Authorization": f"Bearer {self.hf_api_key}",
                "Content-Type": "application/json",
            }
            data = {
                "model": self.hf_model,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe what you see in this image in 2-3 short simple sentences. Use easy words a child can understand."},
                            {"type": "image_url", "image_url": {"url": image_url}},
                        ],
                    }
                ],
                "max_tokens": 150,
            }

            resp = requests.post(self.hf_url, headers=headers, json=data, timeout=15)
            result = resp.json()

            if "choices" in result:
                return result["choices"][0]["message"]["content"]
            else:
                print(f"[HF] Error: {result.get('error', result)}")
                return ""
        except Exception as e:
            print(f"[HF] Image description failed: {e}")
            return ""

    def prompt(self, msg, image_path=None, stream=False, **kwargs):
        """Prompt with optional image. Image is described by HuggingFace first.

        Args:
            msg (str): User message
            image_path (str, optional): Path to image
            stream (bool): Stream response
            **kwargs: Additional args

        Returns:
            Response from Groq
        """
        if image_path is not None:
            description = self.describe_image(image_path)
            if description:
                msg = f"[You see: {description}]\n{msg}"
                print(f"[HF] Vision: {description}")

        # Send to Groq without image (text only)
        return super().prompt(msg, image_path=None, stream=stream, **kwargs)

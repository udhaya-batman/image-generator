import streamlit as st
import openai
import os

st.set_page_config(page_title="AI Image Generator 🎨", layout="centered")

st.title("🧠 AI Image Generator from Text")
st.write("Enter a prompt, and get an AI-generated image!")

openai.api_key = os.getenv(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)

prompt = st.text_input("Enter image description:", placeholder="e.g. A cat wearing sunglasses on a beach")

if st.button("Generate Image"):
    if not prompt:
        st.warning("Please enter a prompt!")
    else:
        with st.spinner("Generating image..."):
            try:
                response = openai.Image.create(
                    prompt=prompt,
                    n=1,
                    size="512x512"
                )
                image_url = response['data'][0]['url']
                st.image(image_url, caption="Generated Image", use_column_width=True)
                st.success("Image generated successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

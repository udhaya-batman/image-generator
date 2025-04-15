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

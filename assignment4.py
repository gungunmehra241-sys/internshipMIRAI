import streamlit as st 
import requests
import random

st.title("MY AI IMAGE GENERATOR")

st.sidebar.header("SETTINGS")

art_style=st.sidebar.selectbox("Select desired Art Style",["Photorealistic","Cyberpunk","Ghibli","3D render"])

width = st.sidebar.slider("Image width",min_value=256,max_value=1024,value=768)
height = st.sidebar.slider("Image height",min_value=256,max_value=1024,value=768)
magic_tool= st.sidebar.checkbox("✨ Enable Magic Enhance")
user_prompt = st.text_input("Describe the image you want to generate:")

#surprise prompts

surprise =  [
    "A cyber punk giant horse riding the land of Mars",
    "A vintage BMW car driving on Jupiter",
    "A vintage 1950s diner run entirely by aliens on the moon",
    "A tinkerbell inspired amazon forest with fairies",
    "A city built inside a giant seashell at the bottom of the ocean"
]

final_prompt=None

if st.button(" 🎲 Surprise Me!"):
    final_prompt= random.choice(surprise)
    st.info(f"Surprise prompt: {final_prompt}")

if st.button("Generate image"):
    if user_prompt:
        final_prompt=user_prompt
    else:
        st.warning("Please give an image description!")

if final_prompt:
    with st.spinner("Rendering the image:"):
            full_prompt=f"{user_prompt},make the art style : {art_style}"
            if magic_tool:
                full_prompt+=" -Masterpiece, 8k resolution, highly detailed, trending on art station, unreal engine 5 render"
            url=f"https://image.pollinations.ai/prompt/{full_prompt}?width={width}&height={height}"
            response = requests.get(url)

            if response.status_code==200:
                st.success("IMAGE GENERATED")
                #st.write(response)
                # convert the binary into pixels or an actual image
                st.image(response.content,caption=full_prompt)
                st.download_button(
                    label = "Download",
                    data=response.content,
                    file_name="MY_AI_IMAGE.png",
                    mime="image/png"
                )
else:
     st.error("API NOT WORKING")

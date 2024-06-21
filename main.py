import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import streamlit as st

pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4",
                                                  torch_dtype=torch.float32)

def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols
    
    w, h = imgs[0].size
    grid = Image.new('RGB', size = (cols*w,
                                   rows * w))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box = (i%cols*w, i // cols*h))
    return grid

def generate_images(prompt):
    images = pipeline(prompt).images
    grid = image_grid(images, rows=1, cols=len(images))
    return grid

def app():
    st.title("Stable Diffusion Image Generation")
    prompt = st.text_input("Enter your prompt:")
    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            image = generate_images([prompt])
            st.image(image)

if __name__ == "__main__":
    app()

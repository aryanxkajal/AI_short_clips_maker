#import openai
from openai import OpenAI

client = OpenAI(api_key='add_your_api_key_here')


import re
import requests
from pathlib import Path
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips, TextClip, ColorClip

# Initialize OpenAI with your API key

def get_city_fact(city_name):
    # Generate a fact about the city using OpenAI's chat completion method
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides fun facts about cities. The facts shoul be under 50 words."},
            {"role": "user", "content": f"Tell me an interesting fact about {city_name}."}
        ]
    )
    fact = completion.choices[0].message.content.strip()  # Access `.content` to get the text
    print(f"Fact about {city_name}: {fact}")
    return fact

def generate_dalle_image(prompt, output_path):
    # Generates an image using OpenAI's DALL-E and saves it locally
    response = client.images.generate(model="dall-e-3", prompt=prompt, n=1, size="1024x1792")
    image_url = response.data[0].url  # Access the URL correctly from the response

    # Download and save the image
    image_response = requests.get(image_url)
    with open(output_path, 'wb') as file:
        file.write(image_response.content)
    print(f"Image saved to {output_path}")


def generate_openai_voiceover(text, output_path):
    # Generates a voiceover using OpenAI's TTS API
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    
    # Save the voiceover as an MP3 file
    with open(output_path, 'wb') as file:
        file.write(response.content)
    print(f"Voiceover saved to {output_path}")

def create_reel(city_name):
    clips = []
    # Get a fact about the city
    fact = get_city_fact(city_name)
    
    image_description = f"An image representing {city_name}. {fact}"
    
    # File paths for generated media
    image_path = f"image.png"
    audio_path = f"voiceover.mp3"
    
    # Generate image and voiceover
    generate_dalle_image(image_description, image_path)
    generate_openai_voiceover(fact, audio_path)
    
  

    # Load the audio and image files
    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path).set_duration(audio_clip.duration)

    
    overlay_color = (0, 0, 0)  
    overlay_opacity = 0.4  
    
    
    overlay_clip = ColorClip(size=image_clip.size, color=overlay_color, ismask=False).set_opacity(overlay_opacity).set_duration(audio_clip.duration)

    # Create a text clip for the fun fact
    text_lines = fact.split('. ')  
    wrapped_text = '\n\n'.join(text_lines)  
    
    fontsize = 60  
    
    
    
    # Create the text clip without a background and with padding
    text_clip = TextClip(
        wrapped_text,
        fontsize=fontsize,  
        color='white',
        
        size=(image_clip.w - 200, None),  
        method='caption'  
    )

    # Position the text in the center with padding
    text_clip = text_clip.set_position(('center', 'center')).set_duration(audio_clip.duration)

    # Create a background clip for padding
    padding = 20  
    text_background = ColorClip(size=(text_clip.w + padding * 2, text_clip.h + padding * 2), color=(0, 0, 0, 200)).set_opacity(0).set_duration(audio_clip.duration)

    # Position the text background behind the text
    text_background = text_background.set_position(('center', 'center'))

    
    scene_clip = CompositeVideoClip([image_clip, overlay_clip, text_background, text_clip]).set_duration(audio_clip.duration).set_audio(audio_clip)

    clips.append(scene_clip)

    # Concatenate all scene clips into one video
    final_clip = concatenate_videoclips(clips, method="compose")

    # Resize for 9:16 aspect ratio
    final_clip = final_clip.resize(height=1920, width=1080)

    

    # Export the final video
    output_video_path = "final_reel.mp4"
    final_clip.write_videofile(output_video_path, fps=24, codec="libx264", audio_codec="aac")
    print(f"Reel created and saved to {output_video_path}")


city_name = "New York City"  # Replace with any city name

create_reel(city_name, )

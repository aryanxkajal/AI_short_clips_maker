# AI_short_clips_maker


This project generates short video reels featuring fun facts about different cities using OpenAI's APIs. The reels consist of a generated image, a voiceover, and on-screen text displaying the fact about the city.


## Features

- City Fact Generation: Retrieves interesting facts about cities using OpenAI's chat completion model.
- Image Generation: Uses DALL-E to generate images representing the cities based on the retrieved facts.
- Voiceover Creation: Generates a voiceover for the fact using OpenAI's text-to-speech model.
- Video Creation: Combines the generated image, voiceover, and text into a final video reel.


## Requirements

Before running the code, ensure you have the following dependencies installed:

- Python 3.x
- OpenAI Python client
- MoviePy
- Requests
- Pydantic


## Usage

1. Set Up Your OpenAI API Key:
   Replace `add_your_api_key_here` in the code with your actual OpenAI API key.

2. Run the Script:
   Modify the `city_name` variable in the code to the city you want to create a reel for, and run the script:

3. Output:
   After running the script, a video reel named `final_reel.mp4` will be created in the same directory.


## Code Overview

The script consists of several functions:

- `get_city_fact(city_name)`: Generates a fun fact about the specified city using OpenAI's chat model.

- `generate_dalle_image(prompt, output_path)`: Generates an image using OpenAI's DALL-E model based on the given prompt and saves it locally.

- `generate_openai_voiceover(text, output_path)`: Creates a voiceover from the provided text using OpenAI's text-to-speech model and saves it as an MP3 file.

- `create_reel(city_name)`: Main function that orchestrates the process of creating the video reel, which includes generating the city fact, image, and voiceover, as well as composing the final video.

Thanks for checking out!

import argparse
from diffusers import AutoPipelineForText2Image
import torch
import matplotlib.pyplot as plt
import subprocess

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate image based on prompt text.")
    parser.add_argument("prompt", type=str, help="Text prompt for image generation")
    parser.add_argument("filename", type=str, help="Name of the file (without extension) where the generated image will be saved")
    parser.add_argument("--seed", type=int, default=1000, help="Seed for random generation")
    args = parser.parse_args()

    # Determine the save path based on filename argument
    save_path = f"data/{args.filename}.jpg"

    # Initialize pipeline
    pipeline = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16"
    ).to("cuda")
    
    generator = torch.Generator("cuda").manual_seed(args.seed)
    image = pipeline(args.prompt, generator=generator).images[0]

    # Display and save the image
    plt.imshow(image)
    plt.axis('off')  # Hide axis

    try:
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
        print(f"Image saved to {save_path}")

        # Call process.py
        process_command = ["python", "process.py", save_path, "--size", "512"]
        subprocess.run(process_command, check=True)
        print("Image processed successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

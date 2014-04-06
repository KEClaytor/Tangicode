# Main tangicode function
# Import all helper functions
import imagecapture as ic
import block as blk
import processimage as proc
import gamedemo as game

if __name__ == "__main__":
    # Wait for user input

    # Time to run
    # Get an image
    # (imagecapture.py)
    img = ic.take_image(1)
    # Process the image and return our blocks
    # (processimage.py)
    blocks = proc.segment(img)
    blocks.sort(blk.cmp_block)
    # Translate the blocks into a program
    for block in blocks:
        print block.action
    # Run the game
    game.run(blocks)

    # Reset the game

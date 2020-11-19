"""A module for dealing with BMP bitmap image files."""


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.

    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the
            range of 0-255.

    Raises:
        ValueError: If any of the integer values are out of range.
        OSError: If the file couldn't be written.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()      # The next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now.

        bmp.write(b'\x00\x00') # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00') # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell() # The next four bytes hold the integer offset to the
        bmp.write(b'\x00\x00\x00\x00')     # pixel data. Zero placeholder for now.

        # Image Header
        bmp.write(b'\x28\x00\x00\x00')# Image header size in bytes - 40 decimal
        bmp.write(_int32_to_bytes(width)) # Image width in pixels
        bmp.write(_int32_to_bytes(height)) # Image height in pixels
        bmp.write(b'\x01\x00')         # Number of image planes
        bmp.write(b'\x08\x00')         # Bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00') # No compression
        bmp.write(b'\x00\x00\x00\x00') # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00') # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00') # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00') # Use whole color table
        bmp.write(b'\x00\x00\x00\x00') # All colors are important

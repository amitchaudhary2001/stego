import gzip
import base64

def compress_text(text):
    # Convert text to bytes
    input_bytes = text.encode('utf-8')

    # Compress the input bytes
    compressed_bytes = gzip.compress(input_bytes)
    encoded_data = base64.b64encode(compressed_bytes).decode('utf-8')
    
    return encoded_data

def decompress_text(compressed_bytes1):
    compressed_bytes= base64.b64decode(compressed_bytes1.encode('utf-8'))
    decompressed_bytes = gzip.decompress(compressed_bytes)
    decompressed_text = decompressed_bytes.decode('utf-8')

    return decompressed_text

# Example usage
# text="amit"
# compressed_data = compress_text(text)
# print("Compressed data:")
# print((compressed_data))

# decompressed_text = decompress_text(compressed_data)
# print("Decompressed text:")
# print((decompressed_text))

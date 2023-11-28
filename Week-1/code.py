import base64

steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

for step in steps:
    encoded = base64.b64encode(step.encode())
    print(encoded)   
      
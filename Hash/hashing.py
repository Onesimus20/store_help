import json
import hashlib
 
My_info = {
  "Personal": [
   {
    "name": hashlib.sha224(b"Onesimus").hexdigest(),
    "age": hashlib.sha224(b"{21}").digest(),
    "marital_status": hashlib.sha224(b"single").hexdigest(),
    "contact": hashlib.sha224(b"{239348i802}").hexdigest()
   },

       {
    "name": hashlib.sha224(b"Onesimus").hexdigest(),
    "age": hashlib.sha224(b"{21}").digest(),
    "marital_status": hashlib.sha224(b"single").hexdigest(),
    "contact": hashlib.sha224(b"{239348i802}").hexdigest()
   },

      {
    "name": hashlib.sha224(b"Onesimus").hexdigest(),
    "age": hashlib.sha224(b"{21}").digest(),
    "marital_status": hashlib.sha224(b"single").hexdigest(),
    "contact": hashlib.sha224(b"{239348i802}").hexdigest()
   }

  ]
 }

json_string = json.dumps(My_info["Personal"], indent=4)
print(json_string)

with open("contacts.json", "w") as file:
  file.write(json_string)
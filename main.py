import micropip
await micropip.install("razorpay")

import razorpay, setuptools
from pyscript import display

client = razorpay.Client(auth=("rzp_live_h7HHdgtBmhiyff", "yaVQNulYrZwNoetoMPhGySKR"))

DATA = {
    "amount": 100,
    "currency": "INR",
    "receipt": "receipt#1",
    "notes": {
        "key1": "value3",
        "key2": "value2"
    }
}
x = client.order.create(data=DATA)
display(x['id'])

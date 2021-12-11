import os

# if env variables haven't been loaded using other means
if "PAYSTACK_PRIVATE_KEY" not in dict(os.environ):
    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env

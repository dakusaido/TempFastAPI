# import logging
import uvicorn
from dotenv import load_dotenv

from v1 import app as app_file

# from os import getenv
# from pyngrok import ngrok

app = app_file.app
load_dotenv()


def main():
    # if int(getenv("DEBUG")) == 1:
    #     logging.getLogger(__name__).setLevel(level=logging.DEBUG)

        # ngrok.set_auth_token(getenv("NGROK_AUTH_TOKEN"))

        # http_tunnel = ngrok.connect(8080)
        # print(http_tunnel.public_url)

        uvicorn.run(
            "main:app",
            # host=str(getenv("IP")),
            # port=int(getenv("PORT")), reload=True,
            # proxy_headers=False,
            # loop="auto"
        )

    # else:
    #     uvicorn.run(
    #         "main:app",
    #         host=str(getenv("IP")),
    #         port=int(getenv("PORT")),
    #         workers=int(getenv("WORKERS")),
    #         proxy_headers=False,
    #         loop="auto"
    #     )


if __name__ == "__main__":
    main()
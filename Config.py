import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23716755"))
    API_HASH = os.environ.get("API_HASH", "5503b68991d161b6863dba06ff28fcb0)
    BOT_TOKEN = os.environ.get("7475783320:AAFEgPpeHMaMdX9aID7dJsUa2SeU8vzmWiU", "")
    STRING_SESSION = os.environ.get("1BVtsOL8BuyS6lnQe47GETSf4kke192X10j5EkP1soMI8WkIpNblxSesGym_xaBBrtzb39N9tzJXqyFWFKCX_bSVfbG7gfo_CTxKbv5wiDBAJBlsxot2me_Tp0M-pfDD6dX0AsrdVStuAczz1leYKPPwRLafVu5Xs_5VKE4O0a2VUgNpHBbWsql5Bp3oswscRT8ELO_2RsKLCJUfz-vYuDkgUEt7OeqNYKSkryp00NWSxO1vGec7RSByt8NLmBVAhsuwiM7gD1TA5BU43wtbjttpK4hK4zHrvmkZT2HsHbruhXuw5bgY2NT_-MMWRPo05Nl8en-IhVRYw0Nx5O052n_wpi1H6hLg=", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("7233014143", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import logging
from typing import *
from pyrogram import Client
from pyrogram import *
from pyrogram.types import *
from config import API_ID, API_HASH, BOT_TOKEN


logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    plugins = dict(root="chatgpt")

app = Client(
    name="app",
    api_id=3755621,
    api_hash="86a96994dce114bb1b4bd4167c87a62b",
    bot_token="5074293303:AAGQX4Fe3W0viiYqG5Vy7RJzmRr6GAcO-fw",
    openai_api="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",
    plugins=plugins,
    workers=300,
)

app.run()
idle()

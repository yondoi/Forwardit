#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "24926597"
))
    API_HASH = os.environ.get("API_HASH", "86edabf8b1b0d7a767439c7750032f97")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6387438800:AAHVybKpSOmBQD9p3CS4hL_vmYrmf4TkTaw") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "@seven199512")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "videos")
    OWNER_ID = os.environ.get("OWNER_ID", "5399209978")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("AQDQj9UAXB2e2hFkpba2kKXWj-_Jw7V9X1A8AnCwEJJDckWDREPGTAKCCVYs037k74x5sDJ3McM3tV6aOHXed5pt4l4_2ht-MlWKqtyNTN1CWtjWVgMdLN89pcn3hurDqmWteWXKokIEHdKHix6GcJzCSDC8et4K24vHB2gsUxO2DMjMU-0WUH60_lJ29D3Hvzb3PpV-k90dmeogiXWfcZ3-TDFzz-Yo2_U8x4JQTumJiaAg7pu-mWC68IXXYnc1_2N3I5bpEAfE5WTu2qbNFI0K9WBTtALz0gT1kM3V56InSBkEsecV9hKOUe_WhxC4zbFiBFaknZcCDjjFftErF3_u4CdsCQAAAAFB0Wf6AA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", 12345))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

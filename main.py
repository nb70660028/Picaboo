"""
                                ।। श्री ।।
                           ।। श्री गणेशाय नम: ।।

            This is code of Telegram Bot — Picaboo.
            Created by "Niranjan Pratibha Nagnath Bhol."
            Made in 💛 with ........ .
                                                                    """

# Version 1

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import time

with open('Token.txt', 'r') as Token:
    TOKEN = Token.read()

updater = Updater(TOKEN,
        use_context=True)

# Start ------------------------------------------------------------------------------------------------------------

def start(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text(
		"Hi there, I am Picaboo..!! 👻")
    time.sleep(1)
    update.message.reply_text(
		"This is the video Showing how to use me.. 👇")
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/51')
    update.message.reply_text(
		"You don't have to type anything, just click on the blue text, to run the Bot.")
    time.sleep(5)
    update.message.reply_text(
		"I can help you with,\n\n✿ Textbooks\n✿ Notes\n✿ Assignments\n✿ Lab Manual\n✿ Previous Year Question Papers\n    ..... and many more..!!")
    time.sleep(1)
    update.message.reply_text(
		"Please, Select the Subject. 📚")
    time.sleep(1)
    update.message.reply_text(
        "Click on to 👉 /Select_a_Subject to Dive In ...")

def selecting_subject(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Subject :➝\n\n ➜  /Physics - For Physics\n ➜  /Chemistry - For Chemistry\n ➜  /BEE - For BEE\n ➜  /BXE - For BXE\n ➜  /PPS - For PPS\n ➜  /Mechanics - For Mechanics\n ➜  /MathsI - For Maths-I\n ➜  /SME - For SME\n ➜  /More")

# Subjects ------------------------------------------------------------------------------------------------------------

def physics(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Physics_Textbook\n➜ /Physics_Notes\n➜ /Physics_PYQ")

def chemistry(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Chemistry_Textbook\n➜ /Chemistry_Notes\n➜ /Chemistry_PYQ")

def bee(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /BEE_Textbook\n➜ /BEE_Notes\n➜ /BEE_PYQ")

def bxe(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /BXE_Textbook\n➜ /BXE_Notes\n➜ /BXE_PYQ")

def pps(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /PPS_Textbook\n➜ /PPS_Notes\n➜ /PPS_PYQ")

def mechanics(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Mechanics_Textbook\n➜ /Mechanics_Notes\n➜ /Mechanics_PYQ")

def mathsI(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /MathsI_Textbook\n➜ /MathsI_Notes\n➜ /MathsI_PYQ")

def sme(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /SME_Textbook\n➜ /SME_Notes\n➜ /SME_PYQ")

def more(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Timetable\n➜ /Syllabus\n➜ /I_have_a_Suggestion")

# Content
# Physics ------------------------------------------------------------------------------------------------------------

def physics_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Physics Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/14')

def physics_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Physics_Notes_Unit_1\n➜ /Physics_Notes_Unit_2\n➜ /Physics_Notes_Unit_3\n➜ /Physics_Notes_Unit_4\n➜ /Physics_Notes_Unit_5\n➜ /Physics_Notes_Unit_6\n")

def physics_notes_unit_1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/15')
def physics_notes_unit_2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 2 padhane to do. 😅")
def physics_notes_unit_3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 3 padhane to do. 😅")
def physics_notes_unit_4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 4 padhane to do. 😅")
def physics_notes_unit_5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 5 padhane to do. 😅")
def physics_notes_unit_6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 6 padhane to do. 😅")

def physics_pyq(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/35')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/36')

# Chemistry ------------------------------------------------------------------------------------------------------------

def chemistry_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Chemistry Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/23')

def chemistry_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Chemistry_Notes_Unit_1\n➜ /Chemistry_Notes_Unit_2\n➜ /Chemistry_Notes_Unit_3\n➜ /Chemistry_Notes_Unit_4\n➜ /Chemistry_Notes_Unit_5\n➜ /Chemistry_Notes_Unit_6\n")

def chemistry_notes_unit_1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/24')
def chemistry_notes_unit_2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 2 padhane to do. 😅")
def chemistry_notes_unit_3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 3 padhane to do. 😅")
def chemistry_notes_unit_4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 4 padhane to do. 😅")
def chemistry_notes_unit_5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 5 padhane to do. 😅")
def chemistry_notes_unit_6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 6 padhane to do. 😅")

def chemistry_pyq(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/42')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/43')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/44')

# BEE ------------------------------------------------------------------------------------------------------------

def bee_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending BEE Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/27')

def bee_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /BEE_Notes_Unit_1\n➜ /BEE_Notes_Unit_2\n➜ /BEE_Notes_Unit_3\n➜ /BEE_Notes_Unit_4\n➜ /BEE_Notes_Unit_5\n➜ /BEE_Notes_Unit_6\n")

def bee_notes_unit_1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/28')
def bee_notes_unit_2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 2 padhane to do. 😅")
def bee_notes_unit_3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 3 padhane to do. 😅")
def bee_notes_unit_4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 4 padhane to do. 😅")
def bee_notes_unit_5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 5 padhane to do. 😅")
def bee_notes_unit_6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 6 padhane to do. 😅")

def bee_pyq(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/48')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/49')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/50')

# BXE ------------------------------------------------------------------------------------------------------------

def bxe_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending BXE Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/25')

def bxe_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /BXE_Notes_Unit_1\n➜ /BXE_Notes_Unit_2\n➜ /BXE_Notes_Unit_3\n➜ /BXE_Notes_Unit_4\n➜ /BXE_Notes_Unit_5\n➜ /BXE_Notes_Unit_6\n")

def bxe_notes_unit_1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/26')
def bxe_notes_unit_2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 2 padhane to do. 😅")
def bxe_notes_unit_3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 3 padhane to do. 😅")
def bxe_notes_unit_4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 4 padhane to do. 😅")
def bxe_notes_unit_5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 5 padhane to do. 😅")
def bxe_notes_unit_6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 6 padhane to do. 😅")

def bxe_pyq(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/45')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/46')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/47')
    update.message.reply_document('')
# PPS ------------------------------------------------------------------------------------------------------------

def pps_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending PPS Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/7')

def pps_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /PPS_Notes_Unit_1\n➜ /PPS_Notes_Unit_2\n➜ /PPS_Notes_Unit_3\n➜ /PPS_Notes_Unit_4\n➜ /PPS_Notes_Unit_5\n➜ /PPS_Notes_Unit_6\n")

def pps_notes_unit_1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/13')
def pps_notes_unit_2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 2 padhane to do. 😅")
def pps_notes_unit_3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 3 padhane to do. 😅")
def pps_notes_unit_4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 4 padhane to do. 😅")
def pps_notes_unit_5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 5 padhane to do. 😅")
def pps_notes_unit_6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 6 padhane to do. 😅")

def pps_pyq(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/32')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/33')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/34')

# Mechanics ------------------------------------------------------------------------------------------------------------

def mechanics_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Mechanics Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/16')

def mechanics_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Mechanics_Notes_Unit_1\n➜ /Mechanics_Notes_Unit_2\n➜ /Mechanics_Notes_Unit_3\n➜ /Mechanics_Notes_Unit_4\n➜ /Mechanics_Notes_Unit_5\n➜ /Mechanics_Notes_Unit_6\n")

def mechanics_notes_unit_1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/15')
def mechanics_notes_unit_2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 2 padhane to do. 😅")
def mechanics_notes_unit_3(update: Update, context: CallbackContext):update.message.reply_document('')
def mechanics_notes_unit_4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 4 padhane to do. 😅")
def mechanics_notes_unit_5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 5 padhane to do. 😅")
def mechanics_notes_unit_6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 6 padhane to do. 😅")

def mechanics_pyq(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/37')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/38')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/39')

# Maths-I ------------------------------------------------------------------------------------------------------------

def mathsI_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("We are trying to arrange more SE materials. It will be uploaded on the bot as soon as we get it. Please don't spam in the bot. Share any SE material you have by clicking /I_have_a_Suggestion")

def mathsI_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /MathsI_Notes_Unit_1\n➜ /MathsI_Notes_Unit_2\n➜ /MathsI_Notes_Unit_3\n➜ /MathsI_Notes_Unit_4\n➜ /MathsI_Notes_Unit_5\n➜ /MathsI_Notes_Unit_6\n")

def mathsI_notes_unit_1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/22')
def mathsI_notes_unit_2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 2 padhane to do. 😅")
def mathsI_notes_unit_3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 3 padhane to do. 😅")
def mathsI_notes_unit_4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 4 padhane to do. 😅")
def mathsI_notes_unit_5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 5 padhane to do. 😅")
def mathsI_notes_unit_6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 6 padhane to do. 😅")

def mathsI_pyq(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/40')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/41')

# SME ------------------------------------------------------------------------------------------------------------

def sme_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending SME Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/4')

def sme_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /SME_Notes_Unit_1\n➜ /SME_Notes_Unit_2\n➜ /SME_Notes_Unit_3\n➜ /SME_Notes_Unit_4\n➜ /SME_Notes_Unit_5\n➜ /SME_Notes_Unit_6\n")

def sme_notes_unit_1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/6')
def sme_notes_unit_2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 2 padhane to do. 😅")
def sme_notes_unit_3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 3 padhane to do. 😅")
def sme_notes_unit_4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 4 padhane to do. 😅")
def sme_notes_unit_5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 5 padhane to do. 😅")
def sme_notes_unit_6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit 6 padhane to do. 😅")

def sme_pyq(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/30')
    update.message.reply_document('https://t.me/DPU_DIT_Bot/31')

# More ------------------------------------------------------------------------------------------------------------

def timetable(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Your Timetable is changing everyday.\nWait for fixing timetable. 😕")

def syllabus(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Syllabus... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/3')

def whatsapp_me(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text(
        "https://bit.ly/3RgXdkZ")

# Subjects ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('Physics', physics))
updater.dispatcher.add_handler(CommandHandler('Chemistry', chemistry))
updater.dispatcher.add_handler(CommandHandler('BEE', bee))
updater.dispatcher.add_handler(CommandHandler('BXE', bxe))
updater.dispatcher.add_handler(CommandHandler('PPS', pps))
updater.dispatcher.add_handler(CommandHandler('Mechanics', mechanics))
updater.dispatcher.add_handler(CommandHandler('MathsI', mathsI))
updater.dispatcher.add_handler(CommandHandler('SME', sme))
updater.dispatcher.add_handler(CommandHandler('More', more))

# Physics Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('Physics_Textbook', physics_textbook))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes', physics_notes))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes_Unit_1', physics_notes_unit_1))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes_Unit_2', physics_notes_unit_2))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes_Unit_3', physics_notes_unit_3))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes_Unit_4', physics_notes_unit_4))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes_Unit_5', physics_notes_unit_5))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes_Unit_6', physics_notes_unit_6))

# Chemistry Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('Chemistry_Textbook', chemistry_textbook))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes', chemistry_notes))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes_Unit_1', chemistry_notes_unit_1))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes_Unit_2', chemistry_notes_unit_2))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes_Unit_3', chemistry_notes_unit_3))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes_Unit_4', chemistry_notes_unit_4))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes_Unit_5', chemistry_notes_unit_5))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes_Unit_6', chemistry_notes_unit_6))

# BEE Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('BEE_Textbook', bee_textbook))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes', bee_notes))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes_Unit_1', bee_notes_unit_1))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes_Unit_2', bee_notes_unit_2))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes_Unit_3', bee_notes_unit_3))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes_Unit_4', bee_notes_unit_4))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes_Unit_5', bee_notes_unit_5))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes_Unit_6', bee_notes_unit_6))

# BXE Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('BXE_Textbook', bxe_textbook))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes', bxe_notes))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes_Unit_1', bxe_notes_unit_1))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes_Unit_2', bxe_notes_unit_2))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes_Unit_3', bxe_notes_unit_3))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes_Unit_4', bxe_notes_unit_4))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes_Unit_5', bxe_notes_unit_5))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes_Unit_6', bxe_notes_unit_6))

# PPS Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('PPS_Textbook', pps_textbook))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes', pps_notes))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes_Unit_1', pps_notes_unit_1))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes_Unit_2', pps_notes_unit_2))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes_Unit_3', pps_notes_unit_3))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes_Unit_4', pps_notes_unit_4))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes_Unit_5', pps_notes_unit_5))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes_Unit_6', pps_notes_unit_6))

# Mechanics Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('Mechanics_Textbook', mechanics_textbook))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes', mechanics_notes))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes_Unit_1', mechanics_notes_unit_1))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes_Unit_2', mechanics_notes_unit_2))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes_Unit_3', mechanics_notes_unit_3))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes_Unit_4', mechanics_notes_unit_4))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes_Unit_5', mechanics_notes_unit_5))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes_Unit_6', mechanics_notes_unit_6))

# Maths-I Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('MathsI_Textbook', mathsI_textbook))
updater.dispatcher.add_handler(CommandHandler('MathsI_Notes', mathsI_notes))
updater.dispatcher.add_handler(CommandHandler('MathsI_Notes_Unit_1', mathsI_notes_unit_1))
updater.dispatcher.add_handler(CommandHandler('MathsI_Notes_Unit_2', mathsI_notes_unit_2))
updater.dispatcher.add_handler(CommandHandler('MathsI_Notes_Unit_3', mathsI_notes_unit_3))
updater.dispatcher.add_handler(CommandHandler('MathsI_Notes_Unit_4', mathsI_notes_unit_4))
updater.dispatcher.add_handler(CommandHandler('MathsI_Notes_Unit_5', mathsI_notes_unit_5))
updater.dispatcher.add_handler(CommandHandler('MathsI_Notes_Unit_6', mathsI_notes_unit_6))

# SME Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('SME_Textbook', sme_textbook))
updater.dispatcher.add_handler(CommandHandler('SME_Notes', sme_notes))
updater.dispatcher.add_handler(CommandHandler('SME_Notes_Unit_1', sme_notes_unit_1))
updater.dispatcher.add_handler(CommandHandler('SME_Notes_Unit_2', sme_notes_unit_2))
updater.dispatcher.add_handler(CommandHandler('SME_Notes_Unit_3', sme_notes_unit_3))
updater.dispatcher.add_handler(CommandHandler('SME_Notes_Unit_4', sme_notes_unit_4))
updater.dispatcher.add_handler(CommandHandler('SME_Notes_Unit_5', sme_notes_unit_5))
updater.dispatcher.add_handler(CommandHandler('SME_Notes_Unit_6', sme_notes_unit_6))

# PYQ ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('Physics_PYQ', physics_pyq))
updater.dispatcher.add_handler(CommandHandler('Chemistry_PYQ', chemistry_pyq))
updater.dispatcher.add_handler(CommandHandler('BEE_PYQ', bee_pyq))
updater.dispatcher.add_handler(CommandHandler('BXE_PYQ', bxe_pyq))
updater.dispatcher.add_handler(CommandHandler('PPS_PYQ', pps_pyq))
updater.dispatcher.add_handler(CommandHandler('Mechanics_PYQ', mechanics_pyq))
updater.dispatcher.add_handler(CommandHandler('MathsI_PYQ', mathsI_pyq))
updater.dispatcher.add_handler(CommandHandler('SME_PYQ', sme_pyq))

# More Content ------------------------------------------------------------------------------------------------------------

updater.dispatcher.add_handler(CommandHandler('Timetable', timetable))
updater.dispatcher.add_handler(CommandHandler('Syllabus', syllabus))
updater.dispatcher.add_handler(CommandHandler('I_have_a_Suggestion', whatsapp_me))

# ------------------------------------------------------------------------------------------------------------

def unknown_text(update: Update, context: CallbackContext):
    time.sleep(0.5)
    update.message.reply_text(
        "I am still learning,\ngive me a valid input Dear... 😊")

# #####

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Select_a_Subject', selecting_subject))

# Filters out unknown commands & messages.

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# updater.start_polling

updater.start_polling()

# A Special Thanks to Maansi & Sanket.
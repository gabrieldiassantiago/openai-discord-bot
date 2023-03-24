import discord
import openai


DISCORD_TOKEN = "EPjJP47p8RR-e6XdQAtXrIx2RmX9opGZ"
OPENAI_API_KEY = "SUA_CHAVE_API_DO_OPENAI_AQUI"
openai.api_key = OPENAI_API_KEY



client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message.content,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=10,
        frequency_penalty=0,
        presence_penalty=0
    )

    await message.channel.send(response.choices[0].text)
client.run(DISCORD_TOKEN)

import discord
import openai

DISCORD_TOKEN = "8e78f7c6f2b86fa712cd675e8512fe8c07305d4de7b802d91e7c0b133899bbac"
OPENAI_API_KEY = "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"

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "ping":
        await message.channel.send("pong")
    else:
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

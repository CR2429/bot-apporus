import random

async def run(ctx):
    #premier message
    await ctx.respond(f"Utilisation de 1 000 000 piece dans la roue de l'infortune pour <@{ctx.author.id}>")

    #random
    result = [random.randint(1,100) for _ in range(100)]
    r = [result[i:i+10] for i in range(0,len(result),10)]

    for rr in r[0:]:
        await ctx.send(rr)
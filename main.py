import discord
from discord.ext import commands

import os
print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')


@bot.command()
async def hello(ctx):
    if os.path.isfile("images/image1.jpg"):
        with open((f'images/image1.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"Hola, soy Ethan,   ¿como va todo humano?")
@bot.command()
async def bien(ctx):
    await ctx.send(f"me alegra humano, desde hoy tenemos una tarea muy grande por salvar nuestro planeta")
    await ctx.send(f"¡NOTA:Por el resto de dias escribir dia1, dia2...!")

@bot.command()
async def dia1(ctx):
    if os.path.isfile("images/image2.jpg"):
        with open((f'images/image2.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"REDUCCIÓN DE RESIDUOS")
            await ctx.send(f"- Reduce el uso de plasticos de un solo uso.") 
            await ctx.send(f"- Utiliza bolsas reutilizables para las compras.")
            await ctx.send(f"- Recicla papel y carton.")       

@bot.command()
async def dia2(ctx):
    if os.path.isfile("images/image3.jpg"):
        with open((f'images/image3.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"AHORRO DE ENERGIA")
            await ctx.send(f"- Apaga las luces y electrodomesticos cuando no esten en uso.") 
            await ctx.send(f"- Utiliza bombillas LED, que consuman menos energia.")
            await ctx.send(f"- Ajusta el termostato para ahorrar energia encalefaccion y refrigeración.")   

@bot.command()
async def dia3(ctx):
    if os.path.isfile("images/image4.jpg"):
        with open((f'images/image4.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"CONSERVACION DE AGUA")
            await ctx.send(f"- Cierra el grifo mientras te lavas los dientes o te duchas.") 
            await ctx.send(f"- repara las fugas de agua para evitar desperdicio.")
            await ctx.send(f"- Utiliza dispositivos de ahorro de agua en los grifos y duchas.") 
@bot.command()
async def dia4(ctx):
    if os.path.isfile("images/image5.jpg"):
        with open((f'images/image5.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"TRNSPORTE SOSTENIBLE")
            await ctx.send(f"- Utiliza transporte publico,bicicleta o camina para reducir emiciones de gases efecto invernadero.") 
            await ctx.send(f"- Considera la compra de vehiculos electricos o hibrido.")
            await ctx.send(f"- Planifica tus viajes para reducir el numero de desplazamientos.")                          

@bot.command()
async def dia5(ctx):
    if os.path.isfile("images/image6.jpg"):
        with open((f'images/image6.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"JARDINERIA SOSTENIBLE")
            await ctx.send(f"- Crea un jardín con plantas nativas y adaptadas al clima local.") 
            await ctx.send(f"- Utiliza técnicas de jardinería sostenible, como la permacultura.")
            await ctx.send(f"- Recicla el agua de lluvia para regar tus plantas.")

@bot.command()
async def dia6(ctx):
    if os.path.isfile("images/image7.jpg"):
        with open((f'images/image7.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"EDUCACIÓN Y CONCIENCIA")
            await ctx.send(f"- Aprende sobre los problemas ambientales y sus soluciones.") 
            await ctx.send(f"- Comparte tus conocimientos con amigos y familiares.")
            await ctx.send(f"- Participa en actividades de voluntariado para proteger el medio ambiente.")

@bot.command()
async def dia7(ctx):
    if os.path.isfile("images/image8.jpg"):
        with open((f'images/image8.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"COMPRA SOSTENIBLE")
            await ctx.send(f"- Elige productos con embalajes minimalistas o reutilizables.") 
            await ctx.send(f"- Prefiere productos locales y de temporada para reducir la huella de carbon.")
            await ctx.send(f"- Evita la compra de productos con ingredientes nocivos para el medio ambiente.")            
                     
@bot.command()
async def dia8(ctx):
    if os.path.isfile("images/image9.jpg"):
        with open((f'images/image9.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"REDUCCON DE PAPEL")
            await ctx.send(f"- Utiliza notas digitales en lugar de papel.") 
            await ctx.send(f"- Cancela suscripciones a revistas y periódicos en papel.")
            await ctx.send(f"- Utiliza documentos digitales en lugar de imprimirlos.")

@bot.command()
async def dia9(ctx):
    if os.path.isfile("images/image10.jpg"):
        with open((f'images/image10.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"CONSERVACIÓN DE LA BIODIVERSIDAD")
            await ctx.send(f"- Apoya organizaciones que protegen la biodiversidad.") 
            await ctx.send(f"- Crea un hábitat para la vida silvestre en tu jardín.")
            await ctx.send(f"- Evita productos que dañen la biodiversidad.")   

@bot.command()
async def dia10(ctx):
    if os.path.isfile("images/image11.jpg"):
        with open((f'images/image11.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"AHORRO DE ALIMENTOS")
            await ctx.send(f"- Planifica tus comidas para evitar desperdicio de alimentos.") 
            await ctx.send(f"- Utiliza recipientes reutilizables para llevar comida.")
            await ctx.send(f"- Compra alimentos en cantidad adecuada para evitar desperdicio.")                        
#¡NOTA: Para terminar racha de dias digamos "termine"!

@bot.command()
async def finis(ctx):
    if os.path.isfile("images/image1.jpg"):
        with open((f'images/image1.jpg'), 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"Y para terminar, de parte de Ethan,solo queda felicitarte por hacer un cambio en nuestro planeta, ahora viviremos muchos mas años.")


@bot.command()
async def emoji(ctx):
    await ctx.send("¡felicitaciones,vuelvalo a intentar con tus amigos!\U0001F44D\U0001F30E")

bot.run("MTMzNDI4MTQ5MDM2Mzg0MjY3MA.Gxg_yh.3QZMFf9yna7ZhLf7F4NXMFsIxAQP8RO7Oxq3eA")

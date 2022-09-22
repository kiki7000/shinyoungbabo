from AssacCore import AssacCore
from bson.objectid import ObjectId
from AssacCore.models.dataclass.config import Config
from AssacCore.models.database.user import DUser

from json import load

import discord
from discord.ext.commands import Bot

import ast


def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


with open("config.json", "r", encoding="utf-8") as f:
    config = Config(**load(f))
core = AssacCore(config)
bot = Bot(command_prefix="[")


@bot.event
async def on_ready():
    print("Bot start")
    bot.core = core


@bot.command("eval")
async def _eval(ctx, *, cmd):
    if ctx.author.id != 758244072573370380:
        return

    try:
        fn_name = "_eval_expr"
        cmd = cmd.strip("` ").lstrip("py").strip("\n")
        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
        body = f"async def {fn_name}():\n{cmd}"
        parsed = ast.parse(body)
        body = parsed.body[0].body
        insert_returns(body)
        env = {
            "bot": bot,
            "discord": discord,
            "ctx": ctx,
            "__import__": __import__,
            "DUser": DUser,
            "core": core,
            "ObjectId": ObjectId,
        }
        exec(compile(parsed, filename="<ast>", mode="exec"), env)

        result = await eval(f"{fn_name}()", env)
        await ctx.send(result)
    except Exception as a:
        await ctx.send(a)


bot.load_extension("jishaku")
bot.run("ODUwMjc4MjUzNjAwMDQ3MTA1.YLnZVQ.XV3mRJIWAyZ5Ix71HQYz5t8mMAA")

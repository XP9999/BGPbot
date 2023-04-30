from discord.ext import commands
from disputils import BotEmbedPaginator
import discord
import pymongo
from datetime import datetime
print("running")

token = 'MTA5ODk2MTQ1NjQwMzMyOTEwNA.GBOyuf.yW09x1aPdhsgm-mvYPuNEIX_recCUGji0Ew4HU'
bot = commands.Bot(command_prefix = "!" , intents = discord.Intents.all(),help_command=None , case_insensitive = True)
client = pymongo.MongoClient("mongodb+srv://Hosei:WXadNYFszGXCCAwk@bgp.hdqdghf.mongodb.net/?retryWrites=true&w=majority")
exercises = ['air squat', 'back extension', 'band external shoulder rotation', 'band internal shoulder rotation', 'band pull-apart', 'banded side kicks', 'bar dip', 'bar dips', 'bar hang', 'barbell curl', 'barbell front raise', 'barbell hack squat', 'barbell lunge', 'barbell lying triceps extension', 'barbell preacher curl', 'barbell rear delt row', 'barbell row', 'barbell shrug', 'barbell standing triceps extension', 'barbell upright row', 'barbell walking lunge', 'barbell wrist curl', 'barbell wrist curl behind the back', 'barbell wrist extension', 'behind the neck press', 'belt squat', 'bench dip', 'bench press', 'block snatch', 'body weight lunge', 'bodyweight curl', 'box squat', 'bulgarian split squat', 'cable chest press', 'cable close grip seated row', 'cable crunch', 'cable curl with bar', 'cable curl with rope', 'cable lateral raise', 'cable pull through', 'cable rear delt row', 'cable wide grip seated row', 'chair squat', 'chin-up', 'clamshells', 'clean', 'clean and jerk', 'close-grip bench press', 'close-grip feet-up bench press', 'close-grip push-up', 'concentration curl', 'crunch', 'dead bug', 'deadlift', 'decline bench press', 'deficit deadlift', 'dumbbell chest fly', 'dumbbell chest press', 'dumbbell curl', 'dumbbell deadlift', 'dumbbell decline chest press', 'dumbbell floor press', 'dumbbell frog pumps', 'dumbbell front raise', 'dumbbell horizontal external shoulder rotation', 'dumbbell horizontal internal shoulder rotation', 'dumbbell lateral raise', 'dumbbell lunge', 'dumbbell lying triceps extension', 'dumbbell preacher curl', 'dumbbell pullover', 'dumbbell rear delt row', 'dumbbell romanian deadlift', 'dumbbell row', 'dumbbell shoulder press', 'dumbbell shrug', 'dumbbell squat', 'dumbbell standing triceps extension', 'dumbbell wrist curl', 'dumbbell wrist extension', 'eccentric heel drop', 'face pull', 'farmers walk', 'fat bar deadlift', 'feet-up bench press', 'fire hydrants', 'floor back extension', 'floor press', 'frog pumps', 'front hold', 'front squat', 'glute bridge', 'goblet squat', 'good morning', 'gripper', 'hack squat machine', 'hack squats', 'half air squat', 'hammer curl', 'hang clean', 'hang power clean', 'hang power snatch', 'hang snatch', 'hanging knee raise', 'hanging leg raise', 'hanging sit-up', 'heel raise', 'high to low wood chop', 'high to low wood chop with band', 'hip abduction against band', 'hip abduction machine', 'hip adduction machine', 'hip thrust', 'hip thrust machine', 'hip thrust with band around knees', 'horizontal wood chop with band', 'incline bench press', 'incline dumbbell curl', 'incline dumbbell press', 'incline push-up', 'inverted row', 'inverted row with underhand grip', 'kettlebell swing', 'kneeling ab wheel roll-out', 'kneeling incline push-up', 'kneeling plank', 'kneeling push-up', 'kneeling side plank', 'landmine hack squat', 'landmine squat', 'lat pulldown', 'lat pulldown with pronated grip', 'lat pulldown with supinated grip', 'lateral walk with band', 'leg extension', 'leg press', 'lying dumbbell external shoulder rotation', 'lying dumbbell internal shoulder rotation', 'lying leg curl', 'lying leg raise', 'lying windshield wiper', 'lying windshield wiper with bent knees', 'machine bicep curl', 'machine chest fly', 'machine chest press', 'machine crunch', 'machine glute kickbacks', 'machine lateral raise', 'machine shoulder press', 'monkey row', 'mountain climbers', 'oblique crunch', 'oblique sit-up', 'one-handed bar hang', 'one-handed cable row', 'one-handed lat pulldown', 'one-legged glute bridge', 'one-legged hip thrust ', 'overhead cable triceps extension', 'overhead press', 'pause deadlift', 'pause squat', 'pec deck', 'pendlay row', 'plank', 'plate front raise', 'plate pinch', 'plate wrist curl', 'power clean', 'power jerk', 'power snatch', 'pull-up', 'push press', 'push-up', 'push-up against wall', 'push-ups with feet in rings', 'rack pull', 'resistance band chest fly', 'reverse dumbbell fly', 'reverse dumbbell flyes', 'reverse machine fly', 'romanian deadlift', 'safety bar squat', 'seal row', 'seated barbell overhead press', 'seated calf raise', 'seated dumbbell shoulder press', 'seated leg curl', 'seated machine row', 'seated smith machine shoulder press', 'shallow body weight lunge', 'side lunges (bodyweight)', 'side plank', 'single leg romanian deadlift', 'sit-up', 'smith machine bench press', 'smith machine incline bench press', 'smith machine squat', 'snatch', 'snatch grip behind the neck press', 'snatch grip deadlift', 'spider curl', 'split jerk', 'squat', 'squat jerk', 'standing cable chest fly', 'standing calf raise', 'standing glute kickback in machine', 'standing resistance band chest fly', 'step up', 'stiff-legged deadlift', 'straight arm lat pulldown', 'sumo deadlift', 't-bar row', 'towel pull-up', 'trap bar deadlift with high handles', 'trap bar deadlift with low handles', 'tricep bodyweight extension', 'tricep pushdown', 'tricep pushdown with bar', 'tricep pushdown with rope']
users = client["Bot"]["Users"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("could not connect to mongodb")
    print(e)

@bot.event
async def on_ready():
    print("Bot is now online")

async def pfp(id,name):
    pfp = discord.Embed()
    data = users.find_one({"_id":id})
    if data is None:
        data = {}
    startw = data['weight'][list(data['weight'])[0]] if data.get('weight') is not None else 0
    endw = data['weight'][list(data['weight'])[-1]] if data.get('weight') is not None else 0
    height = data['height'] if data.get('height') is not None else 0
    bmi = (endw//2.205) // ((height/100)**2) if height else 0
    gained = endw-startw if startw else 0
    display = "!selectdisplay"
    if data.get("display"):
        display = []
        for x in data['display']:
            display.append(f'{x} : {data["PR"][x]}')
        display = "\n".join(display)
    pfp.set_author(name= name)
    pfp.add_field(name="Weight", value= f"{endw}lbs", inline=True)
    pfp.add_field(name="Height", value= f"{height}cm", inline=True)
    pfp.add_field(name="BMI", value=bmi, inline=True)
    pfp.add_field(name="Weight gained" , value= f"{gained}lbs" , inline=False)
    pfp.add_field(name="Displayed PR" , value= display ,inline=False)
    return pfp

@bot.command()
async def profile(ctx, id = None):
    if id is not None:
        try:
            id = int(id)
        except:
            id = id[2:-1]
        try:
            id = await bot.fetch_user(id)
        except:
            await ctx.send("Invalid ID")
            return
    target = [id.id,id] if id is not None else [ctx.author.id,ctx.author]
    embed= await pfp(target[0],target[1])
    await ctx.send(embed=embed)

@bot.command()
async def setweight(ctx, x):
    if x.isdigit():
        today = datetime.today().date()
        users.update_one({"_id":ctx.author.id}, {"$set":{f"weight.{today}": int(x)}} , upsert = True)
        await ctx.send(f"Updated Weight for **{today}** : **{x}lbs**")
    else:
        await ctx.send("Invalid Weight")

@bot.command()
async def setheight(ctx, x):
    if x.isdigit():
        users.update_one({"_id":ctx.author.id}, {"$set":{f"height": int(x)}} , upsert = True)
        await ctx.send(f"Updated Height : **{x}cm**")
    else: await ctx.send("Pls use cm so at least the number of your size wouldnt be small")

@bot.command()
async def setPR(ctx, pr, *name):
    if len(pr.split("x")) < 2:
        await ctx.send(f"Invalid pr , pls use the format **weight**x**rep**")
        return
    ex = " ".join(name).lower()
    if ex in exercises:
        users.update_one({"_id":ctx.author.id}, {"$set":{f"PR.{ex}": pr}} , upsert = True)
        await ctx.send(f"Congrats on lifting **{pr}** on **{ex}**")
    else:
        await ctx.send(f"**{ex}** not found in database , try using **!search** to find the exercise")

async def getembed(l):
    es = []
    per = []
    for x in l:
        if len(per) == 15:
            e = discord.Embed()
            e.add_field(name = "Search Results" , value= "\n".join(per))
            es.append(e)
            per = []
        per.append(x)
    e = discord.Embed()
    e.add_field(name = "Search Results" , value= "\n".join(per))
    es.append(e)
    return es

@bot.command()
async def search(ctx,s):
    s = s.lower()
    filtered = [x for x in exercises if s in x]
    embeds = await getembed(filtered)
    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()

@bot.command()
async def select(ctx , *name):
    name = " ".join(name).lower()
    dpr = []
    data = users.find_one({"_id":ctx.author.id}, {"PR": True , "display": True})
    if "display" in data:
        dpr += data["display"]
    if name in dpr:
        await ctx.send(f"{name} is already in display")
        return
    if len(dpr) >= 3:
        await ctx.send("You have reached your limit of display , please use **!removedisplay** to remove one")
    else:
        if name in data["PR"]:
            dpr.append(name)
            d = ", ".join(dpr[:-1]) + " and " + dpr[-1] if len(dpr) > 1 else dpr[0]
            await ctx.send(f"Displaying {d} in profile")
        else:
            await ctx.send(f"U haven't put your PR for {name}")

    users.update_one({"_id":ctx.author.id}, {"$set":{f"display": dpr}} , upsert = True)

@bot.command()
async def remove(ctx, *name):
    name = " ".join(name).lower()
    dpr = []
    data = users.find_one({"_id":ctx.author.id}, {"PR": True , "display": True})
    if "display" in data:
        dpr += data["display"]
    if name in dpr:
        dpr.remove(name)
        users.update_one({"_id":ctx.author.id}, {"$set":{"display": dpr}} , upsert = True)
        await ctx.send(f"Removed {name} from display")
    else:
        await ctx.send(f"{name} is not in display")

@bot.command()
async def lb(ctx, *name):
    if ctx.guild:
        name= " ".join(name).lower()
        if name not in exercises:
            await ctx.send("Exercise not in database")
            return
        embed = discord.Embed(title= f"Leaderboard for {name}")
        names = []
        prs = []
        rm = []
        data = list(users.find({ f"PR.{name}": {"$exists": True } }, {"_id": True, "PR": True}))
        if not data:
            await ctx.send(f"No PR for {name}")
            return
        for x in data:
            try:
                names.append(bot.get_user(x["_id"]).name)
                pr = x["PR"][name]
                weightrep = pr.split("x")
                prs.append(pr)
                rm.append(str(round(int(weightrep[0]) / (1.0278 - (0.0278 * int(weightrep[1]))),2)))
            except:
                pass

        zipped = list(zip(rm,names, prs))
        sorted_zipped = sorted(zipped, key=lambda x: x[1])
        rm, names,prs = zip(*sorted_zipped)
        embed.add_field(name= "Users" , value= "\n".join(names) , inline=True)
        embed.add_field(name= "PR" , value = "\n".join(prs), inline= True)
        embed.add_field(name= "1RM", value= "\n".join(rm), inline= True)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Server only command")
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot commands")
    embed.add_field(name= "!profile", value="Shows a profile \n example: !profile (id/mention)" , inline=False)
    embed.add_field(name= "!setweight", value="Set your weight for today , uses lb \n example: !setweight 130" , inline=False)
    embed.add_field(name= "!setheight", value="Change your height, uses cm \n example: !setheight 170", inline=False)
    embed.add_field(name= "!setPR", value="Set your PR \n exmaple: !setPR barbell curl 20x10",inline=False)
    embed.add_field(name= "!search", value="Search for exercises in the database \n example: !search barbell",inline=False)
    embed.add_field(name= "!select", value="Select a PR to display , max = 3 \n example: !select barbell curl",inline=False)
    embed.add_field(name= "!remove", value="Remove PR from display \n example: !remove barbell curl",inline=False)
    await ctx.send(embed=embed)

bot.run(token)

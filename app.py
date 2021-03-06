# Welcome to spaghetti code plaza
from urllib import request
import json
import os
from config import *
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed


def main():

    if webhook_id == 'YOUR WEBHOOK ID':
        print('Change the config ya dingus')
        exit(0)

    Input = input('User: ')
    Request = request.urlopen(f'https://www.duolingo.com/2017-06-30/users?username={Input}')
    Json = json.loads(Request.read().decode('utf-8'))

    # Version Number, Do not change
    ver = '1.7.2'

    if len(Json['users']) == 0:
        return print('User Not Found')

    realname = 'Unknown'
    if 'name' in Json['users'][0]:
        realname = Json['users'][0]['name']

    username = Json['users'][0]['username']
    picture = Json['users'][0]['picture']
    motivation = Json['users'][0]['motivation']
    streak = Json['users'][0]['_achievements'][0]['count']
    totalxp = Json['users'][0]['totalXp']
    langfromjson = Json['users'][0]['learningLanguage']
    date = Json['users'][0]['creationDate']
    userid = Json['users'][0]['id']

    date_created = datetime.fromtimestamp(date)

    if Json['users'][0]['hasPlus']:  # == True ??
        duoplus = 'Yes'
    else:
        duoplus = 'No'

    if Json['users'][0]['hasRecentActivity15']:
        wasactive = 'Yes'
    else:
        wasactive = 'No'

    if Json['users'][0]['hasGoogleId']:
        googleac = 'Yes'
    else:
        googleac = 'No'

    if Json['users'][0]['hasFacebookId']:
        facebookac = 'Yes'
    else:
        facebookac = 'No'

    if Json['users'][0]['emailVerified']:
        veryemail = 'Yes'
    else:
        veryemail = 'No'

    languages = {
        'de': 'German',
        'nl-NL': 'Dutch',
        'la': 'Latin',
        'ga': 'Irish',
        'ja': 'Japanese',
        'ru': 'Russian',
        'pt': 'Portuguese',
        'fr': 'French',
        'it': 'Italian',
        'en': 'English',
        'es': 'Spanish',
        'cy': 'Welsh',
        'el': 'Greek',
        'sw': 'Swahili',
        'vi': 'Vietnamese',
        'zh': 'Chinese',
        'sv': 'Swedish',
        'ko': 'Korean'
    }
    outputlang = languages.get(langfromjson, "Unknown")
    print(outputlang)

    os.system('cls')
    print('====DEBUG OUTPUT====')
    print('User ID:', userid)
    print('Username: ' + username)
    print('Real Name: ' + realname)
    print("------------------")
    print('Duolingo Plus:', duoplus)
    print('Recently active:', wasactive)
    print('Linked Google:', googleac)
    print('Linked Facebook:', facebookac)
    print('Verified Email:', veryemail)
    print('Account created:', date_created)
    print("------------------")
    print('Motivation:', motivation)
    print('Streak:', streak, 'days')
    print('Total XP:', totalxp)
    print('Lang Code:', langfromjson)
    print('Current Language:', outputlang)
    print('------------------')

    webhook = DiscordWebhook(url=f'https://discordapp.com/api/webhooks/{webhook_id}/{webhook_secret}', username=webhooker_name, avatar_url=webhooker_avatar_url)

    embed = DiscordEmbed(title='Duolingo Profile', description=f'**User:** {username}\n**Name:** {realname}\n \n**Duolingo Plus**: {duoplus}\n**Recently active:** {wasactive}\n**Linked Google:** {googleac}\n**Linked Facebook:** {facebookac}\n**Verified Email:** {veryemail}\n**Motivation:** {motivation}\n \n**Last Learned:** {outputlang}\n\n**Account created:** {date_created}', url=f'https://www.duolingo.com/profile/{username}', color=4714574)
    embed.set_author(name=f'{username}',
                     icon_url=f'https:{picture}/xlarge')
    embed.set_footer(text=f'Duo-Kartoffel v{ver}')
    embed.set_timestamp()
    embed.add_embed_field(name='Total XP', value=f'{totalxp}')
    embed.add_embed_field(name='Streak', value=f'{streak} Days', inline='true')

    webhook.add_embed(embed)
    response = webhook.execute()
    print('Hook1', response)
    secondswebhook(username, picture)


def secondswebhook(username, picture):

        Embed = DiscordEmbed(title='Language Stats', color=4714574)
        Webhook = DiscordWebhook(url=f'https://discordapp.com/api/webhooks/{webhook_id}/{webhook_secret}', username=webhooker_name, avatar_url=webhooker_avatar_url)

        Request = request.urlopen(f'https://www.duolingo.com/2017-06-30/users?username={username}')
        Json = json.loads(Request.read().decode('utf-8'))

        Embed.set_author(name=f'{username}', icon_url=f'https:{picture}/xlarge')

        for langs in Json['users'][0]['courses']:
            if langs['title']:
                Embed.add_embed_field(name=langs['title'], value=f"XP: {langs['xp']}\nCrowns: {langs['crowns']}")

        Webhook.add_embed(Embed)
        response = Webhook.execute()
        print('Hook2', response)
        print('Done')


if __name__ == "__main__":
    main()

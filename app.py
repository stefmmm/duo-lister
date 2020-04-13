# Welcome to spaghetti code plaza
from urllib import request
import json
import os
from config import *
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed


def main():

    Input = input('User: ')
    Request = request.urlopen(f'https://www.duolingo.com/2017-06-30/users?username={Input}')
    Json = json.loads(Request.read().decode('utf-8'))

    # Version Number, Do not change
    ver = 1.6
    # Release candidate, Do not change
    rl = 1

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
    lastlang = Json['users'][0]['learningLanguage']
    date = Json['users'][0]['creationDate']

    date_created = datetime.fromtimestamp(date)

    if Json['users'][0]['hasPlus'] == True:
        duoplus = 'Yes'
    else:
        duoplus = 'No'

    if Json['users'][0]['hasRecentActivity15'] == True:
        wasactive = 'Yes'
    else:
        wasactive = 'No'

    if Json['users'][0]['hasGoogleId'] == True:
        googleac = 'Yes'
    else:
        googleac = 'No'

    if Json['users'][0]['hasFacebookId'] == True:
        facebookac = 'Yes'
    else:
        facebookac = 'No'

    if Json['users'][0]['emailVerified'] == True:
        veryemail = 'Yes'
    else:
        veryemail = 'No'

    if lastlang == 'de':
        thelang = 'German'
    if lastlang == 'nl-NL':
        thelang = 'Dutch'
    if lastlang == 'la':
        thelang = 'Latin'
    if lastlang == 'ga':
        thelang = 'Irish'
    if lastlang == 'ja':
        thelang = 'Japanese'
    if lastlang == 'ru':
        thelang = 'Russian'
    if lastlang == 'pt':
        thelang = 'Portuguese'
    if lastlang == 'fr':
        thelang = 'French'
    if lastlang == 'it':
        thelang = 'Italian'
    if lastlang == 'en':
        thelang = 'English'
    if lastlang == 'es':
        thelang = 'Spanish'
    if lastlang == 'cy':
        thelang = 'Welsh'
    if lastlang == 'el':
        thelang = 'Greek'
    if lastlang == 'sw':
        thelang = 'Swahili'
    if lastlang == 'vi':
        thelang = 'Vietnamese'


    os.system('cls')
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
    print('Streak:', streak,'days')
    print('Total XP:', totalxp)
    print('Current Language:', lastlang)
    print('------------------')

    webhook = DiscordWebhook(url=f'https://discordapp.com/api/webhooks/{webhook_id}/{webhook_secret}', username=webhooker_name, avatar_url=webhooker_avatar_url)

    embed = DiscordEmbed(title='Duolingo Profile', description=f'**User:** {username}\n**Name:** {realname}\n \n**Duolingo Plus**: {duoplus}\n**Recently active:** {wasactive}\n**Linked Google:** {googleac}\n**Linked Facebook:** {facebookac}\n**Verified Email:** {veryemail}\n**Motivation:** {motivation}\n \n**Current Language:** {thelang}\n\n**Account created:** {date_created}', url=f'https://www.duolingo.com/profile/{username}', color=4714574)
    embed.set_author(name=f'{username}',
                     icon_url=f'https:{picture}/xlarge')
    embed.set_footer(text=f'Duo-Kartoffel v{ver} RC: {rl}')
    embed.set_timestamp()
    embed.add_embed_field(name='Total XP', value=f'{totalxp}')
    embed.add_embed_field(name='Streak', value=f'{streak} Days', inline='true')

    webhook.add_embed(embed)
    response = webhook.execute()
    print('Hook1', response)
    secondswebhook(Input, picture)


def secondswebhook(username, picture):

        Embed = DiscordEmbed(title='Language Stats', color=4714574)
        Webhook = DiscordWebhook(url=f'https://discordapp.com/api/webhooks/{webhook_id}/{webhook_secret}', username=webhooker_name, avatar_url=webhooker_avatar_url)

        Request = request.urlopen(f'https://www.duolingo.com/2017-06-30/users?username={username}')
        Json = json.loads(Request.read().decode('utf-8'))

        Embed.set_author(name=f'{username}',
                         icon_url=f'https:{picture}/xlarge')


        for langs in Json['users'][0]['courses']:
            if langs['title']:
                Embed.add_embed_field(name=langs['title'],
                                      value=f"XP: {langs['xp']}\nCrowns: {langs['crowns']}")

        Webhook.add_embed(Embed)
        response = Webhook.execute()
        print('Hook2', response)


if __name__ == "__main__":
    main()

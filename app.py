# Welcome to spaghetti code plaza
from urllib import request
import json
import os
from discord_webhook import DiscordWebhook, DiscordEmbed


def main():
    Input = input('User: ')
    Request = request.urlopen(f'https://www.duolingo.com/2017-06-30/users?username={Input}')
    Json = json.loads(Request.read().decode('utf-8'))

    username = Json['users'][0]['username']
    realname = Json['users'][0]['name']
    picture = Json['users'][0]['picture']

    motivation = Json['users'][0]['motivation']
    streak = Json['users'][0]['_achievements'][0]['count']
    totalxp = Json['users'][0]['totalXp']
    lastlang = Json['users'][0]['learningLanguage']

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


    os.system('cls')
    print('Username: ' + username)
    print('Real Name: ' + realname)
    print("------------------")
    print('Duolingo Plus:', duoplus)
    print('Recently active:', wasactive)
    print('Linked Google:', googleac)
    print('Linked Facebook:', facebookac)
    print('Verified Email:', veryemail)
    print("------------------")
    print('Motivation:', motivation)
    print('Streak:', streak,'days')
    print('Total XP:', totalxp)
    print('Current Language:', lastlang)
    print('--- Languages ---')

    webhook = DiscordWebhook(url='YOUR WEBHOOK URL', username="Duolingo", avatar_url="https://www.underconsideration.com/brandnew/archives/duolingo_2018_logo_social.png")

    embed = DiscordEmbed(title='Duolingo Profile', description=f'**User:** {username}\n**Name:** {realname}\n \n**Has Plus**: {duoplus}\n**Recently active:** {wasactive}\n**Linked Google:** {googleac}\n**Linked Facebook:** {facebookac}\n**Verified Email:** {veryemail}\n**Motivation:** {motivation}\n \n**Current Language:** {thelang}', url=f'https://www.duolingo.com/profile/{username}', color=4714574)
    embed.set_author(name=f'{username}',
                     icon_url=f'https:{picture}/xlarge')
    embed.set_footer(text='Powered by: Liquid Kartofler')
    embed.set_timestamp()
    embed.add_embed_field(name='Total XP', value=f'{totalxp}')
    embed.add_embed_field(name='Streak', value=f'{streak} Days', inline='true')

    webhook.add_embed(embed)
    response = webhook.execute()
    print(response)

if __name__ == "__main__":
    main()

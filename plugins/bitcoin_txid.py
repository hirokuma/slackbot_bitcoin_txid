from slackbot.bot import respond_to
import csv
import urllib
import json


TESTNET = 1


@respond_to('txid (.*)')
def analyze_txid(message, params):
    args = [row for row in csv.reader([params], delimiter=' ')][0]
    txdata = get_txinfo(args[0])
    if len(txdata) > 0:
        # msg = 'confirmations:' + str(txdata['confirmations'])
        msg = 'analyze transaction [' + args[0] + ']...\n```' + json.dumps(txdata, indent=2) + '```'
    else:
        msg = 'unknown txid'
    message.reply(msg)


def get_txinfo(txid):
    if TESTNET != 0:
        url = 'https://testnet.blockexplorer.com/api/tx/' + txid
    else:
        url = 'https://blockexplorer.com/api/tx/' + txid
    json_data = ()
    try:
        htmlget = urllib.urlopen(url).read()
        json_data = json.loads(htmlget)
    except ValueError:
        pass
    return json_data

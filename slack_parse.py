import re
def parse(txt):
    """Replaces message with slack-friendly link to ticket ID.

    Takes a string from an email subject and formats it into a link
    that slack can interpret.

    Args:
        txt: the text of the subject.

    Returns as tuple:
        buildStr: a formatted string that acts as a link to slack.
        res_type: the response method that slack should use, options:
            ephemeral: only one person can see it
            in_channel: available for all to see
    """
    if txt == "help":
        return("This will return a completed link to that ticket in KBOX. Neat, huh?","ephemeral")
    else:
        txt = txt.split()
        buildStr = ""
        for word in txt:
            if re.search(".*\d{5,7}",word):
                if not word[-1].isdigit():
                    word = word[0:-1]
                buildStr += "<https://help.luther.edu/adminui/ticket.php?ID=" + word + "|" + word + '>'
                res_type = "in_channel"
    return (buildStr, res_type)

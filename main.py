import json

def restaurant_test(venue, users):
    """ Creates a list of reasons (if any) that a restaurant is not suitable

    Args:
        venue (dict): Contains lists of food and drinks restaurant offers
        users (list): Contains list of dicts, each dict has list of food user won't eat and list of drink preferences

    Returns:
        list: Reasons (if any) that a restaurant is not suitable
    """
    return ["There is nothing for {} to eat".format(k) for k, v
            in {k: bool(set([x.upper() for x in venue["food"]]) - v) for k, v
                in {user["name"]: set([x.upper() for x in user["wont_eat"]]) for user
                    in users}.items()}.items() if not v] + \
           ["There is nothing for {} to drink".format(k) for k, v
            in {k: bool(set([x.upper() for x in venue["drinks"]]) & v) for k, v
                in {user["name"]: set([x.upper() for x in user["drinks"]]) for user
                    in users}.items()}.items() if not v]


if __name__ == "__main__":
    names = input("Who will be attending?").split(',')
    venues = json.load(open("venues.json"))
    users = json.load(open("users.json"))
    result = {venue["name"]: restaurant_test(venue,users) for venue in venues}
    print("Places to go:\n"+"\n".join(str(x) for x,v in result.items() if not v))
    print("Places to avoid:"+"\n".join(str(k)+'\n'+'\n'.join(str(p) for p in v) for k,v in result.items() if v))



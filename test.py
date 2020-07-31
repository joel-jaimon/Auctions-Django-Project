import auctions.models

al = auctions.models.auctionlist.objects.all()

def info():
    for item in al:
        print(item.title)
        print(item.desc)
        print(item.starting_bid)
        print(item.image_url)
        print(item.category + "\n")
        
info()
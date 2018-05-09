from scraper import parse_platform

# <bitbar.title>Daily Game Deals</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Devin Sova</bitbar.author>
# <bitbar.author.github>DevinSova</bitbar.author.github>
# <bitbar.desc>Daily Game Deals Around the Internet</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

def main():
    parse_platform("ps4")
    #parse_platform("xbox")
    #parse_platform("pc")
main()

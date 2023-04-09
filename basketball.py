class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
# assignment one 
kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.age)

# Challenge 2
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_jason = Player(jason["name"], jason["age"], jason["position"], jason["team"])
player_kyrie = Player(kyrie["name"], kyrie["age"], kyrie["position"], kyrie["team"])
print(player_kevin.age)
print(player_jason.age)
print(player_kyrie.age)

# ... (class definition and large list of players here)
new_team = [
    {
    	"name": "Jordan Durant", 
    	"age":31, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Tommy Tatum", 
    	"age":25, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kris Irving", 
    	"age":30, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Fabian Lillard", 
    	"age":35, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joey Embiid", 
    	"age":30, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
]
# Challenge 3
# Write your for loop here to populate the new_team variable with Player objects.
for x in new_team:
    print(x)




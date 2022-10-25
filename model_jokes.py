import random

jokes_data = []
joke_list = [
    "What kind of exercise do lazy people do? Diddly-squats.",
    "What do you call a pony with a cough? A little horse!",
    "What is Forrest Gump's password? 1Forrest1.",
    "Why did the M&M go to school? He wanted to be a Smartie.",
    "What did one traffic light say to the other? Stop looking at me, I'm changing!",
    "What do you call bears with no ears? B.",
    "What's a foot long and slippery? A slipper!",
    "Why do French people eat snails? They don't like fast food!",
    "What's red and moves up and down? A tomato in an elevator!",
    "I invented a new word today: Plagiarism.",
    "What is sticky and brown? A stick!",
    "How does a rabbi make coffee? Hebrews it!",
    "Rest in peace boiling water. You will be mist!",
    "How do you throw a space party? You planet!",
    "Want to hear a construction joke? Oh never mind, I'm still working on that one.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I hate Russian dolls… they're so full of themselves!",
    "Talk is cheap? Have you ever talked to a lawyer?",
    "Why did the gym close down? It just didn't work out!",
    "Two artists had an art contest. It ended in a draw!",
    "A plateau is the highest form of flattery.",
    "I have a fear of speed bumps. But I am slowly getting over it.",
    "You can only get spoiled milk from a pampered cow.",
    "What do you call a boomerang that doesn't come back? A stick!",
    "You know what I saw today? Everything I looked at."
]

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in joke_list:
        jokes_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(jokes_data)

# Joke getter
def getJoke(id):
    return(jokes_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(jokes_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return jokes_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['boohoo'] > worst:
            worst = joke['boohoo']
            worstID = joke['id']
    return jokes_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    jokes_data[id]['haha'] = jokes_data[id]['haha'] + 1
    return jokes_data[id]['haha']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    jokes_data[id]['boohoo'] = jokes_data[id]['boohoo'] + 1
    return jokes_data[id]['boohoo']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(jokes_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['haha'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['boohoo'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))
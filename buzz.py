import random

choose = random.choice

def monetize():
	return choose ( ["Monetize", "Awesomize", "Leverage"] )

def high_level_structure():
	return choose ( [
			lambda: monetize() + " your " + suckers() + " with " + solution(),
			lambda:  you_should() + " " + do_something() + " to " + maximize_shareholder_value()
		]
	) ()

def suckers():
	return choose ( ["customers", "experience", "social graph", 
					"data-mining potential", "employees' nubile children",
					"web 2.0 magic", ""] )


def do_something():
	return choose ( [
		lambda: connect() + " " + community() + " with " + buzzword(),
		lambda: connect() + " " + buzzword()
	] ) ()


def connect():
	return choose ( [ "connect", "revolutionize", "arouse", "twitterize"] )


def community():
	return choose ( [ "friends", "cow-orkers", "grandmothers", "wives and mistresses", "the world"] )


def buzzword():
	return choose ( [ "photos", "breasts", "micropayment systems"] ) 
	
	
def you_should():
    you_shoulds = [
     "You need to",
     "I heard that you should",
     "The way you gotta approach this is",
    ]
    return choose(you_shoulds)

def maximize_shareholder_value():
    maximum = [
        "maximize shareholder value",
        "revolutionize",
    ]
    return choose(maximum)

def industry():
    industries = [
        "friendship bracelets",
        "peer-to-peer commerce",
        "virual worlds",
        "social media",
    ]
    return choose(industries)

def solution():
    solution = [
     "a social media strategy",
     "a variable cost business model on a fixed engineering base",
     "a viral video",
     "a micropayment solution",
     "a virtual good",
     "a customer social network",
     "customer created content",
    ]
    return choose(solution)


if __name__ == "__main__": print high_level_structure()



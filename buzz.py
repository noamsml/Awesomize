import random

choose = random.choice

def awesomize():
	return (source(), high_level_structure())

def monetize():
	return choose ( ["Monetize", "Awesomize", "Leverage"] )

def high_level_structure():
	return choose ( [
			lambda: you_should() + " " + monetize() + " your " + suckers() + " to " + maximize_shareholder_value(),
		]
	) ()

def suckers():
	return choose ( ["customers", "experience", "social graph", 
					"data-mining potential", "employees' nubile children",
					"web 2.0 magic", "lock-in content", "thought leaders"] )


def do_something():
	return choose ( [
		lambda: connect() + " " + community() + " with " + solution(),
		lambda: connect() + " " + industry()
	] ) ()


def connect():
	return choose ( [ "connect", "revolutionize", "arouse", "twitterize"] )


def community():
	return choose ( [ "friends", "cow-orkers", "grandmothers", "wives and mistresses", "the world"] )


	
	
def you_should():
    you_shoulds = [
     "You need to",
     "I heard that you should",
     "The way you gotta approach this is",
    ]
    return choose(you_shoulds)


def source():
	return choose ( [
		lambda: self_deprecate() + ", but I read this " + in_journal() + " " + a_while_back(),
		lambda: guy() + " thinks that",
		lambda: "Well, people seem to think that"
		]
	)()

def self_deprecate():
	return choose ([
		"I'm no expert",
		"This isn't generally my area",
		"I've never been loved", 
		"I'm no programmer",
		"I don't do this for a living",
		"This isn't what I do for a living",
		"I'm no startup guy",
		"I'm not a Harvard grad"
	])
	
def in_journal():
	return choose([
		"in The Wall Street Journal",
		"on Hacker News",
		"on Reddit",
		"on 4chan",
		"in The New York Times",
		"in Foreign Affairs",
		"in Freakonomics",
		"in The Economist",
		"in SIGINT"
	])

def a_while_back():
	return str(random.randint(2,5)) + " " + choose(["days", "years", "months"]) + " ago"

def guy():
	return choose(["Donald Knuth", "Sergey Brin", "Leonardo Dicaprio", "Paul Graham", "Linus Torvalds", "Tim O'Reilly", "Mark Zuckerbed", "Ashton Kucher"])
	
def maximize_shareholder_value():
    maximum = [
        lambda: "maximize shareholder value",
        lambda: "revolutionize the way we think about " + industry(),
    ]
    return choose(maximum)()

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


if __name__ == "__main__": print awesomize()



import random

choose = random.choice

def awesomize():
	return (source(), high_level_structure())

def monetize():
	return choose ( ["monetize", "awesomize", "leverage", "synergize", "emphasize"] )

def high_level_structure():
	a = lambda: you_should() + " " + monetize() + " your " + suckers() + " to " + maximize_shareholder_value()
	return choose ( [
			a,a,a,a,socialmobile 
			
		]
	) ()


def socialmobile():
	buzzword = lambda: choose( [industry, community, verbing, verbing] )()
	a = adjective()
	b = adjective()
	c = buzzword()
	d = app()
	return "%s. %s. %s. %s. %s %s %s %s" % (a.capitalize(),b.capitalize(),c.capitalize(),d.capitalize(),a.capitalize(),b,c,d)


def app():
	return choose([ "app", "site", "twitterstream", "cloud", "device",
		"revolution", "course", "experience", "crowdsource", "game",
		"challenge"])

def verbing():
	return choose([ "thinking", 
	"doing", "sharing", 
	"clicking", "twitterizing", "verbing",
	"eating", "buying", "selling",
	"writing", "collaborating",
	"caring", "filming", "drawing",
	"staring", "charring", "energizing",
	"motivating", "socializing",
	"networking", "creativing"])
	
def adjective():
	return choose(["social", "mobile", "colorful",
	"web 2.0", "twitteriffic", "online", "HTML5",
	"videofied", "futuristic", "magical", "powerful",
	"professional"])

def suckers():
	return choose ( [
        "customer experience", 
        "user interactivity", 
        "social graph", 
        "noSQL database",
        "customer data", 
        "employees' nubile children", 
        "economic lock-in", 
        "technology stack",
        "thought leaders"] )


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
     "What you should do is",
     "You gotta",
     "To compete you have to",
     "You should",
     "You need to",
     "We all know you should",
     "The best way is to",
     "The way you gotta approach this is",
    ]
    return choose(you_shoulds)


def source():
	return choose ( [
		lambda: self_deprecate() + ", but I read this " + in_journal() + " " + a_while_back(),
		lambda: guy() + " thinks that",
		lambda: self_deprecate() + ", but " + guy() + " said",
		lambda: choose(["Well, ", (self_deprecate() + " but, ")]) + "people seem to think that"
		]
	)()

def self_deprecate():
	return choose ([
		"I'm no expert",
		"This isn't generally my area",
        "I'm not so good with computers",
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
        "in The New Yorker",
        "on Proggit",
        "in 2600",
        "on Phrack",
        "on TechCrunch",
        "on ValleyWag",
		"in The New York Times",
		"in Foreign Affairs",
		"in Freakonomics",
		"in The Economist",
		"in SIGINT"
	])

def a_while_back():
	return choose(["", "", "", "", "", "about", "like"]) + " " + choose(['two', 'three', 'four', 'five']) + " " + choose(["days", "years", "months"]) + " ago"

def guy():
	return choose(["Donald Knuth", "Donal Trump","Sergey Brin", "Leonardo Dicaprio", "Paul Graham", "Linus Torvalds", "Tim O'Reilly", "Mark Zuckerberg", "Ashton Kucher", "The Woz", "Steve Jobs", "Jeff Bezos", "Evan Williams", "Sean Parker", "Meg Whitman", "Bain Capital VC", "Thomas Malthus", "Henry Kissinger"])
	
def maximize_shareholder_value():
    maximum = [
        lambda: "capture higher mind-share",
        lambda: "please the investors",
        lambda: "land that VC money",
        lambda: "pierce into new market spaces",
        lambda: "maximize shareholder value",
        lambda: "grow product revenue",
        lambda: "increase customer conversions",
        lambda: "revolutionize the way we think about " + industry(),
        lambda: "change the way we think about " + industry(),
        lambda: "grab market share in " + industry(),
    ]
    return choose(maximum)()

def industry():
    industries = [
        "friendship bracelets",
        "local",
        "social",
        "video",
        "social video editing",
        "document collaboration tools",
        "virtual e-commerce",
        "e-commerce",
        "gold farming",
        "spider caching",
        "web analytics",
        "independent music",
        "silkscreened t-shirts",
        "independent film",
        "recommender systems",
        "polymer engineering",
        "telepresence",
        "wearable tech",
        "augmented reality",
        "qr codes",
        "HTML5",
        "mobile",
        "mobile apps",
        "peer-to-peer commerce",
        "social gaming",
        "social media",
        "photo sharing",
    ]
    return choose(industries)

def solution():
    solution = [
     "a social media strategy",
     "a variable cost business model on a fixed engineering base",
     "a micropayment solution",
     "a virtual good marketplace",
     "social coupons",
     "a customer social network",
     "customer created content",
     "local monetization",
     "Justin Beiber",
     "hiring a revenue engineer",
    ]
    return choose(solution)


if __name__ == "__main__": print awesomize()



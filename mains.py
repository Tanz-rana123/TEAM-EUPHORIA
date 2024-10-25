import re
import long_responses as long

# Color constants
class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    BLACK = "\033[30m"
name_is = input("What is your name ? :  ")
a = (name_is + ':')

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'you'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Bliss Bot is here to help. What’s bothering you kid ?', ['not', 'feeling', 'good'], required_words=['not', 'good'])
    response('I would suggest that you build up the courage and tell them when they seem to be in a good mood.', ['not', 'score', 'parents','react','semester'], required_words=['score','parents',])
    response('You parents love you deeply and would never judge you based on a single piece of paper.', ['what', 'if', 'they','judge','me'], required_words=['judge', 'me','they',])
    response('If they are your true friends then there is nothing for you to worry about and if somebody does judge you, I’d suggest you maintain your distance with them.', ['my', 'friends', 'already','judge','me'], required_words=['judge','friends'])
    response('A 100 %', ['You', 'u', 'sure','are'], required_words=['sure'])
    response('Don’t worry kid tell me which stream did u choose or planning to choose ?', ['know', 'my', 'life','dont',], required_words=['life','dont'])
    response('Humanities is a vast field with various career options. If you are creative and can come up with unique ideas, explore fields like designing, animation, visual arts, to name a few. If you are good with facts and have a strong memorization power, then you could pursue a degree in law. If you want to help others and brings positive changes in the country, you could appear for UPSC and become a civil servant. There are several others career options to choose from.', ['humanities','arts'], required_words=['humanities'])
    response('Science is a vast field with various career options. If you like helping others and have good eye-hand coordination, then you could consider medical as an option. If you enjoy learning about how life works, you could become a research scientist in the field of biology. If you are exemplary at understanding physics and have fine observation skills, you could become a pilot. If your mathematical skills are excellent and have great artistic qualities, you could consider architecture as an option. There are several others career options to choose from.',['sci','science','Science'], required_words=['science'])
    response('Commerce is a vast field with various career options. If your business and commercial aptitude is exemplary then being a chartered accountant is a great option.  If your attention to detail is notable and good with numbers, investment banking as a career can be a good option. If you are good with solving problems and have great analytical skills, then being a business consultant can be a good option as well. There are several other career options for commerce students which suits their set of skills.', ['commerce','Commerce','com'], required_words=['commerce'])
    response('Changes in life are inevitable whether they are drastic or gradual. We have to learn to cope up with what life gives and make the best out of the situation we are in. Focus on the potential benefits of the change to foster a positive mind-set, and establish routines to create a sense of stability. Seeking support from friends or family can provide comfort, while breaking the change into manageable steps can prevent feeling overwhelmed.', ['everything', 'change', 'changing','dont','like'], required_words=['changing','everything'])
    response('Its okay to feel low and under confident about yourself on some days. You should just remember that everyone is unique and no one else is just like you. you too have a set of skills that sets you apart from the world. You should know what are your strong suits and work on honing those skills. Nobody can be good at everything. I would suggest that you spend some time on doing things that you love and finding out new interests which are helpful in boosting confidence.', ['dont', 'feel', 'confident','myself',], required_words=['myself','confident'])
    response('There is always something that an individual is good at. Its very likely that you just haven’t found the set of skills that you enjoy and are great at as well. I suggest you try out different activities to find out your true set of ability.You just have to have faith in yourself and trust the process.', ['what', 'good', 'at', 'nothing'], required_words=['good', 'nothing'])
    response('I empathise with you and am truly sorry that you are going through such a horrendous experience. The topic of bullying is a very sensitive one and each individual has a different experience from one another. Everyone may say to stand up for yourself but I know that it is easier said than done. I would suggest that you talk about it to the people you trust. It may ease the burden on your shoulder experience a situation like this. If the behaviour persists, then I would suggest that you report it to the school authorities to prevent it from occurring any further. Just be reassured that you are not alone and there are people to help you.', ['I','am', 'being', 'bullied'], required_words=['bullied'])
    response('Being cyberbullied can be a horrendous experience and can completely change the way you think about yourself and also drastically decrease your confidence. This practice has been increasing over the years since the use of social media has increased. I would suggest that you immediately stop engaging with the bully.', ['I','am', 'being', 'cyberbullied'], required_words=['cyberbullied'])
    response('I’m very sorry to hear that. If u need emotional support I’m always there by your side. It must have been a painful experience for you. it’s completely okay to take your time and process the situation. I reckon you should try to keep yourself busy and engage in activities to try to distract yourself so that you can focus on your mental health. You could also reconnect with those close to you and try to rebuild your bond. You should give the situation some time and process your feelings.', ['going', 'through', 'heartbreak'], required_words=['heartbreak', 'through'])
    response('No, I don’t think it is advisable for you to reconnect with your ex-partner after such short period of time post break up. You should give it some time and try to work on yourself and move on from the person as well as the relationship itself. Maybe once you and your ex are both healed and moved on, you may try and reconnect and rebuild your bond but as friends.', ['talk', 'to', 'ex', 'my'], required_words=['talk', 'ex'])
    response('Killing anybody is not advisable, however i can understand your feelings. you should let go of all the anger and focus on yourself and your personal growth.', ['should', 'kill', 'ex', 'my'], required_words=['kill'])
    response('Dealing with depression can be tough, but several strategies can help. Seek professional help from a therapist or counselor, and consider medication if appropriate. I reckon you should talk to a clinical psychologist or a therapist so that they can help you overcome this battle. Build a support system by talking to friends or joining support groups to reduce isolation. Stay active with regular exercise, even simple walks, to boost your mood. Establishing a routine and setting small goals can provide structure and prevent overwhelm. Prioritize self-care by engaging in enjoyable activities and practicing mindfulness.', ['sad', 'depressed', 'feeling', 'my'], required_words=['depressed'])
    response('I’m really sorry to hear that. Do you want to talk about what’s making you feel this way?', ['terrible',], required_words=['terrible'])
    response('Having no friends is completely okay as long as you enjoy your own company. You should however, try to socialise and try to talk to people more often and try to get out of your comfort zone but just know that you are not alone and there are peopel who care about you.', ['You', 'u', 'sure','are'], required_words=['friends', 'have'])
    response('feeling lonely is a problem that alot of teenagers face as they feel disconnected forom thier peers and family. i can understand that you might be feeling that nobody can understand you well. you can stop feeling alone by trying to enjoy your own company and spending time with yourself and focusing on you personal care and growth. you could also try socialising more often and trying to build new friendships and also put in effort to reconnect with your family and communicate with them and express how you are feeling', ['feeling', 'am', 'sure','are'], required_words=['lonely'])
    

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    response = get_response(input(a))
    print(Colors.BLUE + 'BLISS.BOT: ' + response + Colors.RESET)

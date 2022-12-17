
from deep_translator import GoogleTranslator
from collections import Counter
from youtube_comment_scraper_python import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    # print("Overall sentiment dictionary is : ", sentiment_dict)
    # print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    # print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    # print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    # print("Sentence Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
       
        return "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
      
        return "Negative"
 
    else :
      
        return "Neutral"

url = "https://www.youtube.com/watch?v=dPNC8Mutdfw"
youtube.open(url)
response=youtube.video_comments()
data=response['body']
print("COMMENTS LEN", len(data))
# out_file = open("myfile.json", "w")
# json.dump(data, out_file, indent = 6)
# out_file.close()



final = []

for i in data:
  final.append(sentiment_scores(GoogleTranslator(source='auto', target='en').translate(i['Comment'].encode('utf-16','surrogatepass').decode('utf-16'))))

print(Counter(final))
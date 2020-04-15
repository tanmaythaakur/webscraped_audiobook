import requests
from bs4 import BeautifulSoup
from gtts import gTTS


for i in range(2, 3): #change it to (2, 238) for complete version

    number = str(i)
    x = (3-len(number))*'0' + number
    url = "https://www.sacred-texts.com/hin/m01/m01%s.htm"%x
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    title = soup.find('title').text.split()
    title = title[-2:]
    title = ' '.join(title)
    # print(title)
    rawPara = soup.findAll('p')
    paragraphs = []

    for para in rawPara:
        text = para.text.strip()
        if not text.startswith('p.'):
            paragraphs.append(text)

    #print(paragraphs)


    speechText = ' '.join(paragraphs)
    #print(speechText)

    language = 'hi'
    myobj = gTTS(text=speechText, lang=language, slow=False)
    myobj.save(f"./Audiofiles/{i-1}_{title}.mp3")


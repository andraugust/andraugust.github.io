---
layout: page
title: "Quora"
permalink: /quora/
---
<br />
<h2><center>Quora Insincere Question Classification</center></h2>
<center><img src="../quora/banner.png"></center>
<br />
The Quora Insincere Question Classification challenge provides a dataset of questions asked on [quora.com](https://www.quora.com/) and a binary label indicating if each question is _sincere_. The goal is to develop a model that accuartely labels a set of testing questions.  This post documents my development of such a model.

## Data Exploration
What are some sincere questions?
```
00002165364db923c7e6,How did Quebec nationalists see their province as a nation in the 1960s?,0
000032939017120e6e44,"Do you have an adopted dog, how would you encourage people to adopt and not shop?",0
0000412ca6e4628ce2cf,Why does velocity affect time? Does velocity affect space geometry?,0
000042bf85aa498cd78e,How did Otto von Guericke used the Magdeburg hemispheres?,0
0000455dfa3e01eae3af,Can I convert montra helicon D to a mountain bike by just changing the tyres?,0
00004f9a462a357c33be,"Is Gaza slowly becoming Auschwitz, Dachau or Treblinka for Palestinians?",0
00005059a06ee19e11ad,"Why does Quora automatically ban conservative opinions when reported, but does not do the same for liberal views?",0
0000559f875832745e2e,Is it crazy if I wash or wipe my groceries off? Germs are everywhere.,0
00005bd3426b2d0c8305,"Is there such a thing as dressing moderately, and if so, how is that different than dressing modestly?",0
00006e6928c5df60eacb,"Is it just me or have you ever been in this phase wherein you became ignorant to the people you once loved, completely disregarding their feelings/lives so you get to have something go your way and feel temporarily at ease. How did things change?",0
000075f67dd595c3deb5,What can you say about feminism?,0
000076f3b42776c692de,How were the Calgary Flames founded?,0
000089792b3fc8026741,"What is the dumbest, yet possibly true explanation for Trump being elected?",0
000092a90bcfbfe8cd88,Can we use our external hard disk as a OS as well as for data storage.will the data be affected?,0
000095680e41a9a6f6e3,"I am 30, living at home and have no boyfriend. I would love a boyfriend and my own home. How can I progress my situation?",0
0000a89942e3143e333a,What do you know about Bram Fischer and the Rivonia Trial?,0
0000b8e1279eaa0a7062,How difficult is it to find a good instructor to take a class near you?,0
0000bc0f62500f55959f,Have you licked the skin of a corpse?,0
0000ce6c31f14d3e09ec,Do you think Amazon will adopt an in house approach to manufacturing similar to the Tesla or Space X business models?,0
0000d329332845b8a7fa,How many baronies might exist within a county palatine?,0
0000dd973dfd35508c16,How I know whether a girl had done sex before sex with me?,0
0000e4d455f9c8877dc9,How do I become a fast learner both in my professional career and in my personal life?,0
000101ac65db6e4a1c13,"What is the strangest phenomenon you know of, have witnessed or have generated in the area of electronics that has no explanation in terms of modern physics?",0
00010632971fe5e3e0e2,Should I leave my friends and find new ones?,0
00010a2e064c3e8f152a,Can you make Amazon Alexa trigger events in the browser?,0
00012011b6c7759461e8,Why haven't two democracies never ever went for a full fledged war? What stops them?,0
00012fd5128d576260ab,How can I top CBSE in 6 months?,0
0001303b1799a042b26b,What should I know before visiting Mcleodganj and doing the Triund trek?,0
00013a8152b5f37b780e,How do modern military submarines reduce noise to achieve stealth?,0
00014b4f153c26b02df2,How can I remove black heads which are all over my nose?,0
0001dffd4f210f6beedb,What do I need to know about buying a car in South Africa as an American?,0
00022b535fb044b4d890,Why do we calead leap year.?,0

```
A few things to note:
- Questions with commas are surrounded by quotes.  We'll eventually want to remove these.
- Some samples are mis-labeled, e.g., `have you licked the skin of a corpse` or `Is Gaza slowly becoming Auschwitz, Dachau or Treblinka for Palestinians?`.
- Some words aren't separated by space, e.g. `..OS as well as for data storage.will the data..`, we'll probably ignore these since they won't have an embedding.
- Sincere questions tend to ask about how to do something, e.g., `Can you make Amazon Alexa trigger events in the browser?`, or about advice regarding something legal or technical, e.g., `What should I know before visiting Mcleodganj and doing the Triund trek?` and `What do I need to know about buying a car in South Africa as an American?`.


What are some insincere questions?
```
0000e91571b60c2fb487,Has the United States become the largest dictatorship in the world?,1
00013ceca3f624b09f42,Which babies are more sweeter to their parents? Dark skin babies or light skin babies?,1
0004a7fcb2bf73076489,If blacks support school choice and mandatory sentencing for criminals why don't they vote Republican?,1
00052793eaa287aff1e1,"I am gay boy and I love my cousin (boy). He is sexy, but I dont know what to do. He is hot, and I want to see his di**. What should I do?",1
000537213b01fd77b58a,Which races have the smallest penis?,1
00056d45a1ce63856fc6,Why do females find penises ugly?,1
0005de07b07a17046e27,How do I marry an American woman for a Green Card? How much do they charge?,1
00068875d7c82a5bcf88,"Why do Europeans say they're the superior race, when in fact it took them over 2,000 years until mid 19th century to surpass China's largest economy?",1
0006ffd99a6599ff35b3,Did Julius Caesar bring a tyrannosaurus rex on his campaigns to frighten the Celts into submission?,1
00075f7061837807c69f,In what manner has Republican backing of 'states rights' been hypocritical and what ways have they actually restricted the ability of states to make their own laws?,1
00076debbd82860ca33a,"Would Europeans continue to participate in the Arab war for the destruction of Israel and killing all the Jews, if they knew that god himself defends Israel and he will do to Europeans what the Arabs want to do to the Jews?",1
000983f5b226cca636f4,"Why are Americans, British, Canadians, Australians and New Zealanders considered to be separate nations even when they all speak the same language?",1
0009fcb845bb24de91f4,"If both Honey Singh and Justin Bieber fall from the 5th floor, who will survive?",1
000a898565e80fe124bf,Why are liberal minorities so voilent towards poeple with diffrent poltical beleifs? Should supporting trump be a sentence to be imprisoned or savegely attacked?,1
000b1f4cbc5c238a765d,Can we all now admit that President Trump doesn't really want Congress to pass legislation replacing DACA to protect dreamers?,1
000c44fe9b2822b25d77,"The American economy is growing under Trump’s presidency, why do people still hate Trump as a president?",1
000d9de4df8d6a31c248,"Why don't poor countries print more money to use for paying for education, etc.?",1
000db4d0223af5dd9c5d,Why do all the people who claim Florida has great weather go silent every time there's a new hurricane?,1
000db9603d16a6d9bb2e,Could the leader of Iran be dead many years ago and the leader of today's Iran is actually a fake leader?,1
000e67648fce55f011be,Why do the Liberals who run schools choose not to have controlled access? The kids in Florida were killed due to an unlocked door.,1
000f0266e12c3349db07,Why did Pakistan pass the Sikh Marriage Act before India?,1
000f89527b907f3ef20f,How do I train my dogs to kill raccoons?,1
0010b8bd37af629de2f9,"Is there any woman (other than Muslim) who is happy after marrying a Muslim guy, as there are a lot of answers on Quora about love jihad, and all of them suffered a lot after marrying a Muslim guy?",1
0012bba774c13ce9cc9e,Do moms have sex with their sons?,1
0012d72ccc14e9329f97,"Why did the Pope say that ""Muslims are a curse to this world""?",1
0014e0200bb280d44ea1,How peoples in India seems hypocritical about womans empowerment?,1
0015e367aa794e5d547f,How much more political fumbling will it take for Republicans to turn on Trump?,1
00175f5e9c85b110614e,Why do Americans prefer just to not show up somewhere rather than face even the mildest of conflicts? (My colleagues and I have noted a growing number of people who skip any face to face meetings without any explanation at all.),1
00199a473cba7b54d974,"Liberals are pro-choice, but the choices must be approved by them first. Is this an accurate description of liberals?",1
0019e01b2a7b09d3cb65,Why are South Indian dishes which are prepared by North Indians more tasty than dishes prepared by South Indian restaurants?,1
0035beccb57afc87545f,"Why Italian so narcist with their own food, like they think their food is the best in the world ever?",1
002409e1ac34d209f6dc,"If Hispanics are so proud of their countries, why do they move out?",1
02d559d602a0a5612f74,"Whenever we missed a dose of ephedrine, could we take 2 doses at once?",1
```
A few things to note:
- Insincere questions tend to be about politics or religion or sex, and often make broad generalizations about groups of people, e.g., `Why Italian so narcist with their own food,...` and `If Hispanics are so proud of their countries, why do they move out?`.
- Insincere questions seem more likely to be premised on an opinion than a fact, e.g., `Why are South Indian dishes which are prepared by North Indians more tasty than dishes prepared by South Indian restaurants?`.
- Some samples are mislabelled, e.g., `Whenever we missed a dose of ephedrine, could we take 2 doses at once?`, but it seems there are fewer mislabels here compared to the sincere set, this is may be what motivated the challenge!

How many samples are there?
- Train: 1,306,122
- Test: 56,372

What's the class bias?
- 1/0 = 80,810/1,225,312 = 0.066

### Embeddings
The challenge provides four embedding sets.  Each has a dimensionality of 300.

- `glove.840B.300d.txt`
    - GloVe vectors from Pennington, et al.
    - vocab: 2.2M
    - training: common crawl
    - format: space-separated text file
    - [reference](https://nlp.stanford.edu/projects/glove/)
- `GoogleNews-vectors-negative300.bin`
    - Google's word2vec Embeddings
    - vocab: 3B
    - training: Google News articles
    - format: binary, load with `gensim`
    - [reference](https://code.google.com/archive/p/word2vec/)
- `paragram_300_sl999.txt`
    - vocab: 1,703,756
    - trained on: paraphrase data
    - format: space-separated text file
    - [reference](https://cogcomp.org/page/resource_view/106)
- `wiki-news-300d-1M.vec`
    - vocab: 999,994
    - format: space-separated text file
    - trained on: Wikipedia 2017, UMBC webbase corpus and statmt.org news dataset
    - [reference](https://fasttext.cc/docs/en/english-vectors.html)

### Modelling

#### lstm
1. make training set
    - embed each word in each sample
    -



{% include disqus.html %}

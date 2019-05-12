# en_personality

How to extract clusters of personality from text?

Texts themselves are short, using a pretrained model for larger corpora won't work well.

There isn't that much data per user.

There is no training set to do ML on this.

So, manual features it is.

Features that might have to do with personality

- Distribution of length of emails (average, median lenght)
- Email count per person
- Sentiment, compliments, agreement
- Informal/formal style
- Negations
- Social words
- Tentativity: perhaps, maybe
- Single
- % of short emails (10 words or less)
- Words: FYI/FYR, ok, thanks, yes, approved, no, please/pls,
- Cute, drinks, horse, football
- Can you/will you (command)
- Number of mentions of I
- Positive words: great

https://www.aaai.org/Papers/JAIR/Vol30/JAIR-3012.pdf
https://pdfs.semanticscholar.org/6eb2/52f76c987c6d88de5c3578d05caf5da5c6b5.pdf

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

After analysis, there is no obvious personality structure in the data. This is unsurprising: in a business setting the kind of language used is constrained to the formal business environment.

There are some emails that do not follow this pattern, talking about personal matters, but they did not meaningfully form a factor of their own.

The way personality tests work is that out of a set of questions, answered by many people, it's possible to use factor analysis to derive a latent structure (the factors).

I did exactly that same thing here. I even tried to use IBM's own predictive system for Big5, but I'm not sure if it works well.

I generated features that according to the literature are likely to correlate with personality: For conscientiousness for example length of message, punctiation used, and parenthesis (reflecting a wish to put in the extra work to be understood). For neuroticism, emotive and positive and negative-valenced words, for extraversion words related to social activities. This wasn't enough.

Even then, and as per IBM's own system, they are able to get a correlation of ~0.33 with the Big5 metrics, which is not that good.

What would work? It depends on what one wants.

The standard way of going about this is a battery of questions, then deriving the Big5 scores, then using those scores to do regressions and predict outcomes. One can do the same thing using individual questions. It can be that a limited set of questions yields a good estimate of what one ultimately cares about.

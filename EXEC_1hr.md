# mini exec-camp

Lecture notes, readings, code samples and resources for a 1 hour preview of [Brad Flaugher's ML Bootcamp for Executives](https://bradflaugher.com/executive.html)


## Part 1: The Regression Theory of Everything (~10 mins)

* Demonstration: Single Cell Neural Network aka Regression in Excel
* Demonstration: [Name and Height "Regression"](https://beta.openai.com/playground/p/z9Jkesb3QnQhym1jxHiw9o3X)
* Definition: [Multicolinearity](https://en.wikipedia.org/wiki/Multicollinearity) and [discussion](https://towardsdatascience.com/why-multicollinearity-isnt-an-issue-in-machine-learning-5c9aa2f1a83a)
* Demonstration: [Preprocessing data for training (AKA Everything is Numbers)](/3_Data_Types/data_loading_preprocessing.ipynb)

## Part 2: The End of Science (~10 mins)
* Definitions: Machine Learning and Artificial Intelligence
* "Codified Human Knowledge" vs "Statistical Knowledge"
* History: [How much of this book is practically useless?](https://github.com/sukantatiger/Artificial_Intelligence/blob/master/Artificial_Intelligence_by_Rich_and_Knight.pdf) 
* Definitions: Data Scientist, Data Engineer, Data Analyst ([What do we spend time doing?](https://stack.bradflaugher.com/Data-Janitors.jpg))
* Discuss: is it intelligence? is it science?
* ["ChatGPT is incredibly limited, but good enough at some things to create a misleading impression of greatness. It's a mistake to be relying on it for anything important right now. it’s a preview of progress; we have lots of work to do on robustness and truthfulness.](https://www.bloomberg.com/news/articles/2023-01-04/microsoft-hopes-openai-s-chatbot-will-make-bing-smarter) .... aside. OpenAI was originally non-profit but was [profit-capped as of 2019](https://openai.com/blog/openai-lp/)

## Part 3: Coding it up (~10 mins)
* [Basic Image Classification](https://www.tensorflow.org/tutorials/keras/classification)
* [Basic Text Classification](https://pytorch.org/tutorials/beginner/text_sentiment_ngrams_tutorial.html)
* [Using the model in reverse, Stable Diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion)
* [it's all a regression part 2, GPT on a napkin](https://dugas.ch/artificial_curiosity/GPT_architecture.html)

## Part 4: Case Studies (~10 mins)

### Software Development
* [Copilot](https://github.com/features/copilot)

### Design and Engineering
* [Nerf](https://developer.nvidia.com/blog/getting-started-with-nvidia-instant-nerfs/)
* [Dreamfusion](https://dreamfusion3d.github.io/)

### "Policing" or Online Dating
* [Earp](https://github.com/Medusa-ML/Earp/blob/main/training_notebooks/earp_v1.ipynb)

### Self-Driving and Skynet
* [calling it "Full Self-Driving" is disallowed in California](https://www.forbes.com/sites/alanohnsman/2023/01/04/tesla-calling-its-cars-full-self-driving-may-run-afoul-of-new-california-law/?sh=1560d0c4e2f3)
* [Edge Cases kill self driving?](https://www.forbes.com/sites/lanceeliot/2021/07/13/whether-those-endless-edge-or-corner-cases-are-the-long-tail-doom-for-ai-self-driving-cars/?sh=474229865933)

# Part 5: What is it Good For?

### It's a lossy database. [From Gary Marcus](https://cacm.acm.org/blogs/blog-cacm/268376-is-chatgpt-really-a-code-red-for-google-search/fulltext)

> (Traditional) search engines are databases, organized collections of data that can be stored, updated, and retrieved at will. (Traditional) search engines are indexes. a form of database, that connect things like keywords to URLs; they can be swiftly updated, incrementally, bit by bit (as when you update a phone number in the database that holds your contacts).

> Large language models do something very different: they are not databases; they are text predictors, turbocharged versions of autocomplete. Fundamentally, what they learn are relationships between bits of text, like words, phrases, even whole sentences. And they use those relationships to predict other bits of text. And then they do something almost magical: they paraphrase those bits of texts, almost like a thesaurus but much much better. But as they do so, as they glom stuff together, something often gets lost in translation: which bits of text do and do not truly belong together.

![Mr. Blend](blend-in.png "Mr. Blend-In")

* When crowds are wise, knowledge can be gathered via democracy, use ML. 
* When the world changes slowly, use ML.
* When there is no right answer, let ML suggest one.
* When you need a magic filter or sort, try ML. [The Harvard Admissions Magic Sort](https://beta.openai.com/playground/p/oDzhJ5GI9FwJGy3QwzIWN0L7)

### Final note on Skynet [From Jeff Hawkins](https://www.amazon.com/Thousand-Brains-New-Theory-Intelligence/dp/1541675797)

> The second requirement of goal-misalignment risk is that an intelligent machine can commandeer the Earth's resources to pursue its goals, or in other ways prevent us from stopping it... We have similar concerns with humans. This is why no single person or entity can control the entire internet and why we require multiple people to launch a nuclear missile. Intelligent machines will not develop misaligned goals unless we go to great lengths to endow them with that ability. Even if they did, no machine can commandeer the world's resources unless we let it. We don't let a single human, or even a small number of humans, control the world's resources. We need to be similarly careful with machines.
## Appendix: Additional readings and resources

### From The Economist...
* [Huge “foundation models” are turbo-charging AI progress](https://www.economist.com/interactive/briefing/2022/06/11/huge-foundation-models-are-turbo-charging-ai-progress)
* [Playing Pong with real neurons](https://stack.bradflaugher.com/Articles/neuron_pong.png)

### Programmer Chatter
* [Is it all just a big regression?](https://www.reddit.com/r/MachineLearning/comments/xrge5d/d_is_neural_network_really_smart_or_just_some/)
* [When was the last time you wrote a custom neural net?](https://www.reddit.com/r/MachineLearning/comments/yto34q/d_when_was_the_last_time_you_wrote_a_custom/)
* [Do you think there is a competitive future for smaller, locally trained/served models?](https://www.reddit.com/r/MachineLearning/comments/yon48p/d_do_you_think_there_is_a_competitive_future_for/)

### Quick Video Tutorials
* [How Deep Learning Works](https://www.youtube.com/watch?v=wBgW3ZtlPT8)
* [Intro to Deep Learning](https://www.youtube.com/watch?v=qj5gUDJ5TnU)

### AI Ethics in the news...
* [Google Researcher Says She Was Fired Over Paper Highlighting Bias in A.I.](https://www.nytimes.com/2020/12/03/technology/google-researcher-timnit-gebru.html)
* [A.I. Is Not Sentient. Why Do People Say It Is?](https://www.nytimes.com/2022/08/05/technology/ai-sentient-google.html)
* [Stuck on the Streets of San Francisco in a Driverless Car](https://www.nytimes.com/2022/09/28/technology/driverless-cars-san-francisco.html)
* [Copilot and the AI Copyright wars](https://www.technollama.co.uk/copilot-the-next-stage-in-the-ai-copyright-wars)
* ["Driverless Cars" with Human Masters](https://www.wsj.com/articles/why-autonomous-vehicles-will-still-need-a-human-minder-11667833922?mod=hp_listc_pos1)
* [ChatGPT Homework](https://stratechery.com/2022/ai-homework/)

### Deeper technical dives
* [The Universal Machine Learning Workflow](https://www.oreilly.com/library/view/deep-learning-with/9781617296864/Text/06.xhtml)
* [Deep Learning Illustrated](https://www.amazon.com/Deep-Learning-Illustrated-Intelligence-Addison-Wesley/dp/0135116694) and [Deep Learning with Tensorflow, Pytorch etc..](https://learning.oreilly.com/videos/deep-learning-with/9780136617617/)

### Recommended Mailing lists and online groups
* [Deep Learning Weekly](https://www.deeplearningweekly.com/)
* [Reddit Machine Learning](https://www.reddit.com/r/MachineLearning/)

### Recommended (in-person) Conferences
* [Ai4](https://ai4.io/)
* [NeurIPS](https://neurips.cc/)

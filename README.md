# bootcamp

Lecture notes, readings, code samples and resources for [Brad Flaugher's Data-Focused Programming Bootcamp](https://bradflaugher.com/bootcamp.html)


# New Student TODOs

## Preparation

* (Required) Install Ubuntu Linux on your PC, [Install Guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview), and [additional notes for dual-booting with Windows](https://linuxconfig.org/how-to-install-ubuntu-20-04-alongside-windows-10-dual-boot) NOTE if you have an M1 Mac this will be almost impossible, so sell that thing or talk to Brad.
* (Required) Install Docker [Install docker Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
* (Required) Read [Command Line for Beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* (Required) If you are not a proficient Python coder please do the entire futurecoder.io course, it's free! [Futurecoder.io](https://futurecoder.io/course/)
* (Required) if you have never used a Jupyter notebook before, please read [Jupyter Notebooks Getting Started Tutorial](https://jupyter.org/try)
* (Required) learn how to use git if you never have before. [Git and GitHub for beginners crash course](https://www.youtube.com/watch?v=RGOj5yH7evk)
* (Recommended) Join the bootcampers [LinkedIn Group](https://www.linkedin.com/groups/12707793/)

# Lecture Outline

* Note 1: Lectures are a small part of the course, most bootcamper's time will be spent working on their final potrfolio projects.
* Note 2: The 6 week course is broken into numeric and alphabetical lectures. Lectures 1-6 are technical in nature, Lectures A-E are soft-skills and history.

## Lesson 1: Practical Science

### Topics
* Definitions: Data Scientist, Data Engineer, Data Analyst ([What do we spend time doing?](https://stack.bradflaugher.com/Data-Janitors.jpg))
* Definitions: Machine Learning and Artificial Intelligence
* History: What kind of ML is used today? [How much of this book is practically useless?](https://github.com/sukantatiger/Artificial_Intelligence/blob/master/Artificial_Intelligence_by_Rich_and_Knight.pdf) 
* Neural Networks: [Babies and Vision](https://www.aoa.org/healthy-eyes/eye-health-for-life/infant-vision?sso=y)
* Neural Networks: Single Cell Neural Network aka Regression in Excel
* Neural Networks: [Name and Height "Regression"](https://beta.openai.com/playground/p/z9Jkesb3QnQhym1jxHiw9o3X)
* Neural Networks: When will GPT-3 "insights" become stale? Is this learning? is this engineering? is this science?
* Neural Networks: [Correllating words and images](https://www.craiyon.com/)
* Neural Networks: Why only study NNs for now? [NNs are Decision Trees](https://arxiv.org/abs/2210.05189), [NNs vs SVMs](https://stackoverflow.com/questions/11632516/what-are-advantages-of-artificial-neural-networks-over-support-vector-machines)
* Neural Networks: [Playing Pong with real neurons](https://stack.bradflaugher.com/Articles/neuron_pong.png)
* Final Project Intro: [Huggable Model](https://github.com/daspartho/is-it-huggable) and [Google Play Virus Model](https://www.sciencedirect.com/science/article/pii/S2772941922000114?via%3Dihub)

### Introduction to Portfolio projects
* [VIDEO: Alwin's Text Classifier](https://youtu.be/biyLyzBt9vE) and [Source Code](https://github.com/shdwhlx/agila)
* [VIDEO: Oleh's Car Price Predictor](https://www.youtube.com/watch?v=I-KL-mWF548) and [Source Code](https://github.com/MorhaliukOL/ML_Project)

### Project Ideas
* Help Brad with FOSS Models for [Medusa](https://github.com/predbrad/medusa)
* Free captioned images from the web, [LAION](https://laion.ai/)
* The entire web, scraped for you, [Common Crawl](https://commoncrawl.org/) via [comcrawl](https://github.com/michaelharms/comcrawl)
* More specialized data... [Datahub](https://datahub.io/collections) and [Awesome pubilc datasets](https://github.com/awesomedata/awesome-public-datasets) and [Huggingface Datasets](https://huggingface.co/datasets) and (Huggingface)[https://huggingface.co/docs/datasets/tutorial]

### Readings
* [Intro to Deep Learning](https://www.youtube.com/watch?v=qj5gUDJ5TnU)
* [Is it all just a big regression?](https://www.reddit.com/r/MachineLearning/comments/xrge5d/d_is_neural_network_really_smart_or_just_some/)

## Lesson A: History, Impostor Syndrome and Working With Technical Professionals

### Topics
* Definitions: Unix, Linux, Command Line, DevOps, Programming Language
* History: Python and C Speed Test, SQL
* History: BERT, GPT3, DALLE, Stable Diffusion and self-driving cars.
* History: A historical perspective on technological adoption, is it fast or slow? Flavors of technological disruption. (Lateral thinking with withered technology, how many people can use spreadsheets, and Keynes quote)
* Impostor Syndrome: "10,000 Qualified data scientists" Can you trust your professor at Berkley? Who are the ML Leads at big companies? Who are the IT consultants?
* Impostor Syndrome: What does MIT Say? A review of [Managing Technical Professionals](https://executive.mit.edu/course/Managing-Technical-Professionals-and-Organizations/a056g00000URaN0AAL.html).
* Practice: "Head of Data" interview question, how fast can you spin up an environment? [Remember your pandas functions](https://www.reddit.com/r/MachineLearning/comments/y7708w/d_how_frustrating_are_the_ml_interviews_these/)

### Readings
* [9 Reasons why you'll never be a data scientist](https://towardsdatascience.com/9-reasons-why-youll-never-become-a-data-scientist-c8c5b75503cf)
* [Huge “foundation models” are turbo-charging AI progress](https://www.economist.com/interactive/briefing/2022/06/11/huge-foundation-models-are-turbo-charging-ai-progress)
* [Language Models: Past, Present, and Future](https://cacm.acm.org/magazines/2022/7/262080-language-models/fulltext)

### Optional Readings
* [History of C](https://en.wikipedia.org/wiki/C_(programming_language))
* [History of Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [History of SQL](https://en.wikipedia.org/wiki/SQL)

## Lesson 2: Docker, DevOps/MLOps, and Environment Setup

### Topics
* Definitions: docker, container, ephemeral, bash
* History: SQL, what it is and why it's important (PowerBI, Tableau, Athena, BigQuery)
* Docker: Command line usage, flags, interactive mode and bash
* Docker in the cloud: How to think about the cloud, Big Providers (AWS, GCP, Azure) and Small (Linode, Oracle, etc...)
* Aside: What are Kaggle and Colab?
* Demonstration: Create a github project, spin up environment, run experiment, save python file, commit changes.

### Post-lecture homework
* [Install and Run a Tensorflow Container](https://www.tensorflow.org/install)
``` 
docker pull tensorflow/tensorflow:latest  # Download latest stable image
docker run -it -p 8888:8888 tensorflow/tensorflow:latest-jupyter  # Start Jupyter server 
```
* Run the tensorflow tutorial notebooks for either ```classification.ipynb``` (if you want to practice image classification) or ```text_classification.ipynb``` and fit the sample models with the sample data.

### Readings
* (this was previously assigned, but you MUST know it for this lecture)  [Command Line for Beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* if you do not have experience with SQL please take the [Interactive SQL course @ Codecademy](https://www.codecademy.com/learn/learn-sql)
* Read the first half of this article, once they get into deployment details you can skip. [Why use Docker for Machine Learning Development?](https://aws.amazon.com/blogs/opensource/why-use-docker-containers-for-machine-learning-development/)

### Optional Readings
* [Docker Documentaton](https://docs.docker.com/)
* [Docker on AWS](https://aws.amazon.com/getting-started/hands-on/deploy-docker-containers/), or the [TLDR version](https://medium.com/geekculture/deploy-to-aws-docker-in-10-minutes-68a60724dcb9)
* [Docker on GCP](https://cloud.google.com/compute/docs/containers), or the [TLDR version](https://www.howtogeek.com/devops/how-to-run-docker-containers-on-google-cloud-platform/)
* [Docker on Azure](https://azure.microsoft.com/en-us/services/kubernetes-service/docker/)
* [Spotty](https://github.com/spotty-cloud/spotty)
* [Tensordock](https://www.tensordock.com/)

## Lesson B: Open Source, Freedom, and how to remove the stress of software choices

### Topics
* History: [The FSF](https://www.fsf.org/) and [Richard Stallman](https://stallman.org/)
* History: [FOSS Products](https://www.designnews.com/design-software/8-popular-products-you-didnt-know-were-built-open-source), [Pixar](https://www.gamingonlinux.com/2016/09/pixar-film-production-show-off-how-they-use-linux-and-opengl-open-sourced-a-major-tool/), [Planes](https://i.pinimg.com/originals/d1/31/89/d13189392a05ff5a325152b3e1b55051.jpg), [Servers](https://hub.docker.com/search?q=)
* History: [Unix Family Tree](http://www.pearltrees.com/s/pic/or/unix-family-tree-73278499) and [Linux Family Tree](https://user.oc-static.com/upload/2021/07/05/16254800984395_6_p1c2-4.png) 
* Aside: “A Generation Behind” - is it true? is it useful? What if the closed-source stuff eventually becomes free?
* FOSS in practice: [calculendar](https://github.com/predbrad/calculendar) and [comcrawl](https://github.com/michaelharms/comcrawl/issues/40)
* Choosing Technologies: How to choose a technology and not stress about it. [How to handle buy vs. build and this map](B_FOSS/AI_Tool_Providers.png) 

### Final Project Update
* Downloading Data, Examples: [Common Crawl](/3_Data_Types/com_crawl.ipynb), [Common Crawl 2](https://github.com/predbrad/webmd-commoncrawl), [direct from webpages](/3_Data_Types/url_text.ipynb) and [CSV](/3_Data_Types/csv_example.ipynb).
* What is your ideal dataset? ```feature1, feature2, feature3, label```
* Image classification examples: [satellite-image-deep-learning](https://github.com/robmarkcole/satellite-image-deep-learning#Classification), [Go-Winner-Prediction](https://github.com/roykoand/GoWinnerPrediction/blob/master/notebooks/production-model.ipynb), [Mushroom Classifier](https://github.com/stepan9773/mashroom-poison-classification/blob/master/notebooks/poison_mushroom_classification_latest.ipynb)

### Optional Readings
* Feel free to skim this, or read in detail any essay with a title that speaks to you. [Free Software, Free Society](https://www.gnu.org/philosophy/fsfs/rms-essays.pdf)
* [Notes on The Software Paradox](https://baus.net/the-software-paradox/) or [The Software Paradox (Full Book)](https://www.amazon.com/Software-Paradox-Rise-Commercial-Market/dp/1491900938)

## Lesson 3: ETL, Loading Data Types, "It's all numbers, man" 

### Topics
* ETL: What is it and why do we need it?
* Demonstration: Numbers are Data
* Demonstration: Text is Data
* Demonstration: Images are Data
* Pandas: what is it and why do we use it?
* Discussion: Data Collection, ETL and "glue code"

### Final Project Update
* Setting up your project with the [medusa-ml-template](https://github.com/Medusa-ML/medusa-ml-template)

### Readings
* [Preprocessing Notebook](/3_Data_Types/data_loading_preprocessing.ipynb)

### Pandas Mini-Courses (required if you do not know pandas)
* [Pandas in Action](https://github.com/paskhaver/pandas-in-action) or read the [O'Reilly book ($ or free trial required)](https://learning.oreilly.com/library/view/pandas-in-action/9781617297434/)
* OR [pandas on datacamp ($ required)](https://www.datacamp.com/courses/data-manipulation-with-pandas) or [pandas on codecademy ($ required)](https://www.codecademy.com/learn/data-processing-pandas)
* OR [Freecodecamp Pandas 10 hour course](https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/)

### Optional Readings (Airflow)
* [Choosing a task orchestration tool](https://www.datarevenue.com/en-blog/airflow-vs-luigi-vs-argo-vs-mlflow-vs-kubeflow)
* [Airflow Tutorial for Beginners](https://www.youtube.com/watch?v=K9AnJ9_ZAXE)

## Lesson C: Data Wrangling 

### Topics
* Scraping Data
* APIs
* Python Requests
* Combining datasets

### Readings
* [Python Requests Tutorial](https://www.geeksforgeeks.org/python-requests-tutorial/)

## Lesson 4: Break to make progress on final projects.

## Lesson D: Features and Labels, how easy is that?

### Topics
* Demonstration: Simplest Text Classification
* Demonstration: Simplest Image Classification
* [Ludwig](https://github.com/ludwig-ai/ludwig)

### Readings
* [How Deep Learning Works](https://www.youtube.com/watch?v=wBgW3ZtlPT8)
* [NLP in 5 Minutes with Tensorflow](https://codesearchonline.com/natural-language-processing-with-tensorflow-cheat-sheet/)

## Lesson 5: Model Architecture

### Topics
* Definition: [Accuracy](https://medium.datadriveninvestor.com/accuracy-trap-pay-attention-to-recall-precision-f-score-auc-d02f28d3299c), [Precision, Recall, F1](https://emkademy.com/research/toolbox/2020-03-02-accuracy-precision-recall), [AUC](https://paulvanderlaken.com/2019/08/16/roc-auc-precision-and-recall-visually-explained/)
* Definition: [Confusion Matrix](https://www.statology.org/confusion-matrix-python/)... [in Tensorflow too](https://www.tensorflow.org/tutorials/audio/simple_audio#display_a_confusion_matrix)
* Discussion: Loss functions vs model metrics?
* Discussion: How do you measure model performance with other ML techniques? (Back to Excel Nerual Net for a moment) then [Custom Loss Functions](https://stackoverflow.com/questions/53980031/pytorch-custom-loss-function) and [Custom Loss Functions #2](https://discuss.pytorch.org/t/custom-loss-functions/29387/3)
* Discussion: "The Price is Right" Loss Function?
* Discussion: Layer Types and Standard or Template Models
* Discussion: Where to start, how to adjust hyperparameters
* Discussion: How can you steal ideas?

### Current Events and Discussions in the Community
* [When was the last time you wrote a custom neural net?](https://www.reddit.com/r/MachineLearning/comments/yto34q/d_when_was_the_last_time_you_wrote_a_custom/)
* [Do you think there is a competitive future for smaller, locally trained/served models?](https://www.reddit.com/r/MachineLearning/comments/yon48p/d_do_you_think_there_is_a_competitive_future_for/)
* [What are the major general advances in ML techniques?](https://www.reddit.com/r/MachineLearning/comments/ylixp5/d_what_are_the_major_general_advances_in/)

### Readings
* [Modeling Natural Language](https://www.youtube.com/watch?v=rqyw06k91pA)

## Lesson E: AI Optimism and Bias

### Topics
* Definitions: AI Ethics Big 3: Explainability, Bias, and Privacy
* Discussion: Who should die? Self-Driving trolley preblems.
* Discussion: I can predict criminality, should I? 
* Discussion: Are biased models useful? When?

### Readings
* [Google Researcher Says She Was Fired Over Paper Highlighting Bias in A.I.](https://www.nytimes.com/2020/12/03/technology/google-researcher-timnit-gebru.html)
* [Tesla’s ‘phantom braking’ problem is getting worse, and the US government has questions](https://www.theverge.com/2022/6/3/23153241/tesla-phantom-braking-nhtsa-complaints-investigation)
* [A.I. Is Not Sentient. Why Do People Say It Is?](https://www.nytimes.com/2022/08/05/technology/ai-sentient-google.html)
* [The Long Road to Driverless Trucks](https://www.nytimes.com/2022/09/28/business/driverless-trucks-highways.html)
* [Stuck on the Streets of San Francisco in a Driverless Car](https://www.nytimes.com/2022/09/28/technology/driverless-cars-san-francisco.html)
* [Copilot and the AI Copyright wars](https://www.technollama.co.uk/copilot-the-next-stage-in-the-ai-copyright-wars)
* ["Driverless Cars" with Human Masters](https://www.wsj.com/articles/why-autonomous-vehicles-will-still-need-a-human-minder-11667833922?mod=hp_listc_pos1)

## Lesson 6: The Universal Machine Learning Workow

### Topics
* Discussion: Tensorflow Lite, Tensorflow Serving
* Discussion: Predict is easy, train is hard (computationally)
* Discussion: Docker + Flask
* Discussion: DevOps vs MLOps, what is special? what is the same?
* Next Steps: Career Coaching, Apprenticeship, Review After-Class Resources and Job Boards
* Next Steps: After-Bootcamp Survey and Payment Options

### Readings
* [The Universal Machine Learning Workflow](https://www.oreilly.com/library/view/deep-learning-with/9781617296864/Text/06.xhtml)
* [Tensorflow Serving with Docker](https://www.tensorflow.org/tfx/serving/docker)

### Optional Readings
* [Create an MLOps Pipeline with github and docker in minutes](https://heartbeat.comet.ml/create-an-mlops-pipeline-with-github-and-docker-hub-in-minutes-4a1515b6a551)

# Final Projects

Bootcampers will spend a tremendous time working on final projects that are targeted to the bootcamper's career goals. For an example final presentation see [Oleh's Video (YouTube)](https://www.youtube.com/watch?v=I-KL-mWF548) and [Oleh's Repository (GitHub)](https://github.com/MorhaliukOL/ML_Project).

You can also see more final project presentations and source code on [Brad's Youtube Channel](https://www.youtube.com/@bradflaugher2452/videos).

# After The Bootcamp

## Recommended courses, videos and books

### Computer Science Fundamentals
* [OSSU Computer Science Curriculum](https://github.com/ossu/computer-science)

### Data Janitoring
* [Fundamentals of Data Engineering](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
* [Python Data Cleaning Cookbook](https://learning.oreilly.com/library/view/python-data-cleaning/9781800565661/)

### Model Training
* [Tensorflow Tutorials](https://www.tensorflow.org/tutorials)
* [PyTorch Tutorials](https://pytorch.org/tutorials/)
* [Deep Learning Illustrated](https://www.amazon.com/Deep-Learning-Illustrated-Intelligence-Addison-Wesley/dp/0135116694) and [Deep Learning with Tensorflow, Pytorch etc..](https://learning.oreilly.com/videos/deep-learning-with/9780136617617/)
* [HuggingFace Course on Transformers](https://huggingface.co/course/chapter0/1?fw=pt)
* [Natural Language Programming Demystified](https://www.nlpdemystified.org/course)
* [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)

### Background Math
* [Stanford ML Lectures, 2018](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)
* [Math for Machine Learning](https://learning.oreilly.com/playlists/b1c03a16-8f1d-44af-b97b-67aed9bace2e/)

### Operationalizing ML with MLFlow and MLOps tools
* [Practical MLOps](https://learning.oreilly.com/library/view/practical-mlops/9781098103002/)
* [Practical Deep Learning with MLFlow](https://learning.oreilly.com/library/view/practical-deep-learning/9781803241333/)

### Ethics and AI
* [Ethical Machines](https://www.reidblackman.com/ethical-machines/)
* [The Alignment Problem](https://brianchristian.org/the-alignment-problem/)

## Recommended Mailing lists and online groups
* [Deep Learning Weekly](https://www.deeplearningweekly.com/)
* [Reddit Machine Learning](https://www.reddit.com/r/MachineLearning/)
* [Hacker News (it's less focused on ML, but worth your time generally)](https://news.ycombinator.com/)
* [Reddit Programming (same as above)](https://www.reddit.com/r/programming/)

## Recommended Professional Groups
* [ACM](https://www.acm.org/)
* [Women in Data](https://www.womenindata.org/)

## Recommended (in-person) Conferences
* [Ai4](https://ai4.io/)
* [NeurIPS](https://neurips.cc/)

## Highly Recommended Job Boards
* [LinkedIn](https://www.linkedin.com/)
* [Angel.co](https://angel.co/job-collections/remote/)
* Hacker News "Who's Hiring" Thread [Sample Post](https://news.ycombinator.com/item?id=33818037) and [Collection of all posts](https://hnhiring.com/)
* [Turing](https://www.turing.com/)

## Salary Comparison Tools
* [Levels.fyi](https://www.levels.fyi)

## Useful Job Boards that sometimes suck
* [Indeed](https://www.indeed.com/)
* [Toptal](https://www.toptal.com/)
* [RemoteOK](https://remoteok.io/)
* [StackOverflow Jobs](https://stackoverflow.com/jobs/)

## Gigs (Freelance work)
* [TopCoder](https://www.topcoder.com/)
* [Experfy](https://www.experfy.com/)
* [Upwork](https://www.upwork.com/)
* [Codementor](https://www.codementor.io/)

## On-Demand Help
* [Apprenticeship via Patreon](https://www.patreon.com/bradflaugher)
* [Codementor](https://www.codementor.io/)

## Huge Foundational Models
* [Huggingface](https://huggingface.co/models)
* [OpenAI](https://openai.com/api/) 

## Competitions
* [Kaggle](https://www.kaggle.com/competitions)
* [ML Safety Competitions](https://safe.ai/competitions)

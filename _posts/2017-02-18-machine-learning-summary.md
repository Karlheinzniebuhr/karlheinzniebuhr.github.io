---
layout: post
title: "Machine Learning -- Summary"
date: 2017-02-18 13:47:00 +0000
categories: [Book Summaries, Technology]
tags: [Technology]
book: true
---

> This book will teach you a solid understanding about the basics of Machine Learning

[![](/assets/images/41kq8b-WROL._SX355_BO1204203200_-215x300.jpg)](https://www.amazon.com/gp/product/0262529513/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=kasbl023-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=0262529513&linkId=41fce8caaed84b248e77e4596d914d97)

#### The silent revolution in Computer Science

In the last decades, there has been a silent revolution in the field of Computer Science. Our daily lives are defined more and more by technology, which means there is more and more data available.
It is that data what makes it possible to explore a new, different approach to creating solutions. Learning from that data. Traditionally, it was the programmers who designed programs, which then executed the task they were designed to perform. This approach works well for many things, but there are areas where it is hard to design algorithms for. Robotics, vision, speech, and translation, are some of the areas where it is hard to design good algorithms for. That's where machine learning comes in.
Machine learning works the other way around. Instead of designing an algorithm to process data, in machine learning, a more general algorithm learns from the data and designs a learned algorithm from it.
Programming: Algorithm --> Data
Machine Learning: Learning Algorithm --> Training Data --> Learned Algorithm --> Data

#### Why does Machine Learning work

Machine Learning (ML) works because we suppose that in all data there is a pattern. Think about your shopping activity on big online retailers like Amazon. You probably have a preference for certain categories of goods, like technology or books. More detailed patterns once enough data is available. For example, a person who buys baby products probably has a baby or is expecting a baby. Now it's time to introduce a new term, hidden factors. Hidden factors in the last example are the baby. It is not named explicitly in the collected shopping data but can be inferred from the shopping activity. This inference of a hidden model is the core of ML.
The challenge then is to have enough training data and sufficient computing power to process and learn from that data.

#### ML, statistics and data analytics

To illustrate how more data makes it possible to design a precise algorithm, take the example of tossing a coin. Suppose we want to design an algorithm which reflects perfectly the behavior of a coin. The way a coin behaves can be described by probability, a subset of statistics. Data analytics is the process of -- you guessed analyzing data. You probably know that a coin has about 50% chance of hitting tail or head. But our algorithm wouldn't know that. Our ML algorithm would have to learn this from data. The
The data, in this case, are coin tosses. If we'd toss the coin three times, getting two heads and one tail, our algorithm would infer that the probability of hitting heads is about 66.6% and the probability of getting tail 33.3%. This wouldn't be accurate of course. When we toss the coin sufficient times we know -- due to statistics -- that eventually the results would even out and we would get about 50/50 heads and tails. To enable our ML algorithm to learn a precise model of coin tossing, we probably would have to perform hundreds or thousands of coin tosses.
Coin tosses are pretty simple, but take for example the estimation of prices of used cars. The reason the prices of cars depreciate so fast is that there is no good way to know whether a used car has a problem. That's why we expect the worst case, in other words, we give it a price we would give to a car which has a problem, even if the seller says it is in perfect conditions. Of course, there are many hidden factors. For example, if you knew the person who drove the car before, you grandma, for example, you know that she always treated her car extremely carefully. Giving it regular maintenance service and so on. You would have much more confidence that the car is actually worth more money.
An ML algorithm would have to infer such hidden factors from data. A lot of data in fact, because we need a lot of hidden factors to show up in the data. Then there is another problem, noise in data.

#### Noise in data

Noisy data is the norm in ML and it needs to be dealt with. Noise happens because our data will never be perfect. We rely on sensors to measure data, and our sensors aren't perfect. Electronic devices may generate errors, but also humans make errors. If a person collected data, they may have without realizing, made an error while writing down their data sheet. Luckily it doesn't represent a big problem if enough data is available. If our ML algorithm has enough data, the underlying patterns will eventually emerge, and the noise will simply be ignored.

#### Compression of knowledge with models

A cool thing about models (ML generated models) is that it enables us to compress knowledge. Take multiplication, for example, once you learned the rules of multiplication, you don't need to store the multiplication tables anymore. The same with coin tossing, once you know that there is a 50/50 chance of head or tail, you don't need to store the data of thousands of coin tosses, because you now have the coin model. This is how models help us compress knowledge.

#### Ambiguity of data is why expert systems failed

Expert systems are a type of systems which were very popular in the 80's, where humans designed logical system of rules to produce a certain outcome. In other words, a knowledge system is an inference engine which produces an output from an input. The data with which the knowledge system makes the inference is called a knowledge base (KB). For example, you may design a KB with the rule "hot phone = phone in usage or phone hit by the sunshine." The inference engine would infer that whenever you mention a hot phone, it would be due to two possible causes, either you used the phone or it is a sunny day and you left your phone somewhere where the sun shined on it.

#### Pattern recognition

Pattern recognition is the task of recognizing the patterns in data. Our brains are superb in this task. But it is hard if not impossible to design programs manually to do it. This is why the ML approach is used. Instead of describing in code how to distinguish the letter A from the letter B, we can program an algorithm which learns by itself how to distinguish different letters. Why is this necessary? Because not all fonts are the same, and not all handwritings are the same.
There is a nearly infinite number of ways people write, so we would need an infinitely big table of data to look up every possible variation of writing for our program to work. To prevent this, we have to generate a model which compresses that knowledge, imitating our brain. If you read the handwriting of a person you've never read before, this means your brain hasn't stored anything of that person's handwriting. But you can read his or her handwriting nonetheless. This is because your brain has a model of reading handwriting with which it can infer and get an accurate result.

#### Artificial Neuronal Networks

The most complex known pattern recognition device is the human brain, so it makes sense to try to learn how it works to imitate it with computers. But we don't want to make an exact copy of it, that would be hard and defy our purpose. We want to abstract the computational theory of how the brain works. An analogy explains this very nicely, the history of airplanes. Once, humans tried to fly imitating birds. They built and moved wings like birds do. Those experiments failed until someone discovered aerodynamics, the physics of how flight works. Once we knew something about aerodynamics, it wasn't necessary to imitate birds any longer. We just could build static wings and an engine with a prop which provided the propulsion.
We are somewhere at the bird-stage now with the brain. Trying to imitate its functionality by creating artificial neuronal networks. One of the earliest types of ANN's was the perceptron. The perceptron consists of a collection of artificial neurons and synaptic connections, where each neuron has an activation value. Neuron A can have an effect on neuron B through the artificial (similar to synapses of the brain) connection between them.
A very complex logic can be stored in a big collection of artificial neurons and synapses. They often are organized in multi-layer, which means there are multiple layers of neurons and synapses where the signal travels until, at the end, specific neurons get activated. Each subsequent neuron represents the total activations of each previous neuron. The last neurons represent the activations of the entire network. This is the output of the ANN.
So in a nutshell, an ANN computes an output from an input. So once we have the basic structure of an ANN, how can we store our model in it? This is what training is for.

#### Training ANN's

To get a specific result from an ANN, we need to make it learn something. Learning is called training. We need to train the network to do a certain task for it to be useful. If the neurons would just activate in a random order, that wouldn't be of much use. So by training, we introduce a program into the ANN.
The training modifies the likelihood of a neuron getting activated. If different neurons have different activation thresholds (weights), we get a pattern. When the network is sufficiently complex, very complex patterns can be stored in it.

#### Unsupervised learning

The previous examples were all examples of supervised learning. Supervised learning means that we know the input and the desired output, and we teach/train the network to accomplish the desired output. In case, of the coin tosses, we know that the output should have 50/50 probability. Unsupervised learning means that the algorithm (network) finds regularities in the data all by itself, without our intervention.
Finding regularities in data is very useful for classification. Say we want to classify items into different categories, but we don't exactly know what those categories are. Unsupervised learning allows us to work with the data without having the correct labels for the output. For example using once more the coin toss, we could just feed the network input data from coin tosses and tell it to find regularities (patterns) in it. Naturally, it would find two possible outcomes.
In the case of coin tosses, this finding isn't really something new for us. If we'd feed the network with dice tosses, it would tell us that there are 6 possible outcomes. Still not very interesting. But suppose we'd feed it with the entire browsing history of different people, and tell us to find regularities. Suddenly we would get completely new insights. The algorithm would probably show us that certain outcomes are disproportionally more common than others. In other words, some websites may get more visits from people in a certain country or during a certain day during the day. Something we wouldn't have guessed or known in advance.
As we see, unsupervised learning is very useful to discover new patterns.

#### Reinforcement learning

Reinforcement learning is fundamentally different from supervised and unsupervised learning discussed earlier. Reinforcement learning can be taught of as **learning with a critic as opposed to learning with a teacher** as in supervised learning. The difference between a critic and a teacher is that **a critic does not tell us what to do, but only how well we do**. And it tells us how well we do with a reward. Every time our algorithm does something which leads it closer to a specified goal, it gets a reward. The reward tells the algorithm that it should do what it just did more often, for example producing certain output for certain input.
The reward often does not come instantly and thus it is harder to learn from it than from a teacher. To better understand this concept let's go back to the coin toss example. If our algorithm produces 2 outputs with the probability of 20/80 and 30/70, it will get a reward in the second output, because it is closer to the goal of 50/50 chance. But the reward could also come much later, after 10 outputs for example. That would make it harder for the algorithm to adjust because now it would have to figure out the average of it's 10 outputs and compare it to the average of its previous 10 outputs. Thus it can take a long time for the algorithm to configure its network correctly so that it gets the highest reward, which in the case of coin tosses would be the 50/50 probability of getting heads or tails.

#### From here to the future

The application of machine learning is expected to only grow in the future. As computation power and data keeps rising exponentially, there will be an exponential growth in machine learning power, even without radical improvements in algorithms. Which is, of course, highly unlikely. In other words, there will be most likely many breakthroughs in Machine Learning and Artificial Intelligence in the near future, which raises many important questions. AI/ML is a power which can be used for good or bad. Then there are those people who worry that an advanced AI could rebel against humanity much like in the movies. One thing is for sure. Interesting things will happen.
Hope you liked this summary, it is the first one about Computer Science which is ironic, because I'm actually studying the subject.
[Get this amazing book](https://www.amazon.com/gp/product/0262529513/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=kasbl023-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=0262529513&linkId=41fce8caaed84b248e77e4596d914d97)

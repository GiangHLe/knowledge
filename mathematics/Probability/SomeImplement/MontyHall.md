# Monty Hall problem

The Monty Hall problem was so popular that was known by not even math lovers but also people in other field. However, it seems that not everyone understands that problem, or understands in wrong ways. This article will talk about:

[1. Where did Monty Hall problem come from?](#history) 
[2. How to image and link it with real life problem?](#another-point-of-view)
[3. How to understand it as mathematics ways?](#under-mathematics)

### History

So who is Monty Hall? 

He is a Canadian game show host. To be clear, the only connection between him and this article just his name and his career as the host of a game show named *"Let's Make a Deal"*.

The inventor of this problem named **Steve Selvin**, a statistician, he publish this problem to *"Scientific American"* - an American Popular science magazine, even **Einstein** had the articles on it.

Anyway, let go to the main point, what is this problem about?

<center>
<img src="./image/MontyHall1.png" alt="yolo" width="500">
<figcaption>
Fig 1. Monty Hall problem
</figcaption>
</center>


Look at the picture, image that you are in the game show, there are three door, behind those door are 2 goats and 1 car. Now, just choose a random door, then Monty will open one of the others two door and it will be the goat (let's assume that Monty know which door has the prize, and if the prize with you is the goat, just feel free to replace all the word "car" to goat and "goat" to "car" in this note). Then he will ask you "Be carefull, player. You wanna stay with your door number or go to the other door?", stop, and the problem here, swap or not?

Okay let's think about it, the first door you chose should have 33.33% is correct (1/3), but after that, when he opened the door, it will be ... wait for it ... 50%. After he open one door, there is only one door left, and the propability of the event the car will be behind that door should be 50%, right? Therefore, swap or not just depend on your luck.

Just kidding, the answer is you should swap for 66.66%, "thank you for that extra 33.33 percents" - One of my favourite gambling movie name "21", said by character named Ben. 

Just be honest, you might thing like the sentence above, right? That all the door have the same percentage even when one door was opened, in other scenario, think like you are at the game show, not in the math article. I know some people want to deny it, but at least I have to admit that I need a long time to find the answer which can satisfy my doubt about the correctness of that answer.

### Another point of view

For those people don't like mathematics, maybe this way of explaination can convince you.

Look around you, find two people have nearly similar body, same gender, image that they play chess together, who will win?

You do not know, right? So it should be 50%. Now, choose a random guy play with Magnus Carlsen (the world champion in chess at the time I am writting this article), who will win?

He will get the higher probability, why? Because you knew about him, or at least knew he is world champion with my information, and you still have a chance to beat him (even you don't know how to play chess), as [this video](https://www.youtube.com/watch?v=wofz0k6FCMU&ab_channel=ChessBaseIndia), he got a terrible stomachache before the game, so if just stay there and do nothing, you will win or play with your ability.

In conclusion, we can see the weight of information, the first case when you know nothing about those guys, the chance is 50-50, but the more information you have, the more percentage you can guess for the result. Back to Monty Hall, the first time you chose, you have no information, so it should be 1/3. However, after he opened other door, you knew that the other door which hadn't opened yet, beated the door that Monty opened. Therefore, it is the stronger door, the higher probability that door keep your new Porsche.

### Under mathematics

It is my pleasure when you read until this part, I just paraphase the answer from Mathematics forum in references, you can go in that link for more information.

Now, let assume we have $n$ doors, and Monty will open $k$ doors for us (I am not sure can we take the goat home or not).

First, just like normal, choose a door with probability is $\frac{1}{n}$ $\Rightarrow$ we will get the sample space of $k$ is $0 \le k \le (n-2)$, the door you chose and at least the last door for you switch).

Call A is the event that you get the car from first choice a door, $P(A)=\frac{1}{n}\Rightarrow P(\overline{A})=1-\frac{1}{n}=\frac{n-1}{n}$

Call B is the event that you get the car from the another choice after $k$ door opened, $P(B)=\frac{1}{n-k-1}$

Remember, the door you choose is in the rest $(n-1)$ door, so the propbability that you get the car if you swap is 

$P(\overline{A}B)=P(\overline{A})\times P(B)=\frac{n-1}{n} \times \frac{1}{n-k-1}=\frac{n-1}{n-k-1}\times\frac{1}{n}$

**Note here:** the event $\overline{A}$ and B is independent.

There is two cases:

1. **k=0**. There is no door opened, the probability will be $\frac{1}{n}$, equal with your choice.
2. **k>0**. The probability will be $\frac{n-1}{n-k-1}\times\frac{1}{n} \ge \frac{1}{n}$, so the more door opened, the higher chance you will get the prize.

Set k = 3 then it will be the original Monty Hall problem.

**Reference**
* [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall#Monty_Hall_problem)
* [Scientific American magazine](https://en.wikipedia.org/wiki/Scientific_American)
* [Explain mathematics 1](https://math.stackexchange.com/questions/2427446/monty-hall-multiple-prizes)
* [Explain mathematics 2](https://math.stackexchange.com/questions/608957/monty-hall-problem-extended)
* [Magnus Carlsen](https://en.wikipedia.org/wiki/World_Chess_Championship#:~:text=The%20current%20world%20champion%20is,which%20was%20won%20by%20Steinitz.)
* [Independent problem, focus on "one more example"](https://www.mathsisfun.com/data/probability-events-independent.html)
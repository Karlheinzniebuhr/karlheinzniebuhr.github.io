---
layout: post
title: "Software Testing: Preventing, Finding, and Fixing Bugs on a Time Budget - Raymond Hettinger"
date: 2018-09-21 14:12:12 +0000
categories: ["Tech-blog"]
tags: ["python", "technology", "programming", "software"]
---

Raymond Hettinger is one of the people I enjoy most giving tech talks. He is one of the people who know how to give very down to earth explanation about many complicated and fun topics. He also loves Python as I do, the difference being that he is a big contributor and bigger expert on Python. Definitely check out his talks on YouTube. In this post, I made some notes from his recent talk called [Keynote - Preventing, Finding, and Fixing Bugs On a Time Budget | Raymond Hettinger @ PyBay2018](https://www.youtube.com/watch?v=ARKbfWk4Xyw)

> What
> testing or debugging tools have the highest payoff for the time
> invested?

First,  select the tooling based on the kinds of problems you have.

Here
are some questions that will point you at the right direction.

- What is your error tolerance? For instance, an air-traffic control system is different than commenting logic on a blog.

- What kind of errors are typical for your application? If conflating data is a problem, static typing tools become more worthwhile.
- If you have to deal with lots of inputs, then automated input generation becomes worthwhile.

Some python tools Raymond finds really useful regarding testing:

## Doctest

Doctest
is good for testing documentation. It is so easy to use, you’d be a
fool not to use it. It teaches you how to use your own software. Once
you write a lot of software you might forget the patterns. That’s
where this tool helps, it help’s you to write persuasive code (code
that convinces you that it is correct).

## py.test

Py.test is good for thorough testing or unit testing. Py.test will save you typing compared to Python’s unit tests and we get paid for working software, not for writing tests. So we should only write tests that optimize that goal, not necessarily to cover 100% of our code.

## Static typing

Static
typing is included in the standard library. Using it improves code
clarity and helps improve documentation. It also helps write cleaner
APIs. Python however does not use static types, the principal tool to
check static types is mypy.

## PyFlakes

Takes 5
seconds to write the line. Unlike pylint, it is not opinionated, but
rather logical. Everything it tells you, is actually a bug.

## Hypothesis

A
library to annotate the relationships between inputs and outputs. The
library then generates test cases for you.

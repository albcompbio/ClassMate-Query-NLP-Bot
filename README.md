Project Description

This project is an interactive AI-powered chatbot that uses Natural Language Processing (NLP) to answer user questions based on previously trained examples. Instead of generating responses on its own, the bot relies on SpaCy’s semantic similarity engine to compare the meaning of a user’s question against a collection of stored questions in a SQLite database. The closest matching question determines the answer. Because of this design, the chatbot must be trained with a set of question–answer pairs before it can be used effectively.

Built with Flask for the web interface, SpaCy for vector-based NLP, and SQLite for lightweight local storage, the project demonstrates how traditional AI techniques can be applied to build a functional, customizable, and explainable question–answer system. It is ideal for learning how NLP similarity works and how to combine web development with basic AI.

Key Features

Semantic NLP matching using SpaCy’s vector model 

AI-driven similarity scoring instead of keyword or rule matching

Requires training with user-provided Q&A pairs, making it fully customizable

Stores all questions and answers locally in a SQLite database

Flask-based interface for chatting, training, and clearing data

Simple architecture that demonstrates the core concepts of NLP and AI

Explainable behavior—responses come from the closest matching stored question

Easy to extend or modify for school projects, demos, or personal use

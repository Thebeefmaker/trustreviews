# TrustReviews — AI-Verified Community Reviews

A decentralized review platform powered by GenLayer's Intelligent Contracts.

## What it does
Users submit reviews for any subject (product, service, person, business).
A GenLayer Intelligent Contract uses AI to verify whether each review is genuine or fake.
Only verified reviews are stored and displayed on-chain.

## How it works
1. User submits a review via the frontend
2. The Intelligent Contract sends the review to an AI prompt
3. AI returns a verdict: GENUINE or FAKE
4. Result is stored permanently on GenLayer

## Tech Stack
- **Smart Contract:** Python (GenLayer Intelligent Contract)
- **Frontend:** HTML/CSS/JS hosted on GitHub Pages
- **AI Layer:** GenLayer's `gl.exec_prompt()`

## Live App
[View on GitHub Pages](https://YOUR_USERNAME.github.io/trustreviews)

## Contract
Deploy `contract.py` on [GenLayer Studio](https://studio.genlayer.com)
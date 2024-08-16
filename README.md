# CS 3200 Summer 2 2024 Final Project

## About

This is BarkFontenot's Team project called PetFetch! PetFetch is a Petalytics application that allows you to view pets and agencies around the area. 

## Elevator Pitch: 
Our goal is to centralize animal rescue data to expand the reach of animal rescues and streamline adoption processes. We want to provide stray, abandoned, and unwanted animals a home, and we want to reduce the amount of kill-shelters. Our intended users consist of employees of animal shelters, individuals looking to adopt or foster pets, individuals looking to put pets up for adoption, and researches who want to use the data our application provides (i.e. government agency trying to figure out which states have high rates of animals being put down before successful adoption).
A sampling of the expected major functionality would consist of search and filtering functionality for animals, updating and creating data for animals, displaying animal health and medical condition/history, and rescue/adoption statistics for each agency.

## Current Project Components

Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- MySQL setup files (in the `./database-files` directory)

## Getting Started
1. Clone the repo to your computer. 
2. Set up the `.env` file in the `api` folder based on the `.env.template` file.
    - To set up `.env` file, please copy and paste the `.env.template` file and rename it `.env`.
3. Start the docker containers using `docker compose up -d` in the terminal. 
4. Access the application with `http://localhost:8501/` on your web browser. 

## Handling User Role Access and Control

When a user logs in, they assume a particular role, each representing a user persona with user stories. 
## Roles and Stories: 
1. Clark: A Potential Adopter
    1. Filter pets based on species, breed, and age, and view pet data and contact information
    2. View Pet Medical History
    3. Find the closest rescue agencies
2. Janet: An Emergency Rescue Manager
    1. Add a new entry to a desired pet's medical history
    2. Edit pet data (put a pet up for adoption, update pet information, delete a pet from the database)
    3. View adoption data of pets (pets, adoption status, adoption date, adopter info)
3. Alex: A Pet Researcher
    1. View and rank total adoptions by agency
    2. Show pets that have not yet been adopted and find which ones have less interest from adopters
    3. View which animal breeds and species are surrendered to resuces the most
 

## Demo Video
https://drive.google.com/file/d/1ifplvoxzd6ubxiZXfNzNjqlvsdGYvV9h/view

## Barkfontenot Members
Caroline Pham
Haylie Pedersen
Andrew Nee
Bryce Mottershead
Junxiang Lin
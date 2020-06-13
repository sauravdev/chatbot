## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## hello world path
* hello_world
  - utter_hello_world

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## website info path
* more_info
  - utter_info

## default fallback story
* bot_challenge
  - action_default_fallback


## path 2
* gr
  - utter_greet
* good
  - utter_askquestion
* question{"document":"Big Data"}
  - slot{"document":"Big Data"}
* sendemail
  - utter_email
* ask_email{"email": "beingdatum@gmail.com"}
  - slot{"email": "beingdatum@gmail.com"}
  - action_send_email
  - utter_confirm_email

## path 3
* question{"document":"Big Data"}
  - slot{"document":"Big Data"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* gr
  - utter_greet
* good
  - utter_askquestion
* question{"document":"Big data Class"}
  - slot{"document":"Big data Class"}
  - action_question
* question{"document":"getting started"}
  - slot{"document":"getting started"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email


## New Story
* gr
  - utter_greet
* good
  - utter_askquestion
* question{"document":"Data Science"}
  - slot{"document":"Data Science"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* gr
  - utter_greet
* good
  - utter_askquestion
* question{"document":"getting started"}
  - slot{"document":"getting started"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* gr
  - utter_greet
* good
  - utter_askquestion
* question{"document":"kafka"}
  - slot{"document":"kafka"}
  - action_question
* question{"document":"hive"}
  - slot{"document":"hive"}
  - slot{"document":"kafka"}
  - action_question
* question{"document":"data science"}
  - slot{"document":"data science"}
  - slot{"document":"hive"}
  - slot{"document":"kafka"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* gr
  - utter_greet
* good
  - utter_askquestion
* question{"document":"Data Science"}
  - slot{"document":"Data science"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"Glossary"}
  - slot{"document":"Glossary"}
  - action_question
* question{"document":"Kafka"}
  - slot{"document":"Kafka"}
  - action_question
* question{"document":"getting started"}
  - slot{"document":"getting started"}
  - action_question
* question{"document":"Big Data"}
  - slot{"document":"Big Data"}
  - action_question
* question{"document":"Factlab"}
  - slot{"document":"Factlab"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"ooz"}
  - slot{"document":"ooz"}
  - action_question
* question{"document":"final"}
  - slot{"document":"final"}
  - action_question
* question{"document":"final"}
  - slot{"document":"final"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* gr
  - utter_greet
* good
  - utter_askquestion
* question{"document":"big data"}
  - slot{"document":"big data"}
  - action_question
* question{"document":"factlabs"}
  - slot{"document":"factlabs"}
  - action_question
* question{"document":"data science"}
  - slot{"document":"data science"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* question{"document":"big data"}
  - slot{"document":"big data"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* greet
  - utter_greet
* good
  - utter_askquestion
* question{"document":"big data"}
  - slot{"document":"big data"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* question{"document":"hive optimizations"}
  - slot{"document":"hive optimizations"}
  - action_question
* question{"document":"hive"}
  - slot{"document":"hive"}
  - action_question
* question{"document":"hive optimization"}
  - slot{"document":"hive optimization"}
  - action_question
* question{"document":"Hive Otimization"}
  - slot{"document":"Hive Otimization"}
  - action_question
* question{"document":"Hive Optimization"}
  - slot{"document":"Hive Optimization"}
  - action_question
* question{"document":"Hive Optimization"}
  - slot{"document":"Hive Optimization"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email

## New Story
* greet
  - utter_greet
* good
  - utter_askquestion
* question{"document":"hive documents"}
  - slot{"document":"hive documents"}
  - action_question
* sendemail
  - utter_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email




## introductory
* hgreet
    - utter_greets
* topic_wise
    - utter_topic
* introductory
    - action_introductory

## machine_learning
* hgreet
   - utter_greets
* topic_wise
  - utter_topic
* introductory
  - action_machine_learning
* question{"document":"Data Science"}
  - slot{"document":"Data science"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"Glossary"}
  - slot{"document":"Glossary"}
  - action_question
* question{"document":"Kafka"}
  - slot{"document":"Kafka"}
  - action_question
* question{"document":"getting started"}
  - slot{"document":"getting started"}
  - action_question
* question{"document":"Big Data"}
  - slot{"document":"Big Data"}
  - action_question
* question{"document":"Factlab"}
  - slot{"document":"Factlab"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"ooz"}
  - slot{"document":"ooz"}
  - action_question
* question{"document":"final"}
  - slot{"document":"final"}
  - action_question
* question{"document":"final"}
  - slot{"document":"final"}
  - action_question

## deep_learning
* hgreet
  - utter_greets
* topic_wise
  - utter_topic
* deep_learning
  - action_deep_learning
* question{"document":"Spark"}
  - slot{"document":"Spark"}
  - action_question
* question{"document":"Data Science"}
  - slot{"document":"Data science"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"Glossary"}
  - slot{"document":"Glossary"}
  - action_question
* question{"document":"Kafka"}
  - slot{"document":"Kafka"}
  - action_question
* question{"document":"getting started"}
  - slot{"document":"getting started"}
  - action_question
* question{"document":"Big Data"}
  - slot{"document":"Big Data"}
  - action_question
* question{"document":"Factlab"}
  - slot{"document":"Factlab"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"ooz"}
  - slot{"document":"ooz"}
  - action_question
* question{"document":"final"}
  - slot{"document":"final"}
  - action_question
* question{"document":"final"}
  - slot{"document":"final"}
  - action_question


## search_topic:
* hgreet
  - utter_greets
* search_topic
  - utter_askquestion
* question{"document":"Data Science"}
  - slot{"document":"Data science"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"Glossary"}
  - slot{"document":"Glossary"}
  - action_question
* question{"document":"Kafka"}
  - slot{"document":"Kafka"}
  - action_question
* question{"document":"getting started"}
  - slot{"document":"getting started"}
  - action_question
* question{"document":"Big Data"}
  - slot{"document":"Big Data"}
  - action_question
* question{"document":"Factlab"}
  - slot{"document":"Factlab"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"ooz"}
  - slot{"document":"ooz"}
  - action_question
* question{"document":"final"}
  - slot{"document":"final"}
  - action_question
* question{"document":"final"}
  - slot{"document":"final"}
  - action_question
* question{"document":"Glossary"}
  - slot{"document":"Glossary"}
  - action_question
* question{"document":"Kafka"}
  - slot{"document":"Kafka"}
  - action_question
* question{"document":"getting started"}
  - slot{"document":"getting started"}
  - action_question
* question{"document":"Big Data"}
  - slot{"document":"Big Data"}
  - action_question
* question{"document":"Factlab"}
  - slot{"document":"Factlab"}
  - action_question
* question{"document":"Hive"}
  - slot{"document":"Hive"}
  - action_question
* question{"document":"ooz"}
  - slot{"document":"ooz"}
  - action_question
* question{"document":"data science"}
  - slot{"document":"data science"}
  - action_question
* question{"document":"Big data Class"}
  - slot{"document":"Big data Class"}
  - action_question

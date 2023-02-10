# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Fahim Kamal

## Lab Question Answers

Answer for Question 1: 
RESTful APIs are scalable because they are optimized
to reduce the size of communication between servers and clients. This is because
REST APIs are stateless which means that the server does not have to hold 
client information to further process a client's request. In addition, caching
allows the number of request/responses to be reduced. This will minimize 
communication slowdowns, allowing APIs to be scalable.

Question 2: According to the definition of “resources” provided in the AWS article above,
What are the resources the mail server is providing to clients?
According to the AWS article, resources are pieces of information provided to clients.
The resources the mail server is providing to clients are mail and meta-data about the 
mail, including a sender, receiver, subject, and mail_id. 


Question 3: What is one common REST Method not used in our mail server? How could
we extend our mail server to use this method?
One common REST Method ont used in our mail server is PUT which is used to update
existing resources on the server. We could extend our mail server to include this
method by creating a put_mail function that takes a mail_id and a JSON object that
represents the changed resource. This function would be similar in implemetation
to the add_mail function, except it wouldn't generate a new mail_id. We would then
create a route for the PUT method on the mail_id endpoint.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!
API keys are used to provide authorization for users or projects. This allows
the API provider to track how their API is being used to protect against abuse
or malicious users. (https://www.fortinet.com/resources/cyberglossary/api-key)

...
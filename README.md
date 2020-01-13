## Coding Challenge ##

I went for Python - Flask for this challenge due to a Flask is a light and micro web framework ideal for prototyping and single page application as opposed to Django which is more suitable for heavy work and admin panel feature in the app.

In this challenge, I have created the independent Backend applicatioon, "words.py", which can be tested as on its own. If you would like to see if it is working, two changes need to be made which is the headers (line 4) and (line 23):-


* Line 4, headers value needs to be your user agent value which can be found by typing "my user agent" on google.

* line 23: please change to the following code as shown below to run the code.
```
for word in words[:100]:
```

And the both frontend (templates -> index.html) and backend (app.py) code can be found on this repository.
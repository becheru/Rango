import os

def populate():
    python_pages = [
         {"title": "Official Python Tutorial",
          "url":"http://docs.python.org/2/tutorial/"},
         {"title":"How to Think like a Computer Scientist",
          "url":"http://www.greenteapress.com/thinkpython/"},
         {"title":"Learn Python in 10 Minutes",
          "url":"http://www.korokithakis.net/tutorials/python/"} ]

    django_pages = [
         {"title":"Official Django Tutorial",
          "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
         {"title":"Django Rocks",
          "url":"http://www.djangorocks.com/"},
         {"title":"How to Tango with Django",
          "url":"http://www.tangowithdjango.com/"} ]

    other_pages = [
         {"title":"Bottle",
          "url":"http://bottlepy.org/docs/dev/"},
         {"title":"Flask",
          "url":"http://flask.pocoo.org"} ]

    cats =  { "Python": {"pages": python_pages},
             "Django": {"pages": django_pages},
             "Other Frameworks": {"pages": other_pages}
            }

    for cat, cat_data in cats.items():
        print(cat, data_data)
        #for p in cat_data["pages"]:
        #    print(p["title"],p["url"])

populate()

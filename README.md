# MelbDjango School - Lesson Two

The slides from the class are available online here:  
https://melbdjango.github.io/lesson-two/

**Important:** Please take the [survey](https://docs.google.com/a/acommoncreative.com/forms/d/1VKqD1-aVsgztk19kdluNtFyTGiarbV9LgBFi2BwYT-g/viewform?c=0&w=1) if you came to the class today.


## Homework Checklist

If you did the homework [last week][lesson-one], you should already have a virtualenv that you can use this week.

- [X] [Fork this repository][gh-fork]
- [X] Clone the repo to your own machine
- [X] Normalise the model we created in class by creating new [Django models][dj-models] that better express the
      relationships. You'll need to add [ForeignKey relationships][dj-fk] between your models and our existing one.
- [X] Update `admin.py` so all your new models show
- [X] Bonus Points: Use [Django's migrations][dj-migrations] in a way that allows us to keep existing data in our model

When you've completed some or all of the homework please make a [Pull Request][gh-pr] against this repository.
If you submit your work before Wednesday evening we'll give you feedback before the next class.



## Displaying the class slides

Install reveal-md with npm and use that to display the class slides.

```
    npm install -g reveal-md

    cd slides
    reveal-md CLASS.md --theme melbdjango
```

[gh-fork]: https://help.github.com/articles/fork-a-repo/
[lesson-one]: https://github.com/melbdjango/lesson-one/
[dj-models]: https://docs.djangoproject.com/en/1.8/topics/db/models/
[dj-fk]: https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey
[gh-pr]: https://help.github.com/articles/using-pull-requests/
[dj-migrations]: https://docs.djangoproject.com/en/1.8/topics/migrations/

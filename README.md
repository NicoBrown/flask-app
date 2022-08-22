<h1 align="center">Flask Test Project</h1>
<p align="center">Note: This project is just demonstrating some backend development, Ive put no effort into the styling other than the bootstrap template</p>

<p align="center">https://nicobrown-flask-app.herokuapp.com/</p>

![image](https://user-images.githubusercontent.com/69271605/185942137-44877275-e04d-4b8e-ae35-7bb44fb6f1c3.png)

### Minimal blog using flask,python and a bootstrap theme 

Started with a code institute template and launched in Gitpod, contains some jinja templating
<hr>

### The careers page includes json data parsed from a file within the repository:

![image](https://user-images.githubusercontent.com/69271605/185999078-63db0625-cc05-4159-bf1d-288d60887b2f.png)

## Bugs

Heroku failed to deploy the app due to this error:
```
022-08-22T20:22:48.565550+00:00 app[web.1]:     from jinja2 import escape
2022-08-22T20:22:48.565570+00:00 app[web.1]: ImportError: cannot import name 'escape' from 'jinja2' (/app/.heroku/python/lib/python3.10/site-packages/jinja2/__init__.py)
2022-08-22T20:24:10.000000+00:00 app[api]: Build started by user n.brown2017@outlook.com
2022-08-22T20:24:26.000000+00:00 app[api]: Build failed -- check your build output: https://dashboard.heroku.com/apps/3fd68bdc-5605-42a1-a929-24141e7a87bc/activity/builds/f6e45d45-3a53-4136-81e6-fc6923b4af9d
```
updated requirements.txt as per https://stackoverflow.com/a/71735103

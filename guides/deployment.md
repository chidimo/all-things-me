# Deployment guides

## `React` App on Heroku

### Resources

1. <https://blog.heroku.com/deploying-react-with-zero-configuration>
1. <https://medium.com/jeremy-gottfrieds-tech-blog/tutorial-how-to-deploy-a-production-react-app-to-heroku-c4831dfcfa08>

1. heroku create <app_name> -b https://github.com/mars/create-react-app-buildpack.git
1. git push heroku master
1. heroku open

## `Meteor` App on Heroku

### Resources

1. <https://medium.com/@leonardykris/how-to-run-a-meteor-js-application-on-heroku-in-10-steps-7aceb12de234>
1. <https://medium.com/@philipaffulnunoo/how-to-deploy-meteor-1-4-app-to-aws-ec2-in-2017-bfea1a7c308a>
1. <https://medium.com/@levente.balogh/deploy-meteor-with-docker-4d251e7916fe>

1. Download and install heroku cli
1. `heroku login`
1. `heroku apps:create <desired app name>`
1. `heroku buildpacks:set https://github.com/AdmitHub/meteor-buildpack-horse.git # add a buildpack`
1. `heroku addons:create mongolab:sandbox # for mongodb database. This step requires you verify your heroku account by adding a credit card`
1. `heroku config # display all my configuration variables`
1. With `heroku config` I see a configuration variable `MONGODB_URI: mongodb://heroku_jblmfbx1:41hufrlg8a3oet55e063f35jte@ds225294.mlab.com:25294/heroku_jblmfbx1`
1. `heroku config:add MONGO_URL=mongodb://heroku_jblmfbx1:41hufrlg8a3oet55e063f35jte@ds225294.mlab.com:25294/heroku_jblmfbx1`
1. `heroku config:add ROOT_URL=https://<desired app name>.herokuapp.com`
1. `git push heroku master`


## `Django` App on Heroku

### Resources

1. <https://devcenter.heroku.com/categories/working-with-django>
1. <https://gearheart.io/blog/how-to-deploy-a-django-application-on-heroku/>

1. Heroku automatically detects `Pipfile` and `Pipfile.lock` and installs dependencies from them.
1. `heroku create <app name>`
1. Create `Procfile` and enter `web: gunicorn <project name>.wsgi` where `wsgi.py` is the `wsgi` file to be used in running the app.
1. Specify the settings you want to run in production inside the `wsgi` settings file.
1. Install and configure `whitenoise` as instructed <http://whitenoise.evans.io/en/stable/django.html>
1. Set up the database using [`dj-database-url`](https://github.com/kennethreitz/dj-database-url)
1. Disable collectstatic with `heroku config:set DISABLE_COLLECTSTATIC=1`
1. Run collectstatic with production settings using `heroku run python manage.py collectstatic --noinput --settings=appname.settings.prod`
1. Run `heroku run python manage.py migrate --settings=appname.settings.prod`

## `Django` App on Pythonanywhere

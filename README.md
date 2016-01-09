# Next Meetup plugin for Pelican

[Pelican](https://github.com/getpelican/pelican) plugin to retrieve information about your group's next meetup by calling [Meetup.com](http://www.meetup.com/) API.



## Install

Run `pip install pelican-next-meetup`, then add `next_meetup` to `pelicanconf.py` configuration's`PLUGINS` list:

``` python
PLUGINS = [
    # all other plugins
    'next_meetup',
]
```

## Set it up

For plugin to call the Meetup.com API, a valid meetup group's URL must be specified in `pelicanconf.py`, such as:

```python
MEETUP_URL = 'python-lv'
```

Plugin will fetch the data of the first upcoming meetup and store data to `next_meetup` variable for use in templates. If code other than HTTO `200 OK` is returned, an exception will be raised by [requests](https://github.com/kennethreitz/requests) library.

Example of data returned:

```javascript
{
  'time': 1452704400000,
  'url': 'http://www.meetup.com/python-lv/events/227548959/',
  'utc_offset': 7200000,
  'name': 'Months 1st #PyNight'
}
```

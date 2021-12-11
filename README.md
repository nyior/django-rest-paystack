<h1 align="center">
	django-rest-paystack: a minimal SDK for integrating Paystack into your django-rest API backend.
</h1>

<p align="center">
	<i>
        Focus on your business logic. Leave all the mundane payment serere to us.
        Our package will do all the heavy lifting for you :D
    </i>
</p>


## what is django-rest-paystack?
some write up here

#### overview
some write up here...

#### Features
    - feature 1
    - feature 2


## How do I use this package in my project?

#### Quick Setup

Install package

    pip install dj-rest-auth
    
Add `paystack` app to INSTALLED_APPS in your django settings.py:

```python
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'paystack'
)
```
    
Add URL patterns

```python
urlpatterns = [
    path('paystack/', include('paystack.urls')),
]
```

Declaring Environment Variables in a .env file

```python
# the below environment variables must be added to your .env file

PAYSTACK_PUBLIC_KEY=18be1670999999999999999
PAYSTACK_PRIVATE_KEY=11d54fbd95a0100000000000000

```

#### Paying for an order
If you like this repo, click the :star:


## Oh okay, I gerrit. Thank you Nyior
You're welcome. If you like this repo, click the :star: I'd appreciate that.


## TODO:
* Add split payments feature
* Enable transfers
* Enable subscription based(recurring) payments
* Make tests more encompassing


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements


## License
[MIT](https://choosealicense.com/licenses/mit/)

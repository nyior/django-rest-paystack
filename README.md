<h1 align="center">
	django-rest-paystack: a minimal SDK for integrating Paystack into your django-rest API backend.
</h1>

<p align="center">
	<small>
        Focus on your business logic. Leave all the mundane payment serere to us.
        Our package will do all the heavy lifting for you :D
    </small>
</p>


## what is django-rest-paystack?

### overview
Creating those payment endpoints for every single e-commerce project we work on could become
brutally redundant and perharps somewhat boring overtime. While there are different approaches to integrating and processing payments with a gateway like Paystack(more on this later), in each approach, the flow doesn't really change. If it doesn't change then why repeat yourself? 

    DRY: Enter django-rest-paystack.
        when installed and configured, this package generates all the endpoints you'd need to start and
        complete a transaction. 

### Endpoints
* initialize a transaction: ```POST /api/v1/paystack/transaction/initiate```
        minimal_payload = {
            "amount": 0,
            "email": "string",
        }
* verify a transaction:  ```GET /api/v1/paystack/transaction/verify/?transaction_ref="ref"```
* Get user authorization code: ```GET /api/v1/paystack/paystack-customer/{user__id}/```
* charge an authorization: ``` POST /api/v1/paystack/transaction/charge-customer```
        minimal_payload = {
            "amount": 0,
            "email": "string",
            "authorization_code": "string",
        }
* handle webhooks: ``` api/v1/paystack/webook-handler```
* get all transactions: ```/api/v1/paystack/transaction```
* retrieve a single transaction: ```/api/v1/paystack/transaction/{uuid}```
* the package also logs some relevant data to the db(e.g transaction log, authorization code)

If you're not very familiar with how some of those endpoints work, don't worry, I will get to that in a bit.


## How do I use this package in my project?

### Quick Setup

Install package

    pip install paystack
    
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

### Paying for an order
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
In building this, I found the following repositories really helpful
* [laravel-paystack](https://github.com/unicodeveloper/laravel-paystack)
* [popoola/pypaystack](https://github.com/edwardpopoola/pypaystack)
* [gbozee/pypaystack](https://github.com/gbozee/pypaystack)

## License
This project is released under the [MIT](https://choosealicense.com/licenses/mit/) License

# Tuesday take home test

## Running tests
Tests must be run from the `src` folder using the command `python -m pytest ../test`

## Candidate Brief

The task is to build a service that will combine data from existing product, price and reductions endpoints into a new product details API. The contracts for the product, stock and reductions endpoints are found in `external_API_contracts.yaml`.


### Instructions

1. Using the product, price, and reductions APIs build a service that returns the full product details including the price and reductions in a structure of your choice
    1. For each product sku you will need to get the price and find any applicable reductions
    2. Using UK as your timezone make sure you only apply discounts that are available now
    3. Only apply reductions that are applicable `ONLINE` and in GBP
    4. Reductions can be by amount, percentage or qualified. Ignore qualified reductions
    5. If there are more than 1 applicable amount(s) and/or percentage(s) reductions, only apply the single greatest reduction
2. Each API can return errors. If there are any errors treat the whole request as an error but make clear in the response where the source of the error was
3. Write a data contract in swagger for the output of your service
### Test data and API access

Using https://interview-tech-testing.herokuapp.com/product-details/ as the base URL, you can use product ids: p22245233, p60107258, p60111867, p60206457 for testing. (These contain the SKUs required to hit the other APIs)

**All endpoints require basic auth with the username: admin and password: password**

### Other Requirements
- The code you submit must build and run. Please include any setup instructions you feel would be helpful
- Use Python for the backend, using the provided template
- Complete the Dockerfile
- If you don't complete all the tasks please include a readme describing the steps you would need to take to finish.

### How to submit
To submit, fork this repository to your own github account and create a pull request using `msventurelabs/tuesday-take-home` as the base repository
If you don't complete all the tasks please include a readme describing the steps you would need to take to finish.
# E-commerce API

# About

### This is E-commerce API<br/>

### In this Api we can register user, login user with JWT,reset-password by sending otp, add product, retrieve product by different category functionality<br/>

# Description

In this API there are 11 endpoints

# GET requests

# url

'/users' is for list of users

# Response

```json
[
  {
    "email": "firstemail@gmail.com",
    "username": "Shiyaan",
    "firstname": "Shiyaan",
    "lastname": "Showkat",
    "address": {
      "city": "Srinagar",
      "street": "Zaina Kadal",
      "number": 123,
      "zipcode": "190002"
    },
    "phone": 123456
  },
  {
    "email": "secondemail@gmail.com",
    "username": "Abrar",
    "firstname": "Abrar",
    "lastname": "Showkat",
    "address": {
      "city": "Srinagar",
      "street": "Zaina Kadal",
      "number": 1245,
      "zipcode": "19002"
    },
    "phone": 12345
  },
  {
    "email": "thirdemail@yahoo.com",
    "username": "Jibby",
    "firstname": null,
    "lastname": null,
    "address": {
      "city": "Srinagar",
      "street": "zain kadla",
      "number": null,
      "zipcode": null
    },
    "phone": 0
  }
]
```

# url

'user/<user_id>' is for getting particular user details

params{

pk

}

# Response

```json
{
  "email": "shiyaan@gmail.com",
  "username": "Shiyaan",
  "firstname": "Shiyaan",
  "lastname": "Showkat",
  "address": {
    "city": "Srinagar",
    "street": "Zaina Kadal",
    "number": 123,
    "zipcode": "190002"
  },
  "phone": 123456
}
```

# url

'products/category/<product_category>' is for getting products of particular category

params{

category

}

# Response

```json
[
  {
    "product_name": "Samsung",
    "product_price": 1234.67,
    "product_description": "This Mobile Phone is best",
    "product_image": null
  },
  {
    "product_name": "Mobile Phone",
    "product_price": 1234.4,
    "product_description": "This is best phone",
    "product_image": null
  }
]
```

# url

'product/<product_id>' is for getting particular product details

params{

    pk

}

# Response

```json
{
  "product_name": "Samsung",
  "product_price": 1234.67,
  "product_description": "This Mobile Phone is best",
  "product_image": null
}
```

# POST,PUT,DELETE requests

# url

'users/register' is for creating user

# Method POST

```json
{
  "email": "jibranjibby2@gmail.com",
  "username": "Abrar",
  "firstname": "Abrar", //optional field
  "lastname": "Showkat", //optional field
  "address": {
    "city": "Srinagar",
    "street": "Zaina Kadal",
    "number": 1245, //optiona field
    "zipcode": "19002" //optional field
  },
  "phone": 12345 //optional field
}
```

# Response

```json
{
  "message": "user created successfully"
}
```

# url

'users/<user_id>'

params{

pk

}

# Method PUT for updating user detail

```json
{
  "email": "jibranjibby2@gmail.com",
  "username": "Abrar",
  "firstname": "Abrar", //optional field
  "lastname": "Showkat", //optional field
  "address": {
    "city": "Srinagar",
    "street": "Zaina Kadal",
    "number": 1245, //optiona field
    "zipcode": "19002" //optional field
  },
  "phone": 12345 //optional field
}
```

# Response

```json
{
  "email": "updated email",
  "username": "upated username",
  "firstname": "updated firstname", //optional field
  "lastname": "updated lastname", //optional field
  "address": {
    "city": "updated city",
    "street": "updated street",
    "number": "updated number", //optiona field
    "zipcode": "updated zipcode" //optional field
  },
  "phone": 1 //optional field
}
```

# url

'users/<user_id>'

params
{

pk

}

# Method DELETE for deleting a particular user

# Response

```json
{ "message": "User deleted successfully" }
```

# url

'users/forgot_password' is for reset password

# Method POST for checking email if it exists and creating otp

```json
{
  "email": "abrar@yahoo.com"
}
```

# Response

```json
{
  "message": "opt has been sent to the email"
}
```

# Then change your method to PUT for setting new password for the user if otp matches

```json
{
  "otp": 12345, //example
  "password": "new_password",
  "password2": "new_password2"
}
```

# Response

```json
{
  "message": "Password changed succesfully"
}
```

# url

'products/create' for creating product

# Method POST

```json
{
  "product_name": "Washing Machine",
  "product_price": 23456,
  "product_description": "This Washing Machine is best machine in the world",
  "product_category": 3 //category id
}
```

# Response

```json
{
  "message": "Product has been added successfully"
}
```

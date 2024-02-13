# i_recipe_api Manual Testing

A series of manual tests were made and will be described in this document. Each app and its functionality where tested and a print-screen image where taken to document each step.
Tests where performed using DRF HTML interface running on a test server.

## Authentication and Registration Tests

#### test 1
when attempting to register and create a new profile:
- "testUser1" was created successfully.

**Result: PASS**

<p align="center">
    <img src="readme_images/authentication-registration-tests/register_new_user_successful.png" width=800>
</p>

#### test 2
when attempting to register with an existing username:
- Message: "A user with that username already exist" was displayed successfully.

**Result: PASS**

<p align="center">
    <img src="readme_images/authentication-registration-tests/registration_username_already_exist.png" width=800>
</p>

#### test 3
When attempting to register and the password fields don't match:
- Message: "The two password fields didn't match".

**Result: PASS**

<p align="center">
    <img src="readme_images/authentication-registration-tests/register_atempt_password_dont_match.png" width=800>
</p>

#### test 4
When attempting to login new user:
- Login successful.

**Result: PASS**

<p align="center">
    <img src="readme_images/authentication-registration-tests/login_newuser_successful.png" width=800>
</p>

#### test 5 
When attempting to login with wrong credentials:
- message: "Unable to login with provided credentials".
- login failed.

**Result: PASS**

<p align="center">
    <img src="readme_images/authentication-registration-tests/wrong_credentials_atempt.png" width=800>
</p>

#### test 6
When attempting to change the password:
- message: "new password has been saved"
- change password successful

**Result: PASS**

<p align="center">
    <img src="readme_images/authentication-registration-tests/password_change_attempt_successful.png" width=800>
</p>

## Category

#### test 1

When attempting to list all categories:
- list successful

**Result: PASS**

<p align="center">
    <img src="readme_images/category_list_deatail/category_list.png" width=800>
</p>

#### test 2

when attempting to create a new category:
- category created successfully:

**Result: PASS**

<p align="center">
    <img src="readme_images/category_list_deatail/category_creat_new_successful.png" width=800>
</p>

#### test 3

when attempting to perform create, update, delete without admin credentials:
- message: "you do not have permission to perform this action"
- credential restriction successful

**Result: PASS**

<p align="center">
    <img src="readme_images/category_list_deatail/category_only_admin_permission.png" width=800>
</p>

#### test 4

when attempting to create a category with an existing name:
- message: "category with this name already exists"
- unique: True; "successful"

**Result: PASS**

<p align="center">
    <img src="readme_images/category_list_deatail/category_unique.png" width=800>
</p>

#### test 5
when attempting to update a category name:
category name updated successfully:

**Result: PASS**

<p align="center">
    <img src="readme_images/category_list_deatail/category_update_successful.png" width=800>
</p>

#### test 6 
when attempting to delete an existing category:
category deleted successfully:

**Result: PASS**

<p align="center">
    <img src="readme_images/category_list_deatail/category_delete_successful.png" width=800>
</p>

## Conversation

#### test 1

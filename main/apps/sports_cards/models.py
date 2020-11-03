from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be two characters long"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be two characters long"
        if len(postData["email"]) < 1:
            errors["email"] = "Email cannot be blank"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter valid email"
        #dont do if len(postData["email"]) < 8
        if len(postData["password"]) < 8:
            errors["password"] = "password must be atleast 8 characters long"
        elif postData["password"] != postData["confirm_password"]:
            errors["password"] = "Passwords do not match."

        result = User.objects.filter(email=postData['email'])
        #use .filter over .get if you dont know what the query result will be
        if result:
            errors['email'] = "Email name already in use "

        
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    #connects to class UserManager

class CardManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["year"]) < 3 :
            errors["year"] = "Year must be 4 digits"
        if len(postData["make"]) < 5:
            errors["make"] = "Please enter correct make of card"
        if len(postData["card_number"]) < 1:
            errors["card_number"] = "Please enter correct card number"
        if len(postData["name"]) < 4:
            errors["name"] = "Player name must be at least 4 characters"
        if len(postData["special"]) < 3:
            errors["special"] = "Card special must be at least 3 characters"

        
        return errors

class Cards(models.Model):
    year = models.IntegerField() 
    make = models.CharField(max_length=255)
    card_number = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    special = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="has_cards", on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="has_likes")

    objects = CardManager()


class ReviewManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["content"]) < 10 :
            errors["review"] = "Review must be at least 10 charachters long"
        if len(postData["rating"]) == 0 :
            errors["rating"] = "Select a rating number"

        
        return errors

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewed_by = models.ForeignKey(User, related_name="has_reviews", on_delete=models.CASCADE)
    cards = models.ForeignKey(Cards, related_name="has_reviews", on_delete=models.CASCADE)

    objects = ReviewManager()




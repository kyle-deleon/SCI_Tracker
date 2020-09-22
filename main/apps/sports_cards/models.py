from django.db import models

class User(models.Model):
    first_name = models.Charfield(max_length=255)
    last_name = models.Charfield(max_length=255)
    email = models.Charfield(max_length=255)
    password = models.Charfield(max_length=255)
    user_name = models.Charfield(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cards(models.Model):
    year = models.DecimalField() 
    make = models.Charfield(max_length=255)
    card_number = models.DecimalField()
    name = models.Charfield(max_length=255)
    special = models.Charfield(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="has_cards", on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="has_likes")

class Review(models.Model):
    content = models.TextField()
    rating = models.IntergerField(min=1,max=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewed_by = models.ForeignKey(User, related_name="has_reviews", on_delete=models.CASCADE)
    cards = models.ForeignKey(Cards, related_name="has_reviews", on_delete=models.CASCADE)




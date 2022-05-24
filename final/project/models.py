from django.db import models

# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class BookManager(models.Manager):
    def create_user(self, name, price, description, **extra_fields):
        if not name:
            raise ValueError('The given username must be set')
        user = self.model(name=name, price=price, description=description, **extra_fields)
        user.save(using=self._db)
        return user

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)

    objects = BookManager()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'created_at': self.created_at,
            'num_pages': self.num_pages,
            'genre': self.genre
        }


class JournalManager(models.Manager):
    def create_user(self, name, price, description, **extra_fields):
        if not name:
            raise ValueError('The given username must be set')
        user = self.model(name=name, price=price, description=description, **extra_fields)
        user.save(using=self._db)
        return user

class Journal(BookJournalBase):
    BULLET = "B"
    FOOD = "F"
    TRAVEL = "T"
    SPORT = "S"

    JOURNAL_CHOICES = (
        (BULLET, "Bullet"),
        (FOOD, "Food"),
        (TRAVEL, "Travel"),
        (SPORT, "Sport")
    )

    type = models.CharField(max_length=255, choices=JOURNAL_CHOICES, default="Bullet")
    publisher = models.CharField(max_length=255)
    objects = JournalManager()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'created_at': self.created_at,
            'type': self.type,
            'publisher': self.publisher
        }

class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.name,
            'password': self.password,
            'email': self.email
        }
class Book(models.Model):
    pass

class Profile(models.Model):
    pass
    
class BookMark(models.Model):
  
    user = models.ManyToManyField(Users)
    book = models.ManyToManyField(Books)
    content = models.DateField("Содержание цитаты")
    page = models.PositiveIntegerField("Номер страницы с цитатой")

class BooksUser(models.Model):
    pass

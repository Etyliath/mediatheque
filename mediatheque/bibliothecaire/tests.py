from django.test import TestCase
from django.urls import reverse
from .models import Member, Book, EmpruntBook


class IndexPageTestCase(TestCase):
    # test index page return 200
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class CreateBookPageTestCase(TestCase):
    
    def setUp(self):
        impossible = Book.objects.create(title = "voyage lune")
        self.book = Book.objects.get(title = "voyage lune")
    
    #test page book detail return staust code 200
    def test_create_book_page_returns_200(self):
        book_id = self.book.id
        response = self.client.get("/bibliothecaire/{}".format( book_id))
        self.assertEqual(response.status_code, 200)


    #test page book detail return staust code 400
    def test_create_book_page_returns_400(self):
        book_id = self.book.id + 1
        response = self.client.get("/bibliothecaire/{}".format( book_id))
        self.assertEqual(response.status_code, 404)
        
    
class EmpruntBookPageTestCase(TestCase):
    
    def setUp(self):
        member = Member.objects.create(name="nicolas", email="nicolas@demo.fr")
        self.member = Member.objects.get(name="nicolas")
        book = Book.objects.create(title = "voyage lune")
        self.book = Book.objects.get(title = "voyage lune")
        
    
    # def test_new_emprunt_book(self):
    #     old_emprunts_book = EmpruntBook.objects.count()
    #     book = self.book.id
    #     member = self.member.id
    #     date_restitution = '2024-04-28'
    #     response = self.client.post("empruntbook/add/", {
    #         'book': book,
    #         'member': member,
    #         'date_restitution': date_restitution})
    #     new_emprunts_book = EmpruntBook.objects.count()
    #     self.assertEqual(new_emprunts_book, old_emprunts_book + 1 )
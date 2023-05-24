from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.models import Article, Item
from blog.views import home_page, article_page
import pytz
from datetime import datetime
from django.test.client import Client


class ProfileArticleTest():

    def text_profile_database_add_comments(self):



class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        # Строчкая ниже сразу создает обьект в бд и сохраняет, без article1.save()
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            categery='categery 1',
            puddate=datetime.utcnow().replace(tzinfo=pytz.UTC),
            slug='slug-1'
        )
        Article.objects.create(
            title='title 2',
            full_text='full_text 2',
            summary='summary 2',
            categery='categery 2',
            puddate=datetime.utcnow().replace(tzinfo=pytz.UTC),
            slug='slug-2'
        )
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('blog/slug-1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('full_text 1', html)

        self.assertIn('title 2', html)
        self.assertIn('blog/slug-2', html)
        self.assertIn('summary 2', html)
        self.assertNotIn('full_text 2', html)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class ArticleModelTest(TestCase):

    def test_articles_page_displays_correct_articles(self):
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            categery='categery 1',
            puddate=datetime.utcnow().replace(tzinfo=pytz.UTC),
            slug='slug-1'
        )

        request = HttpRequest()
        response = article_page(request, 'slug-1')
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertNotIn('summary 1', html)
        self.assertIn('full_text 1', html)

    def test_article_model_save_and_retrieve(self):

        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='summary 1',
            categery='categery 1',
            puddate=datetime.utcnow().replace(tzinfo=pytz.UTC),
            slug='slug-1'
        )
        article1.save()

        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='summary 2',
            categery='categery 2',
            puddate=datetime.utcnow().replace(tzinfo=pytz.UTC),
            slug='slug-2'
        )
        article2.save()

        # загрузи из базы все статьи
        all_articles = Article.objects.all()

        # проверь: статей должно быть 2
        self.assertEqual(len(all_articles), 2)

        # проверь: 1 загруженная статья из БД == статья 1
        self.assertEqual(
            all_articles[0].title,
            article1.title
                        )
        # проверь: 2 загруженная статья из БД == статья 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
                        )
        # Проверяем слаги
        self.assertEqual(
            all_articles[0].slug,
            article1.slug
        )
        self.assertEqual(
            all_articles[1].slug,
            article2.slug
        )


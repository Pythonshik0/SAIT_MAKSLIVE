from django.test import TestCase
from .models import Image
from django.core.files import File


class GalleryModelTest(TestCase):

    def test_article_model_save_and_retrieve(self):

        image1 = Image(
            title='image 1',
            image=File(open('gallery/test_images/1.png', 'rb')),
        )
        image1.save()

        image2 = Image(
            title='image 2',
            image=File(open('gallery/test_images/2.png', 'rb')),
        )
        image2.save()

        # загрузи из базы все статьи
        all_images = Image.objects.all()

        # проверь: статей должно быть 2
        self.assertEqual(len(all_images), 2)

        # проверь: 1 загруженная картинка из БД == картинка 1
        self.assertEqual(
            all_images[0].title,
            image1.title
                        )
        # проверь: 2 загруженная картинка из БД == картинка 2
        self.assertEqual(
            all_images[1].title,
            image2.title
                        )
        # Проверяем image
        self.assertEqual(
            all_images[0].image,
            image1.image
        )
        self.assertEqual(
            all_images[1].image,
            image2.image
        )
from django.test import SimpleTestCase
from django.urls import resolve, reverse

from tasks.views import delete, tasks, complete

class TestUrls(SimpleTestCase):
    

    def test_delete(self):
        url = reverse('delete_task', args=[0])
        self.assertEquals(resolve(url).func, delete)


    def test_complete(self):
        url = reverse('completed_task', args=[0])
        self.assertEquals(resolve(url).func, complete)

    def test_task(self):
        url = reverse('tasks')
        self.assertEquals(resolve(url).func, tasks)

    




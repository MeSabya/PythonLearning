import unittest
from unittest import TestCase
from unittest.mock import patch
from UnitTestingInPython.my_blog import Blog
from UnitTestingInPython.my_blog import requests

class OTFError(Exception):

    # Constructor or Initializer
    def __init__(self, value, code='10'):
        self.code = code
        self.value = value

        # __str__ is to print() the value

    def __str__(self):
        return (repr(self.value + "With code value as "+self.code))



class TestBlog(TestCase):
    # Test how posts will behave when there is a request timeout in requests.get()
    def setUp(self):
        self.blog = Blog("sabya")

    def throws_exception(self, *args, **kwargs):
        print("Throws Exception")
        raise OTFError("OTF timeout exception")

    @patch('UnitTestingInPython.my_blog.requests', autospec=True)
    def test_posts_timeout_with_decorator(self, mock_requests):
        # Here the patch returns a MagicMock() which is passed as an argument to
        # test_posts_timeout_with_decorator as mock_requests
        # We can set .return_value and .side_effect on a Mock directly.

        print("*************** test_posts_timeout_with_decorator ****************************")
        mock_requests.get.side_effect = self.throws_exception
        ret = None
        ret = self.blog.posts()

    def test_posts_timeout_with_context_manager(self):
        print(" ********************* test_posts_timeout_with_context_manager *****************")
        with patch('UnitTestingInPython.my_blog.requests') as mock_requests:
            mock_requests.get.side_effect = self.throws_exception
            ret = self.blog.posts()
            self.assertIsInstance(ret, str)
            self.assertIsNotNone(ret)

    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_posts_timeout_with_object(self, mock_requests):
        print("************* Testing with objects *********************")
        with self.assertRaises(requests.exceptions.Timeout):
            ret = self.blog.posts_timeout()
            self.assertIsInstance(ret, requests.exceptions.Timeout)
            self.blog.posts_timeout.assert_called_once_with()
            self.assertIsNotNone(ret)

    #This is an example for return_value setting using mock object
    @patch('UnitTestingInPython.my_blog.Blog')
    def test_blog_posts_using_return_value(self, mock_blog):
        blog = mock_blog()
        print("************* test_blog_posts_using_return_value *********************")
        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]
        response = blog.posts()
        self.assertIsNotNone(response)




if __name__ == '__main__':
    unittest.main()
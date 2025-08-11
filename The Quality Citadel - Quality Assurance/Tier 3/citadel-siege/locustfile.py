import random
from locust import HttpUser, task, between

class ElysiumUser(HttpUser):
    """
    User class that defines a more complex set of user behaviors.
    """
    wait_time = between(1, 5)
    host = "https://jsonplaceholder.typicode.com"

    @task(10)  # This task will be run 10 times more often than the others
    def get_all_posts(self):
        """
        Defining a user task to get all posts, with performance checks.
        """
        with self.client.get("/posts", name="/posts [all]", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Status code was {response.status_code}, not 200")
            if response.elapsed.total_seconds() > 0.5:
                response.failure(f"Response time was {response.elapsed.total_seconds()}s, which is > 0.5s")

    @task(1)  # This task will be run less frequently
    def create_post(self):
        """
        Defining a user task to create a new post.
        """
        payload = {
            "title": "Elysium Nova Performance Test",
            "body": "This is a test post.",
            "userId": 1
        }
        self.client.post("/posts", json=payload)
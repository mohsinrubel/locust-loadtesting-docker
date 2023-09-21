from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def home(self):
        self.client.get("/")
        self.client.get("/about")

    @task(3)
    def view_blogs(self):
        for item_id in range(10):
            self.client.get(f"/blogs?page={item_id}&limit=50", name="/blogs")

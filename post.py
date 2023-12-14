class Post:
    i = 0

    def __init__(self, post_id, title, subtitle, body) -> None:
        self.post_id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

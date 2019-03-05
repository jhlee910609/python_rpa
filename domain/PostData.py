class PostData:
    date: int
    title: str
    series: str
    view_count: int
    like_count: int
    reply_count: int
    url: str

    def to_string(self):
        print(("%s, %s, %s, %s, %s, %s, %s") % (
            self.date, self.title, self.series, self.view_count, self.like_count, self.reply_count, self.url))

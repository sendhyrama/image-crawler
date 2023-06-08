from icrawler.builtin import GoogleImageCrawler

def download_images(keyword):
    google_crawler = GoogleImageCrawler(storage={"root_dir": "downloads"})
    filters = dict(type="photo", size="medium")  # Optional filters
    google_crawler.crawl(keyword=keyword, max_num=1, filters=filters, file_idx_offset="auto")

keywords = ["cat", "dog", "flower"]
image_count = 0

for keyword in keywords:
    download_images(keyword)
    image_count += 1

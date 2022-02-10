from .setup import NewsCrawler, OfficeOfEduAdminCrawler, MathCrawler, AggregatedCrawler, make_crawler_test

test_news_crawler = make_crawler_test(NewsCrawler)
test_office_of_edu_admin_crawler = make_crawler_test(OfficeOfEduAdminCrawler)
test_math_crawler = make_crawler_test(MathCrawler)


def test_aggregated_crawler():
    crawlers = [
        OfficeOfEduAdminCrawler(),
        NewsCrawler(),
        MathCrawler(),
    ]
    agg = AggregatedCrawler(*crawlers)
    agg.crawl()
    assert len(agg) == sum(len(c) for c in crawlers)
    base_test = make_crawler_test(lambda: agg)
    base_test()

from tags.MetaTag import MetaTag
from tags.HeadTag import HeadTag


class HeaderGenerator:
    def generate(self):
        return HeadTag(self.__get_meta_tags()).get_formatted()

    def __get_meta_tags(self):
        meta_tag = MetaTag({
            'name': 'viewport',
            'content': 'width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0'})

        return meta_tag.get_formatted()

from tags.MetaTag import MetaTag
from tags.HeadTag import HeadTag
from tags.TitleTag import TitleTag
import lorem


class HeaderGenerator:
    def generate(self):
        return HeadTag(self.__get_meta_tags() + self.__get_title()).get_formatted()

    def __get_title(self):
        return TitleTag(lorem.sentence()).get_formatted()

    def __get_meta_tags(self):
        meta_tags_data = [
            {'charset': 'UTF-8'},
            {
                'name': 'viewport',
                'content': 'width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0'
            },
            {
                'http-equiv': 'X-UA-Compatible',
                'content': 'ie=edge'
            }
        ]
        meta_tags = ''
        for meta_tag_data in meta_tags_data:
            meta_tags += ' ' + MetaTag(meta_tag_data).get_formatted() + ' '

        return meta_tags

from googletrans import Translator


def en_to_cn(english):
    translator = Translator(service_urls=['translate.google.cn'])
    translations = translator.translate(english, dest='zh-cn')
    return translations.text


def _test():
    zh_cn = en_to_cn('The quick brown fox')
    print(zh_cn)


_test()



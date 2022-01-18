from HTMLParser import HTMLParser
hp = HTMLParser()
text = u"७ ]। ०-० ०  [>075फ॥70 66 0695    यह तुम्हारे लिए है, है न?"
hp.unescape(text)
print(hp.unescape(text))
hp.unescape(text).split()
print(" ".join(hp.unescape(text).split()))
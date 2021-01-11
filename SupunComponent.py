from psd_tools import PSDImage
import re
import webbrowser

def Supun_LayerIdentifier():
    message = """<DOCTYPE HTML!>"""
    message = message + "\n"
    message = message + """<html>"""
    message = message + "\n"
    message = message + """<head>"""
    message = message + "\n"
    message = message + """<style>"""
    message = message + "\n"
    message = message + """img{ """
    message = message + "\n"
    message = message + """ width: auto; """
    message = message + "\n"
    message = message + """ height: auto; """
    message = message + "\n"
    message = message + """} """

    psd = PSDImage.open('1.psd')
    psd.composite().save('1.png')
    i = 1

    for layer in psd:
        # print(layer)
        # print("DEBUG (1): ", message)

        message = message + "\n"
        message = message + "."
        message = message + ''.join(e for e in layer.name if e.isalnum())
        # print("DEBUG (2): ", message)
        message = message + "\n"
        message = message + """{"""
        message = message + "\n"
        message = message + """position: absolute;"""
        message = message + "\n"
        message = message + """z-index:"""
        # print("DEBUG (3): ", message)
        message = message + str(i)
        message = message + """;"""
        # print("DEBUG (4): ", message)
        i = i + 1
        message = message + "\n"
        # print("DEBUG (5): ", message)
        message = message + """top:"""
        message = message + str(layer.top)
        message = message + """;"""
        message = message + "\n"
        # print("DEBUG (5): ", message)
        message = message + """left:"""
        message = message + str(layer.left)
        message = message + """;"""
        message = message + "\n"
        message = message + """}"""
        message = message + "\n"
        # print("DEBUG (4): ", layer.top)
        # print("DEBUG (5): ", layer.size)
        # print("DEBUG (5a): ", layer.size[0])
        # print("DEBUG (5b): ", layer.size[1])
        image = layer.composite()
        layer_image = layer.composite()
        layer_image.save('%s.png' % ''.join(e for e in layer.name if e.isalnum()))

    message = message + "\n"
    message = message + """</style>"""
    message = message + "\n"
    message = message + """</head>"""
    message = message + "\n"
    message = message + """<body>"""
    message = message + "\n"

    for layer in psd:
        # print(layer)
        # print("DEBUG (6): ", message)
        re.sub('[^A-Za-z0-9]+', '', message)
        message = message + """<div><img src=" """
        message = message + ''.join(e for e in layer.name if e.isalnum())
        message = message + """.png"""
        message = message + """" """
        # print("DEBUG (7): ", message)
        message = message + """ class=" """
        message = message + ''.join(e for e in layer.name if e.isalnum())
        message = message + """" """
        # print("DEBUG (8): ", message)
        message = message + """ width=" """
        message = message + str(layer.width)
        message = message + """" """
        message = message + ","
        message = message + """height=" """
        message = message + str(layer.height)
        message = message + """" """
        message = message + """/></div> """
        message = message + "\n"
    message = message + """</body>"""
    message = message + "\n"
    message = message + """</html>"""

    f = open("ps2web.html", "w")

    # f.write(message.encode('utf-8'))
    f.write(message)
    f.close()

    # open and read the file after the appending:
    f = open("ps2web.html", "r")
    # print(f.read())

    url = 'file:///home/akhitha/Akhitha/Supun%20FYP/PycharmProjects/PycharmProjects/integrated1.0/ps2web.html'
    webbrowser.open(url, new=2)  # open in new tab



# Supun_LayerIdentifier()

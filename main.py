# @author --- IT16521544 B D K Samaraweera

from psd_tools import PSDImage

def processPSD(filename):

    psd = PSDImage.open(filename)


    psd.composite().save('previewpsd.png')

    for index,grpname in enumerate(psd):
        if grpname.kind=='group':
            if grpname.name == 'Images':
                group = psd[index]
                for layer in group:
                    print(layer)
                    layer_image = layer.composite()
                    if layer_image.mode == "RGBA":
                        layer_image.save('static/Images/%s.png' % layer.name)
                    else:
                        layer_image.save('static/Images/%s.jpg' % layer.name)

            if grpname.name == 'Videos':
                group = psd[index]
                for layer in group:
                    print(layer)
                    layer_image = layer.composite()
                    if layer_image.mode == "RGBA":
                        layer_image.save('static/Videos/%s.png' % layer.name)
                    else:
                        layer_image.save('static/Videos/%s.jpg' % layer.name)
#







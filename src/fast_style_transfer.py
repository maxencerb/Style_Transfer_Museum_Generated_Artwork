import tensorflow as tf
import tensorflow_hub as hub

from src.setup import tensor_to_image

def fast_style_transfer(content_image, style_image):
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    return tensor_to_image(stylized_image)

def complete_fast_algorithm(content_path, style_path, img_size = 512):
    """
    returns the instance of image which represents the result
    """
    import matplotlib.pyplot as plt
    from src.setup import load_img
    from src.visualization import imshow

    print('Loading Images ---')
    content_image = load_img(content_path, img_size)
    style_image = load_img(style_path, img_size)

    print('Executing style transfer, this could take a moment\nPlease wait...')
    result_image = fast_style_transfer(content_image, style_image)

    print('plotting images -->')
    plt.subplot(2, 2, 1)
    imshow(content_image, 'Content image')

    plt.subplot(2, 2, 2)
    imshow(style_image, 'Style image')

    return result_image



# Generated artwork

&copy; Maxence Raballand 2021

code from [this repositery](https://github.com/maxencerb/Style_transfer_tensorflow)

The whole project was generated as such :

```python
from src.fast_style_transfer import complete_fast_algorithm

content_path = './artwork/**/content.jpg'
style_path = './artwork/**/style.jpg'

result_image = complete_fast_algorithm(content_path, style_path)

result_image.save('artwork/**/result.png')
```

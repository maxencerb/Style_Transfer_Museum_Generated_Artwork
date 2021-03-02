# Generated artwork

&copy; Maxence Raballand 2021

## Table of content

| Name     | Number of Style | Link |
| --- |:------:| -----------------:|
| Curvy Blue Chicago              | 1               | [link](artwork/Curvy%20blue%20Chicago/README.md)               |
| Maxence Raballand Long Distance | 4               | [link](artwork/Maxence%20Raballand%20Long%20distance/README.md)|
| PoitiersByMonet                 | 1               | [link](artwork/PoitiersByMonet/README.md)                      |
| Portrait of Lea                 | 1               | [link](artwork/Portrait%20of%20Lea%20Noireaux/README.md)       |


## Method

code from [this repositery](https://github.com/maxencerb/Style_transfer_tensorflow)

The whole project was generated as such :

```python
from src.fast_style_transfer import complete_fast_algorithm

content_path = './artwork/**/content.jpg'
style_path = './artwork/**/style.jpg'

result_image = complete_fast_algorithm(content_path, style_path)

result_image.save('artwork/**/result.png')
```
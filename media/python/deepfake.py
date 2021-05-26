import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings
warnings.filterwarnings('ignore')
from IPython.display import HTML
from base64 import b64encode
import sys

source_image = imageio.imread('media/python/frames/img6.png')
reader = imageio.get_reader('media/'+sys.argv[1])
fps = reader.get_meta_data()['fps']

source_image = resize(source_image,(256,256))[..., :3]
driving_video = [resize(frame,(256,256))[..., :3] for frame in reader]

def display(source,driving, generated=None):
  fig = plt.figure(figsize=(8+4*(generated is not None),6))

  ims = []
  for i in range(len(driving)):
    cols=[source]
    cols.append(driving[i])
    if generated is not None:
      cols.append(generated[i])
    im = plt.imshow(np.concatenate(cols, axis=1),animated=True)
    plt.axis('off')
    ims.append([im])
  
  ani = animation.ArtistAnimation(fig, ims, interval=20, repeat_delay=1000)
  #plt.close()
  #return ani

#HTML(display(source_image,driving_video).to_html5_video())

from demo import load_checkpoints
generator, kp_detector = load_checkpoints(config_path='media/python/config/vox-256.yaml',checkpoint_path='media/python/vox-cpk.pth.tar')

from demo import make_animation
from skimage import img_as_ubyte

predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

#save video
imageio.mimsave('media/generated/'+ 'generatednew.mp4', [img_as_ubyte(frame) for frame in predictions], fps=fps)

#HTML(display(source_image, driving_video, predictions).to_html5_video())

from moviepy.editor import *
#source_image = imageio.imread('got-08.png')
clip1 = VideoFileClip('media/generated/'+ 'generatednew.mp4')
clip2 = VideoFileClip('media/'+sys.argv[1])

img = ['media/python/frames/img6.png']

clips = [ImageClip(m).set_duration(clip1.duration)
      for m in img]

concat_clip = concatenate_videoclips(clips, method="compose")
#concat_clip.write_videofile("test.mp4",fps=fps)

final_new = clips_array([[concat_clip,clip2,clip1]])
final_new.write_videofile('media/generated/'+'merge1.mp4')

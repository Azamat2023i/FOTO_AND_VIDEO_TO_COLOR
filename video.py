import os
from moviepy.editor import VideoFileClip, ImageSequenceClip, AudioFileClip
from PIL import Image
import numpy as np
import list_of_files

# Укажите путь к вашему видеофайлу
video_path = 'test_video.mp4'
output_video_path = 'final_video.mp4'

# Укажите папки для сохранения аудио и кадров
audio_output_path = 'output/audio'
frames_output_path = 'output/frames'
converted_output_path = 'output/converted'

# Создайте папки, если они не существуют
os.makedirs(audio_output_path, exist_ok=True)
os.makedirs(frames_output_path, exist_ok=True)
os.makedirs(converted_output_path, exist_ok=True)

# Загружаем видео
video = VideoFileClip(video_path)
audio_path = None

# Сохраняем звуковую дорожку
if video.audio is not None:
    audio_path = os.path.join(audio_output_path, 'audio.mp3')
    video.audio.write_audiofile(audio_path)
else:
    print("В видеофайле отсутствует аудиодорожка.")

# Получаем FPS видео
fps = video.fps

# Сохраняем кадры с тем же FPS
for i, frame in enumerate(video.iter_frames(fps=fps)):
    frame_image_path = os.path.join(frames_output_path, f'frame_{i:04d}.jpg')
    frame_image = Image.fromarray(frame)
    frame_image.save(frame_image_path)

# Закрываем видео
video.close()

print("Разделение завершено!")

list_of_files.transformation(frames_output_path, converted_output_path)

print("Преобразование завершено!")

# Преобразование кадров в видео
frames_list = [os.path.join(converted_output_path, f) for f in sorted(os.listdir(converted_output_path)) if f.endswith('.jpg')]
clip = ImageSequenceClip(frames_list, fps=fps)

if audio_path:
    if os.path.exists(audio_path):
        audio_clip = AudioFileClip(audio_path)
        clip = clip.set_audio(audio_clip)

# Сохраняем финальное видео в MP4 формат
final_video_path = os.path.join(output_video_path)
clip.write_videofile(final_video_path, codec='libx264', audio_codec='aac')

print("Готово!")

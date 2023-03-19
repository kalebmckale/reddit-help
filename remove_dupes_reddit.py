import pathlib

base_path = pathlib.Path.cwd()
file_pattern = "*.mp4"

seen_durations = set()
for vid_path in base_path.glob(file_pattern):
    clip = VideoFileClip(vid_path, target_resolution=(1080, None))
    if clip.duration not in seen_durations:
        seen_durations.add(clip.duration)
        continue
    vid_path.unlink() # This is equivalent to os.remove()
import os

def get_files_in_dir(dir_path):
  """Returns a list of all files in the given directory."""
  files = []
  print(dir_path)
  for root, dirs, filenames in os.walk(dir_path):
    print("root ", root, " dirs:", dirs, " filenames:", filenames)
    for filename in filenames:
      print(os.path.join(root, filename))
      files.append(os.path.join(root, filename))
  print("done get files")
  return files

def run_face_swapper(target_dir, source_dir, output_dir, execution_provider, frame_processor):
  """Runs the face swapper on all files in the target and source directories."""

  # delete the temp directory in the target_dir folder, use the variable target_dir to get the path. Check if it exists first before deleting.
  temp_dir = os.path.join(target_dir, "temp")
  if os.path.exists(temp_dir):
    print(f">>> Deleting directory {temp_dir}")
    # delete using both Windows and Linux. Do not use "rm -rf" because it will not work on Windows. Do not use "rmdir". Use a Pythonic way to delete a directory.






  for target_file in get_files_in_dir(target_dir):
    for source_file in get_files_in_dir(source_dir):
      # Concatenate variables into a filename like {source}-{target}.mp4
      output_filename = os.path.join(output_dir, f"{os.path.basename(source_file)}-{os.path.basename(target_file)}")

      # Skip if the output file already exists
      if os.path.exists(output_filename):
        print(f"Skipping {output_filename} because it already exists.")
        continue

      # Run the face swapper
      print(f"python run.py --target {target_file} --source {source_file} -o {output_filename} --execution-provider {execution_provider} --frame-processor {frame_processor} --similar-face-distance 1000 --many-faces")
      # print(f"python run.py --target {target_file} --source {source_file} -o {output_filename} --execution-provider {execution_provider} --frame-processor {frame_processor} --temp-frame-quality 100 --similar-face-distance 1000")
      os.system(f"python run.py --target {target_file} --source {source_file} -o {output_filename} --execution-provider {execution_provider} --frame-processor {frame_processor} --similar-face-distance 1000 --many-faces")
      # os.system(f"python run.py --target {target_file} --source {source_file} -o {output_filename} --execution-provider {execution_provider} --frame-processor {frame_processor} --temp-frame-quality 100 --similar-face-distance 1000")

# Example usage:
print("Running faceswapper")
run_face_swapper("batch-mp4/", "batch-jpg/", "out/", "cuda", "face_swapper face_enhancer")

print("DONE!")
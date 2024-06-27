To set up the camera, you first need to set up timelapse capabilities for your printer. (https://github.com/mainsail-crew/moonraker-timelapse/blob/main/docs/installation.md) However, there are a few things that you need to change from the base setup.

1. Make sure you have this directory setup: ~/3d_print_error_detector/images
2. Change frame_path in moonraker config to ~/3d_print_error_detector/images
3. When setting up where the extruder head goes when parked, ideally it should not be able to be seen from the camera

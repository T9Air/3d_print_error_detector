python3 ~/3d_print_error_detector/image-compare.py 12

python_script_return_code=$?


if [ $python_script_return_code -eq 0 ]; then
  echo "No movement detected. Continue print."
else
  echo "PRINT MOVED FROM ORIGINAL SPOT! STOP NOW!"
  echo "!klipper; gcode_macro check_macro_docs" > /tmp/klipper_fifo
fi

;; Auto-generated. Do not edit!


(when (boundp 'get_rs_image::FLIR_image)
  (if (not (find-package "GET_RS_IMAGE"))
    (make-package "GET_RS_IMAGE"))
  (shadow 'FLIR_image (find-package "GET_RS_IMAGE")))
(unless (find-package "GET_RS_IMAGE::FLIR_IMAGE")
  (make-package "GET_RS_IMAGE::FLIR_IMAGE"))
(unless (find-package "GET_RS_IMAGE::FLIR_IMAGEREQUEST")
  (make-package "GET_RS_IMAGE::FLIR_IMAGEREQUEST"))
(unless (find-package "GET_RS_IMAGE::FLIR_IMAGERESPONSE")
  (make-package "GET_RS_IMAGE::FLIR_IMAGERESPONSE"))

(in-package "ROS")



(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass get_rs_image::FLIR_imageRequest
  :super ros::object
  :slots ())

(defmethod get_rs_image::FLIR_imageRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass get_rs_image::FLIR_imageResponse
  :super ros::object
  :slots (_data ))

(defmethod get_rs_image::FLIR_imageResponse
  (:init
   (&key
    ((:data __data) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&rest __data)
   (if (keywordp (car __data))
       (send* _data __data)
     (progn
       (if __data (setq _data (car __data)))
       _data)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/Image _data
    (send _data :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/Image _data
       (send _data :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/Image _data
     (send _data :deserialize buf ptr-) (incf ptr- (send _data :serialization-length))
   ;;
   self)
  )

(defclass get_rs_image::FLIR_image
  :super ros::object
  :slots ())

(setf (get get_rs_image::FLIR_image :md5sum-) "a4166222fac24d9abf5822c7d9b15b3b")
(setf (get get_rs_image::FLIR_image :datatype-) "get_rs_image/FLIR_image")
(setf (get get_rs_image::FLIR_image :request) get_rs_image::FLIR_imageRequest)
(setf (get get_rs_image::FLIR_image :response) get_rs_image::FLIR_imageResponse)

(defmethod get_rs_image::FLIR_imageRequest
  (:response () (instance get_rs_image::FLIR_imageResponse :init)))

(setf (get get_rs_image::FLIR_imageRequest :md5sum-) "a4166222fac24d9abf5822c7d9b15b3b")
(setf (get get_rs_image::FLIR_imageRequest :datatype-) "get_rs_image/FLIR_imageRequest")
(setf (get get_rs_image::FLIR_imageRequest :definition-)
      "---
sensor_msgs/Image data


================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
")

(setf (get get_rs_image::FLIR_imageResponse :md5sum-) "a4166222fac24d9abf5822c7d9b15b3b")
(setf (get get_rs_image::FLIR_imageResponse :datatype-) "get_rs_image/FLIR_imageResponse")
(setf (get get_rs_image::FLIR_imageResponse :definition-)
      "---
sensor_msgs/Image data


================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
")



(provide :get_rs_image/FLIR_image "a4166222fac24d9abf5822c7d9b15b3b")



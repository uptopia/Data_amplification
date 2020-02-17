
(cl:in-package :asdf)

(defsystem "get_rs_image-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "FLIR_image" :depends-on ("_package_FLIR_image"))
    (:file "_package_FLIR_image" :depends-on ("_package"))
  ))
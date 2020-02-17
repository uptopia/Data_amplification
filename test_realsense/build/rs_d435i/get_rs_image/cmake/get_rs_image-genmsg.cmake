# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "get_rs_image: 1 messages, 1 services")

set(MSG_I_FLAGS "-Iget_rs_image:/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/kinetic/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(get_rs_image_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg" NAME_WE)
add_custom_target(_get_rs_image_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "get_rs_image" "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg" ""
)

get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv" NAME_WE)
add_custom_target(_get_rs_image_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "get_rs_image" "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv" "sensor_msgs/Image:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/get_rs_image
)

### Generating Services
_generate_srv_cpp(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/get_rs_image
)

### Generating Module File
_generate_module_cpp(get_rs_image
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/get_rs_image
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(get_rs_image_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(get_rs_image_generate_messages get_rs_image_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg" NAME_WE)
add_dependencies(get_rs_image_generate_messages_cpp _get_rs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv" NAME_WE)
add_dependencies(get_rs_image_generate_messages_cpp _get_rs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(get_rs_image_gencpp)
add_dependencies(get_rs_image_gencpp get_rs_image_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_rs_image_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/get_rs_image
)

### Generating Services
_generate_srv_eus(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/get_rs_image
)

### Generating Module File
_generate_module_eus(get_rs_image
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/get_rs_image
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(get_rs_image_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(get_rs_image_generate_messages get_rs_image_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg" NAME_WE)
add_dependencies(get_rs_image_generate_messages_eus _get_rs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv" NAME_WE)
add_dependencies(get_rs_image_generate_messages_eus _get_rs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(get_rs_image_geneus)
add_dependencies(get_rs_image_geneus get_rs_image_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_rs_image_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/get_rs_image
)

### Generating Services
_generate_srv_lisp(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/get_rs_image
)

### Generating Module File
_generate_module_lisp(get_rs_image
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/get_rs_image
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(get_rs_image_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(get_rs_image_generate_messages get_rs_image_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg" NAME_WE)
add_dependencies(get_rs_image_generate_messages_lisp _get_rs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv" NAME_WE)
add_dependencies(get_rs_image_generate_messages_lisp _get_rs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(get_rs_image_genlisp)
add_dependencies(get_rs_image_genlisp get_rs_image_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_rs_image_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/get_rs_image
)

### Generating Services
_generate_srv_nodejs(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/get_rs_image
)

### Generating Module File
_generate_module_nodejs(get_rs_image
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/get_rs_image
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(get_rs_image_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(get_rs_image_generate_messages get_rs_image_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg" NAME_WE)
add_dependencies(get_rs_image_generate_messages_nodejs _get_rs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv" NAME_WE)
add_dependencies(get_rs_image_generate_messages_nodejs _get_rs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(get_rs_image_gennodejs)
add_dependencies(get_rs_image_gennodejs get_rs_image_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_rs_image_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_rs_image
)

### Generating Services
_generate_srv_py(get_rs_image
  "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_rs_image
)

### Generating Module File
_generate_module_py(get_rs_image
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_rs_image
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(get_rs_image_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(get_rs_image_generate_messages get_rs_image_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/msg/Num.msg" NAME_WE)
add_dependencies(get_rs_image_generate_messages_py _get_rs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/iclab/Desktop/test/src/rs_d435i/get_rs_image/srv/FLIR_image.srv" NAME_WE)
add_dependencies(get_rs_image_generate_messages_py _get_rs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(get_rs_image_genpy)
add_dependencies(get_rs_image_genpy get_rs_image_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_rs_image_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/get_rs_image)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/get_rs_image
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(get_rs_image_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(get_rs_image_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/get_rs_image)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/get_rs_image
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(get_rs_image_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(get_rs_image_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/get_rs_image)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/get_rs_image
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(get_rs_image_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(get_rs_image_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/get_rs_image)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/get_rs_image
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(get_rs_image_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(get_rs_image_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_rs_image)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_rs_image\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_rs_image
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_rs_image
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_rs_image/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(get_rs_image_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(get_rs_image_generate_messages_py sensor_msgs_generate_messages_py)
endif()

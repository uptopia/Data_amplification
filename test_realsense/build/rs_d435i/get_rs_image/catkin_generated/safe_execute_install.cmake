execute_process(COMMAND "/home/iclab/Desktop/test/build/rs_d435i/get_rs_image/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/iclab/Desktop/test/build/rs_d435i/get_rs_image/catkin_generated/python_distutils_install.sh) returned error code ")
endif()

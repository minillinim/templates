AC_PREREQ(2.61)
AC_INIT(Whatever, 0.1, michael.imelfort@gmail.com)

AC_CONFIG_AUX_DIR([build-aux])

AC_PROG_CC
AC_PROG_CXX

# test for libm
m_flags=
AC_CHECK_LIB([m],[lgamma,log,exp],
             [m_flags="-lm"
              AC_DEFINE([HAVE_M],[1],[Defines to 1 if the m library (-lm) is found])],
             [AC_MSG_ERROR([libm not found])])

AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([Makefile])
AC_OUTPUT

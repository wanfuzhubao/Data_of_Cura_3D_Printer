'''OpenGL extension EXT.separate_shader_objects

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_separate_shader_objects'
_DEPRECATED = False
GL_ACTIVE_PROGRAM_EXT = constant.Constant( 'GL_ACTIVE_PROGRAM_EXT', 0x8B8D )
glUseShaderProgramEXT = platform.createExtensionFunction( 
'glUseShaderProgramEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,),
doc='glUseShaderProgramEXT(GLenum(type), GLuint(program)) -> None',
argNames=('type','program',),
deprecated=_DEPRECATED,
)

glActiveProgramEXT = platform.createExtensionFunction( 
'glActiveProgramEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,),
doc='glActiveProgramEXT(GLuint(program)) -> None',
argNames=('program',),
deprecated=_DEPRECATED,
)

glCreateShaderProgramEXT = platform.createExtensionFunction( 
'glCreateShaderProgramEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLuint, 
argTypes=(constants.GLenum,arrays.GLcharArray,),
doc='glCreateShaderProgramEXT(GLenum(type), GLcharArray(string)) -> constants.GLuint',
argNames=('type','string',),
deprecated=_DEPRECATED,
)


def glInitSeparateShaderObjectsEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )

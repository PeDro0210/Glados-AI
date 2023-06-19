from cx_Freeze import setup, Executable
import sys

sys.setrecursionlimit(3000)

setup(name='GLaDOS_AI',
      version='0.1',
      executables = [Executable("glados_AI_main.py",icon="Logo.ico")])


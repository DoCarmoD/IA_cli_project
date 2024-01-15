import argparse, sys
import markdown

def markdonw_converter(text):
  """Converte uma string em markdown.

  Args:
    text: A string para converter.

  Returns:
    Uma string em markdown.
  """

  return markdown.markdown(text)
import os

os.chdir('/home/sleyder/SEII-LucasSleyderMachadoDicencio/Semana02/Exercicio04')

print(os.getcwd())

for f in os.listdir():
  print(f)

for f in os.listdir():
  print(os.path.splitext(f))

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name)

for f in os.listdir():
  f_name, f_ext = os.path.splitext(f)

  f_title, f_course, f_num = f_name.split('-')
  
  f_title = f_title.strip()
  f_course = f_course.strip()
  f_num = f_num.strip()[1:].zfill(2)

  print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

for f in os.listdir():
  f_name, f_ext = os.path.splitext(f)
  f_title, f_course, f_num = f_name.split('-')
  f_title = f_title.strip()
  f_course = f_course.strip()
  f_num = f_num.strip()[1:].zfill(2)

  new_name = '{}-{}{}'.format(f_num, f_title, f_ext)

  os.rename(f, new_name)
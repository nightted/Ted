# coding=UTF-8
import datetime
import os
import urllib2,urllib


# 起始日期
START_DATE = datetime.date(year=2016, month=6, day=1)
# 結束日期
END_DATE = datetime.date(year=2016, month=6, day=5)
# 本地存放的資料夾路徑
LOCAL_SAVE_PATH = os.path.join('C:/Users\h5904\Desktop/data/')
# 衛星
SATELLITES = ['GOE-15', 'HIM-8', 'GOE-13']
# 圖種類
TYPES = ['IR', 'VS', 'WV']

def daterange(start_date, end_date):
  for n in range(int ((end_date - start_date).days) + 1):
    yield start_date + datetime.timedelta(n)


def get_img():
  for date in daterange(START_DATE, END_DATE):
    for satellite in SATELLITES:
      for img_type in TYPES:
        for i in range(0, 24, 3):
          img_name = '{}-{:02}'.format(date.strftime('%Y-%m-%d'), i)
          img_src = 'http://www.ncdc.noaa.gov/gibbs/image/{}/{}/{}'.format(
                     satellite, img_type, img_name)
          img_dest = os.path.join(LOCAL_SAVE_PATH, '{}-{}-{}.jpg'.format(
                     satellite, img_type, img_name))
          try:
            urllib.urlretrieve(img_src, img_dest)
            print('Save url:[{}] to file [{}]'.format(img_src, img_dest))
          except urllib2.HTTPError as err:
            print('Save url:[{}] meet error [{}] !!'.format(img_src, err))


if __name__ == '__main__':
  get_img()

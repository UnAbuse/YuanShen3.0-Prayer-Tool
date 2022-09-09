import requests, time, sqlite3
from rich import print

def clean(authkey):
	# 200, 301, 302
	allPoint = []
	for page in range(1, 101):
		try:
			if len(allPoint) == 0:
				end_id = 0
				params = {
					'authkey_ver': 1,
					'lang': 'zh-cn',
					'authkey': authkey,
					'gacha_type': 301,
					'page': page,
					'size': 10,
					'end_id': end_id
				}
				url = f'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog'
				data = gethtml(url, params)["data"]["list"]
				allPoint = allPoint + data
			else:
				end_id = allPoint[-1]["id"]
				params = {
					'authkey_ver': 1,
					'lang': 'zh-cn',
					'authkey': authkey,
					'gacha_type': 301,
					'page': page,
					'size': 10,
					'end_id': end_id
				}
				url = f'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog'
				data = gethtml(url, params)["data"]["list"]
				allPoint = allPoint + data
		except:
			break
		time.sleep(1)
	return allPoint

def gethtml(url, params):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'}
	html = requests.get(url=url, headers=headers, params=params)
	html.encoding = 'utf-8'
	return html.json()


def find_data():
	conn = sqlite3.connect('anl.db')
	cur = conn.cursor()
	cur.execute('create table if not exists data_list (sel_id int ,id int ,name varchar ,item_type varchar(100) ,item_time datetime)')
	conn.commit()
	authkey = input("请输入authkey:")
	print('为了不对服务器造成困扰导致查询失败，请耐心等待……')
	allpoint = clean(authkey)
	allpoint.reverse()
	for items in enumerate(allpoint, 1):
		cur.execute('insert into data_list values(?,?,?,?,?)', (items[0], items[1]["id"], items[1]["item_type"],items[1]["name"], items[1]["time"]))
		conn.commit()
	try:
		print(f'共存入{items[0]}条数据')
		cur.execute('select * from data_list group by sel_id having count(*)>1;')
		conn.commit()
		print(f'共有{len(cur.fetchall())}条重复数据')
		cur.execute('delete from data_list where data_list.rowid not in (select MAX(data_list.rowid) from data_list group by sel_id);')
		conn.commit()
		print('数据已去重')
	except:
		print('存入失败')

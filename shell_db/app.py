import sqlite3, yuan_db

conn = sqlite3.connect('anl.db')
cur = conn.cursor()

def find_all_info():
	custom = ['神里绫人', '八重神子', '申鹤', '荒泷一斗', '珊瑚宫心海', '埃洛伊', '雷电将军', '宵宫', '神里绫华', '枫原万叶', '优菈', '胡桃', '魈', '甘雨', '阿贝多', '钟离', '达达利亚', '可莉', '温迪', '迪卢克', '七七', '琴', '莫娜', '刻晴']
	cur.execute("SELECT * from data_list order by item_time asc;")
	conn.commit()
	data = cur.fetchall()
	kr = 0
	for items in enumerate(data, 1):
		if any(i in items[1][3] for i in custom):
			tf_list = [i in items[1][3] for i in custom]
			for i in enumerate(tf_list):
				if i[1] == True:
					print(f'{custom[i[0]]} {items[0]-kr}')
					kr = items[0]
	print(f'此时已垫{items[0]-kr}抽')

while True:
	print('''
	原神祈愿分析工具使用说明：
	作者:UnAbuse
	1.获取能查询到的所有up祈愿（保存到数据库，减少工作量）
	2.对数据库中的数据进行分析（用这个请确保数据库中已经保存数据，目前只支持up池，以后也许会做界面吧）
	3.退出工具
	''')
	num = eval(input('请输入要进行的操作：'))
	if num == 1:
		anl_db.find_data()
	if num == 2:
		find_all_info()
	if num == 3:
		break

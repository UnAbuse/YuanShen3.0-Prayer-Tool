import sqlite3, yuan_db
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("角色")
table.add_column("抽卡次数")

conn = sqlite3.connect('anl.db')
cur = conn.cursor()

def find_all_info():
	custom = ['钟离', '神里绫人', '八重神子', '申鹤', '荒泷一斗', '珊瑚宫心海', '埃洛伊', '雷电将军', '宵宫', '神里绫华', '枫原万叶', '优菈', '胡桃', '魈', '甘雨', '阿贝多', '达达利亚', '可莉', '温迪', '迪卢克', '七七', '琴', '莫娜', '刻晴']
	cur.execute("SELECT * from data_list order by sel_id asc;")
	conn.commit()
	data = cur.fetchall()
	kr = 0
	for items in enumerate(data, 1):
		if any(i in items[1][3] for i in custom):
			table.add_row(f'{items[1][3]}', f'{items[0]-kr}')
			kr = items[0]
	table.add_row("垫子", f'{items[0]-kr}')
	console.print(table)

while True:
	plug = '''
	原神祈愿分析工具使用说明：
	作者:UnAbuse
	文档:https://github.com/UnAbuse/YuanShen3.0-Prayer-Tool
	1.获取能查询到的所有up祈愿（保存到数据库，减少工作量）
	2.对数据库中的数据进行分析（用这个请确保数据库中已经保存数据，目前只支持up池，以后也许会做界面吧）
	3.退出工具
	'''
	print(plug)
	num = eval(input('请输入要进行的操作：'))
	if num == 1:
		yuan_db.find_data()
	if num == 2:
		find_all_info()
	if num == 3:
		break

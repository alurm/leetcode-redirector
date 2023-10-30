import json
import types
import subprocess

raw_data = subprocess.run(
	'curl -L https://leetcode.com/api/problems/all',
	shell=True,
	check=True,
	stdout=subprocess.PIPE,
	stderr=subprocess.DEVNULL,
).stdout

data = json.loads(raw_data, object_hook = lambda x: types.SimpleNamespace(**x))

ids = {}

for problem in data.stat_status_pairs:
	problem = problem.stat
	id = problem.frontend_question_id
	name = problem.question__title_slug
	ids[id] = name

def id_or_name_to_name(id_or_name):
	if id_or_name.isdecimal():
		id = int(id_or_name)
		return ids[id]
	name = id_or_name
	return name

def name_to_leetcode_url(name):
	return f'https://leetcode.com/problems/{name}/'

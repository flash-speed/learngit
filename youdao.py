from urllib import request
from urllib import parse
import json

if __name__ == '__main__':
	Request_URL='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
	Form_Data = {}
	Form_Data['i'] = 'jack'
	Form_Data['from'] = 'AUTO'
	Form_Data['to'] = 'AUTO'
	Form_Data['smartresult'] = 'dict'
	Form_Data['client'] = 'fanyideskweb'
	Form_Data['salt'] = '1528296111533'
	Form_Data['doctype'] = 'json'
	Form_Data['version'] = '2.1'
	Form_Data['keyform'] = 'fanyi.web'
	Form_Data['action'] = 'FY_BY_REALTIME'
	data = parse.urlencode(Form_Data).encode('utf-8')
	response = request.urlopen(Request_URL,data)
	html = response.read().decode('utf-8')
	translate_results = json.loads(html)
	translate_results = translate_results['translateResult'][0][0]['tgt']
	print(translate_results)
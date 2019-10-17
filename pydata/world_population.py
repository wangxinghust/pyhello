"""
制作世界人口地图：JSON格式
"""
import json
from pygal.maps.world import World
from country_codes import get_country_code

# 将数据加载到一个列表中
filename = "pydata/data/population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

wm = World()
wm.force_uri_protocal = 'http'
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)
wm.render_to_file('world_population.svg')

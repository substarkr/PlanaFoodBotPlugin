from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *
import random

# 食物列表
food = [
    "三明治和牛奶", 
    "豆浆油条", 
    "燕麦粥", 
    "煎蛋配吐司", 
    "水果沙拉",
    "牛肉面",
    "披萨",
    "寿司",
    "炒饭",
    "沙拉轻食",
    "火锅",
    "牛排",
    "烤鸡",
    "海鲜大餐",
    "素食套餐"
]

"""
当用户输入"早上/中午/晚上吃什么"时，回复推荐食物
"""

class MealRecommendPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        pass

    async def initialize(self):
        pass

    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message.strip()
        time_keyword = None
        reply_template = "普拉娜建议{}吃{}哦"
        
        if msg.startswith("早上吃什么"):
            time_keyword = "早上"
        elif msg.startswith("中午吃什么"):
            time_keyword = "中午"
        elif msg.startswith("晚上吃什么"):
            time_keyword = "晚上"
        
        if time_keyword:
            # 随机选择食物
            selected_food = random.choice(food)
            reply = reply_template.format(time_keyword, selected_food)
            
            # 输出调试信息
            self.ap.logger.debug("推荐食物: {}".format(selected_food))
            
            # 回复消息
            ctx.add_return("reply", [reply])
            ctx.prevent_default()

    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message.strip()
        time_keyword = None
        reply_template = "普拉娜建议{}吃{}哦"
        
        if msg.startswith("早上吃什么"):
            time_keyword = "早上"
        elif msg.startswith("中午吃什么"):
            time_keyword = "中午"
        elif msg.startswith("晚上吃什么"):
            time_keyword = "晚上"
        
        if time_keyword:
            # 随机选择食物
            selected_food = random.choice(food)
            reply = reply_template.format(time_keyword, selected_food)
            
            # 输出调试信息
            self.ap.logger.debug("推荐食物: {}".format(selected_food))
            
            # 回复消息
            ctx.add_return("reply", [reply])
            ctx.prevent_default()

    def __del__(self):
        pass
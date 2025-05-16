from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import random

# 食物列表
food = [
    "豆浆油条",
    "鸡蛋灌饼",
    "皮蛋瘦肉粥",
    "小笼包",
    "煎饼果子",
    "肠粉",
    "牛奶燕麦",
    "三明治",
    "法式吐司",
    "粢饭团",
    "黄焖鸡米饭",
    "牛肉拉面",
    "麻辣香锅",
    "盖浇饭",
    "海南鸡饭",
    "酸菜鱼",
    "番茄牛腩饭",
    "卤肉饭",
    "咖喱鸡饭",
    "排骨饭",
    "火锅",
    "烧烤",
    "寿司拼盘",
    "意大利面",
    "披萨",
    "牛排套餐",
    "烤鱼",
    "小龙虾",
    "韩式炸鸡",
    "日式拉面",
    "蔬菜沙拉",
    "鸡胸肉糙米饭",
    "藜麦沙拉",
    "素食套餐",
    "低脂三明治",
    "芒果班戟",
    "提拉米苏",
    "章鱼小丸子",
    "鸡蛋仔"
]

# 注册插件
@register(name="PlanaFood", description="FoodToEat", version="0.1", author="WindRose")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        if msg == "早上吃什么" or msg == "早饭吃什么":  

            # 输出调试信息
            self.ap.logger.debug(f"普拉娜建议早上吃{random.choice(food)}哦")

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("reply", [f"普拉娜建议早上吃{random.choice(food)}哦"])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "中午吃什么" or msg == "中饭吃什么":  

            # 输出调试信息
            self.ap.logger.debug(f"普拉娜建议中午吃{random.choice(food)}哦")

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("reply", [f"普拉娜建议中午吃{random.choice(food)}哦"])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "晚上吃什么" or msg == "晚饭吃什么":  

            # 输出调试信息
            self.ap.logger.debug(f"普拉娜建议晚上吃{random.choice(food)}哦")

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("reply", [f"普拉娜建议晚上吃{random.choice(food)}哦"])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 GroupNormalMessageReceived 的对象
        if msg == "早上吃什么" or msg == "早饭吃什么":  

            # 输出调试信息
            self.ap.logger.debug(f"普拉娜建议早上吃{random.choice(food)}哦")

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("reply", [f"普拉娜建议早上吃{random.choice(food)}哦"])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "中午吃什么" or msg == "中饭吃什么":  

            # 输出调试信息
            self.ap.logger.debug(f"普拉娜建议中午吃{random.choice(food)}哦")

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("reply", [f"普拉娜建议中午吃{random.choice(food)}哦"])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()
        elif msg == "晚上吃什么" or msg == "晚饭吃什么":  

            # 输出调试信息
            self.ap.logger.debug(f"普拉娜建议晚上吃{random.choice(food)}哦")

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("reply", [f"普拉娜建议晚上吃{random.choice(food)}哦"])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass

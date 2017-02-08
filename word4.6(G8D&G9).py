# word4.6
# -*- coding: GBK -*-
# word1.0 made by Zhao Shuo on 2015-11-27
# word2.0 updated by Zhao Shuo on 2015-11-29
# word2.5 updated by Zhao Shuo on 2016-02-12
# word3.0 updated by Zhao Shuo on 2016-02-22
# word3.5 updated by Zhao Shuo on 2016-03-12
# word3.6 updated by Zhao Shuo on 2016-03-19
# word4.0 updated by Zhao Shuo on 2016-08-09
# word4.1 updated by Zhao Shuo on 2016-08-19
# word4.2 updated by Zhao Shuo on 2016-08-22
# word4.3 updated by Zhao Shuo on 2016-08-26
# word4.5 updated by Zhao Shuo on 2017-01-22
# word4.6 updated by Zhao Shuo on 2017-02-08

# 赵硕制作 qq：2090737490
# 考单词程序4.6
# 可以考在英汉列表里的单词
# 并可以随机考单词（不重不漏）
# 还可以得到错误单词的个数，并总结错误的单词，方便背诵
# 2.0新增功能：
# 可以对照英语词和汉语词表的个数，若数量不对应会提示检查
# 可以统计出总词数，并在开头汇报
# 在开头会汇报所有需要考的单词和对应汉语，方便背诵
# 如果单词错误，会提示还剩下多少个单词没有考，用于掌握进度
# 每一回合结束会统计出正确率，并汇报
# 2.5新增功能：
# 可选择是否进行随机考试（可以按顺序进行考察，便于调试）
# 增加了回合数
# 改进了退出界面样式
# 3.0新增功能:
# 本版本可选择考哪一个单元
# 还可以选择考哪几个单元
# 也可以选择考全部单元
# 本次升级可以集合多个列表进行考单词的选择
# 3.5新增功能：
# 支持考某个（些）单元中的部分词，方便紧仅背诵部分词
# 修复了选择第10单元和选择不输入的bug
# 3.6新增功能：
# 修复了考部分词的bug
# 4.0新增功能：
# 增加了给出英文选择汉意的模式
# 增加了测验模式
# 修复了已知bug
# 4.1新增功能：
# 新增随机考汉意的模式
# 改进了交互对话
# 修复了已知bug
# 4.2新增功能：
# 改进选择测试单词的样式，更加便捷，且方便更多单元
# 完善词库（九年级全部单词已完成）
# 4.3新增功能：
# 修复了部分单词错误
# 增加了目录索引功能
# 改变了选取单元的样式
# 增加汉意模式统计剩余次数模式
# 增加统计单词错误次数功能
# 测验增加测验汉意模式
# 4.5新增功能：
# 改进了词库的选择方式
# 可以随意增添词库
# 4.6新增功能：
# 修复了部分单词错误
# 新增了U8D单词
# 考英语模式下增加了剩余词数
# 改进了考英语模式的速度算法



# 未来升级预告：
# 测验增加测验汉意模式 ****
# 改进代码规范
# 升级交互体验（模式选择）****
# 完善词库 ****
# 改进词库索引 ****
# 增加统计单词错误次数功能 ****
# 增加汉意模式统计剩余次数模式 ****
# 改进选择模式的交互方式
# 增加自动模式
# 增加倒计时模式
# 改进汉意候选单词选择方法
# 统计每个单词错误次数
# 将错误次数大于一定次数的整合成列表并保存


# 欢迎使用
# 使用前需要将所需考的单词及其汉语录入到word and Chinese list块中的相应列表里

# ------------------------------word and Chinese list--------------------------------------------
# Unit1
# "","","","","","","","","","","","","","","","","",""

# +++++++++++++++++++++++Grade 7++++++++++++++++++++++++++++++



# ++++++++++++++++++++++++Grade 8+++++++++++++++++++++++++++++++
#Unit1

Name_English_G8D_U01 = "英语八年级下第01单元"
Questions_English_G8D_U01 = ['matter',"What's the matter?",'sore','have a cold','stomachache','have a stomachache','foot','neck','stomach','throat','fever','lie',
          'lie down','rest','cough','X-ray','toothache',"take one's temperature",'headache','have a fever','break','take breaks',
          'hurt','passenger','off','get off',"to one's surprise",'onto','trouble','hit','right away','get into','herself',
          'bandage','press','sick','knee','nosebleed','breathe','sunburned','ourselves','climber','be used to','risk',
          'take risks','accident','situation','kilo','rock','run out','knife','cut off','blood','mean','get out of',
          'importance','decision','control','be in control of','spirit','death','give up','nurse',]
Answers_English_G8D_U01 = ['问题', "怎么了？",'疼痛的','得了感冒','胃痛','得了胃痛','脚','脖子','胃','喉咙','发烧','平躺',
          '躺下','放松休息','咳嗽','x光','牙痛','量体温','头痛','得了发烧','间歇休息','做个休息',
          '疼痛、受伤','乘客','离开、不工作','下车','使...惊讶','向朝','问题、苦恼','击打','立即马上','陷入参与','她自己','绷带',
          '按','生病的','膝盖','鼻出血','呼吸','晒伤的','我们自己','登山者','适用于','危险','冒险',
          '事故','情况状况','千克公斤','岩石','用尽耗尽','刀','切除','血','意思是','离开、从。。。出来','重要性',
          '决定抉择','限制管理','掌管管理','勇气意志','死死亡','放弃','护士']

#Unit2

Name_English_G8D_U02 = "英语八年级下第02单元"
Questions_English_G8D_U02 = ['clean up','cheer','cheer up','give out','volunteer','come up with','put off',
          'sign','notice','hand out','call up','used to','lonely','care for',
          'several','strong','feeling','satisfaction','joy','owner','try out',
          'journey','raise','midnight','alone','repair','fix','fix up',
          'give away','take after','broken','wheel','letter','Miss','set up',
          'disabled','make a difference','blind','deaf','imagine','difficulty','open',
          'door','carry','train','excited','training','kindness','clever',
          'understand','change','interest','sir','madam']    #英语单词表，录入需要考的单词
Answers_English_G8D_U02 = ['打扫干净','欢呼 喝彩','变得高兴起来','分发散发','义务做 志愿者','想出提出','推迟',
          '标志 信号','通知 注意到','分发','打电话给','曾经...','孤独的寂寞的','照顾 非常喜欢',
          '几个数个一些','强壮的强烈的','感觉感触','满足满意','高兴愉快','物主主人','试用',
          '旅行 行程','募集征集','子夜午夜','独自单独','修理修补','修理安装','修理装饰',
          '赠送捐赠','（外貌或行为)像','破损的残缺的','车轮轮子','信、函','女士小姐','建立设立',
          '丧失能力','影响 有作用','瞎的失明的','聋的','想象 设想','困难难题','打打开',
          '门','拿','培训、训练v.','激动的、兴奋的','训练、培训n.','仁慈、善良','聪明的、聪颖的','理解','变化改变',
          '兴趣关注','先生','夫人女士']    #汉语对照表（需与英语单词表一一对应录入）


#Unit 3

Name_English_G8D_U03 = "英语八年级下第03单元"
Questions_English_G8D_U03 = ['rubbish','take out the rubbish','fold','sweep','floor','mess','throw',
          'all the time','neither','shirt','as soon as','pass','borrow','lend',
          'finger','hate','chore','while','snack','stress','waste',
          'in order to','provide','anyway','depend','depend on','develop','independence',
          'fairness','since','neighbor','take care of','ill','drop','independent',
          'fair','unfair']  # 英语单词表，录入需要考的单词
Answers_English_G8D_U03 = ['垃圾','倒垃圾','对折折叠','扫 打扫','地板','杂乱不整洁','扔',
          '频繁 反复','也不 两者都不','衬衫','一...就...','给 递 通过','借 借用','借给 借出',
          '手指','厌恶 讨厌','杂务','当...的时候','点心 快餐','精神压力 心理负担','浪费',
          '为了 目的是','提供 供应','而且 加之','依靠 信赖','依靠信赖（短语）','发展 壮大','独立',
          '公正性 合理性（n）','因为既然 从...以后','邻居','照顾 处理','有病不舒服','落下 掉下','独立的自主的',
          '公正的 合理的（adj）','不合理的 不公正的']  # 汉语对照表（需与英语单词表一一对应录入）


#Unit 4
Name_English_G8D_U04 = "英语八年级下第04单元"
Questions_English_G8D_U04 = ['allow','wrong',"What's wrong?",'look through','guess','deal',
          'big deal','work out','get on with','relation','communication','argue',
          'cloud','elder','instead','whatever','nervous','offer',
          'proper','secondly','communicate','explain','clear','copy',
          'return','anymore','member','pressure','compete','opinion',
          'skill','typical','football','cut out','quick','continue',
          'compare','compare...with','crazy','push','development','cause',
          'usual',"in one's opinion",'perhaps']  # 英语单词表，录入需要考的单词
Answers_English_G8D_U04 = ['允许','有毛病 错误的','哪不舒服','浏览','猜测 估计','协议 交易',
          '重要的事','成功的发展 解决','和睦相处 关系良好','关系 联系 交往','交流 沟通n','争吵 争论',
          '云 云朵','年纪较长的','代替 反而 却','任何 每一','焦虑的','主动提出 自愿给予',
          '正确的 恰当的','第二 其次（adv）','交流 沟通v','解释 说明','清楚易懂的 晴朗的','复制',
          '归还 返回','再也不','成员','压力','竞争','意见想法',
          '技艺 技巧','典型的','橄榄球 足球','删除 删去','快的 迅速的','持续 继续存在',
          '比较','比较 对比（短语）','不理智的 疯狂的','鞭策 督促 推动','发展 发育 成长','造成 引起',
          '通常的 寻常的','依...看','可能 大概 也许']


#Unit5
Name_English_G8D_U05 = "英语八年级下第05单元"
Questions_English_G8D_U05 = ['rainstorm','alarm','go off','begin','heavily','suddenly','pick up',
          'strange','storm','wind','light','report','area','wood','window',
          'flashlight','match','beat','against','at first','asleep','fall asleep','die down',
          'rise','fallen','apart','have a look','icy','kid','realize',"make one's way",
          'passage','pupil','completely','shocked','silence','in silence','recently','take down',
          'terrorist','date','tower','truth']  # 英语单词表，录入需要考的单词
Answers_English_G8D_U05 = ['暴风雨','闹钟','发出响声','开始','大量地','突然 忽然','接电话',
          '奇特的 奇怪的','暴风雨（短）','风','光','报道 公布','地域 地区','木木头','窗窗户',
          '手电筒','火柴','敲打 打败','撞 碰','起初 起先','睡着','进入梦乡','逐渐变弱 逐渐消失',
          '升起 增高','倒下的 落下的','分离分开','看一看','覆盖着冰的 冰冷的','开玩笑 欺骗','理解 领会','前往',
          '章节','学生','彻底地 完全地','惊愕的 受震惊的','沉默 无声','沉默 无声（短语）','不久前 最近','拆除 记录',
          '恐怖分子','日期','塔','实情 事实']   #汉语对照表（需与英语单词表一一对应录入）


# Unit6
Name_English_G8D_U06 = "英语八年级下第06单元"
Questions_English_G8D_U06 = ['shoot','stone','weak','god','remind','bit','a little bit',
          'silly','instead of','turn...into','object','hide','tail','magic','stick',
          'excite','Western','once upon','stepsister','prince','fall in love','fit','couple',
          'smile','marry','get married','gold','emperor','silk','underwear','nobody',
          'stupid','cheat','stepmother','wife','husband','whole','scene','moonlight',
          'shine','bright','ground','lead','voice','brave']
Answers_English_G8D_U06 = ['射击','石头','虚弱的 无力的','神 上帝','提醒','一点','有点 稍微',
          '愚蠢的 不明事理的','代替 反而','变成','物体 物品','隐藏 隐蔽','尾巴','有魔力','棍',
          '使激动','西方国家','从前','继姐妹','王子','喜欢上 爱上','适合 合身','夫妻',
          '微笑','结婚','结婚（短）','金子','皇帝','丝绸','内衣','没有人',
          '愚蠢的','欺骗 骗子','继母','妻子 太太', '丈夫','全部的 整体的','场 场景','月光',
            '发光','光亮地 明亮的','地面','带路 领路','声音','勇敢的无谓的']


# Unit7
Name_English_G8D_U07 = "英语八年级下第07单元"
Questions_English_G8D_U07 = ['square','meter','deep','desert','population','Asia','feel free',
          'tour','tourist','wall','amazing','ancient','protect','wide','as far as I know','man-made',
          'achievement','southwestern','thick','include','freezing','condition','take in','succeed',
          'challenge','in the face of','achieve','force','nature','even though','ocean','the Pacific Ocean',
          'cm','weigh','birth','at birth','up to','adult','bamboo','endangered',
          'research','keeper','awake','excitement','walk into','fall over','or so','illness',
            'wild','government','whale','oil','protection','huge']
Answers_English_G8D_U07 = ['正方形','米','深的','沙漠','人口','亚洲','随便',
          '旅游','旅行者','墙','令人大为惊奇的','古代的','保护','宽的','就我所知','人造的',
          '成就 成绩','西南的','厚的','包括','极冷的','条件','吸入','实现目标 成功',
          '挑战 考验','面对','达到 完成 成功','力量','自然界 大自然','即使 虽然','大海 海洋','太平洋',
          '厘米','重量是','出生','出生时','达到','成年的 成人','竹子','濒危的',
          '研究 调查','饲养员','醒着','激动 兴奋','走路时撞着','绊倒','大约','疾病 病',
            '野生的','政府 内阁','鲸','油','保护 保卫','巨大的 极多的']


# Unit 8
Name_English_G8D_U08 = "英语八年级下第08单元"
Questions_English_G8D_U08 = ['treasure','island','full of','classic','page','hurry','hurry up',
          'due','ship','tool','gun','mark','sand','cannibal','towards',
          'land','fiction','science fiction','technology','French','pop','rock','band',
          'country music','forever','abroad','actually','ever since','fan','southern','modern',
          'success','belong','one another','laughter','beauty','million','record','introduce',
          'line']
Answers_English_G8D_U08 = ['珠宝 财富','岛','满是...的','名著','页','匆忙 赶快','赶快 急忙',
          '预期 预定','船','工具','枪炮','记号 分数','沙','食人肉者','朝向对着',
          '陆地 大地','小说','科幻小说','科技 工艺','法语','流行音乐','摇滚乐','乐队',
          '乡村音乐','永远','在国外','事实上','自从','迷 狂热爱好者','南方的','现代的',
          '成功n','属于','互相','笑 笑声', '美丽','一百万','唱片 录制','介绍',
          '行 排']


# Unit 9
Name_English_G8D_U09 = "英语八年级下第09单元"
Questions_English_G8D_U09 = ['amusement','amusement park','somewhere','camera','invention','invent','unbelievable',
          'progress','rapid','unusual','toilet','encourage','social','peaceful','tea art',
          'performance','perfect','tea set','itself','collect','a couple of','German','theme',
          'ride','province','thousand','thousand of','on the one hand...on the other hand','safe','simply','fear',
          'whether','Indian','Japanese','fox','all year round','equator','whenever','spring',
          'mostly','location']
Answers_English_G8D_U09 = ['娱乐','游乐场','在某处','照相机','发明n','发明v','难以置信',
          '进步','迅速的 快速的','特别的','厕所 坐便器','鼓励','社会的','和平的 安宁的','茶艺',
          '表演 演出','完美的 完全的','茶具','它自己','收集 采集','两个 一对','德国人','主题',
          '短途旅行','省份','一千','数以千计的 许许多多多的','一方面 另一方面','安全 ','仅仅 只','害怕',
          '不管','印度人','日本人','狐狸','全年','赤道','在任何时候','春天',
          '主要的','地点 位置']


# Unit 10

Name_English_G8D_U10 = "英语八年级下第10单元"
Questions_English_G8D_U10 = ['yard','yard sale','sweet','memory','cent','toy','bear',
          'maker','bread maker','scarf','soft','soft toy','check','check out','board',
          'board game','junior','junior high school','clear','clear out','bedroom','no longer','own',
          'railway','part','part with','certain','as for','honest','to be honest','while',
          'truthful','hometown','nowadays','search','among','crayon','shame','regard',
          'count','century','according','opposite','especially','childhood','consider','close to','hold']
Answers_English_G8D_U10 = ['院子','庭院拍卖会','甜蜜的','记忆 内存条','分 分币','玩具','熊',
          '生产者 制订者','面包机','围巾 头巾','软的 柔软的','软体玩具 布绒玩具','检查审查','察看 观察','板 木板',
          '棋类游戏','低下的','初级中学','清理 清除','清理 丢掉','卧室','不再 不复','拥有',
          '铁路 铁道','离开 分开','放弃 交出','某种某事某人','至于 关于','诚实的 老实的','说实在的','一段时间 一会儿',
          '诚实的 真实的','家乡 故乡','现今 现在 目前','搜索','...之一','彩色铅笔 蜡笔 粉笔','羞耻 惭愧','将...认为 看待',
          '数数','百年 世纪','依据按照','对面的 另一边的','尤其 特别 格外','童年 幼年','注视 仔细考虑','几乎 接近','拥有 抓住']



# +++++++++++++++++++++++Grade 9+++++++++++++++++++++++++++++++
Name_English_G9_PP = "英语九年级过去分词"
Questions_English_G9_PP = ['be','bear','beat','become','begin','blow','break','bring','build','burn',
             'buy','catch','choose','come','cost','cut','dig','do','draw','dream',
            'drink',"drive","eat","fall","feed","feel","fight","find","fly","forget","get",
            "give","go","grow","hang","have","hear","hide","hit",'hold',
            "hurt","keep","know","lay","lead","learn","leave","lend","let","lie",
            "light","lose","make","mean","meet","mistake","pay","put","read","ride",
            "ring","rise","run","say","see","sell","send","set","shake","shine","show",
            "shut","sing","sit","sleep","smell","speak","speed","spell","spend","spread",
            "stand","steal","stick","swim","take","teach","tell","think","throw",
            "understand","wake","wear","win",'write']
Answers_English_G9_PP = ['was been','bore born','beat beaten','became become','began begun',
             'blew blown','broke broken','brought brought','built built','burnt/burned burnt/burned',
             'bought bought','caught caught','chose chosen','came come','cost cost','cut cut',
             'dug dug','did done','drew drawn','dreamt/dreamed dreamt/dreamed',
            "drank drunk","drove driven","ate eaten","fell fallen","fed fed","felt felt",
            "fought fought","found found","flew flown","forgot forgotten","got got/gotten",
            "gave given","went gone","grew grown","hung hung","had had","heard heard",
            "hid hidden","hit hit","held held","hurt hurt","kept kept","knew known",
            "laid laid",'led led',"learnt/learned learnt/learned","left left","lent lent",
            "let let","lay lain","lit/lighted lit/lighted","lost lost","made made",
            "meant meant","met met","mistook mistaken","paid paid","put put","read read",
            "rode ridden","rang rang","rose risen","ran run","said said","saw seen",
            "sold sold","sent sent","set set","shook shaken","shone shone","showed shown",
            "shut shut","sang sung","sat sat","slept slept","smelt/smelled smelt/smelled",
            "spoke spoken","sped/speeded sped/speeded","spelt/spelled spelt/spelled",
            "spent spent","spread spread","stood stood","stole stolen","stuck stuck",
            "swam swum","took taken","taught taught","told told","thought thought",
            "threw thrown","understood understood","woke woken","wore worn",
            "won won","wrote written"]


Name_English_G9_U01 = "英语九年级1单元"
Questions_English_G9_U01 = ["textbook","conversation","aloud","pronunciation","sentence","patient","expression","discover",
            "secret","look up","grammar","repeat","note","pal","physics",'chemistry',"memorize","pattern","pronounce","increase","speed","partner","born","be born with","ability",
            "create","brain","active","attention","pay attention to","connect","connect...with","overnight",
            "review","knowledge","lifelong","wisely"]
Answers_English_G9_U01 = ["教科书课本","交谈 谈话","大声地 出生地","读音 发音n.","句子","有耐心的 病人","表情 表示 表达方式",
            "发现 发觉v.","秘密秘诀","查阅 抬头看","语法","重做 重复","笔记 记录","朋友 伙伴","物理 物理学","化学",
            "记忆 记住","模式 方式","发音v.","增加 增长","速度","搭档 同伴","出生","天生具有","能力 才能","创造 创建","大脑","活跃的 积极的adj.",
            "注意（词）","注意 关注（短语）","连接","把...和...连接起来","一夜之间","回顾 复习","知识 学问","终身的","明智地"]



#Unit2

Name_English_G9_U02 = "英语九年级第2单元"
Questions_English_G9_U02 = ["mooncake","lantern","stranger","relative","put on","pound","folk",
            "goddess","whoever","steal","lay","lay out","dessert","garden","tradition",
            "admire","tie","haunted","ghost","trick","treat","spider","Christmas","lie","novel","eve",
            "dead","business","punish","warn","end up","present","warmth","spread","Mid-Autumn Festival",
            "Mother's Day","Father's Day","Halloween","Easter"]    #英语单词表，录入需要考的单词
Answers_English_G9_U02 = ["月饼","灯笼","陌生人","亲属","增加 发胖","英镑、磅","民间的民俗的",
            "女神","无论谁","偷 窃取","安置 安放","摆开 布置","甜点 甜食","花园 园子",
            "传统","欣赏 仰慕","领带 捆","闹鬼的","鬼 鬼魂","花招 把戏","款待 招待",
            "蜘蛛","圣诞节","存在 平躺处于","小说","前夕 前夜","死的 失去生命的",
            "生意 商业","处罚 惩罚","警告 告诫","最终成为 最后处于","现在 礼物 现在的",
            "温暖 暖和","传播 展开 蔓延 传播","中秋节","母亲节","父亲节","万圣节前夕","复活节"]    #汉语对照表（需与英语单词表一一对应录入）


#Unit 3

Name_English_G9_U03 = "英语九年级第3单元"
Questions_English_G9_U03 = ["restroom","stamp","bookstore","beside","postcard","pardon","washroom",
            "bathroom","normally","rush","suggest","pass by","staff","grape","central",
            "nearby","pardon me","mail","east","fascinating","inexpensive",
            "uncrowded","convenient","mall","clerk","corner","politely",
            "request","direction","correct","polite","direct","speaker",
            "whom","impolite","address","underground","parking lot","course",
            "Italian"]  # 英语单词表，录入需要考的单词
Answers_English_G9_U03 = ["洗手间（美），公共厕所","邮票 印章","书店","在旁边 在附近",
            "明信片","原谅 再说一遍","洗手间 厕所","浴室 洗手间","通常 正常情况下",
            "仓促 急促","建议 提议v.","路过 经过","管理人员 职工","葡萄","中心的",
            "邻近的 附近的","抱歉 对不起请再说一遍","邮寄邮件","东 东方的 向东","迷人的",
            "不昂贵的","不拥挤的","便利的 方便的","商场 购物中心","职员","拐角 角落",
            "礼貌的 客气的","要求 请求","方向 方位","正确的 恰当的","有礼貌的 客气的adv.",
            "直接的 直率的","发言者","谁 什么人","不礼貌的 粗鲁的","住址 地址",
            "地下的 地铁","停车场","课程 学科","意大利人 意大利语"]  # 汉语对照表（需与英语单词表一一对应录入）

#"","","","","","","","","","","","","","","","","",""
#Unit 4
Name_English_G9_U04 = "英语九年级第4单元"
Questions_English_G9_U04 = ["humorous","silent","helpful","from time to time","score",
            "background","interview","Asian","deal","deal with","shyness",
            "dare","crowd","ton","private","guard","require","European",
            "African","British","speech","public","in public","ant",
            "insect","seldom","influence","absent","fail","examination",
            "boarding","in person","exactly","pride","take pride in","proud",
            "be proud of","general","introduction"]  # 英语单词表，录入需要考的单词
Answers_English_G9_U04 = ["有幽默感的","不说话的 沉默的","有用的 有帮助的","时常有时","得分进球",
            "背景","采访 面试","亚洲的亚洲人","对付 对待","应对 处理","害羞 腼腆n.",
            "敢于 胆敢","人群 观众","吨 大量许多","私人的 私密的","警卫 看守 保卫","需要 要求",
            "欧洲人","非洲人","英国的","讲话 发言","民众 公开的","公开地 在别人面前",
            "蚂蚁","昆虫","不常 很少","影响","缺席 不在","不及格 失败","考试 审查","寄宿学校",
            "亲身 亲自","确切的 精确地","自豪 骄傲n.","为...感到自豪","自豪的 骄傲的adj.","为...骄傲 感到自豪","总的 普遍的 常规的 将军",
            "介绍"]


#Unit5
Name_English_G9_U05 = "英语九年级第5单元"
Questions_English_G9_U05 = ["chopstick","coin","fork","blouse","silver","glass","cotton",
            "steel","fair","environmental","grass","leaf","produce",
            "widely","be known for","process","pack","product","France",
            "no matter","local","brand","avoid","handbag","mobile","everyday",
            "boss","Germany","surface","material","traffic","postman","cap",
            "glove","international","competitor","its","form","clay","celebration",
            "balloon","paper cutting","scissors","lively","fairy","historical",
            "heat","polish","complete"]  # 英语单词表，录入需要考的单词
Answers_English_G9_U05 = ["筷子","硬币","叉子","女短上衣 衬衫","银 银器","玻璃","棉花","钢铁","展览会 交易会",
            "自然环境的 有关环境的","草 草地","叶 叶子","生产 制造 出产","广泛地 普遍地",
            "以...闻名 为人知晓","加工 处理 过程","包装 装箱","产品 制品","法国",
            "不论 无论","当地的 本地的","品牌 牌子","避免 回避","小手提包","可移动的",
            "每天的 日常的 每天","老板 上司","德国","表面 表层 微软平板","材料 原料","交通 路上行驶的车辆",
            "邮递员","帽子","手套","国际的","参赛者 竞争者","它的","形式 类型","黏土 陶土",
            "庆典 庆祝活动","气球","剪纸","剪刀","生气勃勃的 鲜艳的","童话故事","历史的","高温 加热",
            "磨光 润色","完成"]   #汉语对照表（需与英语单词表一一对应录入）


# Unit6
Name_English_G9_U06 = "英语九年级第6单元"
Questions_English_G9_U06 = ["heel","scoop","electricity","style","project","pleasure",
            "zipper","daily","have a point","website","pioneer","list",
            "mention","accidental","by accident","nearly","ruler","boil",
            "remain","smell","saint","national","trade","take place","doubt",
            "without doubt","fridge","low","somebody","translate","lock",
            "earthquake","sudden","all of a sudden","bell","biscuit",
            "cookie","musical","instrument","crispy","salty","sour",
            "by mistake","customer","the Olympics","Canadian","divide",
            "divide...into","basket","popularity","not only...but also...",
            "look up to","hero","professional"]
Answers_English_G9_U06 = ["鞋跟 足跟","勺铲子","电 电能","样式 款式","项目 工程","高兴 愉快",
            "拉链 拉锁","每日的 日常的 每日一次的","有道理","网站","先锋 先驱","列表","提到 说道",
            "意外的 偶然的","偶然 意外地（短语）","几乎 差不多","统治者 支配者","煮沸烧开",
            "保持不变 剩余","气味","圣人 圣徒","国家的 民族的","贸易 教益","发现 出现（短语）",
            "疑惑 疑问 怀疑","毫无疑问 的确","冰箱","低的 矮的","某人 重要人物",
            "翻译","锁上 锁","地震","突然的","突然（短语）","铃声","饼干","曲奇饼",
            "音乐的","器械 仪器 工具","脆的 酥脆的","咸的","酸的","错误地 无意中",
            "顾客 客户","奥林匹克运动会","加拿大的 加拿大人","分开 分散","把...分开",
            "篮筐","受欢迎 普及","不但...而且...","钦佩 仰慕","英雄","职业的 专业的"]

#"","","","","","","","","","","","","","","","","",""
# Unit7
Name_English_G9_U07 = "英语九年级第7单元"
Questions_English_G9_U07 = ["license","safety","smoke","part-time","pierce","earring","flash",
            "tiny","cry","field","hug","lift","badly","talk back","awful",
            "teen","regret","poem","community","keep...away from","chance",
            "make one's own decision","educate","manage","society","get in the way of",
            "support","enter","choice"]
Answers_English_G9_U07 = ["证 证件","安全","吸烟 烟","兼职的","扎 刺破 穿透","耳环 耳饰","闪光灯 闪光",
            "极小的微小的","哭 喊叫","田野 场地","拥抱 搂抱","举起抬高电梯","严重地 差",
            "回嘴 顶嘴","很坏的 讨厌的","青少年","感到遗憾 懊悔","诗 韵文","社区 社团",
            "避免接近 远离","机会 可能性","自己做决定","教育 教导","经营 使用 完成 应付",
            "社会","挡...的路 妨碍","支持","进来 进去 进入","选择 挑选n."]


# Unit 8
Name_English_G9_U08 = "英语九年级第8单元"
Questions_English_G9_U08 = ["whose","truck","picnic","rabbit","attend","valuable","pink","anybody",
            "happening","noise","policeman","wolf","uneasy","laboratory",
            "outdoors","coat","sleepy","land","alien","run after","suit",
            "express","at the same time","circle","Britain","mystery",
            "receive","historian","leader","midsummer","medical","purpose",
            "prevent","energy","position","burial","honor","ancestor","victory",
            "enemy","period","hard-working"]
Answers_English_G9_U08 = ["谁的","卡车 货车","野餐","兔 野兔","出席 参加","贵重的 宝贵的",
            "粉红色","任何人","事件 发生的事情","声音 噪音","男警察","狼","担心的 不安的",
            "实验室","在户外 在野外","外套 外衣","困倦的 瞌睡的","着陆 降落","外星人",
            "追逐 追赶","西服 套装 适合","表达表示","在同一时刻 一起","圆圈 圈出",
            "大不列颠","奥秘 神秘事物","接收 收到","历史学家","领导领袖","仲夏中夏",
            "医疗的医学的","目的 目标","阻止 阻挠","力量 精力","位置 地方","埋葬 安葬",
            "尊重 表示敬意","祖宗 祖先","胜利成功","敌人 仇人","一段时间 时期","工作努力的 辛勤的"]


# Unit 9
Name_English_G9_U09 = "英语九年级第9单元"
Questions_English_G9_U09 = ["prefer","lyrics","Australian","electronic","suppose","smooth",
            "spare","director","case","in that case","war","stick","stick to",
            "down","dialog","ending","documentary","drama","plenty","plenty of",
            "shut","shut off","superhero","once in a while","intelligent",
            "sense","sadness","pain","reflect","moving","perform","lifetime",
            "pity","total","in total","master","praise","recall","wound","painful"]
Answers_English_G9_U09 = ["更喜欢","歌词","澳大利亚人","电子设备的","推断料想","悦耳的平滑的","空闲的不用的 抽出",
            "导演 部门负责人","情况 实情","既然那样 假使那样的话","战争","粘贴","坚持 固守",
            "悲哀 沮丧","对话 对白","结局 结尾","记录片","戏 剧","大量 众多","大量充足（短语）",
            "关闭 关上","关闭 停止运转","超级英雄","偶尔地","有才智的 聪明的","感觉到 意识到  感觉意识",
            "悲伤 悲痛","痛苦 疼痛 苦恼","反映 映出","动人的 令人感动的","表演执行","一生有生之年",
            "遗憾怜悯同情","总数 合计总的 团体的","总共 合计","大师主人掌握","表扬 赞扬","回想起 回忆起",
            "伤 伤口 创伤 使身体受伤 伤害","令人疼痛的"]


# Unit 10

Name_English_G9_U10= "英语九年级第10单元"
Questions_English_G9_U10 = ["custom","bow","kiss","greet","relaxed","value","drop by","capital",
             "after all","noon","mad","get mad","effort","make an effort",
             "passport","clean...off","chalk","blackboard","northern","coast",
             "season","knock","eastern","take off","worth","manner","empty",
             "basic","exchange","go out of one's way","make...feel at home",
             "teenage","granddaughter","behave","except","elbow","gradually",
             "get used to","suggestion"]
Answers_English_G9_U10 = ["风俗 习俗","鞠躬","亲吻 接吻","和...打招呼 迎接","放松的 自在的",
             "重视 价值","随便访问 随便进入","首都 国都","毕竟 终归","正午 中午",
             "很生气 疯的","大动肝火 气愤","努力 尽力","作出努力","护照","把..擦掉",
             "粉笔","黑板","北方的 北部的","海岸 海滨","季 季节","敲 敲击声","东方的",
             "脱下 起飞","值的 有价值的","方式 礼貌礼仪","空的 空洞的","基本的 基础的",
             "交换","特地 格外努力","使某人感到宾至如归","青少年的","孙女","表现 举止",
             "除...之外 除了 只是","胳膊 肘","逐步地 渐进地","习惯于","建议n."]


Name_English_G9_U11= "英语九年级第11单元"
Questions_English_G9_U11 = ["rather","would rather","drive","drive sb. crazy",
             "the more...the more...","lately","be friends with sb.","leave out",
             "friendship","king","power","prime","minister","prime minister",
             "banker","fame","pale","queen","call in","examine","nor",
             "neither...nor...","palace","wealth","to start with","grey",
             "lemon","uncomfortable","weight","shoulder","goal","let...down",
             "coach","kick","kick sb. off","be hard on sb.","besides",
             "teammate","courage","rather than","guy","pull","pull together",
             "relief","nod","agreement","fault","disappoint"]
Answers_English_G9_U11 = ["相当 相反","宁愿","迫使","使人发疯","越...越...","最近 不久前","成为某人的朋友",
             "忽略 不提及 不包括","友谊 友情","国王 君主","权力 力量","首要的 基本的",
             "大臣 部长","首相 大臣","银行家","名声 声誉","苍白的 灰白的","王后女王",
             "召来 叫来","检查 检验","也不","既不 也不","王宫 宫殿","财富","作为开始 起初 开始时",
             "阴沉的 灰色的","柠檬","使人不舒服的","重量 分量","肩膀","球门 射门 目标",
             "使...失望","教练 私人教师","踢踹","开除某人","对某人苛刻要求严厉","而且",
             "同队队员 队友","勇敢 勇气","而不是","家伙 伙计们","拉 拖","齐心协力 通力合作",
             "轻松 解脱","点头","一致 同意","过失 缺点","使失望"]


Name_English_G9_U12= "英语九年级第12单元"
Questions_English_G9_U12 = ["unexpected","by the time...","backpack","oversleep","ring",
             "give...a lift","block","in line with","worker","stare","disbelief",
             "above","burn","burning","alive","airport","till","west","cream",
             "workday","pie","show up","bean","market","by the end of","fool",
             "costume","embarrassed","costume party","announce","spaghetti",
             "hoax","sell out","discovery","lady","cancel","officer","believable",
             "disappear","embarrassing"]
Answers_English_G9_U12 = ["出乎意料的 始料不及的","在...（时间）之前","背包","睡过头","鸣 响","捎...一程",
             "街区","成一排","工作者 工人","盯着看 凝视","不信 怀疑","在...上面",
             "着火 燃烧","着火的 燃烧的","活着","机场","到 直到","西向西 朝西","奶油",
             "工作日","果馅饼 派","赶到 露面","豆 豆荚","市场 集市","在..以前","傻瓜",
             "服装 装束","窘迫的 害羞的","化妆舞会","宣布 宣告","意大利面条","骗局 恶作剧",
             "卖光","发现发觉n.","女士 女子","取消 终止","军官 官员","可相信的 可信任的","消失 不见",
             "使人害羞的"]
#"","","","","","","","","","","","","","","","","",""
Name_English_G9_U13= "英语九年级第13单元"
Questions_English_G9_U13 = ["litter","bottom","fisherman","coal","ugly","advantage","cost","wooden",
             "plastic","takeaway","bin","shark","fin","cruel","harmful","be harmful to","at the top of",
             "chain","the food chain","ecosystem","industry","law","scientific","take part in",
             "afford","turn off","reusable","pay for","take action","transportation","recycle",
             "napkin","throw away","put sth. to good use","pull...down","upside","gate","bottle",
             "president","inspiration","iron","work","metal","bring back","creativity"]
Answers_English_G9_U13 = ["乱扔 垃圾 废弃物","底部 最底下","渔民 钓鱼的人","煤",
             "丑陋的 难看的","优点 有利条件","花费 价钱","木制的 木头的","塑料的 塑料",
             "外卖食物","垃圾箱","鲨鱼","鱼鳍","残酷的 残忍的","有害的","对...有害",
             "在...顶部或顶端","链子 链条","食物链","生态系统","工业 行业","法律 法规",
             "科学的","参加","承担得起 买得起","关掉（电器）","可重复使用的 可再次使用的",
             "付费 付出代价","采取行动","交通业 交通运输","回收利用 再利用","餐巾餐巾纸",
             "扔掉 抛弃","好好利用某物","拆下 摧毁","上下颠倒 倒转","大门","瓶子",
             "负责人 主席 总统","灵感 鼓舞人心的人","铁","作品","金属",
             "恢复 使想起 归还","创造力 独创性"]

Name_English_G9_U14= "英语九年级第14单元"
Questions_English_G9_U14 = ["survey","standard","row","in a row","keyboard","method","instruction",
             "double","shall","look back at","overcome","make a mess","graduate",
             "keep one's cool","caring","ours","senior","senior high school",
             "text","go by","level","degree","manager","believe in","gentleman",
             "graduation","ceremony","first of all","congratulate","thirsty",
             "be thirsty for","thankful","be thankful to sb.","lastly",
             "task","ahead","ahead of","along with","responsible",
             "be responsible for","separate","set out",
             "separate from","wing"]
Answers_English_G9_U14 = ["调查","标准 水平","一排一列一行","连续几次地",
             "键盘 电子乐器","方法 措施","指示 命令","加倍 两倍的",
             "将要 将会","回忆 回首 回顾","克服 战胜","弄得一团糟",
             "毕业 获得学位","沉住气 保持冷静","体贴人的 关心他人的",
             "我们的","级别高的","高中","课文 文本","逝去 过去",
             "水平","学位 度数 程度","经理 经营者","信赖 信任",
             "先生 绅士","毕业","典礼 仪式","首先","祝贺","渴望的 口渴的",
             "渴望 渴求","感谢 感激","对某人心存感激","最后",
             "任务 工作","向前面 在前面","在...前面",
             "连同 除...以外还","有责任心的","对...有责任 负责任",
             "单独的 分离的 分开分离","出发 启程","分离隔开（短语）",
             "翅膀"]


# ---------------------def word-------------------------------------
all_value = dir()
# print all_value

def get_name_names(d):
    questions_index_list = []  # to get ready for next <type 'list'>: ['Name_English_G1_U1', 'Name_English_G1_U2']
    for i in range(0, len(d)):  # get the key words in the D
        d_str = d[i]
        if "Name" in d_str:  # it's the key word
            questions_index_list.append(d[i])  # append to the list

    name_names_list_in = []

    for i in range(0, len(questions_index_list)):
        names_one = ""
        instrument_name = "names_one = " + questions_index_list[i]  # for exec
        exec instrument_name
        name_names_list_in.append(names_one)  # add to the list

    return name_names_list_in  # to return a list


def get_questions_list(d):
    questions_index_list = []  # to get ready for next
    for i in range(0, len(d)):  # get the key words in the D
        d_str = d[i]
        if "Questions" in d_str:  # it's the key word
            questions_index_list.append(d[i])  # append to the list

    questions_list_in = []

    for i in range(0, len(questions_index_list)):
        instrument_questions = "questions_list_in.append(" + questions_index_list[i] + ")"
        exec instrument_questions

    return questions_list_in  # to return a list


def get_answers_list(d):
    answers_index_list = []  # to get ready for next
    for i in range(0, len(d)):  # get the key words in the D
        d_str = d[i]
        if "Answers" in d_str:  # it's the key word
            answers_index_list.append(d[i])  # append to the list

    answers_list_in = []

    for i in range(0, len(answers_index_list)):
        instrument_answers = "answers_list_in.append(" + answers_index_list[i] + ")"
        exec instrument_answers

    return answers_list_in  # to return a list

list_names = get_name_names(all_value)  # it's a list full of the names of all the units
e_list_all = get_questions_list(all_value)
c_list_all = get_answers_list(all_value)


# ------------------------------------------------------------------


'''
#---------------------------------------------------------------------
list_1_name = 'Uint 1'
list_2_name = 'Uint 2'
list_3_name = 'Uint 3'
list_4_name = 'Uint 4'
list_5_name = 'Uint 5'
list_6_name = 'Uint 6'
list_7_name = 'Uint 7'
list_8_name = 'Uint 8'
list_9_name = 'Uint 9'
list_10_name = 'Uint 10'
list_11_name = 'Uint 11'
list_12_name = 'Uint 12'
list_13_name = 'Uint 13'
list_14_name = 'Uint 14'
#list_15_name = 'always wrong list'

list_names = [list_1_name,  list_2_name,  list_3_name,  list_4_name,  list_5_name,
              list_6_name,  list_7_name,  list_8_name,  list_9_name,  list_10_name,
              list_11_name,  list_12_name,  list_13_name,  list_14_name]  # ,  list_15_name]
e_list_all = [e_list_1,e_list_2,e_list_3,e_list_4,e_list_5,
                  e_list_6,e_list_7,e_list_8,e_list_9,e_list_10,
              e_list_11,e_list_12,e_list_13,e_list_14,]
              #e_list_15]
c_list_all = [c_list_1,c_list_2,c_list_3,c_list_4,c_list_5,
                  c_list_6,c_list_7,c_list_8,c_list_9,c_list_10,
              c_list_11,c_list_12,c_list_13,c_list_14,]
              #c_list_15]
'''
# -----------------------------------------------------
mix_c_list = []

for i in range(0,len(c_list_all)):
    mix_c_list.extend(c_list_all[i])

# -----------------------def-------------------------------------------------------------------


def choice_unit(e_list_all, c_list_all):
    e_list_finish = []
    c_list_finish = []
    # global user_choice
    list_num = len(e_list_all)
    print "目录索引:"
    for i in range(1,len(list_names)+1):
        print str(i)+": "+list_names[i-1]
    print
    print "请选择要考哪个单词列表(请根据上方索引输入要测试的内容，多个单元请输入数字并在中间加上a（1a2a3a4），全部请输入all）"

    while True:
        user_choice = raw_input("请输入你要考什么: ")
        if user_choice == "":
            continue
        if user_choice.isdigit() == True:
            if int(user_choice)>=1 and int(user_choice)<= len(list_names):
                make_sure_str = "你将测试：" + list_names[int(user_choice)-1] + "，确认请按回车，重新输入请输入N："

        if user_choice.isdigit() == False:
            make_sure_str = "你将测试：" + user_choice + "，确认请按回车，重新输入请输入N："
        make_sure = raw_input(make_sure_str)
        if make_sure != "N":
            break

    mix_or_not = user_choice.find("a")  # the_type:int
    if mix_or_not == -1:  # it's a only list
        load_choice_index = int(user_choice) - 1
        e_list_finish = e_list_all[load_choice_index][:]
        c_list_finish = c_list_all[load_choice_index][:]  # only need to return

    if mix_or_not != -1:  # mix list
        if user_choice == "all":
            for all_index in range(0, list_num):
                e_list_finish.extend(e_list_all[all_index])
                c_list_finish.extend(c_list_all[all_index])
        else:
            user_choice = "a" + user_choice + "a"
            units_num_total = user_choice.count("a") - 1
            a_position_n = 0
            for i in range(0, units_num_total):
                a_position_f = user_choice.find("a", a_position_n)
                a_position_n = user_choice.find("a", a_position_f + 1)
                unit_num = user_choice[a_position_f + 1:a_position_n]

                unit_index = int(unit_num) - 1
                e_list_finish.extend(e_list_all[unit_index])
                c_list_finish.extend(c_list_all[unit_index])

    list_finish = [e_list_finish, c_list_finish]
    return list_finish


def some_word(list_all):
    ee_list = list_all[0]
    ccc_list = list_all[1]
    while True:
        the_for_that = ee_list[:]
        first_word = raw_input("从哪个词开始？(f代表第一个）: ")
        if first_word not in ee_list and first_word != "f":
            print "开始词拼写错误，请重试"
            continue

        if first_word in ee_list or first_word == "f":
            if first_word == "f":
                f_num = 0
                ee_list = ee_list[0:]
                ccc_list = ccc_list[0:]
            if first_word != "f":
                f_num = ee_list.index(first_word)
                ee_list = ee_list[f_num:]
                ccc_list = ccc_list[f_num:]

        while True:
            last_word = raw_input("到哪个词结束？（l代表最后一个）: ")
            if last_word not in ee_list and last_word != "l":
                print "结束词拼写错误或前后顺序错误，请检查"
                continue
            else:
                break

        if last_word in ee_list or last_word == "l":
            if last_word == "l":
                l_num = len(the_for_that)
                ee_list = ee_list[:]
                ccc_list = ccc_list[:]
            if last_word != "l":
                l_num = ee_list.index(last_word)

                ee_list = ee_list[:l_num + 1]
                ccc_list = ccc_list[:l_num + 1]
        break

    list_finished = [ee_list, ccc_list]
    return list_finished




def list_random(elistbefore, clistbefore):
    new_list = []
    new_clist = []
    clistdoing = clistbefore[:]

    new_elist = []
    elistdoing = elistbefore[:]
    elist_num = len(elistbefore)
    for i in range(0, elist_num):
        the_random = random.randint(0, len(elistdoing) - 1)
        move_eword = elistdoing.pop(the_random)
        new_elist.append(move_eword)
        move_cword = clistdoing.pop(the_random)
        new_clist.append(move_cword)

    new_list.append(new_elist)
    new_list.append(new_clist)
    return new_list


def kao_english(en_list, ch_list):
    e_list = en_list
    c_list = ch_list
    en_list_num = len(e_list)
    for i in range(0, en_list_num):
        print "请写出：", c_list[i]
        count_e = len(e_list[i])
        speed_enter = 2
        think_time = 2
        if count_e >= 13:
            think_time = 0
        sleep =  think_time + count_e / speed_enter
        time.sleep(sleep)
        remain_num = en_list_num - i - 1
        print "还剩下%s个,正确答案为：%s" %(str(remain_num), e_list[i])
        print


def kao_chinese(en_list, ch_list):
    e_list = en_list
    c_list = ch_list
    en_list_num = len(e_list)
    for i in range(0, en_list_num):
        print "请写出：", e_list[i]
        count_c = len(c_list[i])
        speed_enter = 1.5
        sleep = count_c / speed_enter
        time.sleep(sleep)
        print "正确答案为：", c_list[i]
        print



def test_english(en_list, ch_list):  # 定义test测验，传递英语表和汉语表两个参数
    wrong_en_list = []  # 空的所答错误的英语单词列表（表内为正确）
    wrong_ch_list = []  # 空的所答错误的汉语列表（表内为正确）
    wrong_list = []  # 英语和汉语结合的列表，用于后方返回参数

    en_list_num = len(en_list)  # 得到英语列表总词数
    num = []  # 新建词数个数的数字表，为后面随机做铺垫
    for k in range(0, en_list_num):  # 有多少个单词就循环多少次
        num.append(k)  # 每循环一次，把第几次的几加到数字表中，为随机做铺垫
    num_n = len(num)
    for j in range(0, len(num)):  # 有多少单词，就循环多少次，保证全部都考到
        xuan_n = j  # 随机选择一个数字，作为序列号
        xuan_w = num[xuan_n]  # 把随机选的序列号所对应的单词找出来
        num_n -= 1
        eng = raw_input('请拼写  ' + ch_list[xuan_w] + ': ')  # 人机交互，给出汉语，输入所对应单词
        if eng == en_list[xuan_w]:  # 检测是否正确
            print '回答正确'  # 若正确所打印
            print  # 空出一行，美观;)

        else:  # 若错误
            print '回答错误，正确答案应为：', en_list[xuan_w]  # 打印正确的答案
            print "你已经错了:",str(len(wrong_en_list)+1),"个单词。",'还剩下', num_n, '个单词'  # 统计还剩余多少个单词
            #print "wrong for:", str(len(wrong_en_list)+1)
            print  # 美观

            wrong_en = en_list[xuan_w]  # 得到错误的英语单词，并赋值于变量wrong_en
            wrong_en_list.append(wrong_en)  # 将错误单词加到所答错误的英语单词列表（表内为正确）
            wrong_ch = ch_list[xuan_w]  # 得到错误的英语单词所对应的汉语，并赋值于变量wrong_ch
            wrong_ch_list.append(wrong_ch)  # 将错误单词所对应的汉语加到所答错误的汉语列表（表内为正确）

            # been = num.pop(xuan_n)            #删掉这个词，避免重复

    wrong_list.append(wrong_en_list)  # 把所答错误的英语单词列表加入到整体错误列表
    wrong_list.append(wrong_ch_list)  # 把所答错误的英语单词所对应的汉语列表加入到整体错误列表

    return wrong_list  # 返回英语和汉语结合的列表集合，后方还需拆开


def test_chinese(en_list, ch_list):
    letters = ["A", "B", "C", "D"]
    en_list_num = len(en_list)
    ch_list_num = len(ch_list)
    wrong_list = []
    wrong_e_list = []
    wrong_c_list = []
    remain_word = len(en_list)

    for list_index in range(0, ch_list_num):
        remain_word -= 1
        chinese_test_words = []
        all_chinese_word = mix_c_list[:]
        en_word = en_list[list_index]
        ch_word = ch_list[list_index]

        if ch_word in all_chinese_word:
            all_chinese_word.remove(ch_word)  # delete the word need to be test in the all list
        for all_index in range(0, 3):
            otherword_index = random.randint(0, len(all_chinese_word) - 1)
            other_word = all_chinese_word[otherword_index]
            chinese_test_words.append(other_word)
            del all_chinese_word[otherword_index]
        test_word_location = random.randint(0, 3)
        chinese_test_words.insert(test_word_location, ch_word)

        choice_show = "A:" + chinese_test_words[0] + "\t  B:" + chinese_test_words[1] + "\t  C:" + \
                      chinese_test_words[2] + "\t  D:" + chinese_test_words[3]
        all_show = "请选择 " + en_word + " 的汉语意思:" + "\n" + choice_show + "\n" + "答案："
        user_choice = raw_input(all_show)
        if user_choice in letters:
            if letters.index(user_choice) == test_word_location:
                print "正确"
            else:
                print "错误，正确答案为：" + letters[test_word_location]
                wrong_c_list.append(ch_word)
                wrong_e_list.append(en_word)
                print "你已经错了:", len(wrong_e_list),"个单词。",'还剩下', remain_word, '个单词'
                #print "wrong for:", len(wrong_e_list)
        else:
            print "错误，正确答案为：" + letters[test_word_location]
            wrong_c_list.append(ch_word)
            wrong_e_list.append(en_word)
            print "你已经错了:", len(wrong_e_list),"个单词。",'还剩下', remain_word, '个单词'
            #print "wrong for:", len(wrong_e_list)

        print

    wrong_list.append(wrong_e_list)
    wrong_list.append(wrong_c_list)
    return wrong_list





list_all_mix = choice_unit(e_list_all,c_list_all)

whether_need_some = raw_input("如果需要考部分请输入S： ")

if whether_need_some == "S":
    some_w = some_word(list_all_mix)
    e_list = some_w[0]
    c_list = some_w[1]

else:
    e_list = list_all_mix[0]
    c_list = list_all_mix[1]





# --------------------------------------------------------------------------------
import random,time  # 调用随机函数
ans = "A"
e_b_list = e_list
c_b_list = c_list
while ans == "A":
    e_list = e_b_list
    c_list = c_b_list
    e_r_num = len(e_list)  # 统计出所有英语单词的数量
    c_r_num = len(c_list)  # 统计出所有汉语的数量
    test_time = 0

    # ----------------------program----------------------------------------------------------------------------
    while True:  # 为下面的break做铺垫
        if len(e_list) != len(c_list):  # 如果英汉词数不对应
            print '单词表个数不对应，请检查'  # 提示此话，为检查
            for l in range(0, len(e_list)):  # 为打印出所有单词做铺垫
                print e_list[l], c_list[l]
            break  # 跳出循环，并结束程序

        for l in range(0, len(e_list)):  # 为打印出所有单词做铺垫
            print e_list[l], c_list[l]  # 打印出所有单词及其汉语

        print '本次需要考的单词有', len(e_list), '个'  # 开头首先说出需要考的数量
        v = raw_input("请输入模式(t：英语顺序)(s：英语随机)(c：汉意顺序)(h：汉意随机)(k：测验英语)(z：测验汉意):")  # 准备开始

        for g in range(0, 50):  # 循环五十次
            print  # 五十个空行，为挡住上方答案


        if v == "h":
            listn = list_random(e_list, c_list)
            result = test_chinese(listn[0], listn[1])
        if v == "k":
            kao_english(e_list, c_list)
            break
        if v == "z":
            kao_chinese(e_list,c_list)
            break
        if v == "c":
            result = test_chinese(e_list, c_list)
        if v == "t":
            result = test_english(e_list, c_list)
        if v == "s":
            listn = list_random(e_list, c_list)
            result = test_english(listn[0], listn[1])
            #print result
        if v != "k" and v != "c" and v != "t" and v != "s" and v != "h":
            result = test_english(e_list, c_list)

        while True:  # 反复调试的循环
            e_list = result[0]  # 拆开的英语错误列表（表内为正确）
            c_list = result[1]  # 拆开的汉语错误列表（表内为正确）

            if len(e_list) == 0:  # 如果错误的个数为0，也就是全部都对
                print '正确率： 100 %'
                print '恭喜你全部单词回答正确'  # 打印此话
                break  # 跳出循环

            test_time += 1
            print "第", test_time, '回合'
            print '你一共错了：', len(e_list), '个单词'  # 打印出错误单词的个数
            print '正确率：', 100 - int(len(e_list) / float(e_r_num) / 0.01), '%'  # 统计正确率，并打印出来
            print  # 美观
            for p in range(0, len(e_list)):  # 循环，并得到错误次序，无遗漏
                print '你所错的单词是： ', e_list[p], c_list[p]  # 打印出全部所错的单词及其汉语翻译，方便背诵
            print  # 美观

            raw_input('准备好了吗？（按回车开始）')  # 背诵完成后，将要继续，按回车键继续开始测验

            for j in range(0, 50):  # 循环为打印空行
                print  # 为了阻挡看见上方答案

            if v == "h":
                listn = list_random(e_list, c_list)
                result = test_chinese(listn[0], listn[1])
            if v == "c":
                result = test_chinese(e_list, c_list)
            if v == "t":
                result = test_english(e_list, c_list)
            if v == "s":
                listn = list_random(e_list, c_list)
                result = test_english(listn[0], listn[1])  # 再次调用函数，本次参数为上次所错单词
            if v != "k" and v != "c" and v != "t" and v != "s" and v != "h":
                result = test_english(e_list, c_list)
        break  # 为全对的break终止大while
    ans = raw_input("退出请按回车，再来一次请输入A:")
# -------------------------------------------------------------------------------------------------------------
print '******************'
print '*      再见!     *'
print '******************'
# 最后再见

# 感谢使用

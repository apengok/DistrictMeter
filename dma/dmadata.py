# -*- coding: utf-8 -*-

from collections import OrderedDict
#分区资料
dma_file = OrderedDict()

dma_file['zone_name']={'value':'somecity','name':'分区名称','note':''}
dma_file['zone_area']={'value':'1000','name':'分区面积（平方公里）','note':''}
dma_file['zone_water_in']={'value':14490,'name':'分区进水量（ m3）','note':''}
dma_file['registed_user']={'value':10000,'name':'注册用户总数（万户）','note':''}
dma_file['pipeline_length']={'value':2000,'name':'管线长度（ km）','note':''}
dma_file['sub_zone_num']={'value':10,'name':'下一级分区数量（个）','note':''}
dma_file['dma_num']={'value':20,'name':'分区中 DMA 数量（个）','note':''}
dma_file['measure_per_actual']={'value':89,'name':'水表抄见率（ %）','note':'抄表数量与实际立户水表数量一致程度'}
dma_file['measure_precision']={'value':95,'name':'抄表准确率（ %）','note':''}
dma_file['zone_sale']={'value':12345,'name':'分区销售水量（ m3）','note':'该分区销售水量'}
dma_file['nightflow_min']={'value':2000,'name':'夜间最小流量（ m3）','note':'仅适用于 DMA'}
dma_file['online_presspoint_num']={'value':10,'name':'在线压力点数量（个）','note':''}
dma_file['online_flowmeter_num']={'value':20,'name':'在线流量计数量（个）','note':''}
dma_file['online_water_quality_m_num']={'value':30,'name':'在线水质监测点数量（个）','note':''}
dma_file['charge_watermeter_num']={'value':1000,'name':'收费用远传水表数量（只）','note':''}
dma_file['charge_waterwater_percent']={'value':70,'name':'收费用远传水表水量占分区销 水量比（ %）','note':''}
dma_file['zone_detect_leak_num']={'value':5,'name':'分区探出漏点总数（个）','note':''}
dma_file['leak_water']={'value':100,'name':'漏失水量（ m3）','note':''}
dma_file['leak_obscur_water']={'value':30,'name':'暗漏水量（ m3）','note':''}
dma_file['leak_obvious_water']={'value':70,'name':'明漏水量（ m3）','note':''}
dma_file['leak_rate']={'value':12,'name':'漏损率（ %）','note':''}
dma_file['pressure_quality']={'value':90,'name':'压力合格率（ %）','note':''}
dma_file['water_quality']={'value':99,'name':'水质合格率（ %）','note':''}
dma_file['zone_inner_pressure']={'value':30,'name':'分区内压力（ MPa）','note':''}

#汇总资料
summary_file = OrderedDict()
summary_file['totol_water_yearly']={'value':10000,'name':'年供水总量（万 m3）','note':''}
summary_file['registed_user_use_water_yearly']={'value':1000,'name':'年注册用户用水量（万 m3）','note':''}
summary_file['leak_obvious_water']={'value':14490,'name':'明漏水量（万 m3）','note':''}
summary_file['leak_obscur_water']={'value':10000,'name':'暗漏水量（万 m3）','note':''}
summary_file['background_leak_water']={'value':2000,'name':'背景漏失水量（万 m3）','note':''}
summary_file['box_sank_leak']={'value':10,'name':'水箱、水池的渗漏和溢流水量 （万 m3）','note':''}
summary_file['resident_loss_distant']={'value':20,'name':'居民用户总分表差损失水量（万 m3）','note':''}
summary_file['no_resident_loss_distant']={'value':89,'name':'非居民用户表具误差损失水量（万m3）','note':''}
summary_file['measure_read_resident_use']={'value':95,'name':'抄表到户居民用户用水量（万 m3）','note':''}
summary_file['average_press_out']={'value':12345,'name':'年平均出厂压力（ MPa）','note':''}
summary_file['max_frozone_depth']={'value':2000,'name':'最大冻土深度（ m）','note':''}
summary_file['pipenet_length']={'value':10,'name':'管网长度（ km）','note':''}
summary_file['pipenet_distribute_level']={'value':20,'name':'管网分区计量级别数','note':''}
summary_file['distribute_num_1']={'value':30,'name':'一级分区数量（个）','note':''}
summary_file['distribute_cover_water_1']={'value':1000,'name':'一级分区覆盖水量（万 m3）','note':''}
summary_file['distribute_cover_pipeline_1']={'value':70,'name':'一级分区覆盖管网长度（ km）','note':''}
summary_file['distribute_num_2']={'value':30,'name':'二级分区数量（个）','note':''}
summary_file['distribute_cover_water_2']={'value':1000,'name':'二级分区覆盖水量（万 m3）','note':''}
summary_file['distribute_cover_pipeline_2']={'value':70,'name':'二级分区覆盖管网长度（ km）','note':''}
summary_file['distribute_num_n']={'value':30,'name':'N级分区数量（个）','note':''}
summary_file['distribute_cover_water_n']={'value':1000,'name':'N级分区覆盖水量（万 m3）','note':''}
summary_file['distribute_cover_pipeline_n']={'value':70,'name':'N级分区覆盖管网长度（ km）','note':''}
summary_file['pipenet_press_qulity']={'value':5,'name':'管网压力合格率','note':''}
summary_file['pipenet_water_qulity']={'value':100,'name':'管网水质合格率','note':''}
summary_file['service_content_rate']={'value':30,'name':'用户服务综合满意率','note':''}
summary_file['pipeline_leak_rate']={'value':70,'name':'管网漏损率','note':''}
summary_file['measure_read_rate']={'value':12,'name':'水表抄见率（ %）','note':''}
summary_file['measure_right_rate']={'value':90,'name':'抄表准确率（ %）','note':''}
summary_file['online_presspoint_num']={'value':99,'name':'在线压力点数量（个）','note':''}
summary_file['online_flow_calc_num']={'value':30,'name':'在线流量计数量（个）','note':''}
summary_file['online_water_quality_m_num']={'value':12,'name':'在线水质监测点数量（个）','note':''}
summary_file['charge_remote_water_num']={'value':90,'name':'收费用远传水表数量（只）','note':''}
summary_file['charge_remote_water_percent']={'value':99,'name':'收费用远传水表水量占销售水量比（ %）','note':''}
summary_file['detect_leak_num']={'value':30,'name':'探出漏点总数（个）','note':''}
summary_file['water_leakloss']={'value':30,'name':'漏失水量(万 m3)','note':''}
summary_file['leak_rate']={'value':12,'name':'漏损率（ %）','note':''}
summary_file['pressure_quality']={'value':90,'name':'压力合格率（ %）','note':''}
summary_file['water_quality']={'value':99,'name':'水质合格率（ %）','note':''}
summary_file['distribute_pressure']={'value':30,'name':'压力（ MPa）','note':''}
summary_file['economic_invest']={'value':12,'name':'经济投入','note':''}
summary_file['economic_benefit']={'value':90,'name':'经济效益','note':''}
summary_file['socity_benefit']={'value':99,'name':'社会效益','note':''}

static_monthly = OrderedDict() 
static_monthly['total_in']={'name':'1、供水总量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['provid_self']={'name':'    其中：1.1 自产供水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['provid_out']={'name':'        1.2 外购供水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['register_resident_use']={'name':'2、注册用户用水量(有效供水量)','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['charge_water']={'name':'2.1 计费用水量(售水量)','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['charge_measure_water']={'name':'2.1.1 计费计量用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['resisent_use']={'name':'2.1.1.1 居民用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['measure_read_resident_use']={'name':'其中:抄表到户的居民用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['no_measure_read_resident_use']={'name':'未抄表到户的居民用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['no_resident_use']={'name':'2.1.1.2 非居民用水量(含特殊行业)','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['high_precise_meter_use']={'name':'其中:高精度水表用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['other_meter_use']={'name':'其他类型水表用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['uncharge_unmeter_use']={'name':'2.1.2 计费未计量用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['new_pipeline_wash']={'name':'其中:新建管线冲洗水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['pipeline_rebuild_use']={'name':'管网改造冲洗水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['urgent_vihicle_use']={'name':'应急供水车水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['project_leak']={'name':'工程漏水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['free_use']={'name':'2.2免费用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['free_measure_use']={'name':'2.2.1免费计量用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['free_unmeasure_use']={'name':'2.2.2免费未计量用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['fireproof_use']={'name':'其中消防用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['new_pipeline_wash_2']={'name':'新建管线冲洗水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['pipeline_rebuild_use_2']={'name':'管网改造冲洗水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['pipenet_maintain_use']={'name':'管网维护用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['leakloss']={'name':'3、漏损水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['leak_rate']={'name':'漏损率(%)','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['produce_loss']={'name':'4、产销差水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['produce_loss_rate']={'name':'产销差率','last_month_total':'','cur_month':'','cur_month_total':'','note':''}

def generet_static():
    import random

    for key , item in static_monthly.items():
        item['last_month_total'] = random.randint(10000,20000)
        item['cur_month'] = random.randint(9000,18000)
        item['cur_month_total'] = random.randint(11000,22000)

    return static_monthly

dma_tree = [
    {
        'text':'深圳市',
        'href':'#',
        'nodes':[
            {
                'text':'南山区',
                'href':'/sub_dma/南山区',
                'nodes':[
                    {
                        'text':'西丽',
                        'href':'/sub_dma/南山区/西丽',
                        'nodes':[
                            {
                        'text':'asdf',
                        'href':'/sub_dma/南山区/西丽',
                        'nodes':[
                        
                        ]
                    },
                    {
                        'text':'蛇口12',
                        'href':'/sub_dma/南山区/蛇口12',
                        'nodes':[]
                    },
                    {
                        'text':'桃源12',
                        'href':'/sub_dma/南山区/桃源12',
                        'nodes':[]
                    },
                        ]
                    },
                    {
                        'text':'蛇口',
                        'href':'/sub_dma/南山区/蛇口',
                        'nodes':[]
                    },
                    {
                        'text':'桃源',
                        'href':'/sub_dma/南山区/桃源',
                        'nodes':[]
                    },
                ]
            },
            {
                'text':'福田区',
                'href':'/sub_dma/福田区',
                'nodes':[]
            },
            {
                'text':'罗湖区',
                'href':'/sub_dma/罗湖区',
                'nodes':[]
            },
            {
                'text':'宝安区',
                'href':'/sub_dma/宝安区',
                'nodes':[]
            },
            {
                'text':'龙华区',
                'href':'/sub_dma/龙华区',
                'nodes':[]
            },
            {
                'text':'盐田区',
                'href':'/sub_dma/盐田区',
                'nodes':[]
            },
            {
                'text':'坪山区',
                'href':'/sub_dma/坪山区',
                'nodes':[]
            }
        ]
    },
    {
        'text': '汇总资料',
        'href': "/dma_summary/",
        'tags': ['0']
    },
]

#1.漏损率的计算 漏损率是指由供水总量和注册用户用水量直接计算出来的漏损率
#R_wl = (Qs-Qa)/Qs x 100% (1)#R_wl——漏损率（ %）;Qs ——供水总量（万 m3）；Qa ——注册用户用水量（万 m3）。
# 1）居民抄表到户水量的修正值 R1 :R1 = 0.08r x 100% (2) R1 ——居民抄表到户水量的修正值（ %）；r ——居民抄表到户水量占总供水量比例；0.08 ——居民用户总分表差率。
# 2）单位供水量管长的修正值 R2 应按公式（ 3）（ 4）计算
# R2 = 0.99(A-0.0693)x 100%  (3)
# A = L/Qs      (4)
# R2 ——单位供水量管长的修正值（ %）
# A ——单位供水量管长（ km/万 m3）；
#0.99 ——单位供水量管长对漏损率的影响系数；
#0.0693 ——常数（ km/万 m3），代表单位供水量管长的基准值
#L —— DN75（含）以上管道长度（ km）
#当 R2 值大于 3%时，应取 3%；当 R2 值小于-3%时，应取-3%
#  3）年平均出厂压力大于 0.35MPa 小于等于 0.55MPa 时，
#修正值 R3 应为 0.5%；年平均出厂压力大于 0.55MPa 小于等
#于 0.75MPa 时，修正值 R3 应为 1%；年平均出厂压力大于
#0.75MPa 时，修正值 R3 应为 2%。
# 4）最大冻土深度大于 1.4m 时，修正值 R4 应为 1%；最
#大冻土深度小于 1.4m 时， R4=0。
#（ 5）供水单位的基本漏损率 R_wln=R_wl - R1 - R2 - R3 - R4 

def leak_rate(Qs,Qa,r,L,p,d):
    '''
        Qs:供水总量（万 m3）
        Qa:注册用户用水量（万 m3）
        r:居民抄表到户水量占总供水量比例
        L:DN75（含）以上管道长度（ km）
        p:年平均出厂压力
        d:最大冻土深度
    '''
    R_wl = (Qs-Qa)/Qs * 100
    R1 = 0.08*r * 100
    A = L/Qs
    R2 = 0.09*(A - 0.0693)*100
    if R2 > 0.03:
        R2 = 0.03
    if R2 < -0.03:
        R2 = -0.03
    R3 = 0
    if p > 0.35 and p <= 0.55:
        R3 = 0.005
    elif p > 0.55 and p < 0.75:
        R3 = 0.01
    elif p > 0.75:
        R3 = 0.02
    R4 = 0
    if d > 1.4:
        R4 = 0.01
    if d <= 1.4:
        R4 = 0
    R_wln = R_wl - R1 - R2 - R3 - R4
    
    return R_wln
    
''' 节能潜力分析
计算供水综合单位电耗G=105/367η[KWh/(km3•MPa)]，当G＞350kWh/(m3•MPa)时，η＜77.85%时，泵站需要开展节能降耗工作。
'''

'''
1.1.2.3 降漏潜力分析
计算供水企业管网基本漏损情况。
1）城市供水企业管网基本漏损率不应大于12%。
2）抄表到户水平修正。当居民用水按户抄表的水量大于70%时，漏损率应增加1%
3）单位供水量管长修正。
供水管径 DN     单位供水量管长                 修正值 
≥75             ＜1.4km/km3/d                    减2% 
≥75             ≥1.40km/km3/d,≤1.64km/km3/d     减1% 
≥75             ≥2.06km/km3/d,≤2.40km/km3/d     加1% 
≥75             ≥2.41km/km3/d,≤2.70km/km3/d     加2% 
≥75             ≥2.70km/km3/d   加3% 

'''

'''
常用的漏损评价的指标主要有：
（1）漏失率（%）=Q漏失量/Q供水量；
（2）产销差率（%）=（ Q供水量- Q售水量）/ Q供水量；
（3）单位管长漏失量（m³/km/h）= Q漏失量/∑L配水管总长；
（4）基础设施漏失指数（ILI）=当前物理损失水量/不可避免物理损失水量。
不可避免物理损失水量(L/d)=（18•Lm+0.8•Nc+25•Lp）•P 
式中——Lm：主干管长度（Km）； Nc：接户数；Lp：用户连接管总长度（Km）； P：管网平均压力（m）。

'''
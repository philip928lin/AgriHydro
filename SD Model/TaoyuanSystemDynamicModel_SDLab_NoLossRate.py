"""
Python model "TaoYuanSystem_SDLab_NoLossRate.py"
Translated using PySD version 0.9.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME':
    'time',
    'Time':
    'time',
    'Sum Allocation ShiMenReservoir To HouChiWeir':
    'sum_allocation_shimenreservoir_to_houchiweir',
    'Operation Rule Record Industry':
    'operation_rule_record_industry',
    'Operation Rule Record Agriculture':
    'operation_rule_record_agriculture',
    'Allocation BanXin WPP':
    'allocation_banxin_wpp',
    'Allocation DaNan WPP1':
    'allocation_danan_wpp1',
    'Allocation DaNan WPP2':
    'allocation_danan_wpp2',
    'Allocation LongTan WPP':
    'allocation_longtan_wpp',
    'Allocation NCSIST':
    'allocation_ncsist',
    'Allocation PingZhen WPP1':
    'allocation_pingzhen_wpp1',
    'Allocation PingZhen WPP2':
    'allocation_pingzhen_wpp2',
    'Allocation Proportion of BanXinWPP':
    'allocation_proportion_of_banxinwpp',
    'Allocation Proportion of DaNanWPP1':
    'allocation_proportion_of_dananwpp1',
    'Allocation Proportion of DaNanWPP2':
    'allocation_proportion_of_dananwpp2',
    'Allocation Proportion of LongTanWPP':
    'allocation_proportion_of_longtanwpp',
    'Allocation Proportion of PingZhenWPP1':
    'allocation_proportion_of_pingzhenwpp1',
    'Allocation Proportion of PingZhenWPP2':
    'allocation_proportion_of_pingzhenwpp2',
    'Allocation Proportion of ShiMenWPP':
    'allocation_proportion_of_shimenwpp',
    'Allocation ShiMen AgriChannel AgriWater':
    'allocation_shimen_agrichannel_agriwater',
    'Allocation ShiMen WPP':
    'allocation_shimen_wpp',
    'Allocation TaoYuan AgriChannel AgriWater':
    'allocation_taoyuan_agrichannel_agriwater',
    'Allocation TaoYuan CPC Refinery':
    'allocation_taoyuan_cpc_refinery',
    'Allocation TaoYuanDaHanRiver AgriWater':
    'allocation_taoyuandahanriver_agriwater',
    'BanXin Water Demand':
    'banxin_water_demand',
    'BanXin WPP':
    'banxin_wpp',
    'Channel Transfer Loss Rate':
    'channel_transfer_loss_rate',
    'DaNan WPP':
    'danan_wpp',
    'Date':
    'date',
    'Domestic Water Demand':
    'domestic_water_demand',
    '"Domestic-Industry Proportion"':
    'domesticindustry_proportion',
    'EcoBaseFlow':
    'ecobaseflow',
    'Final Allocation ShiMenReservoir To HouChiWeir':
    'final_allocation_shimenreservoir_to_houchiweir',
    'Final Allocation ShiMenReservoir To ShiMenAgriChannel':
    'final_allocation_shimenreservoir_to_shimenagrichannel',
    'HouChi Weir':
    'houchi_weir',
    'HsinChu Water Demand':
    'hsinchu_water_demand',
    'Industry Water Demand':
    'industry_water_demand',
    'Irrigation Tranfer Loss Amount':
    'irrigation_tranfer_loss_amount',
    'LongTan WPP':
    'longtan_wpp',
    'North TaoYuan Water Demand':
    'north_taoyuan_water_demand',
    'PingZhen WPP1':
    'pingzhen_wpp1',
    'PingZhen WPP2':
    'pingzhen_wpp2',
    'Proportion Checking Variable':
    'proportion_checking_variable',
    'Public Water Demand':
    'public_water_demand',
    'Ratio AgriWater HouChiWeir To TaoYuanAgriChannel':
    'ratio_agriwater_houchiweir_to_taoyuanagrichannel',
    'Ratio AgriWater HouChiWeir To ZhongZhuangWeir':
    'ratio_agriwater_houchiweir_to_zhongzhuangweir',
    'Ratio AgriWater ShiMenReservoir To HouChiWeir':
    'ratio_agriwater_shimenreservoir_to_houchiweir',
    'Ratio AgriWater ShiMenReservoir To HouChiWeir In DaHanRiver':
    'ratio_agriwater_shimenreservoir_to_houchiweir_in_dahanriver',
    'Ratio AgriWater ShiMenReservoir To HouChiWeir In TaoYuanAgriChannel':
    'ratio_agriwater_shimenreservoir_to_houchiweir_in_taoyuanagrichannel',
    'Ratio AgriWater ShiMenReservoir To ShiMenAgriChannel':
    'ratio_agriwater_shimenreservoir_to_shimenagrichannel',
    'Ratio BanXinWPP Allocation At YuanShanWeir':
    'ratio_banxinwpp_allocation_at_yuanshanweir',
    'Ratio BanXinWPP At HouChiWeir':
    'ratio_banxinwpp_at_houchiweir',
    'Ratio DaNanWPP1 Allocation At YuanShanWei':
    'ratio_dananwpp1_allocation_at_yuanshanwei',
    'Ratio DaNanWPP1 At HouChiWeir':
    'ratio_dananwpp1_at_houchiweir',
    'Ratio DaNanWPP2 At HouChiWeir':
    'ratio_dananwpp2_at_houchiweir',
    'Ratio LongTanWPP At ShiMenAgriChannel':
    'ratio_longtanwpp_at_shimenagrichannel',
    'Ratio NCSIST At HouChiWeir':
    'ratio_ncsist_at_houchiweir',
    'Ratio NCSIST At ShiMenAgriChannel':
    'ratio_ncsist_at_shimenagrichannel',
    'Ratio NCSIST At TaoYuanAgriChannel':
    'ratio_ncsist_at_taoyuanagrichannel',
    'Ratio PingZhenWPP1 At ShiMenAgriChannel':
    'ratio_pingzhenwpp1_at_shimenagrichannel',
    'Ratio PingZhenWPP2 At HouChiWeir':
    'ratio_pingzhenwpp2_at_houchiweir',
    'Ratio ShiMenReservoir To HouChiWeir':
    'ratio_shimenreservoir_to_houchiweir',
    'Ratio ShiMenReservoir To ShiMenAgriChannel':
    'ratio_shimenreservoir_to_shimenagrichannel',
    'Ratio ShiMenWPP At ShiMenAgriChannel':
    'ratio_shimenwpp_at_shimenagrichannel',
    'Ratio TaoYuan CPC Refinery At HouChiWeir':
    'ratio_taoyuan_cpc_refinery_at_houchiweir',
    'Ratio TaoYuan CPC Refinery At TaoYuanAgriChannel':
    'ratio_taoyuan_cpc_refinery_at_taoyuanagrichannel',
    'Ratio WPP HouChiWeir To TaoYuanAgriChannel':
    'ratio_wpp_houchiweir_to_taoyuanagrichannel',
    'Ratio WPP HouChiWeir To ZhongZhuangWeir':
    'ratio_wpp_houchiweir_to_zhongzhuangweir',
    'Ratio WPP ShiMenReservoir To HouChiWeir':
    'ratio_wpp_shimenreservoir_to_houchiweir',
    'Ratio WPP ShiMenReservoir To ShiMenAgriChannel':
    'ratio_wpp_shimenreservoir_to_shimenagrichannel',
    'Ratio ZhongZhuangAdjustmentReservoir take':
    'ratio_zhongzhuangadjustmentreservoir_take',
    'SanXia River Ecological Base Stream Flow':
    'sanxia_river_ecological_base_stream_flow',
    'SanXia River Inflow':
    'sanxia_river_inflow',
    'SanXia Weir':
    'sanxia_weir',
    'SanXia Weir Outflow':
    'sanxia_weir_outflow',
    'SanXiaWeir Transfer Loss Amount':
    'sanxiaweir_transfer_loss_amount',
    'ShiMen AgriChannel':
    'shimen_agrichannel',
    'ShiMen AgriChannel AgriWater Actual Consumption':
    'shimen_agrichannel_agriwater_actual_consumption',
    'ShiMen AgriChannel AgriWater Demand':
    'shimen_agrichannel_agriwater_demand',
    'ShiMen AgriChannel Irrigation Transfer Loss Amount':
    'shimen_agrichannel_irrigation_transfer_loss_amount',
    'ShiMen AgriChannel Irrigation Transfer Loss Rate':
    'shimen_agrichannel_irrigation_transfer_loss_rate',
    'ShiMen AgriChannel Transfer Loss Amount':
    'shimen_agrichannel_transfer_loss_amount',
    'ShiMen Irrigation Area Outflow':
    'shimen_irrigation_area_outflow',
    'ShiMen Reservoir':
    'shimen_reservoir',
    'ShiMen Reservoir Area':
    'shimen_reservoir_area',
    'ShiMen Reservoir Depth':
    'shimen_reservoir_depth',
    'ShiMen Reservoir Evaporation':
    'shimen_reservoir_evaporation',
    'ShiMen Reservoir Inflow':
    'shimen_reservoir_inflow',
    'ShiMen Reservoir Max Volume':
    'shimen_reservoir_max_volume',
    'ShiMen Reservoir Overflow':
    'shimen_reservoir_overflow',
    'ShiMen WPP':
    'shimen_wpp',
    'ShiMen WPP Adjusted':
    'shimen_wpp_adjusted',
    'ShiMen WPP Storage Pool':
    'shimen_wpp_storage_pool',
    'ShiMenReservoir Operation Rule Lower Limit':
    'shimenreservoir_operation_rule_lower_limit',
    'ShiMenReservoir Operation Rule Lower Severe Limit':
    'shimenreservoir_operation_rule_lower_severe_limit',
    'ShiMenReservoir Operation Rule Upper Limit':
    'shimenreservoir_operation_rule_upper_limit',
    'ShiMenReseverior Month Evaporation Table':
    'shimenreseverior_month_evaporation_table',
    'South TaoYuan Water Demand':
    'south_taoyuan_water_demand',
    'Sum AgriWater HouChiWeir To TaoYuanAgriChannel':
    'sum_agriwater_houchiweir_to_taoyuanagrichannel',
    'Sum AgriWater HouChiWeir To ZhongZhuangWeir':
    'sum_agriwater_houchiweir_to_zhongzhuangweir',
    'Sum AgriWater ShiMenReservoir To HouChiWeir':
    'sum_agriwater_shimenreservoir_to_houchiweir',
    'Sum AgriWater ShiMenReservoir To ShiMenAgriChannel':
    'sum_agriwater_shimenreservoir_to_shimenagrichannel',
    'Sum Allcation From ShiMenReservoir':
    'sum_allcation_from_shimenreservoir',
    'Sum Allocation HouChiWeir To TaoYuanAgriChannel':
    'sum_allocation_houchiweir_to_taoyuanagrichannel',
    'Sum Allocation HouChiWeir To ZhongZhuangWeir':
    'sum_allocation_houchiweir_to_zhongzhuangweir',
    'Sum Allocation ShiMenReservoir To ShiMenAgriChannel':
    'sum_allocation_shimenreservoir_to_shimenagrichannel',
    'Sum WPP HouChiWeir To TaoYuanAgriChannel':
    'sum_wpp_houchiweir_to_taoyuanagrichannel',
    'Sum WPP HouChiWeir To ZhongZhuangWeir':
    'sum_wpp_houchiweir_to_zhongzhuangweir',
    'Sum WPP ShiMenReservoir To HouChiWeir':
    'sum_wpp_shimenreservoir_to_houchiweir',
    'Sum WPP ShiMenReservoir To ShiMenAgriChannel':
    'sum_wpp_shimenreservoir_to_shimenagrichannel',
    'Support EcoBaseFlow':
    'support_ecobaseflow',
    'Support For DaHan River Ecological Base Stream Flow':
    'support_for_dahan_river_ecological_base_stream_flow',
    'Taipei Water Department Source':
    'taipei_water_department_source',
    'TaoChu TwoWay Support 1':
    'taochu_twoway_support_1',
    'TaoChu TwoWay Support 2':
    'taochu_twoway_support_2',
    'TaoYuan AgriChannel':
    'taoyuan_agrichannel',
    'TaoYuan AgriChannel AgriWater Actual Consumption':
    'taoyuan_agrichannel_agriwater_actual_consumption',
    'TaoYuan AgriChannel AgriWater Demand':
    'taoyuan_agrichannel_agriwater_demand',
    'TaoYuan AgriChannel Irrigation Transfer Loss Amount':
    'taoyuan_agrichannel_irrigation_transfer_loss_amount',
    'TaoYuan AgriChannel Irrigation Transfer Loss Rate':
    'taoyuan_agrichannel_irrigation_transfer_loss_rate',
    'TaoYuan AgriChannel Transfer Loss Amount':
    'taoyuan_agrichannel_transfer_loss_amount',
    'TaoYuan Irrigation Area Outflow':
    'taoyuan_irrigation_area_outflow',
    'TaoYuan Water Supply Network 1':
    'taoyuan_water_supply_network_1',
    'TaoYuan Water Supply Network 2':
    'taoyuan_water_supply_network_2',
    'TaoYuanDaHanRiver AgriWater Demand':
    'taoyuandahanriver_agriwater_demand',
    'Tap Water Loss Rate':
    'tap_water_loss_rate',
    'TargetYear DomesticWaterDemand':
    'targetyear_domesticwaterdemand',
    'TargetYear IndustryWaterDemand':
    'targetyear_industrywaterdemand',
    'Total Allocation Proportion At HouChiWeir':
    'total_allocation_proportion_at_houchiweir',
    'Total Allocation Proportion At ShiMenAgriChannel':
    'total_allocation_proportion_at_shimenagrichannel',
    'Total Allocation Proportion At ZhongZhuangWeir':
    'total_allocation_proportion_at_zhongzhuangweir',
    'Total WPP Allocation':
    'total_wpp_allocation',
    'Total WPP Allocation At HouChiWeir':
    'total_wpp_allocation_at_houchiweir',
    'Total WPP Allocation At ShiMenAgriChannel':
    'total_wpp_allocation_at_shimenagrichannel',
    'Total WPP Allocation At YuanShanWeir':
    'total_wpp_allocation_at_yuanshanweir',
    'Tranfer From YuanShanWeir To DaNanWPP':
    'tranfer_from_yuanshanweir_to_dananwpp',
    'Transfer From BanXinWPP To BanXinWaterDemand':
    'transfer_from_banxinwpp_to_banxinwaterdemand',
    'Transfer From BanXinWPP To NorthTaoYuanWaterDemand':
    'transfer_from_banxinwpp_to_northtaoyuanwaterdemand',
    'Transfer From DaNanWPP To NorthTaoYuanWaterDemand':
    'transfer_from_dananwpp_to_northtaoyuanwaterdemand',
    'Transfer From HouChiWeir To TaoYuanAgriChannel':
    'transfer_from_houchiweir_to_taoyuanagrichannel',
    'Transfer From HouChiWeir To ZhongZhuangWeir':
    'transfer_from_houchiweir_to_zhongzhuangweir',
    'Transfer From SanXiaWeir To BanXinWPP':
    'transfer_from_sanxiaweir_to_banxinwpp',
    'Transfer From ShiMenAgriChannel To NCSIST':
    'transfer_from_shimenagrichannel_to_ncsist',
    'Transfer From ShiMenAgriChannel To ShiMenAgriWaterDemand':
    'transfer_from_shimenagrichannel_to_shimenagriwaterdemand',
    'Transfer From ShiMenReservoir To HouChiWeir':
    'transfer_from_shimenreservoir_to_houchiweir',
    'Transfer From ShiMenReservoir To ShiMenAgriChannel':
    'transfer_from_shimenreservoir_to_shimenagrichannel',
    'Transfer From TaoYuanAgriChannel To DaNanWPP':
    'transfer_from_taoyuanagrichannel_to_dananwpp',
    'Transfer From TaoYuanAgriChannel To NCSIST':
    'transfer_from_taoyuanagrichannel_to_ncsist',
    'Transfer From TaoYuanAgriChannel To TaoYuanAgriWaterDemand':
    'transfer_from_taoyuanagrichannel_to_taoyuanagriwaterdemand',
    'Transfer From TaoYuanAgriChannel To TaoYuanCPCRefinery':
    'transfer_from_taoyuanagrichannel_to_taoyuancpcrefinery',
    'Transfer From YuanShanWeir To BanXinWPP':
    'transfer_from_yuanshanweir_to_banxinwpp',
    'Transfer From ZhongZhuangAdjustmentReservoir To BanXinWPP':
    'transfer_from_zhongzhuangadjustmentreservoir_to_banxinwpp',
    'Transfer From ZhongZhuangAdjustmentReservoir To DaNanWPP':
    'transfer_from_zhongzhuangadjustmentreservoir_to_dananwpp',
    'Transfer From ZhongZhuangWeir To TaoYuanDaHanRiver AgriWater Demand':
    'transfer_from_zhongzhuangweir_to_taoyuandahanriver_agriwater_demand',
    'Transfer From ZhongZhuangWeir To YuanShanWeir':
    'transfer_from_zhongzhuangweir_to_yuanshanweir',
    'Transfer From ZhongZhuangWeir To ZhongZhuangAdjustmentReservoir':
    'transfer_from_zhongzhuangweir_to_zhongzhuangadjustmentreservoir',
    'Water Right BanXin WPP':
    'water_right_banxin_wpp',
    'Water Right DaNan WPP1':
    'water_right_danan_wpp1',
    'Water Right DaNan WPP2':
    'water_right_danan_wpp2',
    'Water Right PingZhen WPP1':
    'water_right_pingzhen_wpp1',
    'Water Right PingZhen WPP2':
    'water_right_pingzhen_wpp2',
    'Water Right ShiMen AgriChannel AgriWater':
    'water_right_shimen_agrichannel_agriwater',
    'Water Right ShiMenLongTan WPP':
    'water_right_shimenlongtan_wpp',
    'Water Right TaoYuan AgriChannel AgriWater':
    'water_right_taoyuan_agrichannel_agriwater',
    'Water Right TaoYuan CPC Refinery':
    'water_right_taoyuan_cpc_refinery',
    'Water Right TaoYuanDaHanRiver AgriWater':
    'water_right_taoyuandahanriver_agriwater',
    'WPP Transfer Loss Rate':
    'wpp_transfer_loss_rate',
    'YuanShan Lateral Flow':
    'yuanshan_lateral_flow',
    'YuanShan Weir':
    'yuanshan_weir',
    'YuanShan Weir Ecological Base Stream Flow':
    'yuanshan_weir_ecological_base_stream_flow',
    'YuanShan Weir Outflow':
    'yuanshan_weir_outflow',
    'YuanShanWeir Transfer Loss Amount':
    'yuanshanweir_transfer_loss_amount',
    'ZhongZhuang Adjustment Reservoir':
    'zhongzhuang_adjustment_reservoir',
    'ZhongZhuang Support To BanXinWPP':
    'zhongzhuang_support_to_banxinwpp',
    'ZhongZhuang Support To DaNanWPP':
    'zhongzhuang_support_to_dananwpp',
    'ZhongZhuang Weir':
    'zhongzhuang_weir',
    'ZhongZhuangAdjustmentReservoir Transfer Loss Amount':
    'zhongzhuangadjustmentreservoir_transfer_loss_amount',
    'FINAL TIME':
    'final_time',
    'INITIAL TIME':
    'initial_time',
    'SAVEPER':
    'saveper',
    'TIME STEP':
    'time_step'
}

__pysd_version__ = "0.9.0"


@cache('step')
def sum_allocation_shimenreservoir_to_houchiweir():
    """
    Real Name: Sum Allocation ShiMenReservoir To HouChiWeir
    Original Eqn: Allocation NCSIST+Allocation TaoYuan AgriChannel AgriWater+Allocation TaoYuan CPC Refinery\ +Allocation TaoYuanDaHanRiver AgriWater +Sum WPP ShiMenReservoir To HouChiWeir
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_ncsist() + allocation_taoyuan_agrichannel_agriwater(
    ) + allocation_taoyuan_cpc_refinery() + allocation_taoyuandahanriver_agriwater(
    ) + sum_wpp_shimenreservoir_to_houchiweir()


@cache('step')
def operation_rule_record_industry():
    """
    Real Name: Operation Rule Record Industry
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , 1 , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , 0.9 , 0.8 ))
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(), 1,
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(), 0.9,
            0.8))


@cache('step')
def operation_rule_record_agriculture():
    """
    Real Name: Operation Rule Record Agriculture
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , 1\ , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , 0.75 , 0.5 ))
    Units: 
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(), 1,
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(), 0.75,
            0.5))


@cache('step')
def allocation_banxin_wpp():
    """
    Real Name: Allocation BanXin WPP
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit ,Water Right BanXin WPP\ , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , Water Right BanXin WPP*0.9,Water Right BanXin WPP*0.8 ))
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_banxin_wpp(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_banxin_wpp() * 0.9,
            water_right_banxin_wpp() * 0.8))


@cache('step')
def allocation_danan_wpp1():
    """
    Real Name: Allocation DaNan WPP1
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , Water Right DaNan WPP1 , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , Water Right DaNan WPP1*0.9 , Water Right DaNan WPP1*0.8 ))
    Units: m3
    Limits: (None, None)
    Type: component

    source from YuanShan Weir;        water right 155520(m^3 per day)is the same for each Ten-days;
    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_danan_wpp1(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_danan_wpp1() * 0.9,
            water_right_danan_wpp1() * 0.8))


@cache('step')
def allocation_danan_wpp2():
    """
    Real Name: Allocation DaNan WPP2
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , Water Right DaNan WPP2 , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , Water Right DaNan WPP2*0.9 , Water Right DaNan WPP2*0.8 ))
    Units: m3
    Limits: (None, None)
    Type: component

    source from TaoYuan AgriChannel
    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_danan_wpp2(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_danan_wpp2() * 0.9,
            water_right_danan_wpp2() * 0.8))


@cache('step')
def allocation_longtan_wpp():
    """
    Real Name: Allocation LongTan WPP
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , Water Right ShiMenLongTan WPP\ *0.613, IF THEN ELSE ( ShiMen Reservoir Depth >=ShiMenReservoir Operation Rule Lower Severe Limit , Water Right ShiMenLongTan WPP*\ 0.613*0.9 , Water Right ShiMenLongTan WPP*0.613*0.8 ) )
    Units: m3
    Limits: (None, None)
    Type: component

    water right 146880(m^3 per day)is the sum of LongTan WPP & ShiMen WPP, the same for 
        each Ten-days;        "0.613" is the % responsibility of LomgTan WPP, calculated from their max 
        capacity.
    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_shimenlongtan_wpp() * 0.613,
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_shimenlongtan_wpp() * 0.613 * 0.9,
            water_right_shimenlongtan_wpp() * 0.613 * 0.8))


@cache('step')
def allocation_ncsist():
    """
    Real Name: Allocation NCSIST
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , 6048\ , IF THEN ELSE( ShiMen Reservoir Depth >=ShiMenReservoir Operation Rule Lower Severe Limit, 6048*0.9 , 6048*0.8 ) )
    Units: m3
    Limits: (None, None)
    Type: component

    water right 6048(m^3 per day), the same for each Ten-days;        0.07 CMSD, classified as Domestic.
    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(), 6048,
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            6048 * 0.9, 6048 * 0.8))


@cache('step')
def allocation_pingzhen_wpp1():
    """
    Real Name: Allocation PingZhen WPP1
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , Water Right PingZhen WPP1 , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , Water Right PingZhen WPP1*0.9 , Water Right PingZhen WPP1*0.8 ))
    Units: m3
    Limits: (None, None)
    Type: component

    source from ShiMen AgriChannel
    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_pingzhen_wpp1(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_pingzhen_wpp1() * 0.9,
            water_right_pingzhen_wpp1() * 0.8))


@cache('step')
def allocation_pingzhen_wpp2():
    """
    Real Name: Allocation PingZhen WPP2
    Original Eqn: IF THEN ELSE(ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit, Water Right PingZhen WPP2\ , IF THEN ELSE( ShiMen Reservoir Depth >=ShiMenReservoir Operation Rule Lower Severe Limit, Water Right PingZhen WPP2*0.9 ,\ Water Right PingZhen WPP2*0.8 ))
    Units: m3
    Limits: (None, None)
    Type: component

    source from HouChi Weir;        water right 172800(m^3 per day), the same for each Ten-days
    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_pingzhen_wpp2(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_pingzhen_wpp2() * 0.9,
            water_right_pingzhen_wpp2() * 0.8))


@cache('step')
def allocation_proportion_of_banxinwpp():
    """
    Real Name: Allocation Proportion of BanXinWPP
    Original Eqn: Allocation BanXin WPP/Total WPP Allocation
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_banxin_wpp() / total_wpp_allocation()


@cache('step')
def allocation_proportion_of_dananwpp1():
    """
    Real Name: Allocation Proportion of DaNanWPP1
    Original Eqn: Allocation DaNan WPP1/Total WPP Allocation
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_danan_wpp1() / total_wpp_allocation()


@cache('step')
def allocation_proportion_of_dananwpp2():
    """
    Real Name: Allocation Proportion of DaNanWPP2
    Original Eqn: Allocation DaNan WPP2/Total WPP Allocation
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_danan_wpp2() / total_wpp_allocation()


@cache('step')
def allocation_proportion_of_longtanwpp():
    """
    Real Name: Allocation Proportion of LongTanWPP
    Original Eqn: Allocation LongTan WPP/Total WPP Allocation
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_longtan_wpp() / total_wpp_allocation()


@cache('step')
def allocation_proportion_of_pingzhenwpp1():
    """
    Real Name: Allocation Proportion of PingZhenWPP1
    Original Eqn: Allocation PingZhen WPP1/Total WPP Allocation
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_pingzhen_wpp1() / total_wpp_allocation()


@cache('step')
def allocation_proportion_of_pingzhenwpp2():
    """
    Real Name: Allocation Proportion of PingZhenWPP2
    Original Eqn: Allocation PingZhen WPP2/Total WPP Allocation
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_pingzhen_wpp2() / total_wpp_allocation()


@cache('step')
def allocation_proportion_of_shimenwpp():
    """
    Real Name: Allocation Proportion of ShiMenWPP
    Original Eqn: Allocation ShiMen WPP/Total WPP Allocation
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_shimen_wpp() / total_wpp_allocation()


@cache('step')
def allocation_shimen_agrichannel_agriwater():
    """
    Real Name: Allocation ShiMen AgriChannel AgriWater
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , Water Right ShiMen AgriChannel AgriWater\ , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , Water Right ShiMen AgriChannel AgriWater*0.75 , Water Right ShiMen AgriChannel AgriWater\ *0.5 ))
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_shimen_agrichannel_agriwater(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_shimen_agrichannel_agriwater() * 0.75,
            water_right_shimen_agrichannel_agriwater() * 0.5))


@cache('step')
def allocation_shimen_wpp():
    """
    Real Name: Allocation ShiMen WPP
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , Water Right ShiMenLongTan WPP\ *0.387, IF THEN ELSE( ShiMen Reservoir Depth >=ShiMenReservoir Operation Rule Lower Severe Limit , Water Right ShiMenLongTan WPP*\ 0.387*0.9 , Water Right ShiMenLongTan WPP*0.387*0.8 ))
    Units: m3
    Limits: (None, None)
    Type: component

    water right 146880(m^3 per day)is the sum of LongTan WPP & ShiMen WPP, the same for 
        each Ten-days;        "0.387" is the % responsibility of ShiMen WPP, calculated from their max 
        capacity.
    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_shimenlongtan_wpp() * 0.387,
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_shimenlongtan_wpp() * 0.387 * 0.9,
            water_right_shimenlongtan_wpp() * 0.387 * 0.8))


@cache('step')
def allocation_taoyuan_agrichannel_agriwater():
    """
    Real Name: Allocation TaoYuan AgriChannel AgriWater
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , Water Right TaoYuan AgriChannel AgriWater\ , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , Water Right TaoYuan AgriChannel AgriWater*0.75 , Water Right TaoYuan AgriChannel AgriWater\ *0.5 ))
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_taoyuan_agrichannel_agriwater(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_taoyuan_agrichannel_agriwater() * 0.75,
            water_right_taoyuan_agrichannel_agriwater() * 0.5))


@cache('step')
def allocation_taoyuan_cpc_refinery():
    """
    Real Name: Allocation TaoYuan CPC Refinery
    Original Eqn: IF THEN ELSE(ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit, Water Right TaoYuan CPC Refinery , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , Water Right TaoYuan CPC Refinery*0.9 , Water Right TaoYuan CPC Refinery*0.8 ))
    Units: m3
    Limits: (None, None)
    Type: component

    classified as Domestic.
    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_taoyuan_cpc_refinery(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_taoyuan_cpc_refinery() * 0.9,
            water_right_taoyuan_cpc_refinery() * 0.8))


@cache('step')
def allocation_taoyuandahanriver_agriwater():
    """
    Real Name: Allocation TaoYuanDaHanRiver AgriWater
    Original Eqn: IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Limit , Water Right TaoYuanDaHanRiver AgriWater\ , IF THEN ELSE( ShiMen Reservoir Depth>=ShiMenReservoir Operation Rule Lower Severe Limit\ , Water Right TaoYuanDaHanRiver AgriWater*0.75 , Water Right TaoYuanDaHanRiver AgriWater\ *0.5 ))
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_limit(),
        water_right_taoyuandahanriver_agriwater(),
        functions.if_then_else(
            shimen_reservoir_depth() >= shimenreservoir_operation_rule_lower_severe_limit(),
            water_right_taoyuandahanriver_agriwater() * 0.75,
            water_right_taoyuandahanriver_agriwater() * 0.5))


@cache('step')
def banxin_water_demand():
    """
    Real Name: BanXin Water Demand
    Original Eqn: Transfer From BanXinWPP To BanXinWaterDemand*(1-Tap Water Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_banxinwpp_to_banxinwaterdemand() * (1 - tap_water_loss_rate())


@cache('step')
def banxin_wpp():
    """
    Real Name: BanXin WPP
    Original Eqn: (Taipei Water Department Source+Transfer From SanXiaWeir To BanXinWPP+Transfer From YuanShanWeir To BanXinWPP\ +Transfer From ZhongZhuangAdjustmentReservoir To BanXinWPP)-(Transfer From BanXinWPP To NorthTaoYuanWaterDemand\ +Transfer From BanXinWPP To BanXinWaterDemand)
    Units: m3
    Limits: (None, None)
    Type: component

    outcome should be zero, all in and out.
    """
    return (taipei_water_department_source() + transfer_from_sanxiaweir_to_banxinwpp() +
            transfer_from_yuanshanweir_to_banxinwpp() +
            transfer_from_zhongzhuangadjustmentreservoir_to_banxinwpp()) - (
                transfer_from_banxinwpp_to_northtaoyuanwaterdemand() +
                transfer_from_banxinwpp_to_banxinwaterdemand())


@cache('run')
def channel_transfer_loss_rate():
    """
    Real Name: Channel Transfer Loss Rate
    Original Eqn: 0
    Units: m3/m3
    Limits: (None, None)
    Type: constant

    This is "no loss rate" version.
    """
    return 0


@cache('step')
def danan_wpp():
    """
    Real Name: DaNan WPP
    Original Eqn: Tranfer From YuanShanWeir To DaNanWPP+Transfer From TaoYuanAgriChannel To DaNanWPP+Transfer From ZhongZhuangAdjustmentReservoir To DaNanWPP\ -(Transfer From DaNanWPP To NorthTaoYuanWaterDemand)
    Units: m3
    Limits: (None, None)
    Type: component

    outcome should be zero, all in and out.
    """
    return tranfer_from_yuanshanweir_to_dananwpp() + transfer_from_taoyuanagrichannel_to_dananwpp(
    ) + transfer_from_zhongzhuangadjustmentreservoir_to_dananwpp() - (
        transfer_from_dananwpp_to_northtaoyuanwaterdemand())


@cache('run')
def date():
    """
    Real Name: Date
    Original Eqn: 123
    Units: Day
    Limits: (None, None)
    Type: constant


    """
    return 123


@cache('step')
def domestic_water_demand():
    """
    Real Name: Domestic Water Demand
    Original Eqn: Public Water Demand*"Domestic-Industry Proportion"
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return public_water_demand() * domesticindustry_proportion()


@cache('step')
def domesticindustry_proportion():
    """
    Real Name: "Domestic-Industry Proportion"
    Original Eqn: TargetYear DomesticWaterDemand/(TargetYear DomesticWaterDemand+TargetYear IndustryWaterDemand\ )
    Units: m3/m3
    Limits: (None, None)
    Type: component

    Set by model context
    """
    return targetyear_domesticwaterdemand() / (
        targetyear_domesticwaterdemand() + targetyear_industrywaterdemand())


@cache('step')
def ecobaseflow():
    """
    Real Name: EcoBaseFlow
    Original Eqn: MIN(YuanShan Weir Ecological Base Stream Flow, Transfer From ZhongZhuangWeir To YuanShanWeir\ )
    Units: m3
    Limits: (None, None)
    Type: component

    198720 (m^3/day) is DaHan downstream EcoBaseFlow.
    """
    return np.minimum(yuanshan_weir_ecological_base_stream_flow(),
                      transfer_from_zhongzhuangweir_to_yuanshanweir())


@cache('step')
def final_allocation_shimenreservoir_to_houchiweir():
    """
    Real Name: Final Allocation ShiMenReservoir To HouChiWeir
    Original Eqn: MIN((ShiMen Reservoir-Support For DaHan River Ecological Base Stream Flow)*Ratio ShiMenReservoir To HouChiWeir\ , Allocation NCSIST+Allocation TaoYuan CPC Refinery+Sum AgriWater ShiMenReservoir To HouChiWeir +Sum WPP ShiMenReservoir To HouChiWeir )
    Units: m3
    Limits: (None, None)
    Type: component

    It's final, which has considered the Reservoir volumn.
    """
    return np.minimum(
        (shimen_reservoir() - support_for_dahan_river_ecological_base_stream_flow()) *
        ratio_shimenreservoir_to_houchiweir(),
        allocation_ncsist() + allocation_taoyuan_cpc_refinery() +
        sum_agriwater_shimenreservoir_to_houchiweir() + sum_wpp_shimenreservoir_to_houchiweir())


@cache('step')
def final_allocation_shimenreservoir_to_shimenagrichannel():
    """
    Real Name: Final Allocation ShiMenReservoir To ShiMenAgriChannel
    Original Eqn: MIN( (ShiMen Reservoir-Support For DaHan River Ecological Base Stream Flow)*Ratio ShiMenReservoir To ShiMenAgriChannel\ , Allocation NCSIST+Sum AgriWater ShiMenReservoir To ShiMenAgriChannel +Sum WPP ShiMenReservoir To ShiMenAgriChannel )
    Units: m3
    Limits: (None, None)
    Type: component

    It's final, which has considered the Reservoir volumn.
    """
    return np.minimum((shimen_reservoir() - support_for_dahan_river_ecological_base_stream_flow())
                      * ratio_shimenreservoir_to_shimenagrichannel(),
                      allocation_ncsist() + sum_agriwater_shimenreservoir_to_shimenagrichannel() +
                      sum_wpp_shimenreservoir_to_shimenagrichannel())


@cache('step')
def houchi_weir():
    """
    Real Name: HouChi Weir
    Original Eqn: Transfer From ShiMenReservoir To HouChiWeir+ShiMen Reservoir Overflow+Support EcoBaseFlow\ -Transfer From HouChiWeir To TaoYuanAgriChannel -Transfer From HouChiWeir To ZhongZhuangWeir -(PingZhen WPP2/(1-WPP Transfer Loss Rate))
    Units: m3
    Limits: (None, None)
    Type: component

    Should be zero(all in and out)
    """
    return transfer_from_shimenreservoir_to_houchiweir() + shimen_reservoir_overflow(
    ) + support_ecobaseflow() - transfer_from_houchiweir_to_taoyuanagrichannel(
    ) - transfer_from_houchiweir_to_zhongzhuangweir() - (pingzhen_wpp2() /
                                                         (1 - wpp_transfer_loss_rate()))


@cache('step')
def hsinchu_water_demand():
    """
    Real Name: HsinChu Water Demand
    Original Eqn: TaoChu TwoWay Support 1*(1-Tap Water Loss Rate)-TaoChu TwoWay Support 2
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return taochu_twoway_support_1() * (1 - tap_water_loss_rate()) - taochu_twoway_support_2()


@cache('step')
def industry_water_demand():
    """
    Real Name: Industry Water Demand
    Original Eqn: Public Water Demand*(1-"Domestic-Industry Proportion")
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return public_water_demand() * (1 - domesticindustry_proportion())


@cache('step')
def irrigation_tranfer_loss_amount():
    """
    Real Name: Irrigation Tranfer Loss Amount
    Original Eqn: Transfer From ZhongZhuangWeir To TaoYuanDaHanRiver AgriWater Demand*TaoYuan AgriChannel Irrigation Transfer Loss Rate
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_zhongzhuangweir_to_taoyuandahanriver_agriwater_demand(
    ) * taoyuan_agrichannel_irrigation_transfer_loss_rate()


@cache('step')
def longtan_wpp():
    """
    Real Name: LongTan WPP
    Original Eqn: Transfer From ShiMenReservoir To ShiMenAgriChannel*Ratio WPP ShiMenReservoir To ShiMenAgriChannel\ *Ratio LongTanWPP At ShiMenAgriChannel*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component

    WPP transfer loss is considered in the Demand section.
    """
    return transfer_from_shimenreservoir_to_shimenagrichannel(
    ) * ratio_wpp_shimenreservoir_to_shimenagrichannel() * ratio_longtanwpp_at_shimenagrichannel(
    ) * (1 - wpp_transfer_loss_rate())


@cache('step')
def north_taoyuan_water_demand():
    """
    Real Name: North TaoYuan Water Demand
    Original Eqn: (Transfer From BanXinWPP To NorthTaoYuanWaterDemand+Transfer From DaNanWPP To NorthTaoYuanWaterDemand\ +TaoYuan Water Supply Network 2)*(1-Tap Water Loss Rate)-TaoYuan Water Supply Network 1
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return (transfer_from_banxinwpp_to_northtaoyuanwaterdemand() +
            transfer_from_dananwpp_to_northtaoyuanwaterdemand() + taoyuan_water_supply_network_2()
            ) * (1 - tap_water_loss_rate()) - taoyuan_water_supply_network_1()


@cache('step')
def pingzhen_wpp1():
    """
    Real Name: PingZhen WPP1
    Original Eqn: Transfer From ShiMenReservoir To ShiMenAgriChannel*Ratio WPP ShiMenReservoir To ShiMenAgriChannel\ *Ratio PingZhenWPP1 At ShiMenAgriChannel*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component

    source from ShiMen AgriChannel;        WPP transfer loss is considered in the Demand section.
    """
    return transfer_from_shimenreservoir_to_shimenagrichannel(
    ) * ratio_wpp_shimenreservoir_to_shimenagrichannel() * ratio_pingzhenwpp1_at_shimenagrichannel(
    ) * (1 - wpp_transfer_loss_rate())


@cache('step')
def pingzhen_wpp2():
    """
    Real Name: PingZhen WPP2
    Original Eqn: Transfer From ShiMenReservoir To HouChiWeir*Ratio WPP ShiMenReservoir To HouChiWeir*\ Ratio PingZhenWPP2 At HouChiWeir*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component

    source from HouChi Weir;        WPP transfer loss is considered in the Demand section.
    """
    return transfer_from_shimenreservoir_to_houchiweir() * ratio_wpp_shimenreservoir_to_houchiweir(
    ) * ratio_pingzhenwpp2_at_houchiweir() * (1 - wpp_transfer_loss_rate())


@cache('step')
def proportion_checking_variable():
    """
    Real Name: Proportion Checking Variable
    Original Eqn: Total Allocation Proportion At HouChiWeir+Total Allocation Proportion At ShiMenAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component

    the sum should be 1.
    """
    return total_allocation_proportion_at_houchiweir(
    ) + total_allocation_proportion_at_shimenagrichannel()


@cache('step')
def public_water_demand():
    """
    Real Name: Public Water Demand
    Original Eqn: North TaoYuan Water Demand+South TaoYuan Water Demand
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return north_taoyuan_water_demand() + south_taoyuan_water_demand()


@cache('step')
def ratio_agriwater_houchiweir_to_taoyuanagrichannel():
    """
    Real Name: Ratio AgriWater HouChiWeir To TaoYuanAgriChannel
    Original Eqn: Sum AgriWater HouChiWeir To TaoYuanAgriChannel/Sum Allocation HouChiWeir To TaoYuanAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_agriwater_houchiweir_to_taoyuanagrichannel(
    ) / sum_allocation_houchiweir_to_taoyuanagrichannel()


@cache('step')
def ratio_agriwater_houchiweir_to_zhongzhuangweir():
    """
    Real Name: Ratio AgriWater HouChiWeir To ZhongZhuangWeir
    Original Eqn: Sum AgriWater HouChiWeir To ZhongZhuangWeir/Sum Allocation HouChiWeir To ZhongZhuangWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_agriwater_houchiweir_to_zhongzhuangweir(
    ) / sum_allocation_houchiweir_to_zhongzhuangweir()


@cache('step')
def ratio_agriwater_shimenreservoir_to_houchiweir():
    """
    Real Name: Ratio AgriWater ShiMenReservoir To HouChiWeir
    Original Eqn: Sum AgriWater ShiMenReservoir To HouChiWeir/Sum Allocation ShiMenReservoir To HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_agriwater_shimenreservoir_to_houchiweir(
    ) / sum_allocation_shimenreservoir_to_houchiweir()


@cache('step')
def ratio_agriwater_shimenreservoir_to_houchiweir_in_dahanriver():
    """
    Real Name: Ratio AgriWater ShiMenReservoir To HouChiWeir In DaHanRiver
    Original Eqn: Allocation TaoYuanDaHanRiver AgriWater/Sum Allocation ShiMenReservoir To HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_taoyuandahanriver_agriwater() / sum_allocation_shimenreservoir_to_houchiweir(
    )


@cache('step')
def ratio_agriwater_shimenreservoir_to_houchiweir_in_taoyuanagrichannel():
    """
    Real Name: Ratio AgriWater ShiMenReservoir To HouChiWeir In TaoYuanAgriChannel
    Original Eqn: Allocation TaoYuan AgriChannel AgriWater/Sum Allocation ShiMenReservoir To HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_taoyuan_agrichannel_agriwater(
    ) / sum_allocation_shimenreservoir_to_houchiweir()


@cache('step')
def ratio_agriwater_shimenreservoir_to_shimenagrichannel():
    """
    Real Name: Ratio AgriWater ShiMenReservoir To ShiMenAgriChannel
    Original Eqn: Sum AgriWater ShiMenReservoir To ShiMenAgriChannel/Sum Allocation ShiMenReservoir To ShiMenAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_agriwater_shimenreservoir_to_shimenagrichannel(
    ) / sum_allocation_shimenreservoir_to_shimenagrichannel()


@cache('step')
def ratio_banxinwpp_allocation_at_yuanshanweir():
    """
    Real Name: Ratio BanXinWPP Allocation At YuanShanWeir
    Original Eqn: Allocation BanXin WPP/Total WPP Allocation At YuanShanWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_banxin_wpp() / total_wpp_allocation_at_yuanshanweir()


@cache('step')
def ratio_banxinwpp_at_houchiweir():
    """
    Real Name: Ratio BanXinWPP At HouChiWeir
    Original Eqn: Allocation BanXin WPP/Total WPP Allocation At HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_banxin_wpp() / total_wpp_allocation_at_houchiweir()


@cache('step')
def ratio_dananwpp1_allocation_at_yuanshanwei():
    """
    Real Name: Ratio DaNanWPP1 Allocation At YuanShanWei
    Original Eqn: Allocation DaNan WPP1/Total WPP Allocation At YuanShanWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_danan_wpp1() / total_wpp_allocation_at_yuanshanweir()


@cache('step')
def ratio_dananwpp1_at_houchiweir():
    """
    Real Name: Ratio DaNanWPP1 At HouChiWeir
    Original Eqn: Allocation DaNan WPP1/Total WPP Allocation At HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_danan_wpp1() / total_wpp_allocation_at_houchiweir()


@cache('step')
def ratio_dananwpp2_at_houchiweir():
    """
    Real Name: Ratio DaNanWPP2 At HouChiWeir
    Original Eqn: Allocation DaNan WPP2/Total WPP Allocation At HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_danan_wpp2() / total_wpp_allocation_at_houchiweir()


@cache('step')
def ratio_longtanwpp_at_shimenagrichannel():
    """
    Real Name: Ratio LongTanWPP At ShiMenAgriChannel
    Original Eqn: Allocation LongTan WPP/Total WPP Allocation At ShiMenAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_longtan_wpp() / total_wpp_allocation_at_shimenagrichannel()


@cache('step')
def ratio_ncsist_at_houchiweir():
    """
    Real Name: Ratio NCSIST At HouChiWeir
    Original Eqn: Allocation NCSIST/Sum Allocation ShiMenReservoir To HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_ncsist() / sum_allocation_shimenreservoir_to_houchiweir()


@cache('step')
def ratio_ncsist_at_shimenagrichannel():
    """
    Real Name: Ratio NCSIST At ShiMenAgriChannel
    Original Eqn: Allocation NCSIST/Sum Allocation ShiMenReservoir To ShiMenAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_ncsist() / sum_allocation_shimenreservoir_to_shimenagrichannel()


@cache('step')
def ratio_ncsist_at_taoyuanagrichannel():
    """
    Real Name: Ratio NCSIST At TaoYuanAgriChannel
    Original Eqn: Allocation NCSIST/Sum Allocation HouChiWeir To TaoYuanAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_ncsist() / sum_allocation_houchiweir_to_taoyuanagrichannel()


@cache('step')
def ratio_pingzhenwpp1_at_shimenagrichannel():
    """
    Real Name: Ratio PingZhenWPP1 At ShiMenAgriChannel
    Original Eqn: Allocation PingZhen WPP1/Total WPP Allocation At ShiMenAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_pingzhen_wpp1() / total_wpp_allocation_at_shimenagrichannel()


@cache('step')
def ratio_pingzhenwpp2_at_houchiweir():
    """
    Real Name: Ratio PingZhenWPP2 At HouChiWeir
    Original Eqn: Allocation PingZhen WPP2/Total WPP Allocation At HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_pingzhen_wpp2() / total_wpp_allocation_at_houchiweir()


@cache('step')
def ratio_shimenreservoir_to_houchiweir():
    """
    Real Name: Ratio ShiMenReservoir To HouChiWeir
    Original Eqn: Sum Allocation ShiMenReservoir To HouChiWeir/Sum Allcation From ShiMenReservoir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_allocation_shimenreservoir_to_houchiweir() / sum_allcation_from_shimenreservoir()


@cache('step')
def ratio_shimenreservoir_to_shimenagrichannel():
    """
    Real Name: Ratio ShiMenReservoir To ShiMenAgriChannel
    Original Eqn: Sum Allocation ShiMenReservoir To ShiMenAgriChannel/Sum Allcation From ShiMenReservoir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_allocation_shimenreservoir_to_shimenagrichannel(
    ) / sum_allcation_from_shimenreservoir()


@cache('step')
def ratio_shimenwpp_at_shimenagrichannel():
    """
    Real Name: Ratio ShiMenWPP At ShiMenAgriChannel
    Original Eqn: Allocation ShiMen WPP/Total WPP Allocation At ShiMenAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_shimen_wpp() / total_wpp_allocation_at_shimenagrichannel()


@cache('step')
def ratio_taoyuan_cpc_refinery_at_houchiweir():
    """
    Real Name: Ratio TaoYuan CPC Refinery At HouChiWeir
    Original Eqn: Allocation TaoYuan CPC Refinery/Sum Allocation ShiMenReservoir To HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_taoyuan_cpc_refinery() / sum_allocation_shimenreservoir_to_houchiweir()


@cache('step')
def ratio_taoyuan_cpc_refinery_at_taoyuanagrichannel():
    """
    Real Name: Ratio TaoYuan CPC Refinery At TaoYuanAgriChannel
    Original Eqn: Allocation TaoYuan CPC Refinery/Sum Allocation HouChiWeir To TaoYuanAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_taoyuan_cpc_refinery() / sum_allocation_houchiweir_to_taoyuanagrichannel()


@cache('step')
def ratio_wpp_houchiweir_to_taoyuanagrichannel():
    """
    Real Name: Ratio WPP HouChiWeir To TaoYuanAgriChannel
    Original Eqn: Sum WPP HouChiWeir To TaoYuanAgriChannel/Sum Allocation HouChiWeir To TaoYuanAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_wpp_houchiweir_to_taoyuanagrichannel(
    ) / sum_allocation_houchiweir_to_taoyuanagrichannel()


@cache('step')
def ratio_wpp_houchiweir_to_zhongzhuangweir():
    """
    Real Name: Ratio WPP HouChiWeir To ZhongZhuangWeir
    Original Eqn: Sum WPP HouChiWeir To ZhongZhuangWeir/Sum Allocation HouChiWeir To ZhongZhuangWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_wpp_houchiweir_to_zhongzhuangweir() / sum_allocation_houchiweir_to_zhongzhuangweir()


@cache('step')
def ratio_wpp_shimenreservoir_to_houchiweir():
    """
    Real Name: Ratio WPP ShiMenReservoir To HouChiWeir
    Original Eqn: Sum WPP ShiMenReservoir To HouChiWeir/Sum Allocation ShiMenReservoir To HouChiWeir
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_wpp_shimenreservoir_to_houchiweir() / sum_allocation_shimenreservoir_to_houchiweir()


@cache('step')
def ratio_wpp_shimenreservoir_to_shimenagrichannel():
    """
    Real Name: Ratio WPP ShiMenReservoir To ShiMenAgriChannel
    Original Eqn: Sum WPP ShiMenReservoir To ShiMenAgriChannel/Sum Allocation ShiMenReservoir To ShiMenAgriChannel
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return sum_wpp_shimenreservoir_to_shimenagrichannel(
    ) / sum_allocation_shimenreservoir_to_shimenagrichannel()


@cache('run')
def ratio_zhongzhuangadjustmentreservoir_take():
    """
    Real Name: Ratio ZhongZhuangAdjustmentReservoir take
    Original Eqn: 0
    Units: m3/m3
    Limits: (None, None)
    Type: constant

    this ratio means how much amount ZhongZhuang Adgustment Reservoir share the YuanShan 
        Weir's flow.        Here assume zero to ignore this facility.
    """
    return 0


@cache('run')
def sanxia_river_ecological_base_stream_flow():
    """
    Real Name: SanXia River Ecological Base Stream Flow
    Original Eqn: 43459.2
    Units: m3
    Limits: (None, None)
    Type: constant

    0.503cms, equals 43459.2 m^3 per day
    """
    return 43459.2


@cache('run')
def sanxia_river_inflow():
    """
    Real Name: SanXia River Inflow
    Original Eqn: 450000
    Units: m3
    Limits: (None, None)
    Type: constant

    use 450000 to test
    """
    return 450000


@cache('step')
def sanxia_weir():
    """
    Real Name: SanXia Weir
    Original Eqn: SanXia River Inflow-SanXia Weir Outflow-Transfer From SanXiaWeir To BanXinWPP-SanXiaWeir Transfer Loss Amount
    Units: m3
    Limits: (None, None)
    Type: component

    Should be zero(all in and out)
    """
    return sanxia_river_inflow() - sanxia_weir_outflow() - transfer_from_sanxiaweir_to_banxinwpp(
    ) - sanxiaweir_transfer_loss_amount()


@cache('step')
def sanxia_weir_outflow():
    """
    Real Name: SanXia Weir Outflow
    Original Eqn: IF THEN ELSE(SanXia River Inflow<=SanXia River Ecological Base Stream Flow, SanXia River Inflow\ , IF THEN ELSE ( Transfer From SanXiaWeir To BanXinWPP=(530000*(1-WPP Transfer Loss Rate)) , SanXia River Inflow\ -(Transfer From SanXiaWeir To BanXinWPP /(1-WPP Transfer Loss Rate)) , SanXia River Ecological Base Stream Flow ))
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        sanxia_river_inflow() <= sanxia_river_ecological_base_stream_flow(), sanxia_river_inflow(),
        functions.if_then_else(
            transfer_from_sanxiaweir_to_banxinwpp() == (530000 * (1 - wpp_transfer_loss_rate())),
            sanxia_river_inflow() -
            (transfer_from_sanxiaweir_to_banxinwpp() / (1 - wpp_transfer_loss_rate())),
            sanxia_river_ecological_base_stream_flow()))


@cache('step')
def sanxiaweir_transfer_loss_amount():
    """
    Real Name: SanXiaWeir Transfer Loss Amount
    Original Eqn: Transfer From SanXiaWeir To BanXinWPP/(1-WPP Transfer Loss Rate)*WPP Transfer Loss Rate
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_sanxiaweir_to_banxinwpp() / (
        1 - wpp_transfer_loss_rate()) * wpp_transfer_loss_rate()


@cache('step')
def shimen_agrichannel():
    """
    Real Name: ShiMen AgriChannel
    Original Eqn: Transfer From ShiMenReservoir To ShiMenAgriChannel-LongTan WPP-PingZhen WPP1-ShiMen AgriChannel Transfer Loss Amount\ -ShiMen WPP -Transfer From ShiMenAgriChannel To NCSIST-Transfer From ShiMenAgriChannel To ShiMenAgriWaterDemand
    Units: m3
    Limits: (None, None)
    Type: component

    Should be zero(all in and out)
    """
    return transfer_from_shimenreservoir_to_shimenagrichannel() - longtan_wpp() - pingzhen_wpp1(
    ) - shimen_agrichannel_transfer_loss_amount() - shimen_wpp(
    ) - transfer_from_shimenagrichannel_to_ncsist(
    ) - transfer_from_shimenagrichannel_to_shimenagriwaterdemand()


@cache('run')
def shimen_agrichannel_agriwater_actual_consumption():
    """
    Real Name: ShiMen AgriChannel AgriWater Actual Consumption
    Original Eqn: 0
    Units: m3
    Limits: (None, None)
    Type: constant

    need to input data file;        asume zero for test.
    """
    return 0


@cache('step')
def shimen_agrichannel_agriwater_demand():
    """
    Real Name: ShiMen AgriChannel AgriWater Demand
    Original Eqn: Transfer From ShiMenAgriChannel To ShiMenAgriWaterDemand-ShiMen Irrigation Area Outflow\ -ShiMen AgriChannel Irrigation Transfer Loss Amount
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenagrichannel_to_shimenagriwaterdemand(
    ) - shimen_irrigation_area_outflow() - shimen_agrichannel_irrigation_transfer_loss_amount()


@cache('step')
def shimen_agrichannel_irrigation_transfer_loss_amount():
    """
    Real Name: ShiMen AgriChannel Irrigation Transfer Loss Amount
    Original Eqn: Transfer From ShiMenAgriChannel To ShiMenAgriWaterDemand*ShiMen AgriChannel Irrigation Transfer Loss Rate
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenagrichannel_to_shimenagriwaterdemand(
    ) * shimen_agrichannel_irrigation_transfer_loss_rate()


@cache('run')
def shimen_agrichannel_irrigation_transfer_loss_rate():
    """
    Real Name: ShiMen AgriChannel Irrigation Transfer Loss Rate
    Original Eqn: 0
    Units: m3/m3
    Limits: (None, None)
    Type: constant

    This is "no loss rate" version.
    """
    return 0


@cache('step')
def shimen_agrichannel_transfer_loss_amount():
    """
    Real Name: ShiMen AgriChannel Transfer Loss Amount
    Original Eqn: Transfer From ShiMenReservoir To ShiMenAgriChannel*Ratio WPP ShiMenReservoir To ShiMenAgriChannel\ *WPP Transfer Loss Rate+Transfer From ShiMenReservoir To ShiMenAgriChannel*(Ratio AgriWater ShiMenReservoir To ShiMenAgriChannel +Ratio NCSIST At ShiMenAgriChannel) *Channel Transfer Loss Rate
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenreservoir_to_shimenagrichannel(
    ) * ratio_wpp_shimenreservoir_to_shimenagrichannel() * wpp_transfer_loss_rate(
    ) + transfer_from_shimenreservoir_to_shimenagrichannel() * (
        ratio_agriwater_shimenreservoir_to_shimenagrichannel() +
        ratio_ncsist_at_shimenagrichannel()) * channel_transfer_loss_rate()


@cache('step')
def shimen_irrigation_area_outflow():
    """
    Real Name: ShiMen Irrigation Area Outflow
    Original Eqn: Transfer From ShiMenAgriChannel To ShiMenAgriWaterDemand-ShiMen AgriChannel Irrigation Transfer Loss Amount\ -ShiMen AgriChannel AgriWater Actual Consumption
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenagrichannel_to_shimenagriwaterdemand(
    ) - shimen_agrichannel_irrigation_transfer_loss_amount(
    ) - shimen_agrichannel_agriwater_actual_consumption()


@cache('step')
def shimen_reservoir():
    """
    Real Name: ShiMen Reservoir
    Original Eqn: INTEG ( ShiMen Reservoir Inflow-ShiMen Reservoir Evaporation-ShiMen Reservoir Overflow-Support EcoBaseFlow\ -Transfer From ShiMenReservoir To HouChiWeir-Transfer From ShiMenReservoir To ShiMenAgriChannel\ , 1.06071e+008)
    Units: m3
    Limits: (None, None)
    Type: component

    Should adjust corespond Initial depth value.        Volume constraint is considered in the Variable "ShiMen Reservoir Outflow".
    """
    return integ_shimen_reservoir()


@cache('step')
def shimen_reservoir_area():
    """
    Real Name: ShiMen Reservoir Area
    Original Eqn: WITH LOOKUP ( ShiMen Reservoir, ([(0,0)-(2.02278e+008,9e+006)],(0,822667),(896296,972000),(1.89843e+006,1.03257e+006\ ),(3.00141e+006,1.17492e+006),(4.2111e+006,1.24479e+006),(5.49883e+006,1.33117e+006\ ),(6.85434e+006,1.37999e+006),(8.27291e+006,1.45751e+006),(9.77081e+006,1.53867e+006\ ),(1.13411e+007,1.60218e+006),(1.29775e+007,1.67079e+006),(1.46904e+007,1.75543e+006\ ),(1.64853e+007,1.83452e+006),(1.83768e+007,1.94916e+006),(2.04074e+007,2.11318e+006\ ),(2.25632e+007,2.19873e+006),(2.47986e+007,2.27217e+006),(2.71057e+007,2.34227e+006\ ),(2.9498e+007,2.44276e+006),(3.19865e+007,2.5345e+006),(3.45703e+007,2.63342e+006)\ ,(3.72513e+007,2.72885e+006),(4.00261e+007,2.82085e+006),(4.29298e+007,2.98752e+006\ ),(4.59992e+007,3.15203e+006),(4.92558e+007,3.36226e+006),(5.2845e+007,3.82106e+006\ ),(5.68249e+007,4.1408e+006),(6.10739e+007,4.35817e+006),(6.5513e+007,4.52044e+006)\ ,(7.01011e+007,4.65611e+006),(7.4826e+007,4.79401e+006),(7.96996e+007,4.95359e+006)\ ,(8.47447e+007,5.1372e+006),(8.99704e+007,5.31475e+006),(9.53755e+007,5.49595e+006)\ ,(1.00962e+008,5.67808e+006),(1.06734e+008,5.86525e+006),(1.12706e+008,6.07969e+006\ ),(1.18915e+008,6.33995e+006),(1.25416e+008,6.66374e+006),(1.32177e+008,6.85797e+006\ ),(1.39119e+008,7.02591e+006),(1.46231e+008,7.19871e+006),(1.53542e+008,7.42388e+006\ ),(1.61098e+008,7.69011e+006),(1.68904e+008,7.92251e+006),(1.76932e+008,8.13304e+006\ ),(1.85168e+008,8.33844e+006),(1.93618e+008,8.56386e+006),(2.02278e+008,8.75639e+006\ ) ))
    Units: m2
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(shimen_reservoir(), [
        0, 896296, 1.89843e+006, 3.00141e+006, 4.2111e+006, 5.49883e+006, 6.85434e+006,
        8.27291e+006, 9.77081e+006, 1.13411e+007, 1.29775e+007, 1.46904e+007, 1.64853e+007,
        1.83768e+007, 2.04074e+007, 2.25632e+007, 2.47986e+007, 2.71057e+007, 2.9498e+007,
        3.19865e+007, 3.45703e+007, 3.72513e+007, 4.00261e+007, 4.29298e+007, 4.59992e+007,
        4.92558e+007, 5.2845e+007, 5.68249e+007, 6.10739e+007, 6.5513e+007, 7.01011e+007,
        7.4826e+007, 7.96996e+007, 8.47447e+007, 8.99704e+007, 9.53755e+007, 1.00962e+008,
        1.06734e+008, 1.12706e+008, 1.18915e+008, 1.25416e+008, 1.32177e+008, 1.39119e+008,
        1.46231e+008, 1.53542e+008, 1.61098e+008, 1.68904e+008, 1.76932e+008, 1.85168e+008,
        1.93618e+008, 2.02278e+008
    ], [
        822667, 972000, 1.03257e+006, 1.17492e+006, 1.24479e+006, 1.33117e+006, 1.37999e+006,
        1.45751e+006, 1.53867e+006, 1.60218e+006, 1.67079e+006, 1.75543e+006, 1.83452e+006,
        1.94916e+006, 2.11318e+006, 2.19873e+006, 2.27217e+006, 2.34227e+006, 2.44276e+006,
        2.5345e+006, 2.63342e+006, 2.72885e+006, 2.82085e+006, 2.98752e+006, 3.15203e+006,
        3.36226e+006, 3.82106e+006, 4.1408e+006, 4.35817e+006, 4.52044e+006, 4.65611e+006,
        4.79401e+006, 4.95359e+006, 5.1372e+006, 5.31475e+006, 5.49595e+006, 5.67808e+006,
        5.86525e+006, 6.07969e+006, 6.33995e+006, 6.66374e+006, 6.85797e+006, 7.02591e+006,
        7.19871e+006, 7.42388e+006, 7.69011e+006, 7.92251e+006, 8.13304e+006, 8.33844e+006,
        8.56386e+006, 8.75639e+006
    ])


@cache('step')
def shimen_reservoir_depth():
    """
    Real Name: ShiMen Reservoir Depth
    Original Eqn: WITH LOOKUP ( ShiMen Reservoir, ([(0,195)-(2.067e+008,245)],(0,195),(896296,196),(1.89843e+006,197),(3.00141e+006,198\ ),(4.2111e+006,199),(5.49883e+006,200),(6.85434e+006,201),(8.27291e+006,202),(9.77081e+006\ ,203),(1.13411e+007,204),(1.29775e+007,205),(1.46904e+007,206),(1.64853e+007,207),(\ 1.83768e+007,208),(2.04074e+007,209),(2.25632e+007,210),(2.47986e+007,211),(2.71057e+007\ ,212),(2.9498e+007,213),(3.19865e+007,214),(3.45703e+007,215),(3.72513e+007,216),(4.00261e+007\ ,217),(4.29298e+007,218),(4.59992e+007,219),(4.92558e+007,220),(5.2845e+007,221),(5.68249e+007\ ,222),(6.10739e+007,223),(6.5513e+007,224),(7.01011e+007,225),(7.4826e+007,226),(7.96996e+007\ ,227),(8.47447e+007,228),(8.99704e+007,229),(9.53755e+007,230),(1.00962e+008,231),(\ 1.06734e+008,232),(1.12706e+008,233),(1.18915e+008,234),(1.25416e+008,235),(1.32177e+008\ ,236),(1.39119e+008,237),(1.46231e+008,238),(1.53542e+008,239),(1.61098e+008,240),(\ 1.68904e+008,241),(1.76932e+008,242),(1.85168e+008,243),(1.93618e+008,244),(2.02278e+008\ ,245) ))
    Units: m
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(shimen_reservoir(), [
        0, 896296, 1.89843e+006, 3.00141e+006, 4.2111e+006, 5.49883e+006, 6.85434e+006,
        8.27291e+006, 9.77081e+006, 1.13411e+007, 1.29775e+007, 1.46904e+007, 1.64853e+007,
        1.83768e+007, 2.04074e+007, 2.25632e+007, 2.47986e+007, 2.71057e+007, 2.9498e+007,
        3.19865e+007, 3.45703e+007, 3.72513e+007, 4.00261e+007, 4.29298e+007, 4.59992e+007,
        4.92558e+007, 5.2845e+007, 5.68249e+007, 6.10739e+007, 6.5513e+007, 7.01011e+007,
        7.4826e+007, 7.96996e+007, 8.47447e+007, 8.99704e+007, 9.53755e+007, 1.00962e+008,
        1.06734e+008, 1.12706e+008, 1.18915e+008, 1.25416e+008, 1.32177e+008, 1.39119e+008,
        1.46231e+008, 1.53542e+008, 1.61098e+008, 1.68904e+008, 1.76932e+008, 1.85168e+008,
        1.93618e+008, 2.02278e+008
    ], [
        195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
        213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230,
        231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245
    ])


@cache('step')
def shimen_reservoir_evaporation():
    """
    Real Name: ShiMen Reservoir Evaporation
    Original Eqn: ShiMen Reservoir Area*ShiMenReseverior Month Evaporation Table*0.001
    Units: m3
    Limits: (None, None)
    Type: component

    unit m^3 per day
    """
    return shimen_reservoir_area() * shimenreseverior_month_evaporation_table() * 0.001


@cache('run')
def shimen_reservoir_inflow():
    """
    Real Name: ShiMen Reservoir Inflow
    Original Eqn: 5e+006
    Units: m3
    Limits: (None, None)
    Type: constant

    use 5000000 to test
    """
    return 5e+006


@cache('run')
def shimen_reservoir_max_volume():
    """
    Real Name: ShiMen Reservoir Max Volume
    Original Eqn: 2.02278e+008
    Units: m3
    Limits: (None, None)
    Type: constant

    for depth=245m;        unit (m^3)
    """
    return 2.02278e+008


@cache('step')
def shimen_reservoir_overflow():
    """
    Real Name: ShiMen Reservoir Overflow
    Original Eqn: IF THEN ELSE((ShiMen Reservoir Inflow-Transfer From ShiMenReservoir To HouChiWeir-Transfer From ShiMenReservoir To ShiMenAgriChannel -ShiMen Reservoir Evaporation +ShiMen Reservoir)>=(ShiMen Reservoir Max Volume), ShiMen Reservoir Inflow-Transfer From ShiMenReservoir To HouChiWeir\ - Transfer From ShiMenReservoir To ShiMenAgriChannel-ShiMen Reservoir Evaporation +ShiMen Reservoir-ShiMen Reservoir Max Volume, 0)
    Units: m3
    Limits: (None, None)
    Type: component

    assume no transfer loss
    """
    return functions.if_then_else(
        (shimen_reservoir_inflow() - transfer_from_shimenreservoir_to_houchiweir() -
         transfer_from_shimenreservoir_to_shimenagrichannel() - shimen_reservoir_evaporation() +
         shimen_reservoir()) >= (shimen_reservoir_max_volume()),
        shimen_reservoir_inflow() - transfer_from_shimenreservoir_to_houchiweir() -
        transfer_from_shimenreservoir_to_shimenagrichannel() - shimen_reservoir_evaporation() +
        shimen_reservoir() - shimen_reservoir_max_volume(), 0)


@cache('step')
def shimen_wpp():
    """
    Real Name: ShiMen WPP
    Original Eqn: Transfer From ShiMenReservoir To ShiMenAgriChannel*Ratio WPP ShiMenReservoir To ShiMenAgriChannel\ *Ratio ShiMenWPP At ShiMenAgriChannel*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenreservoir_to_shimenagrichannel(
    ) * ratio_wpp_shimenreservoir_to_shimenagrichannel() * ratio_shimenwpp_at_shimenagrichannel(
    ) * (1 - wpp_transfer_loss_rate())


@cache('step')
def shimen_wpp_adjusted():
    """
    Real Name: ShiMen WPP Adjusted
    Original Eqn: ShiMen WPP
    Units: m3
    Limits: (None, None)
    Type: component

    Here assume that it equals to ShiMen WPP inflow.        WPP transfer loss is considered in the Demand section.
    """
    return shimen_wpp()


@cache('step')
def shimen_wpp_storage_pool():
    """
    Real Name: ShiMen WPP Storage Pool
    Original Eqn: INTEG ( IF THEN ELSE(ShiMen WPP+ShiMen WPP Storage Pool-ShiMen WPP Adjusted>=500000, 0 , ShiMen WPP\ -ShiMen WPP Adjusted ), 500000)
    Units: m3
    Limits: (None, None)
    Type: component

    500000 m^3 Max Storage Pool Volume
    """
    return integ_shimen_wpp_storage_pool()


@cache('step')
def shimenreservoir_operation_rule_lower_limit():
    """
    Real Name: ShiMenReservoir Operation Rule Lower Limit
    Original Eqn: WITH LOOKUP ( Date, ([(1,190)-(366,250)],(1,240),(32,240),(152,220),(182,220),(244,225),(335,240),(365,\ 240) ))
    Units: m
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(date(), [1, 32, 152, 182, 244, 335, 365],
                            [240, 240, 220, 220, 225, 240, 240])


@cache('step')
def shimenreservoir_operation_rule_lower_severe_limit():
    """
    Real Name: ShiMenReservoir Operation Rule Lower Severe Limit
    Original Eqn: WITH LOOKUP ( Date, ([(1,190)-(366,250)],(1,225),(60,223),(91,220),(152,210),(182,210),(213,213),(274,213\ ),(305,215),(365,225) ))
    Units: m
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(date(), [1, 60, 91, 152, 182, 213, 274, 305, 365],
                            [225, 223, 220, 210, 210, 213, 213, 215, 225])


@cache('step')
def shimenreservoir_operation_rule_upper_limit():
    """
    Real Name: ShiMenReservoir Operation Rule Upper Limit
    Original Eqn: WITH LOOKUP ( Date, ([(1,190)-(366,250)],(1,245),(32,245),(42,244.333),(52,243.667),(60,243),(91,240),(\ 152,235),(182,235),(213,236),(244,240 ),(274,240),(305,245),(365,245) ))
    Units: m
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(
        date(), [1, 32, 42, 52, 60, 91, 152, 182, 213, 244, 274, 305, 365],
        [245, 245, 244.333, 243.667, 243, 240, 235, 235, 236, 240, 240, 245, 245])


@cache('step')
def shimenreseverior_month_evaporation_table():
    """
    Real Name: ShiMenReseverior Month Evaporation Table
    Original Eqn: WITH LOOKUP ( Date, ([(1,0)-(365,4)],(1,1.348),(31,1.348),(32,1.292),(59,1.292),(60,1.415),(90,1.415),(\ 91,1.72),(120,1.72),(121,2.168),(151,2.168),(152,2.694),(181,2.694),(182,3.611),(212\ ,3.611),(213,3.383),(243,3.383),(244,2.871),(273,2.871),(274,3.151),(304,3.151),(305\ ,2.097),(334,2.097),(335,1.875),(365,1.875) ))
    Units: mm
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(date(), [
        1, 31, 32, 59, 60, 90, 91, 120, 121, 151, 152, 181, 182, 212, 213, 243, 244, 273, 274, 304,
        305, 334, 335, 365
    ], [
        1.348, 1.348, 1.292, 1.292, 1.415, 1.415, 1.72, 1.72, 2.168, 2.168, 2.694, 2.694, 3.611,
        3.611, 3.383, 3.383, 2.871, 2.871, 3.151, 3.151, 2.097, 2.097, 1.875, 1.875
    ])


@cache('step')
def south_taoyuan_water_demand():
    """
    Real Name: South TaoYuan Water Demand
    Original Eqn: (LongTan WPP+PingZhen WPP1+PingZhen WPP2+ShiMen WPP Adjusted+TaoChu TwoWay Support 2\ +TaoYuan Water Supply Network 1)*(1-Tap Water Loss Rate)-TaoChu TwoWay Support 1-TaoYuan Water Supply Network 2
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return (longtan_wpp() + pingzhen_wpp1() + pingzhen_wpp2() + shimen_wpp_adjusted(
    ) + taochu_twoway_support_2() + taoyuan_water_supply_network_1()) * (
        1 - tap_water_loss_rate()) - taochu_twoway_support_1() - taoyuan_water_supply_network_2()


@cache('step')
def sum_agriwater_houchiweir_to_taoyuanagrichannel():
    """
    Real Name: Sum AgriWater HouChiWeir To TaoYuanAgriChannel
    Original Eqn: Allocation TaoYuan AgriChannel AgriWater
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_taoyuan_agrichannel_agriwater()


@cache('step')
def sum_agriwater_houchiweir_to_zhongzhuangweir():
    """
    Real Name: Sum AgriWater HouChiWeir To ZhongZhuangWeir
    Original Eqn: Allocation TaoYuanDaHanRiver AgriWater
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_taoyuandahanriver_agriwater()


@cache('step')
def sum_agriwater_shimenreservoir_to_houchiweir():
    """
    Real Name: Sum AgriWater ShiMenReservoir To HouChiWeir
    Original Eqn: Allocation TaoYuan AgriChannel AgriWater+Allocation TaoYuanDaHanRiver AgriWater
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_taoyuan_agrichannel_agriwater() + allocation_taoyuandahanriver_agriwater()


@cache('step')
def sum_agriwater_shimenreservoir_to_shimenagrichannel():
    """
    Real Name: Sum AgriWater ShiMenReservoir To ShiMenAgriChannel
    Original Eqn: Allocation ShiMen AgriChannel AgriWater
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_shimen_agrichannel_agriwater()


@cache('step')
def sum_allcation_from_shimenreservoir():
    """
    Real Name: Sum Allcation From ShiMenReservoir
    Original Eqn: Sum Allocation ShiMenReservoir To HouChiWeir+Sum Allocation ShiMenReservoir To ShiMenAgriChannel
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return sum_allocation_shimenreservoir_to_houchiweir(
    ) + sum_allocation_shimenreservoir_to_shimenagrichannel()


@cache('step')
def sum_allocation_houchiweir_to_taoyuanagrichannel():
    """
    Real Name: Sum Allocation HouChiWeir To TaoYuanAgriChannel
    Original Eqn: Allocation NCSIST+Allocation TaoYuan CPC Refinery+Sum AgriWater HouChiWeir To TaoYuanAgriChannel\ +Sum WPP HouChiWeir To TaoYuanAgriChannel
    Units: m3
    Limits: (None, None)
    Type: component

    Just the sum to calculate the ratio in the "Transfer ratio" sheet.
    """
    return allocation_ncsist() + allocation_taoyuan_cpc_refinery(
    ) + sum_agriwater_houchiweir_to_taoyuanagrichannel(
    ) + sum_wpp_houchiweir_to_taoyuanagrichannel()


@cache('step')
def sum_allocation_houchiweir_to_zhongzhuangweir():
    """
    Real Name: Sum Allocation HouChiWeir To ZhongZhuangWeir
    Original Eqn: Sum AgriWater HouChiWeir To ZhongZhuangWeir+Sum WPP HouChiWeir To ZhongZhuangWeir
    Units: m3
    Limits: (None, None)
    Type: component

    Just the sum to calculate the ratio in the "Transfer ratio" sheet.
    """
    return sum_agriwater_houchiweir_to_zhongzhuangweir() + sum_wpp_houchiweir_to_zhongzhuangweir()


@cache('step')
def sum_allocation_shimenreservoir_to_shimenagrichannel():
    """
    Real Name: Sum Allocation ShiMenReservoir To ShiMenAgriChannel
    Original Eqn: Allocation NCSIST+Sum AgriWater ShiMenReservoir To ShiMenAgriChannel+Sum WPP ShiMenReservoir To ShiMenAgriChannel
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_ncsist() + sum_agriwater_shimenreservoir_to_shimenagrichannel(
    ) + sum_wpp_shimenreservoir_to_shimenagrichannel()


@cache('step')
def sum_wpp_houchiweir_to_taoyuanagrichannel():
    """
    Real Name: Sum WPP HouChiWeir To TaoYuanAgriChannel
    Original Eqn: Allocation DaNan WPP2
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_danan_wpp2()


@cache('step')
def sum_wpp_houchiweir_to_zhongzhuangweir():
    """
    Real Name: Sum WPP HouChiWeir To ZhongZhuangWeir
    Original Eqn: Allocation BanXin WPP+Allocation DaNan WPP1
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_banxin_wpp() + allocation_danan_wpp1()


@cache('step')
def sum_wpp_shimenreservoir_to_houchiweir():
    """
    Real Name: Sum WPP ShiMenReservoir To HouChiWeir
    Original Eqn: Allocation BanXin WPP+Allocation DaNan WPP1+Allocation DaNan WPP2+Allocation PingZhen WPP2
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_banxin_wpp() + allocation_danan_wpp1() + allocation_danan_wpp2(
    ) + allocation_pingzhen_wpp2()


@cache('step')
def sum_wpp_shimenreservoir_to_shimenagrichannel():
    """
    Real Name: Sum WPP ShiMenReservoir To ShiMenAgriChannel
    Original Eqn: Allocation LongTan WPP+Allocation PingZhen WPP1+Allocation ShiMen WPP
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_longtan_wpp() + allocation_pingzhen_wpp1() + allocation_shimen_wpp()


@cache('step')
def support_ecobaseflow():
    """
    Real Name: Support EcoBaseFlow
    Original Eqn: Support For DaHan River Ecological Base Stream Flow
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return support_for_dahan_river_ecological_base_stream_flow()


@cache('step')
def support_for_dahan_river_ecological_base_stream_flow():
    """
    Real Name: Support For DaHan River Ecological Base Stream Flow
    Original Eqn: MIN(ShiMen Reservoir, MAX(0, YuanShan Weir Ecological Base Stream Flow-YuanShan Lateral Flow\ ) )
    Units: m3
    Limits: (None, None)
    Type: component

    Below YuanShanWeir, need 2.3cms (198720 m^3 per day) for Ecological Base 
        Stream Flow.
    """
    return np.minimum(
        shimen_reservoir(),
        np.maximum(0,
                   yuanshan_weir_ecological_base_stream_flow() - yuanshan_lateral_flow()))


@cache('step')
def taipei_water_department_source():
    """
    Real Name: Taipei Water Department Source
    Original Eqn: IF THEN ELSE(ShiMen Reservoir Depth>243, 300000 , 650000 )
    Units: m3
    Limits: (None, None)
    Type: component

    BanXin WPP purchasing rule
    """
    return functions.if_then_else(shimen_reservoir_depth() > 243, 300000, 650000)


@cache('run')
def taochu_twoway_support_1():
    """
    Real Name: TaoChu TwoWay Support 1
    Original Eqn: 10000
    Units: m3
    Limits: (None, None)
    Type: constant

    assume 10000 m^3 per day
    """
    return 10000


@cache('run')
def taochu_twoway_support_2():
    """
    Real Name: TaoChu TwoWay Support 2
    Original Eqn: 0
    Units: m3
    Limits: (None, None)
    Type: constant

    assume zero
    """
    return 0


@cache('step')
def taoyuan_agrichannel():
    """
    Real Name: TaoYuan AgriChannel
    Original Eqn: Transfer From HouChiWeir To TaoYuanAgriChannel-Transfer From TaoYuanAgriChannel To DaNanWPP\ -Transfer From TaoYuanAgriChannel To NCSIST-Transfer From TaoYuanAgriChannel To TaoYuanAgriWaterDemand\ -Transfer From TaoYuanAgriChannel To TaoYuanCPCRefinery-TaoYuan AgriChannel Transfer Loss Amount
    Units: m3
    Limits: (None, None)
    Type: component

    Should be zero(all in and out)
    """
    return transfer_from_houchiweir_to_taoyuanagrichannel(
    ) - transfer_from_taoyuanagrichannel_to_dananwpp() - transfer_from_taoyuanagrichannel_to_ncsist(
    ) - transfer_from_taoyuanagrichannel_to_taoyuanagriwaterdemand(
    ) - transfer_from_taoyuanagrichannel_to_taoyuancpcrefinery(
    ) - taoyuan_agrichannel_transfer_loss_amount()


@cache('run')
def taoyuan_agrichannel_agriwater_actual_consumption():
    """
    Real Name: TaoYuan AgriChannel AgriWater Actual Consumption
    Original Eqn: 0
    Units: m3
    Limits: (None, None)
    Type: constant

    need to input data file;        asume zero for test.
    """
    return 0


@cache('step')
def taoyuan_agrichannel_agriwater_demand():
    """
    Real Name: TaoYuan AgriChannel AgriWater Demand
    Original Eqn: Transfer From TaoYuanAgriChannel To TaoYuanAgriWaterDemand-TaoYuan Irrigation Area Outflow\ -TaoYuan AgriChannel Irrigation Transfer Loss Amount
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_taoyuanagrichannel_to_taoyuanagriwaterdemand(
    ) - taoyuan_irrigation_area_outflow() - taoyuan_agrichannel_irrigation_transfer_loss_amount()


@cache('step')
def taoyuan_agrichannel_irrigation_transfer_loss_amount():
    """
    Real Name: TaoYuan AgriChannel Irrigation Transfer Loss Amount
    Original Eqn: Transfer From TaoYuanAgriChannel To TaoYuanAgriWaterDemand*TaoYuan AgriChannel Irrigation Transfer Loss Rate
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_taoyuanagrichannel_to_taoyuanagriwaterdemand(
    ) * taoyuan_agrichannel_irrigation_transfer_loss_rate()


@cache('run')
def taoyuan_agrichannel_irrigation_transfer_loss_rate():
    """
    Real Name: TaoYuan AgriChannel Irrigation Transfer Loss Rate
    Original Eqn: 0
    Units: m3/m3
    Limits: (None, None)
    Type: constant

    This is "no loss rate" version.
    """
    return 0


@cache('step')
def taoyuan_agrichannel_transfer_loss_amount():
    """
    Real Name: TaoYuan AgriChannel Transfer Loss Amount
    Original Eqn: (Transfer From TaoYuanAgriChannel To NCSIST+Transfer From TaoYuanAgriChannel To TaoYuanAgriWaterDemand\ +Transfer From TaoYuanAgriChannel To TaoYuanCPCRefinery)/(1-Channel Transfer Loss Rate\ )*Channel Transfer Loss Rate+Transfer From TaoYuanAgriChannel To DaNanWPP/(1-WPP Transfer Loss Rate\ )*WPP Transfer Loss Rate
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return (transfer_from_taoyuanagrichannel_to_ncsist() +
            transfer_from_taoyuanagrichannel_to_taoyuanagriwaterdemand() +
            transfer_from_taoyuanagrichannel_to_taoyuancpcrefinery()) / (
                1 - channel_transfer_loss_rate()
            ) * channel_transfer_loss_rate() + transfer_from_taoyuanagrichannel_to_dananwpp() / (
                1 - wpp_transfer_loss_rate()) * wpp_transfer_loss_rate()


@cache('step')
def taoyuan_irrigation_area_outflow():
    """
    Real Name: TaoYuan Irrigation Area Outflow
    Original Eqn: Transfer From TaoYuanAgriChannel To TaoYuanAgriWaterDemand-TaoYuan AgriChannel AgriWater Actual Consumption\ -TaoYuan AgriChannel Irrigation Transfer Loss Amount
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_taoyuanagrichannel_to_taoyuanagriwaterdemand(
    ) - taoyuan_agrichannel_agriwater_actual_consumption(
    ) - taoyuan_agrichannel_irrigation_transfer_loss_amount()


@cache('run')
def taoyuan_water_supply_network_1():
    """
    Real Name: TaoYuan Water Supply Network 1
    Original Eqn: 0
    Units: m3
    Limits: (None, None)
    Type: constant

    primary design assumes zero in this model, which means does not consider 
        the impact of this pipeline.
    """
    return 0


@cache('run')
def taoyuan_water_supply_network_2():
    """
    Real Name: TaoYuan Water Supply Network 2
    Original Eqn: 0
    Units: m3
    Limits: (None, None)
    Type: constant

    primary design assumes zero in this model, which means does not consider 
        the impact of this pipeline.
    """
    return 0


@cache('step')
def taoyuandahanriver_agriwater_demand():
    """
    Real Name: TaoYuanDaHanRiver AgriWater Demand
    Original Eqn: Transfer From ZhongZhuangWeir To TaoYuanDaHanRiver AgriWater Demand-Irrigation Tranfer Loss Amount
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_zhongzhuangweir_to_taoyuandahanriver_agriwater_demand(
    ) - irrigation_tranfer_loss_amount()


@cache('run')
def tap_water_loss_rate():
    """
    Real Name: Tap Water Loss Rate
    Original Eqn: 0.1616
    Units: m3/m3
    Limits: (None, None)
    Type: constant

    Tap water loss rate in 2016
    """
    return 0.1616


@cache('run')
def targetyear_domesticwaterdemand():
    """
    Real Name: TargetYear DomesticWaterDemand
    Original Eqn: 704604
    Units: m3
    Limits: (None, None)
    Type: constant

    total domestic water consumption is 257180530 m^3 in year 2016;        Around 704604 m^3 per day.
    """
    return 704604


@cache('run')
def targetyear_industrywaterdemand():
    """
    Real Name: TargetYear IndustryWaterDemand
    Original Eqn: 351204
    Units: m3
    Limits: (None, None)
    Type: constant

    total industry water consumption is 128189600 m^3 in year 2016;        Around 351204 m^3 per day.
    """
    return 351204


@cache('step')
def total_allocation_proportion_at_houchiweir():
    """
    Real Name: Total Allocation Proportion At HouChiWeir
    Original Eqn: Allocation Proportion of BanXinWPP+Allocation Proportion of DaNanWPP1+Allocation Proportion of DaNanWPP2\ +Allocation Proportion of PingZhenWPP2
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_proportion_of_banxinwpp() + allocation_proportion_of_dananwpp1(
    ) + allocation_proportion_of_dananwpp2() + allocation_proportion_of_pingzhenwpp2()


@cache('step')
def total_allocation_proportion_at_shimenagrichannel():
    """
    Real Name: Total Allocation Proportion At ShiMenAgriChannel
    Original Eqn: Allocation Proportion of LongTanWPP+Allocation Proportion of PingZhenWPP1+Allocation Proportion of ShiMenWPP
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_proportion_of_longtanwpp() + allocation_proportion_of_pingzhenwpp1(
    ) + allocation_proportion_of_shimenwpp()


@cache('step')
def total_allocation_proportion_at_zhongzhuangweir():
    """
    Real Name: Total Allocation Proportion At ZhongZhuangWeir
    Original Eqn: Allocation Proportion of BanXinWPP+Allocation Proportion of DaNanWPP1
    Units: m3/m3
    Limits: (None, None)
    Type: component


    """
    return allocation_proportion_of_banxinwpp() + allocation_proportion_of_dananwpp1()


@cache('step')
def total_wpp_allocation():
    """
    Real Name: Total WPP Allocation
    Original Eqn: Allocation BanXin WPP+Allocation DaNan WPP1+Allocation DaNan WPP2+Allocation LongTan WPP\ +Allocation PingZhen WPP1+Allocation PingZhen WPP2+Allocation ShiMen WPP
    Units: m3
    Limits: (None, None)
    Type: component

    Not include NCSIST and CPC Refinery, it's used to calculate each WPP's 
        proportion.
    """
    return allocation_banxin_wpp() + allocation_danan_wpp1() + allocation_danan_wpp2(
    ) + allocation_longtan_wpp() + allocation_pingzhen_wpp1() + allocation_pingzhen_wpp2(
    ) + allocation_shimen_wpp()


@cache('step')
def total_wpp_allocation_at_houchiweir():
    """
    Real Name: Total WPP Allocation At HouChiWeir
    Original Eqn: Allocation BanXin WPP+Allocation DaNan WPP1+Allocation DaNan WPP2+Allocation PingZhen WPP2
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_banxin_wpp() + allocation_danan_wpp1() + allocation_danan_wpp2(
    ) + allocation_pingzhen_wpp2()


@cache('step')
def total_wpp_allocation_at_shimenagrichannel():
    """
    Real Name: Total WPP Allocation At ShiMenAgriChannel
    Original Eqn: Allocation LongTan WPP+Allocation PingZhen WPP1+Allocation ShiMen WPP
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_longtan_wpp() + allocation_pingzhen_wpp1() + allocation_shimen_wpp()


@cache('step')
def total_wpp_allocation_at_yuanshanweir():
    """
    Real Name: Total WPP Allocation At YuanShanWeir
    Original Eqn: Allocation BanXin WPP+Allocation DaNan WPP1
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return allocation_banxin_wpp() + allocation_danan_wpp1()


@cache('step')
def tranfer_from_yuanshanweir_to_dananwpp():
    """
    Real Name: Tranfer From YuanShanWeir To DaNanWPP
    Original Eqn: IF THEN ELSE((Transfer From ZhongZhuangWeir To YuanShanWeir-EcoBaseFlow)*Ratio BanXinWPP Allocation At YuanShanWeir\ >Allocation BanXin WPP, MIN(350000, Transfer From ZhongZhuangWeir To YuanShanWeir-EcoBaseFlow\ -Allocation BanXin WPP) , (Transfer From ZhongZhuangWeir To YuanShanWeir-EcoBaseFlow\ )*Ratio DaNanWPP1 Allocation At YuanShanWei )*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component

    Channel max ability = 350000 m^3 per day
    """
    return functions.if_then_else(
        (transfer_from_zhongzhuangweir_to_yuanshanweir() - ecobaseflow()) *
        ratio_banxinwpp_allocation_at_yuanshanweir() > allocation_banxin_wpp(),
        np.minimum(
            350000,
            transfer_from_zhongzhuangweir_to_yuanshanweir() - ecobaseflow() -
            allocation_banxin_wpp()),
        (transfer_from_zhongzhuangweir_to_yuanshanweir() - ecobaseflow()) *
        ratio_dananwpp1_allocation_at_yuanshanwei()) * (1 - wpp_transfer_loss_rate())


@cache('step')
def transfer_from_banxinwpp_to_banxinwaterdemand():
    """
    Real Name: Transfer From BanXinWPP To BanXinWaterDemand
    Original Eqn: Taipei Water Department Source+Transfer From SanXiaWeir To BanXinWPP+Transfer From YuanShanWeir To BanXinWPP\ +Transfer From ZhongZhuangAdjustmentReservoir To BanXinWPP-Transfer From BanXinWPP To NorthTaoYuanWaterDemand
    Units: m3
    Limits: (None, None)
    Type: component

    WPP transfer loss is considered in the Demand section
    """
    return taipei_water_department_source() + transfer_from_sanxiaweir_to_banxinwpp(
    ) + transfer_from_yuanshanweir_to_banxinwpp(
    ) + transfer_from_zhongzhuangadjustmentreservoir_to_banxinwpp(
    ) - transfer_from_banxinwpp_to_northtaoyuanwaterdemand()


@cache('run')
def transfer_from_banxinwpp_to_northtaoyuanwaterdemand():
    """
    Real Name: Transfer From BanXinWPP To NorthTaoYuanWaterDemand
    Original Eqn: 170000
    Units: m3
    Limits: (None, None)
    Type: constant

    Assume 170000 m^3 per day.        WPP transfer loss is considered in the Demand section.
    """
    return 170000


@cache('step')
def transfer_from_dananwpp_to_northtaoyuanwaterdemand():
    """
    Real Name: Transfer From DaNanWPP To NorthTaoYuanWaterDemand
    Original Eqn: Tranfer From YuanShanWeir To DaNanWPP+Transfer From TaoYuanAgriChannel To DaNanWPP+Transfer From ZhongZhuangAdjustmentReservoir To DaNanWPP
    Units: m3
    Limits: (None, None)
    Type: component

    WPP transfer loss is considered in the Demand section
    """
    return tranfer_from_yuanshanweir_to_dananwpp() + transfer_from_taoyuanagrichannel_to_dananwpp(
    ) + transfer_from_zhongzhuangadjustmentreservoir_to_dananwpp()


@cache('step')
def transfer_from_houchiweir_to_taoyuanagrichannel():
    """
    Real Name: Transfer From HouChiWeir To TaoYuanAgriChannel
    Original Eqn: Transfer From ShiMenReservoir To HouChiWeir*(Ratio WPP ShiMenReservoir To HouChiWeir\ *Ratio DaNanWPP2 At HouChiWeir+Ratio AgriWater ShiMenReservoir To HouChiWeir In TaoYuanAgriChannel\ +Ratio NCSIST At HouChiWeir+Ratio TaoYuan CPC Refinery At HouChiWeir )
    Units: m3
    Limits: (None, None)
    Type: component

    assume no transfer loss        should include the results of operation rule, each allocation under each 
        situation
    """
    return transfer_from_shimenreservoir_to_houchiweir() * (
        ratio_wpp_shimenreservoir_to_houchiweir() * ratio_dananwpp2_at_houchiweir() +
        ratio_agriwater_shimenreservoir_to_houchiweir_in_taoyuanagrichannel() +
        ratio_ncsist_at_houchiweir() + ratio_taoyuan_cpc_refinery_at_houchiweir())


@cache('step')
def transfer_from_houchiweir_to_zhongzhuangweir():
    """
    Real Name: Transfer From HouChiWeir To ZhongZhuangWeir
    Original Eqn: Transfer From ShiMenReservoir To HouChiWeir+ShiMen Reservoir Overflow+Support EcoBaseFlow\ -Transfer From HouChiWeir To TaoYuanAgriChannel-PingZhen WPP2/(1-WPP Transfer Loss Rate\ )
    Units: m3
    Limits: (None, None)
    Type: component

    Assume that he transfer loss between HouChiWeir and YuanShanWeir is 
        considered and included in "YuanShan Lateral Flow".
    """
    return transfer_from_shimenreservoir_to_houchiweir() + shimen_reservoir_overflow(
    ) + support_ecobaseflow() - transfer_from_houchiweir_to_taoyuanagrichannel(
    ) - pingzhen_wpp2() / (1 - wpp_transfer_loss_rate())


@cache('step')
def transfer_from_sanxiaweir_to_banxinwpp():
    """
    Real Name: Transfer From SanXiaWeir To BanXinWPP
    Original Eqn: IF THEN ELSE( SanXia River Inflow<=SanXia River Ecological Base Stream Flow, 0 , MIN\ (530000,(SanXia River Inflow -SanXia River Ecological Base Stream Flow))*(1-WPP Transfer Loss Rate))
    Units: m3
    Limits: (None, None)
    Type: component

    intake constraint is 530000(cubic meter per day)
    """
    return functions.if_then_else(
        sanxia_river_inflow() <= sanxia_river_ecological_base_stream_flow(), 0,
        np.minimum(530000, (sanxia_river_inflow() - sanxia_river_ecological_base_stream_flow())) *
        (1 - wpp_transfer_loss_rate()))


@cache('step')
def transfer_from_shimenagrichannel_to_ncsist():
    """
    Real Name: Transfer From ShiMenAgriChannel To NCSIST
    Original Eqn: Transfer From ShiMenReservoir To ShiMenAgriChannel*Ratio NCSIST At ShiMenAgriChannel\ *(1-Channel Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenreservoir_to_shimenagrichannel(
    ) * ratio_ncsist_at_shimenagrichannel() * (1 - channel_transfer_loss_rate())


@cache('step')
def transfer_from_shimenagrichannel_to_shimenagriwaterdemand():
    """
    Real Name: Transfer From ShiMenAgriChannel To ShiMenAgriWaterDemand
    Original Eqn: Transfer From ShiMenReservoir To ShiMenAgriChannel*Ratio AgriWater ShiMenReservoir To ShiMenAgriChannel\ *(1-Channel Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenreservoir_to_shimenagrichannel(
    ) * ratio_agriwater_shimenreservoir_to_shimenagrichannel() * (1 - channel_transfer_loss_rate())


@cache('step')
def transfer_from_shimenreservoir_to_houchiweir():
    """
    Real Name: Transfer From ShiMenReservoir To HouChiWeir
    Original Eqn: Final Allocation ShiMenReservoir To HouChiWeir
    Units: m3
    Limits: (None, None)
    Type: component

    assume no transfer loss        includes DaHan River Ecological Base Stream Flow
    """
    return final_allocation_shimenreservoir_to_houchiweir()


@cache('step')
def transfer_from_shimenreservoir_to_shimenagrichannel():
    """
    Real Name: Transfer From ShiMenReservoir To ShiMenAgriChannel
    Original Eqn: Final Allocation ShiMenReservoir To ShiMenAgriChannel
    Units: m3
    Limits: (None, None)
    Type: component

    assume no transfer loss;        should include the results of operation rule, each allocation under each 
        situation
    """
    return final_allocation_shimenreservoir_to_shimenagrichannel()


@cache('step')
def transfer_from_taoyuanagrichannel_to_dananwpp():
    """
    Real Name: Transfer From TaoYuanAgriChannel To DaNanWPP
    Original Eqn: Transfer From ShiMenReservoir To HouChiWeir*Ratio WPP ShiMenReservoir To HouChiWeir*\ Ratio DaNanWPP2 At HouChiWeir*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenreservoir_to_houchiweir() * ratio_wpp_shimenreservoir_to_houchiweir(
    ) * ratio_dananwpp2_at_houchiweir() * (1 - wpp_transfer_loss_rate())


@cache('step')
def transfer_from_taoyuanagrichannel_to_ncsist():
    """
    Real Name: Transfer From TaoYuanAgriChannel To NCSIST
    Original Eqn: Transfer From ShiMenReservoir To HouChiWeir*Ratio NCSIST At HouChiWeir*(1-Channel Transfer Loss Rate\ )
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenreservoir_to_houchiweir() * ratio_ncsist_at_houchiweir() * (
        1 - channel_transfer_loss_rate())


@cache('step')
def transfer_from_taoyuanagrichannel_to_taoyuanagriwaterdemand():
    """
    Real Name: Transfer From TaoYuanAgriChannel To TaoYuanAgriWaterDemand
    Original Eqn: (Transfer From ShiMenReservoir To HouChiWeir*Ratio AgriWater ShiMenReservoir To HouChiWeir In TaoYuanAgriChannel\ )*(1-Channel Transfer Loss Rate )
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return (transfer_from_shimenreservoir_to_houchiweir() *
            ratio_agriwater_shimenreservoir_to_houchiweir_in_taoyuanagrichannel()) * (
                1 - channel_transfer_loss_rate())


@cache('step')
def transfer_from_taoyuanagrichannel_to_taoyuancpcrefinery():
    """
    Real Name: Transfer From TaoYuanAgriChannel To TaoYuanCPCRefinery
    Original Eqn: Transfer From ShiMenReservoir To HouChiWeir*Ratio TaoYuan CPC Refinery At HouChiWeir\ *(1-Channel Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenreservoir_to_houchiweir(
    ) * ratio_taoyuan_cpc_refinery_at_houchiweir() * (1 - channel_transfer_loss_rate())


@cache('step')
def transfer_from_yuanshanweir_to_banxinwpp():
    """
    Real Name: Transfer From YuanShanWeir To BanXinWPP
    Original Eqn: MIN( 600000 , Transfer From ZhongZhuangWeir To YuanShanWeir-EcoBaseFlow-Tranfer From YuanShanWeir To DaNanWPP\ /(1-WPP Transfer Loss Rate))*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component

    assume use the limit of Power transmission culvert, which is 600000 m^3 
        per day as the constraint.
    """
    return np.minimum(
        600000,
        transfer_from_zhongzhuangweir_to_yuanshanweir() - ecobaseflow() -
        tranfer_from_yuanshanweir_to_dananwpp() /
        (1 - wpp_transfer_loss_rate())) * (1 - wpp_transfer_loss_rate())


@cache('step')
def transfer_from_zhongzhuangadjustmentreservoir_to_banxinwpp():
    """
    Real Name: Transfer From ZhongZhuangAdjustmentReservoir To BanXinWPP
    Original Eqn: ZhongZhuang Support To BanXinWPP*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return zhongzhuang_support_to_banxinwpp() * (1 - wpp_transfer_loss_rate())


@cache('step')
def transfer_from_zhongzhuangadjustmentreservoir_to_dananwpp():
    """
    Real Name: Transfer From ZhongZhuangAdjustmentReservoir To DaNanWPP
    Original Eqn: ZhongZhuang Support To DaNanWPP*(1-WPP Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return zhongzhuang_support_to_dananwpp() * (1 - wpp_transfer_loss_rate())


@cache('step')
def transfer_from_zhongzhuangweir_to_taoyuandahanriver_agriwater_demand():
    """
    Real Name: Transfer From ZhongZhuangWeir To TaoYuanDaHanRiver AgriWater Demand
    Original Eqn: Transfer From ShiMenReservoir To HouChiWeir*Ratio AgriWater ShiMenReservoir To HouChiWeir In DaHanRiver\ *(1-Channel Transfer Loss Rate)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return transfer_from_shimenreservoir_to_houchiweir(
    ) * ratio_agriwater_shimenreservoir_to_houchiweir_in_dahanriver() * (
        1 - channel_transfer_loss_rate())


@cache('step')
def transfer_from_zhongzhuangweir_to_yuanshanweir():
    """
    Real Name: Transfer From ZhongZhuangWeir To YuanShanWeir
    Original Eqn: Transfer From HouChiWeir To ZhongZhuangWeir+YuanShan Lateral Flow-(Transfer From ZhongZhuangWeir To TaoYuanDaHanRiver AgriWater Demand\ +Transfer From ZhongZhuangWeir To ZhongZhuangAdjustmentReservoir)/(1-Channel Transfer Loss Rate\ )
    Units: m3
    Limits: (None, None)
    Type: component

    Assume that the transfer loss between HouChiWeir and YuanShanWeir is 
        considered and included in "YuanShan Lateral Flow".
    """
    return transfer_from_houchiweir_to_zhongzhuangweir() + yuanshan_lateral_flow() - (
        transfer_from_zhongzhuangweir_to_taoyuandahanriver_agriwater_demand() +
        transfer_from_zhongzhuangweir_to_zhongzhuangadjustmentreservoir()) / (
            1 - channel_transfer_loss_rate())


@cache('step')
def transfer_from_zhongzhuangweir_to_zhongzhuangadjustmentreservoir():
    """
    Real Name: Transfer From ZhongZhuangWeir To ZhongZhuangAdjustmentReservoir
    Original Eqn: (Transfer From HouChiWeir To ZhongZhuangWeir+YuanShan Lateral Flow-Transfer From ZhongZhuangWeir To TaoYuanDaHanRiver AgriWater Demand\ /(1-Channel Transfer Loss Rate))*Ratio ZhongZhuangAdjustmentReservoir take*(1-Channel Transfer Loss Rate\ )
    Units: m3
    Limits: (None, None)
    Type: component

    do not consider it in the Market Version, so "Ratio 
        ZhongZhuangAdjustmentReservoir take" is zero here.
    """
    return (transfer_from_houchiweir_to_zhongzhuangweir() + yuanshan_lateral_flow() -
            transfer_from_zhongzhuangweir_to_taoyuandahanriver_agriwater_demand() /
            (1 - channel_transfer_loss_rate())) * ratio_zhongzhuangadjustmentreservoir_take() * (
                1 - channel_transfer_loss_rate())


@cache('run')
def water_right_banxin_wpp():
    """
    Real Name: Water Right BanXin WPP
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    source from YuanShan Weir;        input data.
    """
    return 123


@cache('run')
def water_right_danan_wpp1():
    """
    Real Name: Water Right DaNan WPP1
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    source from TaoYuan AgriChannel;        input data.
    """
    return 123


@cache('run')
def water_right_danan_wpp2():
    """
    Real Name: Water Right DaNan WPP2
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    source from TaoYuan AgriChannel;        input data.
    """
    return 123


@cache('run')
def water_right_pingzhen_wpp1():
    """
    Real Name: Water Right PingZhen WPP1
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    because in different Ten-days, the allocated water right is different, use this 
        variable to identify.        input data.
    """
    return 123


@cache('run')
def water_right_pingzhen_wpp2():
    """
    Real Name: Water Right PingZhen WPP2
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    source from YuanShan Weir;        input data.
    """
    return 123


@cache('run')
def water_right_shimen_agrichannel_agriwater():
    """
    Real Name: Water Right ShiMen AgriChannel AgriWater
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    input data.
    """
    return 123


@cache('run')
def water_right_shimenlongtan_wpp():
    """
    Real Name: Water Right ShiMenLongTan WPP
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    because in different Ten-days, the allocated water right is different, use this 
        variable to identify.        input data.
    """
    return 123


@cache('run')
def water_right_taoyuan_agrichannel_agriwater():
    """
    Real Name: Water Right TaoYuan AgriChannel AgriWater
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    input data.
    """
    return 123


@cache('run')
def water_right_taoyuan_cpc_refinery():
    """
    Real Name: Water Right TaoYuan CPC Refinery
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    source from TaoYuan AgriChannel;        input data.
    """
    return 123


@cache('run')
def water_right_taoyuandahanriver_agriwater():
    """
    Real Name: Water Right TaoYuanDaHanRiver AgriWater
    Original Eqn: 123
    Units: m3
    Limits: (None, None)
    Type: constant

    input data.
    """
    return 123


@cache('run')
def wpp_transfer_loss_rate():
    """
    Real Name: WPP Transfer Loss Rate
    Original Eqn: 0
    Units: m3/m3
    Limits: (None, None)
    Type: constant

    Assume 0% WPP transfer loss rate.
    """
    return 0


@cache('run')
def yuanshan_lateral_flow():
    """
    Real Name: YuanShan Lateral Flow
    Original Eqn: 300000
    Units: m3
    Limits: (None, None)
    Type: constant

    No further data, so assume that All the YuanShan Lateral Flow comes into the point 
        of ZhongZhuang Weir;        The transfer loss between HouChiWeir and YuanShanWeir is considered and included in 
        this variable.        use 300000 to test
    """
    return 300000


@cache('step')
def yuanshan_weir():
    """
    Real Name: YuanShan Weir
    Original Eqn: Transfer From ZhongZhuangWeir To YuanShanWeir-EcoBaseFlow-Tranfer From YuanShanWeir To DaNanWPP\ -Transfer From YuanShanWeir To BanXinWPP-YuanShanWeir Transfer Loss Amount-YuanShan Weir Outflow
    Units: m3
    Limits: (None, None)
    Type: component

    max effective storage volume = 4900000 m^3.
    """
    return transfer_from_zhongzhuangweir_to_yuanshanweir() - ecobaseflow(
    ) - tranfer_from_yuanshanweir_to_dananwpp() - transfer_from_yuanshanweir_to_banxinwpp(
    ) - yuanshanweir_transfer_loss_amount() - yuanshan_weir_outflow()


@cache('run')
def yuanshan_weir_ecological_base_stream_flow():
    """
    Real Name: YuanShan Weir Ecological Base Stream Flow
    Original Eqn: 198720
    Units: m3
    Limits: (None, None)
    Type: constant

    2.3cms, equals 198720 m^3 per day
    """
    return 198720


@cache('step')
def yuanshan_weir_outflow():
    """
    Real Name: YuanShan Weir Outflow
    Original Eqn: Transfer From ZhongZhuangWeir To YuanShanWeir-EcoBaseFlow-Tranfer From YuanShanWeir To DaNanWPP\ -Transfer From YuanShanWeir To BanXinWPP-YuanShanWeir Transfer Loss Amount
    Units: m3
    Limits: (None, None)
    Type: component

    May be zero because some included in "EcoBaseFlow".
    """
    return transfer_from_zhongzhuangweir_to_yuanshanweir() - ecobaseflow(
    ) - tranfer_from_yuanshanweir_to_dananwpp() - transfer_from_yuanshanweir_to_banxinwpp(
    ) - yuanshanweir_transfer_loss_amount()


@cache('step')
def yuanshanweir_transfer_loss_amount():
    """
    Real Name: YuanShanWeir Transfer Loss Amount
    Original Eqn: (Tranfer From YuanShanWeir To DaNanWPP+Transfer From YuanShanWeir To BanXinWPP)/(1-WPP Transfer Loss Rate\ )*WPP Transfer Loss Rate
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return (tranfer_from_yuanshanweir_to_dananwpp() + transfer_from_yuanshanweir_to_banxinwpp()
            ) / (1 - wpp_transfer_loss_rate()) * wpp_transfer_loss_rate()


@cache('step')
def zhongzhuang_adjustment_reservoir():
    """
    Real Name: ZhongZhuang Adjustment Reservoir
    Original Eqn: INTEG ( IF THEN ELSE(Transfer From ZhongZhuangWeir To ZhongZhuangAdjustmentReservoir+ZhongZhuang Adjustment Reservoir\ -Transfer From ZhongZhuangAdjustmentReservoir To BanXinWPP-Transfer From ZhongZhuangAdjustmentReservoir To DaNanWPP\ -ZhongZhuangAdjustmentReservoir Transfer Loss Amount>=5.05e+006, 0 , Transfer From ZhongZhuangWeir To ZhongZhuangAdjustmentReservoir\ -Transfer From ZhongZhuangAdjustmentReservoir To BanXinWPP-Transfer From ZhongZhuangAdjustmentReservoir To DaNanWPP\ -ZhongZhuangAdjustmentReservoir Transfer Loss Amount ), 5.05e+006)
    Units: m3
    Limits: (None, None)
    Type: component

    Max Storage Valume = 5050000 m^3 (2017);        general output = 24000 m^3 per day(BanXin WPP assumes 15000 m^3; DaNan WPP assumes 
        9000 m^3 ;        overflow height 68m, designed flood discharge 2.83CMS, water input limit 
        10cms.
    """
    return integ_zhongzhuang_adjustment_reservoir()


@cache('run')
def zhongzhuang_support_to_banxinwpp():
    """
    Real Name: ZhongZhuang Support To BanXinWPP
    Original Eqn: 0
    Units: m3
    Limits: (None, None)
    Type: constant

    do not consider it in the Market Version
    """
    return 0


@cache('run')
def zhongzhuang_support_to_dananwpp():
    """
    Real Name: ZhongZhuang Support To DaNanWPP
    Original Eqn: 0
    Units: m3
    Limits: (None, None)
    Type: constant

    do not consider it in the Market Version
    """
    return 0


@cache('step')
def zhongzhuang_weir():
    """
    Real Name: ZhongZhuang Weir
    Original Eqn: Transfer From HouChiWeir To ZhongZhuangWeir+YuanShan Lateral Flow-(Transfer From ZhongZhuangWeir To TaoYuanDaHanRiver AgriWater Demand\ +Transfer From ZhongZhuangWeir To ZhongZhuangAdjustmentReservoir)/(1-Channel Transfer Loss Rate\ )-Transfer From ZhongZhuangWeir To YuanShanWeir
    Units: m3
    Limits: (None, None)
    Type: component

    Should be zero(all in and out)
    """
    return transfer_from_houchiweir_to_zhongzhuangweir() + yuanshan_lateral_flow() - (
        transfer_from_zhongzhuangweir_to_taoyuandahanriver_agriwater_demand() +
        transfer_from_zhongzhuangweir_to_zhongzhuangadjustmentreservoir()) / (
            1 - channel_transfer_loss_rate()) - transfer_from_zhongzhuangweir_to_yuanshanweir()


@cache('step')
def zhongzhuangadjustmentreservoir_transfer_loss_amount():
    """
    Real Name: ZhongZhuangAdjustmentReservoir Transfer Loss Amount
    Original Eqn: (ZhongZhuang Support To BanXinWPP+ZhongZhuang Support To DaNanWPP)*WPP Transfer Loss Rate
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return (zhongzhuang_support_to_banxinwpp() +
            zhongzhuang_support_to_dananwpp()) * wpp_transfer_loss_rate()


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 364
    Units: Day
    Limits: (None, None)
    Type: constant

    The final time for the simulation.
    """
    return 364


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 0
    Units: Day
    Limits: (None, None)
    Type: constant

    The initial time for the simulation.
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Day
    Limits: (0.0, None)
    Type: component

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 1
    Units: Day
    Limits: (0.0, None)
    Type: constant

    The time step for the simulation.
    """
    return 1


integ_shimen_reservoir = functions.Integ(lambda: shimen_reservoir_inflow()-shimen_reservoir_evaporation()-shimen_reservoir_overflow()-support_ecobaseflow()-transfer_from_shimenreservoir_to_houchiweir()-transfer_from_shimenreservoir_to_shimenagrichannel(), lambda: 1.06071e+008)


integ_shimen_wpp_storage_pool = functions.Integ(lambda: functions.if_then_else(shimen_wpp()+shimen_wpp_storage_pool()-shimen_wpp_adjusted()>=500000,0,shimen_wpp()-shimen_wpp_adjusted()), lambda: 500000)


integ_zhongzhuang_adjustment_reservoir = functions.Integ(lambda: functions.if_then_else(transfer_from_zhongzhuangweir_to_zhongzhuangadjustmentreservoir()+zhongzhuang_adjustment_reservoir()-transfer_from_zhongzhuangadjustmentreservoir_to_banxinwpp()-transfer_from_zhongzhuangadjustmentreservoir_to_dananwpp()-zhongzhuangadjustmentreservoir_transfer_loss_amount()>=5.05e+006,0,transfer_from_zhongzhuangweir_to_zhongzhuangadjustmentreservoir()-transfer_from_zhongzhuangadjustmentreservoir_to_banxinwpp()-transfer_from_zhongzhuangadjustmentreservoir_to_dananwpp()-zhongzhuangadjustmentreservoir_transfer_loss_amount()), lambda: 5.05e+006)

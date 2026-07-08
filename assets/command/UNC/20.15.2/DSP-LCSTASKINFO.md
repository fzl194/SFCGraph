---
id: UNC@20.15.2@MMLCommand@DSP LCSTASKINFO
type: MMLCommand
name: DSP LCSTASKINFO（查询定位任务信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LCSTASKINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCS操作维护
status: active
---

# DSP LCSTASKINFO（查询定位任务信息）

## 功能

MME
该命令用于查询MME上缓存的指定用户的定位任务相关信息。

## 注意事项

定位分立即定位和延迟定位两种。立即定位场景下MME向GMLC即时返回定位结果，MME上的定位任务信息会随之删除。所以，本命令主要应用于延迟定位场景。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询定位任务信息的方式。<br>- “BYIMSI(指定IMSI)”：表示根据IMSI查询。<br>- “BYMSISDN(指定MSISDN)”：表示根据MSISDN查询。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定国际移动用户标识。<br>数据来源：本端规划<br>取值范围：1~15位十进制数字字符串<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动台国际ISDN号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~15。无<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LCSTASKINFO]] · 定位任务信息（LCSTASKINFO）

## 使用实例

1. 根据IMSI查询LCS任务信息:
  DSP LCSTASKINFO: QUERYOPT=BYIMSI, IMSI="123033401000001";
  ```
  %%DSP LCSTASKINFO: QUERYOPT=BYIMSI, IMSI="
  123033401000001
  ";%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------------------
              定位类型 = 激活延迟定位
         LCS客户端名称 = client
         LCS客户端类型 = 运营商应用
           定位QoS级别 = 尽力而为型
          水平定位精度 = 11
          垂直定位精度 = 11
          定位响应级别 = 可容忍时延
        支持的区域形状 = 0
          定位业务类型 = 0
              定位码字 = NULL
      待定位的业务类型 = NULL
    会话类隐私检查策略 = 无效
  非会话类隐私检查策略 = 允许，不用通知UE
          延迟定位类型 = 0
        定位任务参考号 = 0
             PLR标志位 = 4
     接收LCS任务时间戳 = 2018-06-15 03:44:15+08:00
  (结果个数 = 1)
  ---    END
  ```
2. 根据MSISDN查询订阅任务信息:
  DSP LCSTASKINFO: QUERYOPT=BYMSISDN, MSISDN="8613534000001";
  ```
  %%DSP LCSTASKINFO: QUERYOPT=BYMSISDN, MSISDN="8613534000001";%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------------------
              定位类型 = 激活延迟定位
         LCS客户端名称 = client
         LCS客户端类型 = 运营商应用
           定位QoS级别 = 尽力而为型
          水平定位精度 = 11
          垂直定位精度 = 11
          定位响应级别 = 可容忍时延
        支持的区域形状 = 0
          定位业务类型 = 0
              定位码字 = NULL
      待定位的业务类型 = NULL
    会话类隐私检查策略 = 无效
  非会话类隐私检查策略 = 允许，不用通知UE
          延迟定位类型 = 0
        定位任务参考号 = 0
             PLR标志位 = 4
     接收LCS任务时间戳 = 2018-06-15 03:44:15+08:00
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LCSTASKINFO.md`

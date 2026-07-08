---
id: UNC@20.15.2@MMLCommand@DSP AMFMBSSESCTX
type: MMLCommand
name: DSP AMFMBSSESCTX（显示AMF组播广播会话上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AMFMBSSESCTX
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- AMF组播广播管理
- 显示AMF组播广播会话上下文
status: active
---

# DSP AMFMBSSESCTX（显示AMF组播广播会话上下文）

## 功能

**适用NF：AMF**

该命令用于查询AMF组播广播会话上下文的相关信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSIONTYPE | 会话类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的会话类型。<br>数据来源：本端规划<br>取值范围：<br>- BROADCAST（广播）<br>默认值：无<br>配置原则：无 |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定AMF广播上下文的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_TMGI（全量查询）”：查询全量的TMGI。<br>- “SPEC_TMGI（指定TMGI）”：查询指定TMGI的广播上下文信息。<br>- “SPEC_TMGI_GNB（指定TMGI和GNB）”：查询指定TMGI的广播上下文中指定GNB的广播上下文建立状态。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家代码 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPEC_TMGI"、"SPEC_TMGI_GNB"时为条件必选参数。<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPEC_TMGI"、"SPEC_TMGI_GNB"时为条件必选参数。<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| MBSSERVICEID | 组播广播服务标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPEC_TMGI"、"SPEC_TMGI_GNB"时为条件必选参数。<br>参数含义：该参数用于指定组播广播服务标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |
| GNBPLMN | gNodeB PLMN | 可选必选说明：该参数在"QUERYTYPE"配置为"SPEC_TMGI_GNB"时为条件必选参数。<br>参数含义：该参数用于指定NG-RAN的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。<br>默认值：无<br>配置原则：无 |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPEC_TMGI_GNB"时为条件必选参数。<br>参数含义：该参数表示gNodeB类型，包含Global gNB或者Global N3IWF，以及Macro ng-eNB、Short Macro ng-eNB、Long Macro ng-eNB等五种细分类型。<br>数据来源：全网规划<br>取值范围：<br>- “GNB（Global gNB）”：Global gNB<br>- “MACRONGENB（Macro ng-eNB）”：Macro ng-eNB<br>- “SHORTNGENB（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LONGNGENB（Long Macro ng-eNB）”：Long Macro ng-eNB<br>- “N3IWF（Global N3IWF）”：Global N3IWF<br>默认值：无<br>配置原则：无 |
| GNBID | 基站标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPEC_TMGI_GNB"时为条件必选参数。<br>参数含义：该参数用于指定基站标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| GNBLEN | gNB标识长度(比特) | 可选必选说明：该参数在"NGRANNODETYPE"配置为"GNB"时为条件必选参数。<br>参数含义：该参数表示gNB标识的长度（比特）。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [AMF组播广播会话上下文（AMFMBSSESCTX）](configobject/UNC/20.15.2/AMFMBSSESCTX.md)

## 使用实例

- 查询系统中所有广播会话的TMGI，执行如下命令：
  ```
  %%DSP AMFMBSSESCTX:SESSIONTYPE=BROADCAST, QUERYTYPE=ALL_TMGI;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  TMGI           POD ID     

  123-45-123456  gtp-pod-0  
  123-45-123567  gtp-pod-0  
  (结果个数 = 2)

  ---    END
  ```
- 查询MCC为123、MNC为03、TMGI为123456的广播上下文，执行如下命令：
  ```
  %%DSP AMFMBSSESCTX:SESSIONTYPE=BROADCAST, QUERYTYPE=SPEC_TMGI, MCC="123", MNC="45", MBSSERVICEID="123456";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
              切片  =  1-FFFFFF
          广播区域  =  12345000001
  广播会话建立时间  =  2022-12-01T18:24:51+08:00
  广播会话超期时间  =  2022-12-01T20:24:51+08:00
        总基站个数  =  100
      成功基站个数  =  100
      失败基站列表  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示AMF组播广播会话上下文（DSP-AMFMBSSESCTX）_88267226.md`

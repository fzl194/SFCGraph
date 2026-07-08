---
id: UNC@20.15.2@MMLCommand@CLR NGRANNEIBS
type: MMLCommand
name: CLR NGRANNEIBS（清除NG-RAN基站邻接关系）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NGRANNEIBS
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- gNodeB邻接关系管理
status: active
---

# CLR NGRANNEIBS（清除NG-RAN基站邻接关系）

## 功能

![](清除NG-RAN基站邻接关系（CLR NGRANNEIBS）_09653167.assets/notice_3.0-zh-cn_2.png)

执行该命令会导致已学习的邻接关系失效，重新学习完成前可能会增加寻呼量导致系统过载。

**适用NF：AMF**

本命令用于清除系统自学习的NG-RAN基站邻接关系。NG-RAN基站主要分为gNB和ng-eNB两种，其中ng-eNB又细分为Macro ng-eNB、Long Macro ng-eNB和Short Macro ng-eNB三种。

## 注意事项

- 该命令执行后立即生效。

- 删除邻接NG-RAN基站会导致无法以邻接NG-RAN基站为范围进行寻呼。
- AMF自主学习NG-RAN基站邻接关系的时间较长，清除系统内已学习到的所有NG-RAN基站邻接关系，AMF将会花一周以上时间才能恢复。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定清除所有还是特定NG-RAN基站的邻接列表。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（清除所有基站邻接关系）”：清除所有基站邻接关系<br>- “SINGLE_NODE（清除特定基站的邻接关系）”：清除特定基站的邻接关系<br>默认值：无<br>配置原则：无 |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：该参数在"OPTYPE"配置为"SINGLE_NODE"时为条件必选参数。<br>参数含义：该参数用于指定NG接入网中的基站类型。<br>数据来源：全网规划<br>取值范围：<br>- “GNB（Global gNB）”：Global gNB<br>- “MACRONGENB（Macro ng-eNB）”：Macro ng-eNB<br>- “SHORTNGENB（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LONGNGENB（Long Macro ng-eNB）”：Long Macro ng-eNB<br>- “N3IWF（Global N3IWF）”：Global N3IWF<br>默认值：无<br>配置原则：无 |
| PLMN | PLMN | 可选必选说明：该参数在"OPTYPE"配置为"SINGLE_NODE"时为条件必选参数。<br>参数含义：该参数用于指定NG接入网中基站的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NGRANNODEID | NG-RAN基站标识 | 可选必选说明：该参数在"OPTYPE"配置为"SINGLE_NODE"时为条件必选参数。<br>参数含义：该参数用于指定NG接入网中基站的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| LUT | 最后更新时间(h) | 可选必选说明：必选参数<br>参数含义：该参数用于指定清除邻接基站的时间阈值：在本参数时间内未更新的邻接基站才被清除。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~720，单位是小时。当取值是0时，不检查基站邻接关系的更新时间，清除所有邻接关系。推荐值为0。<br>默认值：无<br>配置原则：无 |
| GNBLEN | gNB标识长度(比特) | 可选必选说明：该参数在"NGRANNODETYPE"配置为"GNB"时为条件必选参数。<br>参数含义：该参数表示gNB标识的长度，单位：比特。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGRANNEIBS]] · NG-RAN基站邻接关系（NGRANNEIBS）

## 使用实例

删除所有1小时内未更新的NG-RAN基站邻接关系：

```
CLR NGRANNEIBS: OPTYPE=ALL, LUT=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-NGRANNEIBS.md`

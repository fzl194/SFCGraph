---
id: UNC@20.15.2@MMLCommand@DSP NGRANNEIBS
type: MMLCommand
name: DSP NGRANNEIBS（显示NG-RAN基站邻接关系）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGRANNEIBS
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- gNodeB邻接关系管理
status: active
---

# DSP NGRANNEIBS（显示NG-RAN基站邻接关系）

## 功能

**适用NF：AMF**

查询指定NG-RAN基站的邻接基站列表，对系统无影响。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心NG-RAN基站的类型。<br>数据来源：全网规划<br>取值范围：<br>- “GNB（Global gNB）”：Global gNB<br>- “MACRONGENB（Macro ng-eNB）”：Macro ng-eNB<br>- “SHORTNGENB（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LONGNGENB（Long Macro ng-eNB）”：Long Macro ng-eNB<br>- “N3IWF（Global N3IWF）”：Global N3IWF<br>默认值：无<br>配置原则：无 |
| PLMN | PLMN | 可选必选说明：必选参数<br>参数含义：该参数标识NG接入网基站的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NGRANNODEID | NG-RAN基站标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心NG-RAN基站的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| GNBLEN | gNB标识长度(比特) | 可选必选说明：该参数在"NGRANNODETYPE"配置为"GNB"时为条件必选参数。<br>参数含义：该参数表示gNodeB标识的长度（比特）。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是16~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGRANNEIBS]] · NG-RAN基站邻接关系（NGRANNEIBS）

## 使用实例

查询PLMN为12303，标识为16777216的24个bit位长度的中心gNodeB的邻接基站列表，执行如下命令：

```
%%DSP NGRANNEIBS:NGRANNODETYPE=GNB, PLMN="12303", NGRANNODEID=16777216, GNBLEN=24;%%
RETCODE = 0  操作成功

结果如下
--------
   NG-RAN基站类型  =  Global gNB
             PLMN  =  12303
   NG-RAN基站标识  =  16777216
gNB标识长度(比特)  =  24
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGRANNEIBS.md`

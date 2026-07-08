---
id: UNC@20.15.2@MMLCommand@LST ISMFDFTQOSCTRL
type: MMLCommand
name: LST ISMFDFTQOSCTRL（查询I-SMF的Default QoS Flow配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ISMFDFTQOSCTRL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- ISMF QoS管理
- ISMF QoS协商
status: active
---

# LST ISMFDFTQOSCTRL（查询I-SMF的Default QoS Flow配置）

## 功能

**适用NF：SMF**

该命令用来查询I-SMF的Default QoS Flow配置。

## 注意事项

AMBRUL、AMBRDL、MFBRUL、MFBRDL、GFBRUL、GFBRDL结果如果为0，说明未对该参数进行配置，不进行限速或控制。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成QoS控制的用户归属地网络的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成QoS控制的用户归属地网络的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| CTRLTYPE | 控制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成QoS控制的缺省QoS类型。<br>数据来源：全网规划<br>取值范围：<br>- DNN_LEVEL（DNN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件可选参数。<br>参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [I-SMF的Default QoS Flow配置（ISMFDFTQOSCTRL）](configobject/UNC/20.15.2/ISMFDFTQOSCTRL.md)

## 使用实例

查询I-SMF上所有PLMN的Default QoS Flow配置，执行如下命令:

```
%%LST ISMFDFTQOSCTRL:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
Mobile Country Code  Mobile Network Code  Control Type  DNN   Uplink Session AMBR (kbp/s)  Downlink Session AMBR (kbp/s)  Maximum Uplink Rate (kbit/s)  Maximum Downlink Rate (kbit/s)  Uplink Guaranteed Rate (kbit/s)  Downlink Guaranteed Rate (kbit/s)  Bandwidth Action  Allowed 5QI List Index  Bind Allowed 5QI List  Allowed ARP List Index  Bind Allowed ARP List  

460                  01                   GLOBAL_LEVEL  null  10000000                     10000000                       0                             0                               0                                0                                  reject            65535                   DISABLE                2                       ENABLE                 
460                  02                   GLOBAL_LEVEL  null  10000000                     10000000                       0                             0                               0                                0                                  reject            65535                   DISABLE                65535                   DISABLE                
470                  00                   GLOBAL_LEVEL  null  10000000                     10000000                       0                             0                               0                                0                                  reject            1                       ENABLE                 65535                   DISABLE                
(Number of results = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询I-SMF的Default-QoS-Flow配置（LST-ISMFDFTQOSCTRL）_59000289.md`

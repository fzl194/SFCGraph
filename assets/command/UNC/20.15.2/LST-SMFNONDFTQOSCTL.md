---
id: UNC@20.15.2@MMLCommand@LST SMFNONDFTQOSCTL
type: MMLCommand
name: LST SMFNONDFTQOSCTL（查询SMF的非Default QoS Flow配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFNONDFTQOSCTL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC非缺省Flow QoS
status: active
---

# LST SMFNONDFTQOSCTL（查询SMF的非Default QoS Flow配置）

## 功能

**适用NF：SMF**

该命令用来查询SMF的非Default QoS Flow配置。

## 注意事项

MFBRUL、MFBRDL、GFBRUL、GFBRDL结果如果为0，说明未对该参数进行配置，不进行限速或控制。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成QoS控制的用户归属地网络的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成QoS控制的用户归属地网络的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| CTRLTYPE | 控制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成QoS控制的缺省QoS类型。<br>数据来源：全网规划<br>取值范围：<br>- DNN_LEVEL（DNN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFNONDFTQOSCTL]] · SMF的非Default QoS Flow配置（SMFNONDFTQOSCTL）

## 使用实例

查询I-SMF/V-SMF上所有PLMN的Non Default QoS Flow配置，执行如下命令:

```
%%LST SMFNONDFTQOSCTL:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
Mobile Country Code  Mobile Network Code  Control Type  DNN   Maximum Uplink Rate (kbit/s)  Maximum Downlink Rate (kbit/s)  Uplink Guaranteed Rate (kbit/s)  Downlink Guaranteed Rate (kbit/s)  Bandwidth Action  Allowed 5QI List Index  Bind Allowed 5QI List  Allowed ARP List  Bind Allowed ARP List  

460                  00                   GLOBAL_LEVEL  null  0                             0                               0                                0                                  reject            65535                   DISABLE                65535             DISABLE                
460                  01                   GLOBAL_LEVEL  null  1                             0                               0                                0                                  reject            1                       ENABLE                 65535             DISABLE                
460                  09                   GLOBAL_LEVEL  null  0                             0                               0                                0                                  reject            1                       ENABLE                 65535             DISABLE                
470                  00                   DNN_LEVEL     aaa   0                             3                               0                                0                                  reject            65535                   DISABLE                3                 ENABLE                 
501                  00                   GLOBAL_LEVEL  null  0                             0                               0                                0                                  reject            65535                   DISABLE                1                 DISABLE                
(Number of results = 5)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMF的非Default-QoS-Flow配置（LST-SMFNONDFTQOSCTL）_58680355.md`

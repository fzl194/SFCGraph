---
id: UNC@20.15.2@MMLCommand@LST VSMFDFTQOSCTRL
type: MMLCommand
name: LST VSMFDFTQOSCTRL（查询VSMF的Default QoS Flow配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VSMFDFTQOSCTRL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- VSMF QoS管理
- VPLMN QoS协商
status: active
---

# LST VSMFDFTQOSCTRL（查询VSMF的Default QoS Flow配置）

## 功能

**适用NF：SMF**

该命令用来查询V-SMF的Default QoS Flow配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成QoS控制的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成QoS控制的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| CTRLTYPE | 控制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- DNN_LEVEL（DNN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件可选参数。<br>参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VSMFDFTQOSCTRL]] · VSMF的Default QoS Flow配置（VSMFDFTQOSCTRL）

## 使用实例

查询VSMF上所有PLMN的Default QoS Flow配置：

```
%%LST VSMFDFTQOSCTRL:;%%
            RETCODE = 0 操作成功

            操作结果如下
            ------------
            移动国家码 = 460
            #移动网络码 = 00
            控制类型 = GLOBAL_LEVEL
            DNN = null
            缺省QoS类型 = Non-GBR
            上行Session AMBR(千比特/秒) = 1000
            下行Session AMBR(千比特/秒) = 1000
            标准化5QI = 5
            ARP的优先级别 = 1
            ARP的抢占能力 = 不抢占
            ARP的被抢占能力 = 可抢占
            上行最大速率 (千比特/秒) = 0
            下行最大速率 (千比特/秒) = 0
            上行保证速率 (千比特/秒) = 0
            下行保证速率 (千比特/秒) = 0
            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VSMFDFTQOSCTRL.md`

---
id: UNC@20.15.2@MMLCommand@ADD USRLOCATIONGRP
type: MMLCommand
name: ADD USRLOCATIONGRP（增加用户位置组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: USRLOCATIONGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- 用户位置组
status: active
---

# ADD USRLOCATIONGRP（增加用户位置组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加位置组。位置组是一种初始接入位置的位置组定义。当需要将多个位置信息组合起来对外呈现时，可将其绑定到同一位置组。该位置组可以在ADD UPBINDUPG命令中用于UsrProfGroup下的UserProfile的策略选择。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置1000条UsrLocationGrp，每个UsrLocationGrp最多支持配置20个UserLocation。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGROUPNAME | 位置组名称 | 可选必选说明：必选参数<br>参数含义：指定位置组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCATIONNAME | 位置名称 | 可选必选说明：可选参数<br>参数含义：指定位置信息名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USRLOCATION命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRLOCATIONGRP]] · 用户位置组（USRLOCATIONGRP）

## 使用实例

假如运营商需要希望增加一个位置组用于后续绑定位置信息使用：

```
ADD USRLOCATIONGRP:LOCGROUPNAME="test01",LOCATIONNAME="testloc01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加用户位置组（ADD-USRLOCATIONGRP）_09897148.md`

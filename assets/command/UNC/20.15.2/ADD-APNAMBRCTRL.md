---
id: UNC@20.15.2@MMLCommand@ADD APNAMBRCTRL
type: MMLCommand
name: ADD APNAMBRCTRL（增加APN-AMBR控制的配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNAMBRCTRL
command_category: 配置类
applicable_nf:
- GGSN
- SMF
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QoS映射
- APN-AMBR控制
status: active
---

# ADD APNAMBRCTRL（增加APN-AMBR控制的配置）

## 功能

**适用NF：GGSN、SMF、PGW-C**

该命令用来增加APN-AMBR控制的配置，适用于WSFD-105007 5G QoS到4G QoS灵活映射特性。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- APN_LEVEL（APN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| APN | APN | 可选必选说明：该参数在"CTRLTYPE"配置为"APN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| AMBRUL | 上行APN-AMBR(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成QoS控制的上行APN-AMBR。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~20000000。<br>默认值：无<br>配置原则：无 |
| AMBRDL | 下行APN-AMBR(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成QoS控制的下行APN-AMBR。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~20000000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNAMBRCTRL]] · APN-AMBR控制的配置（APNAMBRCTRL）

## 使用实例

如果想新增一条APNAMBRCTRL配置，执行如下命令：

```
ADD APNAMBRCTRL:CTRLTYPE=APN_LEVEL,APN="huawei.com",AMBRUL=1000,AMBRDL=1000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APN-AMBR控制的配置（ADD-APNAMBRCTRL）_39919385.md`

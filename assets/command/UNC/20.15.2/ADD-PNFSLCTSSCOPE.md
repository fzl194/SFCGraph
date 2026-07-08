---
id: UNC@20.15.2@MMLCommand@ADD PNFSLCTSSCOPE
type: MMLCommand
name: ADD PNFSLCTSSCOPE（增加选择对端NF时使用的业务服务区）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PNFSLCTSSCOPE
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- PCC公共参数
status: active
---

# ADD PNFSLCTSSCOPE（增加选择对端NF时使用的业务服务区）

## 功能

**适用NF：SMF**

该命令用于增加选择对端NF时使用的业务服务区。

## 注意事项

- 该命令执行后立即生效。

- 当PCFSSCOPE配置无记录时（通过LST PCFSSCOPE查询），此配置才会生效。

- 最多可输入1条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNFTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（默认的对端NF类型）”：默认的对端NF类型。<br>默认值：无<br>配置原则：无 |
| SRVSCOPENAME | 服务区名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [选择对端NF时使用的业务服务区（PNFSLCTSSCOPE）](configobject/UNC/20.15.2/PNFSLCTSSCOPE.md)

## 使用实例

配置选择对端NF时使用的业务服务区为CityA。

```
ADD PNFSLCTSSCOPE: PEERNFTYPE=DEFAULT, SRVSCOPENAME="CityA";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加选择对端NF时使用的业务服务区（ADD-PNFSLCTSSCOPE）_32390457.md`

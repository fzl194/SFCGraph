---
id: UNC@20.15.2@MMLCommand@ADD CCGROUP
type: MMLCommand
name: ADD CCGROUP（增加计费特征组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CCGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- 计费特征组
status: active
---

# ADD CCGROUP（增加计费特征组）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于增加计费特征组。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCGROUPNAME | 计费特征组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于计费特征组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。由英文字母（大小写）、数字、下划线构成，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [计费特征组（CCGROUP）](configobject/UNC/20.15.2/CCGROUP.md)

## 使用实例

增加“计费特征组名称”为“c1”的计费特征组配置：

```
ADD CCGROUP: CCGROUPNAME="c1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加计费特征组（ADD-CCGROUP）_88613375.md`

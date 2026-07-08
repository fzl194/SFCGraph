---
id: UDG@20.15.2@MMLCommand@RMV MQCCLASSIFIER
type: MMLCommand
name: RMV MQCCLASSIFIER（删除流分类）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MQCCLASSIFIER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 流分类
status: active
---

# RMV MQCCLASSIFIER（删除流分类）

## 功能

该命令用于删除一个已经定义的流分类。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLASSIFIERNAME | 分类名称 | 可选必选说明：必选参数<br>参数含义：指定流分类的名称。类名不允许为系统预定义类的名称default-class。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [流分类（MQCCLASSIFIER）](configobject/UDG/20.15.2/MQCCLASSIFIER.md)

## 使用实例

删除流分类c1：

```
RMV MQCCLASSIFIER:CLASSIFIERNAME="c1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除流分类（RMV-MQCCLASSIFIER）_00841121.md`

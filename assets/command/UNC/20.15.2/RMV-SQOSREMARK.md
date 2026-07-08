---
id: UNC@20.15.2@MMLCommand@RMV SQOSREMARK
type: MMLCommand
name: RMV SQOSREMARK（删除重标记配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SQOSREMARK
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重标记
status: active
---

# RMV SQOSREMARK（删除重标记配置）

## 功能

该命令用来删流行为下所有的除重标记配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 流行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流行为名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SQOSREMARK]] · 重标记配置（SQOSREMARK）

## 使用实例

删除重标记配置：

```
RMV SQOSREMARK:BEHAVIORNAME="b1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SQOSREMARK.md`

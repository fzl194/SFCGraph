---
id: UNC@20.15.2@MMLCommand@ADD APPLYCMNTYSTRING
type: MMLCommand
name: ADD APPLYCMNTYSTRING（增加团体属性值设置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APPLYCMNTYSTRING
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用团体属性值
status: active
---

# ADD APPLYCMNTYSTRING（增加团体属性值设置）

## 功能

该命令用于添加应用团体属性值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，需要通过ADD APPLYCOMMUNITY配置了应用团体属性值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| STRINGVALUE | 团体属性字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～51。<br>默认值：无<br>配置原则：区分大小写，格式是aa<0-65535>:nn<0-65535>或取值为internet、no-export-subconfed、no-advertise、no-export，以及0-65535的整数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APPLYCMNTYSTRING]] · 团体属性值设置（APPLYCMNTYSTRING）

## 使用实例

增加设置团体属性的操作值：

```
ADD APPLYCMNTYSTRING:NODESEQUENCE=10,POLICYNAME="a",STRINGVALUE="1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APPLYCMNTYSTRING.md`

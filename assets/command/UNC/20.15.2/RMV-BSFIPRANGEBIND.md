---
id: UNC@20.15.2@MMLCommand@RMV BSFIPRANGEBIND
type: MMLCommand
name: RMV BSFIPRANGEBIND（删除BSF实例与IPRANGE之间的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BSFIPRANGEBIND
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- BSF信息管理
status: active
---

# RMV BSFIPRANGEBIND（删除BSF实例与IPRANGE之间的绑定关系）

## 功能

**适用NF：SMF**

该命令用于删除BSF（Binding Support Function）所管辖的IP地址范围。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINSTANCENAME | BSF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BSF的实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>该参数需要在ADD NFUUID中事先配置，可执行LST NFUUID进行查看。 |
| IPRANGENAME | IPRANGE名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该BSF实例所管辖的IP地址范围的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BSFIPRANGEBIND]] · BSF实例与IPRANGE之间的绑定关系（BSFIPRANGEBIND）

## 使用实例

删除NF实例标识为BSF_Instance_0的BSF的rang1的IP地址管辖：

```
RMV BSFIPRANGEBIND: BSFINSTANCENAME="BSF_Instance_0", IPRANGENAME="range1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BSFIPRANGEBIND.md`

---
id: UNC@20.15.2@MMLCommand@ADD QOSDIFFERSERV
type: MMLCommand
name: ADD QOSDIFFERSERV（增加DS域）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QOSDIFFERSERV
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- DS域配置
status: active
---

# ADD QOSDIFFERSERV（增加DS域）

## 功能

该命令用来在接口应用DS（Differ-Server）域，定义一个DS域。DS域中描述了报文优先级与服务等级和颜色之间的映射关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSNAME | DS域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DS域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSDIFFERSERV]] · DS域（QOSDIFFERSERV）

## 使用实例

创建一个新的DS域d1：

```
ADD QOSDIFFERSERV:DSNAME="d1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-QOSDIFFERSERV.md`

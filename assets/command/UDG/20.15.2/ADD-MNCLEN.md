---
id: UDG@20.15.2@MMLCommand@ADD MNCLEN
type: MMLCommand
name: ADD MNCLEN（设置MNC长度信息）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: MNCLEN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- UP信息管理
- MNC长度
status: active
---

# ADD MNCLEN（设置MNC长度信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加指定MCC号对应的MNC长度。UPF上需配置各MCC值所对应的MNC长度，用于解析移动用户的IMSI中MNC的长度，或用于解析SGSN发送的RAI（Routing Area Identity，路由区识别码）中MNC长度，以判别用户是属于本地、漫游还是拜访用户。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| MNCLEN | 对应MCC的MNC长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MCC值所对应的MNC长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为2～3。<br>默认值：2<br>配置原则：无 |

## 操作的配置对象

- [MNC长度信息（MNCLEN）](configobject/UDG/20.15.2/MNCLEN.md)

## 使用实例

增加当前UPF所属的MCC为460，MNC长度为2：

```
ADD MNCLEN:MCC="460";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置MNC长度信息（ADD-MNCLEN）_44865461.md`

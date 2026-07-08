---
id: UNC@20.15.2@MMLCommand@RMV PNFGMLCINFO
type: MMLCommand
name: RMV PNFGMLCINFO（删除对端GMLC信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFGMLCINFO
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端GMLC信息管理
status: active
---

# RMV PNFGMLCINFO（删除对端GMLC信息）

## 功能

**适用NF：AMF**

该命令用于删除本地配置的对端GMLC支持的外部客户端类型。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）建议为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度建议不超过18且不输入只包含0-9和“.”的字符串，例如：1.2.3.4、不建议输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [对端GMLC信息（PNFGMLCINFO）](configobject/UNC/20.15.2/PNFGMLCINFO.md)

## 使用实例

删除对端GMLC信息，NF实例标识为GMLC_Instance_0，

```
RMV PNFGMLCINFO: NFINSTANCEID="GMLC_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端GMLC信息（RMV-PNFGMLCINFO）_49070375.md`

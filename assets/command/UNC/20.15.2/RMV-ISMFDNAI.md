---
id: UNC@20.15.2@MMLCommand@RMV ISMFDNAI
type: MMLCommand
name: RMV ISMFDNAI（删除I-SMF支持的DNAI）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ISMFDNAI
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI管理
- I-SMF DNAI管理
status: active
---

# RMV ISMFDNAI（删除I-SMF支持的DNAI）

## 功能

**适用NF：SMF**

该命令用于删除I-SMF支持的DNAI。

## 注意事项

该命令执行后只对新接入该设备且把该设备作为I-SMF的PDU会话生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识符 | 可选必选说明：必选参数<br>参数含义：该参数用于指定I-SMF支持的DNAI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [I-SMF支持的DNAI（ISMFDNAI）](configobject/UNC/20.15.2/ISMFDNAI.md)

## 使用实例

删除DNAI为“huawei.com.dnai”的I-SMF DNAI，执行如下命令：

```
RMV ISMFDNAI: DNAI="huawei.com.dnai";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除I-SMF支持的DNAI（RMV-ISMFDNAI）_47600749.md`

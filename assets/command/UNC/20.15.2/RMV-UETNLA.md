---
id: UNC@20.15.2@MMLCommand@RMV UETNLA
type: MMLCommand
name: RMV UETNLA（删除UE-TNLA）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UETNLA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# RMV UETNLA（删除UE-TNLA）

## 功能

**适用NF：AMF**

该命令用于删除UE-TNLA。NG-RAN与AMF之间支持多偶联，UE-TNLA表示UE与传输偶联之间的关联关系。该命令仅用于测试场景。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定被删除UE-TNLA的用户IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UE-TNLA（UETNLA）](configobject/UNC/20.15.2/UETNLA.md)

## 使用实例

删除IMSI为460071104000955的用户的UE-TNLA，执行如下命令：

```
RMV UETNLA:  IMSI="460071104000955";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UE-TNLA（RMV-UETNLA）_09652095.md`

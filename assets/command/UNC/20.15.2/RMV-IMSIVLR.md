---
id: UNC@20.15.2@MMLCommand@RMV IMSIVLR
type: MMLCommand
name: RMV IMSIVLR（删除IMSI与VLR对应关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSIVLR
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- IMSI与VLR对应关系
status: active
---

# RMV IMSIVLR（删除IMSI与VLR对应关系）

## 功能

**适用网元：MME**

该命令用于删除IMSI对应的MSC/VLR。

## 注意事项

该命令执行后，用户通过SGs接口选择MSC/VLR时生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的IMSI。<br>数据来源：全网规划<br>取值范围：14~15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [IMSI与VLR对应关系（IMSIVLR）](configobject/UNC/20.15.2/IMSIVLR.md)

## 使用实例

删除指定IMSI"123030000000001"的IMSI与MSC/VLR对应关系记录：

RMV IMSIVLR: IMSI="123030000000001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMSI与VLR对应关系(RMV-IMSIVLR)_26305260.md`

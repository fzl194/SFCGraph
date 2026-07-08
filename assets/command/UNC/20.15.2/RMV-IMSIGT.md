---
id: UNC@20.15.2@MMLCommand@RMV IMSIGT
type: MMLCommand
name: RMV IMSIGT（删除IMSI-GT对应关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSIGT
command_category: 配置类
applicable_nf:
- SGSN
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- MAP应用协议
- IMSI GT转换信息
status: active
---

# RMV IMSIGT（删除IMSI-GT对应关系）

## 功能

![](删除IMSI-GT对应关系(RMV IMSIGT)_26145464.assets/notice_3.0-zh-cn_2.png)

删除IMSI-GT对应关系将导致所有属于该IMSI号段的用户不能在本SGSN内附着或者路由更新。

**适用网元：SGSN、SMSF**

该命令用于删除IMSI前缀与国家代码+网络接入号的对应关系。

## 注意事项

- 该命令执行后，立刻删除原IMSI前缀与国家代码＋网络接入号的转换关系。
- 删除IMSI-GT对应关系将导致所有属于该IMSI号段的用户不能在本SGSN内附着或者路由更新。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>取值范围：5～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [IMSI-GT对应关系（IMSIGT）](configobject/UNC/20.15.2/IMSIGT.md)

## 使用实例

删除IMSI前缀为3080107000的所有记录:

RMV IMSIGT: IMSIPRE="3080107000";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMSI-GT对应关系(RMV-IMSIGT)_26145464.md`

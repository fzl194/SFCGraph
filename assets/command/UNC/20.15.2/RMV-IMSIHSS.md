---
id: UNC@20.15.2@MMLCommand@RMV IMSIHSS
type: MMLCommand
name: RMV IMSIHSS（删除IMSI-HSS对应关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSIHSS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- IMSI-HSS转换信息
status: active
---

# RMV IMSIHSS（删除IMSI-HSS对应关系）

## 功能

![](删除IMSI-HSS对应关系(RMV IMSIHSS)_72225135.assets/notice_3.0-zh-cn_2.png)

可能导致系统无法找到指定IMSI号段用户所归属的HSS，会导致对应用户无法附着。

**适用网元：SGSN、MME**

此命令用于删除IMSI（International Mobile Subscriber Identity）与HSS（Home Subscriber Server）的映射关系表记录。

## 注意事项

- 此命令执行后立即生效。
- 删除后，可能导致系统无法找到指定IMSI号段用户所归属的HSS，会导致对应用户无法附着。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：待删除的IMSI前缀。<br>数据来源：全网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIHSS]] · IMSI-HSS对应关系（IMSIHSS）

## 使用实例

将IMSI前缀为3080107000的记录删除：

```
RMV IMSIHSS: IMSIPRE="3080107000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IMSIHSS.md`

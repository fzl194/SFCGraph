---
id: UDG@20.15.2@MMLCommand@RMV NETWORKINSTVPNMAP
type: MMLCommand
name: RMV NETWORKINSTVPNMAP（删除网络实例配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: NETWORKINSTVPNMAP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 网络实例管理
- 网络实例配置
status: active
---

# RMV NETWORKINSTVPNMAP（删除网络实例配置）

## 功能

**适用NF：UPF**

该命令用于删除网络实例和VPN的绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETWORKINSTANCE | 网络实例名称 | 可选必选说明：可选参数<br>参数含义：网络实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～100，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NETWORKINSTVPNMAP]] · 网络实例配置（NETWORKINSTVPNMAP）

## 使用实例

删除名为"net1"的网络实例：

```
RMV NETWORKINSTVPNMAP: NETWORKINSTANCE="net1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-NETWORKINSTVPNMAP.md`

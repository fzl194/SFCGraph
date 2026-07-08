---
id: UNC@20.15.2@MMLCommand@RMV UCFSVRIP
type: MMLCommand
name: RMV UCFSVRIP（删除UCF报表服务器的接入点IP地址）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UCFSVRIP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- UCF管理
- UCF服务器IP
status: active
---

# RMV UCFSVRIP（删除UCF报表服务器的接入点IP地址）

## 功能

该命令用于删除报表服务器的接入点IP地址。

## 注意事项

- 该命令执行后立即生效。

- 执行命令前请确认UCF服务处于上线状态。
- 如果删除系统中唯一的一个接入点，则会影响报表上传。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACCESSNAME | 接入点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UCF服务器的接入点名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UCFSVRIP]] · UCF报表服务器的接入点IP地址（UCFSVRIP）

## 使用实例

运营商A不再使用1号报表服务器（UCFSVR1）下的1号接入点（ACCESS1），将此接入点删除：

```
RMV UCFSVRIP:ACCESSNAME="ACCESS1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UCFSVRIP.md`

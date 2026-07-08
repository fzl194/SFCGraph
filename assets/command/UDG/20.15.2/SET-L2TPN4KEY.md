---
id: UDG@20.15.2@MMLCommand@SET L2TPN4KEY
type: MMLCommand
name: SET L2TPN4KEY（设置L2TP N4密码配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: L2TPN4KEY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP N4密码
status: active
---

# SET L2TPN4KEY（设置L2TP N4密码配置）

## 功能

**适用NF：PGW-U、UPF**

![](设置L2TP N4密码配置（SET L2TPN4KEY）_64015280.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，需要与SMF的配置保持一致，否则可能会导致L2TP用户激活失败。

该命令用于配置N4接口L2TP私有信元PCO info和Tunnel info的密钥。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置N4KeyValue和CfmN4KeyValue即启用密钥，N4KeyValue和CfmN4KeyValue都输入空格即清空配置关闭密钥。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| N4KEYVALUE | N4密钥 | 可选必选说明：可选参数<br>参数含义：指定N4密钥。<br>数据来源：本端规划<br>取值范围：密码类型，不加密输入时，取值范围16-30位字符串，只能输入0-9，A-F，不区分大小写，最小16位，最大30位。输入N4KEYVALUE时，必须同时输入确认密码CFMN4KEYVALUE，且密码相同。<br>默认值：无<br>配置原则：无 |
| CFMN4KEYVALUE | 确认N4密钥 | 可选必选说明：可选参数<br>参数含义：该参数用于确认N4密钥。<br>数据来源：本端规划<br>取值范围：密码类型，不加密输入时，取值范围16-30位字符串，CfmN4KeyValue需要和N4KeyValue密码相同。<br>默认值：无<br>配置原则：CFMN4KEYVALUE需要和N4KEYVALUE密码相同。 |

## 操作的配置对象

- [L2TP N4密码配置（L2TPN4KEY）](configobject/UDG/20.15.2/L2TPN4KEY.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00140]]

## 使用实例

启用N4KeyValue密钥，配置密码为“123456789ABCDEF123”：

```
SET L2TPN4KEY: N4KEYVALUE="*****", CFMN4KEYVALUE="*****";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置L2TP-N4密码配置（SET-L2TPN4KEY）_64015280.md`

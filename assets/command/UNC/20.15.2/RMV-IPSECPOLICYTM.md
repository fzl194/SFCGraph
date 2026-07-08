---
id: UNC@20.15.2@MMLCommand@RMV IPSECPOLICYTM
type: MMLCommand
name: RMV IPSECPOLICYTM（删除IPsec策略模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPSECPOLICYTM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec策略模板
status: active
---

# RMV IPSECPOLICYTM（删除IPsec策略模板）

## 功能

![](删除IPsec策略模板（RMV IPSECPOLICYTM）_96044558.assets/notice_3.0-zh-cn_2.png)

删除IPsec策略模板，影响业务流量使用IPSEC进行加解密功能，有业务影响。

该命令用于删除IPsec策略模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略模板名称 | 可选必选说明：必选参数<br>参数含义：策略模板名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 策略模板序列号 | 可选必选说明：必选参数<br>参数含义：策略模板序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECPOLICYTM]] · IPsec策略模板（IPSECPOLICYTM）

## 使用实例

删除策略模板名为“temp3”，序列号为1的IPsec策略模板：

```
RMV IPSECPOLICYTM:POLICYNAME="temp3",SEQUENCENUMBER=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IPsec策略模板（RMV-IPSECPOLICYTM）_96044558.md`

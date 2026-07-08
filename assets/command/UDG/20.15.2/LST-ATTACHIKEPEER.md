---
id: UDG@20.15.2@MMLCommand@LST ATTACHIKEPEER
type: MMLCommand
name: LST ATTACHIKEPEER（查询绑定的IKE对等体）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ATTACHIKEPEER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- 绑定的IKE对等体
status: active
---

# LST ATTACHIKEPEER（查询绑定的IKE对等体）

## 功能

该命令用于查询IKE Peer信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 序列号 | 可选必选说明：必选参数<br>参数含义：序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |
| POLICYMODE | 策略模式 | 可选必选说明：必选参数<br>参数含义：策略模式。<br>数据来源：对端协商<br>取值范围：<br>- “Isakmp（ISAKMP模式）”：使用IKE建立IPsec安全联盟的模式<br>默认值：无<br>配置原则：无 |
| TEMPLATEMODE | 模板模式 | 可选必选说明：必选参数<br>参数含义：模板模式。<br>数据来源：对端协商<br>取值范围：<br>- None（无）<br>- “PolicyTemplate（策略模板模式）”：使用策略模板模式创建策略，仅支持用户级IPsec。<br>默认值：无<br>配置原则：无 |
| IKEPEERNAME | IKE对等体名称 | 可选必选说明：可选参数<br>参数含义：IKE对等体名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [绑定IKE对等体（ATTACHIKEPEER）](configobject/UDG/20.15.2/ATTACHIKEPEER.md)

## 使用实例

查询IKE Peer绑定关系：

```
LST ATTACHIKEPEER:POLICYNAME="pol2",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None;
RETCODE = 0  操作成功

结果如下
-------------------------
     策略名称  =  pol2
       序列号  =  1
     策略模式  =  ISAKMP模式
     模板模式  =  无
IKE对等体名称  =  1
       优先级  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询绑定的IKE对等体（LST-ATTACHIKEPEER）_26032193.md`

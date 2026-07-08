---
id: UNC@20.15.2@MMLCommand@LST PROPATTACHIPSECPROPOSAL
type: MMLCommand
name: LST PROPATTACHIPSECPROPOSAL（查询IPsec策略绑定提议）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PROPATTACHIPSECPROPOSAL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- 绑定的IPsec安全提议
status: active
---

# LST PROPATTACHIPSECPROPOSAL（查询IPsec策略绑定提议）

## 功能

该命令用于查询IPsec策略的提议。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：IPsec策略的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 序列号 | 可选必选说明：必选参数<br>参数含义：序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |
| POLICYMODE | 策略模式 | 可选必选说明：必选参数<br>参数含义：策略模式： ISAKMP：表明使用IKE建立IPsec安全联盟。<br>数据来源：对端协商<br>取值范围：<br>- “Isakmp（ISAKMP模式）”：使用IKE建立IPsec安全联盟的模式<br>默认值：无<br>配置原则：无 |
| TEMPLATEMODE | 模板模式 | 可选必选说明：必选参数<br>参数含义：模板模式-绑定一个策略模板到ISAKMP（使用策略模板建立IPsec安全联盟）。<br>数据来源：对端协商<br>取值范围：<br>- None（无）<br>- “PolicyTemplate（策略模板模式）”：使用策略模板模式创建策略，仅支持用户级IPsec。<br>默认值：无<br>配置原则：无 |
| IPSECPROPNAME | IPsec安全提议名称 | 可选必选说明：可选参数<br>参数含义：Proposal名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPsec策略绑定提议（PROPATTACHIPSECPROPOSAL）](configobject/UNC/20.15.2/PROPATTACHIPSECPROPOSAL.md)

## 使用实例

查询IPsec策略的提议：

```
LST PROPATTACHIPSECPROPOSAL:POLICYNAME="pol2",SEQUENCENUMBER=1,POLICYMODE=Isakmp,TEMPLATEMODE=None;

RETCODE = 0  操作成功

结果如下
-------------------------
         策略名称  =  pol2
           序列号  =  1
         策略模式  =  ISAKMP模式
         模板模式  =  无
IPsec安全提议名称  =  ipsecpsl37
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPsec策略绑定提议（LST-PROPATTACHIPSECPROPOSAL）_25830695.md`

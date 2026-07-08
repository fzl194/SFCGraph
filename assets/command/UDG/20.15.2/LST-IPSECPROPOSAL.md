---
id: UDG@20.15.2@MMLCommand@LST IPSECPROPOSAL
type: MMLCommand
name: LST IPSECPROPOSAL（查询IPsec提议）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSECPROPOSAL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- IPsec
- IPsec提议
status: active
---

# LST IPSECPROPOSAL（查询IPsec提议）

## 功能

该命令用于查询IP安全提议。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROPOSALNAME | Proposal名称 | 可选必选说明：可选参数<br>参数含义：Proposal名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPSECPROPOSAL]] · IPsec提议（IPSECPROPOSAL）

## 使用实例

查询IP安全提议：

```
LST IPSECPROPOSAL:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
 Proposal名称  =  asdf2
  ESP认证算法  =  sha2-256算法
  ESP加密算法  =  256位AES算法
IPsec安全协议  =  ESP协议
   AH认证算法  =  NULL
     封装模式  =  传输模式
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPSECPROPOSAL.md`

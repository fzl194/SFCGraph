---
id: UNC@20.15.2@MMLCommand@RMV IKEPROPOSAL
type: MMLCommand
name: RMV IKEPROPOSAL（删除IKE提议）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IKEPROPOSAL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE安全提议
status: active
---

# RMV IKEPROPOSAL（删除IKE提议）

## 功能

![](删除IKE提议（RMV IKEPROPOSAL）_25912255.assets/notice_3.0-zh-cn_2.png)

删除IKE提议，影响业务流量使用IPSEC进行加解密功能，有业务影响。

该命令用于删除IKE安全提议配置。

## 注意事项

- 该命令执行后立即生效。

- 当IKE安全提议被IKE对等体配置时，IKE安全提议不能被删除。如果需要删除IKE安全提议，必须先删除安全IKE对等体中的配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROPOSALNUMBER | 安全提议号 | 可选必选说明：必选参数<br>参数含义：提议编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295。101不支持配置，但可以查询。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IKEPROPOSAL]] · IKE提议（IKEPROPOSAL）

## 使用实例

删除IKE安全提议号为1的IKE安全提议：

```
RMV IKEPROPOSAL:PROPOSALNUMBER=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IKE提议（RMV-IKEPROPOSAL）_25912255.md`

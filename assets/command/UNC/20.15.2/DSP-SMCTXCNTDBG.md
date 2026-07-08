---
id: UNC@20.15.2@MMLCommand@DSP SMCTXCNTDBG
type: MMLCommand
name: DSP SMCTXCNTDBG（显示指定CS类型的上下文数量）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMCTXCNTDBG
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 通用调测
status: active
---

# DSP SMCTXCNTDBG（显示指定CS类型的上下文数量）

## 功能

**适用NF：SMF、PGW-C、GGSN、SGW-C**

本命令用于显示指定CS类型的上下文数量。本命令的使用场景是系统调测。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | 指定CS类型 | 可选必选说明：必选参数<br>参数含义：本参数表示指定CS类型。<br>数据来源：本端规划<br>取值范围：<br>- SMC_SM（会话管理控制cell服务的会话管理模块）<br>- UESM（用户级会话管理cell服务）<br>- UPC（UP管理cell服务）<br>- SMC_UDM（会话管理控制cell服务的签约数据模块）<br>- SM5GPOLICY（5G会话管理策略cell服务）<br>- SM4GPOLICY（4G会话管理策略cell服务）<br>- AMPOLICY（接入移动管理策略cell服务）<br>- SM5GCM（会话管理5G融合计费cell服务）<br>- SM4GCM（会话管理4G计费cell服务）<br>- RADIUSACCT（会话管理AAA计费cell服务）<br>- S6B（会话管理Diameter AAA认证授权cell服务）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMCTXCNTDBG]] · 指定CS类型的上下文数量（SMCTXCNTDBG）

## 使用实例

查询UESM的上下文数量。

```
%%DSP SMCTXCNTDBG: CSTYPE=UESM;%%
RETCODE = 0  操作成功

结果如下
--------
  指定CS类型  =  用户级会话管理cell服务
  上下文数量  =  0
无上下文标志  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示指定CS类型的上下文数量（DSP-SMCTXCNTDBG）_09652986.md`

---
id: UNC@20.15.2@MMLCommand@RMV SELCHFGBYIMSI
type: MMLCommand
name: RMV SELCHFGBYIMSI（删除IMSI与CHF组的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SELCHFGBYIMSI
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- CHF选择
status: active
---

# RMV SELCHFGBYIMSI（删除IMSI与CHF组的绑定关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于删除IMSI与CHF组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 该命令用于拨测CHF，拨测完成后建议立即删除该配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户的IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于设置绑定的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。<br>默认值：无<br>配置原则：<br>该参数表示用户完整的IMSI信息，不支持前缀匹配。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SELCHFGBYIMSI]] · IMSI与CHF组的绑定关系（SELCHFGBYIMSI）

## 使用实例

删除基于IMSI选择CHF处理:

```
RMV SELCHFGBYIMSI: IMSI="123456789012345";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMSI与CHF组的绑定关系（RMV-SELCHFGBYIMSI）_88622274.md`

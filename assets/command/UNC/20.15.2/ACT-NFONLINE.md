---
id: UNC@20.15.2@MMLCommand@ACT NFONLINE
type: MMLCommand
name: ACT NFONLINE（激活NF上线）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: NFONLINE
command_category: 动作类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF 状态管理
status: active
---

# ACT NFONLINE（激活NF上线）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用来激活NF向NRF注册。在完成NF相关基础数据配置后，可以通过本命令手动触发NF到NRF的注册。也可以在NF注册、或者配置数据更新异常的情况下，通过本命令重新手动触发NF到NRF的重新上线注册。

## 注意事项

- 该命令执行后立即生效。

- 执行该命令无法切换注册的NRF，请使用DWORD2 BIT8切换到主用NRF注册。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFPROFILE命令中的NFINSTANCENAME值保持一致。NFINSTANCENAME值可通过LST NFPROFILE获得。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFONLINE]] · NF上线（NFONLINE）

## 使用实例

激活AMF_Instance_0向NRF的注册。

```
ACT NFONLINE: NFINSTANCENAME="AMF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-NFONLINE.md`

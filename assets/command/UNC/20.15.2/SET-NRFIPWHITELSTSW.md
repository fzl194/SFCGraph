---
id: UNC@20.15.2@MMLCommand@SET NRFIPWHITELSTSW
type: MMLCommand
name: SET NRFIPWHITELSTSW（设置NF IP白名单开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFIPWHITELSTSW
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF IP白名单管理
status: active
---

# SET NRFIPWHITELSTSW（设置NF IP白名单开关）

## 功能

![](设置NF IP白名单开关（SET NRFIPWHITELSTSW）_29869622.assets/notice_3.0-zh-cn_2.png)

该命令与ADD NRFIPWHITELST配合使用，在NF IP白名单未设置完成时请勿打开此开关，否则客户端IP未加入到IP白名单中的NF将无法正常注册、去注册、更新及维持到NRF的心跳。

**适用NF：NRF**

该命令用于设置NF IP白名单功能开关，用于控制非预期NF接入。

该命令与ADD NRFIPWHITELST配合使用，在NF IP白名单未设置完成时请勿打开此开关，否则客户端IP未加入到IP白名单中的NF将无法正常注册、去注册、更新及维持到NRF的心跳。

该命令与SET NRFWHITELISTSW开关互斥，两者不能同时打开。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFIPWHITELSTSW |
| --- |
| FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFIPWHITELSTSW | NF IP白名单开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF IP白名单功能是否打开。开关设置为“FUNC_ON”，NRF将基于NF的客户端IP对IP白名单内外的NF做区别处理，正常处理配置在IP白名单内NF的注册、去注册、更新及心跳业务；不在IP白名单内的NF上述业务将不能被处理。开关设置为“FUNC_OFF”，NRF不对IP白名单内外NF区别处理，正常处理所有NF的注册、去注册、更新及心跳业务。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFIPWHITELSTSW]] · NF IP白名单开关（NRFIPWHITELSTSW）

## 使用实例

打开NF IP白名单开关，执行如下命令：

```
SET NRFIPWHITELSTSW: NFIPWHITELSTSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NRFIPWHITELSTSW.md`

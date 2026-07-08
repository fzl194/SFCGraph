---
id: UNC@20.15.2@MMLCommand@SET CERTESCAPESWITCH
type: MMLCommand
name: SET CERTESCAPESWITCH（设置证书过期逃生开关状态）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CERTESCAPESWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 证书维护
status: active
---

# SET CERTESCAPESWITCH（设置证书过期逃生开关状态）

## 功能

![](设置证书过期逃生开关状态（SET CERTESCAPESWITCH）_55469701.assets/notice_3.0-zh-cn_2.png)

执行此命令将修改证书过期逃生开关状态，开关关闭后证书过期业务可能会中断。

设置证书过期逃生开关状态。此命令用于设置证书管理页面所有证书在过期情况下是否仍可以正常使用。开关打开情况下证书过期后仍然能正常使用，业务无中断。

## 注意事项

- 本命令需要在稳态环境下执行。
- 目前不支持[**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)命令的“证书开关”为“OFF（关闭）”时打开证书过期逃生开关。
- 该命令存在系统初始记录，证书过期逃生开关的初始状态和证书开关的初始状态保持一致。
- 关闭证书开关时，会自动关闭证书过期逃生开关。打开证书开关时，会自动打开证书过期逃生开关。
- 本命令设置完成后建议间隔至少10秒后再次设置。
- 初始部署场景下开关默认为开启状态。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CERTESCAPESTATE | 证书过期逃生开关状态 | 可选必选说明：必选参数<br>参数含义：证书过期逃生开关状态。<br>取值范围：<br>- ON（打开）<br>- OFF（关闭）<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CERTESCAPESWITCH]] · 证书过期逃生开关状态（CERTESCAPESWITCH）

## 使用实例

设置证书过期逃生开关状态。

```
%%SET CERTESCAPESWITCH: CERTESCAPESTATE=ON;%%
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CERTESCAPESWITCH.md`

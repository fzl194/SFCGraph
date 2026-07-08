---
id: UNC@20.15.2@MMLCommand@ADD NRFWHITELIST
type: MMLCommand
name: ADD NRFWHITELIST（增加NF白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFWHITELIST
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF白名单配置
status: active
---

# ADD NRFWHITELIST（增加NF白名单）

## 功能

![](增加NF白名单（ADD NRFWHITELIST）_35519265.assets/notice_3.0-zh-cn_2.png)

该命令与SET NRFWHITELISTSW配合使用，在白名单未设置完成时请勿打开NF白名单开关，否则未加入到白名单中的NF将无法正常注册、去注册、更新及维持到NRF的心跳功能。

**适用NF：NRF**

该命令用于增加NF白名单内的NF实例。白名单设置用于支撑NRF可以对不同NF进行区别处理，避免新升级NRF未经功能验证完善后就接入业务，导致错误业务导流。

该命令与NF白名单开关SET NRFWHITELISTSW配合使用，在白名单未设置完成时请勿打开NF白名单开关，否则影响未加入到白名单中NF的正常注册、去注册、更新及心跳功能。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示需要增加到白名单中的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFWHITELIST]] · NF白名单（NRFWHITELIST）

## 使用实例

若查询AMF的实例化ID为“88888888-4444-1234-5678-123456789ABC”，将实例化ID为“88888888-4444-1234-5678-123456789ABC”的网元添加到白名单，执行如下命令。

```
ADD NRFWHITELIST: NFINSTANCEID="88888888-4444-1234-5678-123456789ABC";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFWHITELIST.md`

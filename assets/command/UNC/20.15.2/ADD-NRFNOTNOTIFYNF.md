---
id: UNC@20.15.2@MMLCommand@ADD NRFNOTNOTIFYNF
type: MMLCommand
name: ADD NRFNOTNOTIFYNF（增加不通知NF实例）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFNOTNOTIFYNF
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF通知管理
status: active
---

# ADD NRFNOTNOTIFYNF（增加不通知NF实例）

## 功能

![](增加不通知NF实例（ADD NRFNOTNOTIFYNF）_60329621.assets/notice_3.0-zh-cn_2.png)

该命令与NRF通知策略SET NRFNOTIFYPLY配合使用，当SET NRFNOTIFYPLY的NRFNOTIFYPLY设置为NFINSTANCEIDNOT时，请谨慎添加NF实例信息，否则对于添加到列表中的NF，NRF将不会通知其注册变更信息。

**适用NF：NRF**

该命令用于增加不通知的NF实例，当列表中的NF注册信息发生变更时，NRF将不会发送对应的订阅通知消息。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>该命令与SET NRFNOTIFYPLY配合使用，当SET NRFNOTIFYPLY中的NOTIFYNPLY参数设置为“NFINSTANCEIDNOT”时生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNOTNOTIFYNF]] · 不通知NF实例（NRFNOTNOTIFYNF）

## 使用实例

当运营商希望NF实例标识为“88888888-4444-1234-5678-123456789abc”的NF注册信息发生变更时，NRF不发送通知消息，执行如下命令。

```
ADD NRFNOTNOTIFYNF: NFINSTANCEID="88888888-4444-1234-5678-123456789abc";
SET NRFNOTIFYPLY: NOTIFYPLY=NFINSTANCEIDNOT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加不通知NF实例（ADD-NRFNOTNOTIFYNF）_60329621.md`

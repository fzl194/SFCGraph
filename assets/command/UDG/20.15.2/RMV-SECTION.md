---
id: UDG@20.15.2@MMLCommand@RMV SECTION
type: MMLCommand
name: RMV SECTION（删除地址池IP地址段）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SECTION
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址段配置
status: active
---

# RMV SECTION（删除地址池IP地址段）

## 功能

**适用NF：PGW-U、UPF**

![](删除地址池IP地址段（RMV SECTION）_82837115.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除地址段，使地址段内地址不可用，可能会导致用户激活失败。

该命令为删除地址池里的地址段，当某一地址段不再使用时，系统可使用该命令将其删除。

## 注意事项

- 该命令执行后立即生效。
- 删除地址段时，如果地址段内仍有地址被用户使用，则禁止删除。
- 删除地址段时，需要先使用LCK SECTION命令锁定地址段，收回全部地址后才可以删除该地址段。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SECTIONNUM | 地址段号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置Section的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SECTION]] · 地址段信息（SECTION）

## 使用实例

假设运营商不再使用本地地址池pool1中的一个地址段，当锁定地址段，收回全部地址后，则可删除该地址段，POOLNAME为pool1，SECTIONNUM为0：

```
RMV SECTION:POOLNAME="pool1",SECTIONNUM=0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SECTION.md`

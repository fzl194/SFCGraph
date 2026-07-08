---
id: UNC@20.15.2@MMLCommand@RMV SECTION
type: MMLCommand
name: RMV SECTION（删除地址段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SECTION
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
- 接入管理
- UE地址管理
- UE地址池管理
- 地址段管理
status: active
---

# RMV SECTION（删除地址段）

## 功能

![](删除地址段（RMV SECTION）_09654197.assets/notice_3.0-zh-cn_2.png)

使用该命令后会将强制删除正在使用的地址，对应的正常在线用户将被去活。

**适用NF：SMF、PGW-C、GGSN**

该命令为删除地址池里的地址段，当某一地址段不再使用时，UNC可使用该命令将其删除。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| SECTIONNUM | 地址段号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置Section的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [地址段（SECTION）](configobject/UNC/20.15.2/SECTION.md)

## 使用实例

当不使用地址池名为pool1中的序号为0的地址段时，可以删除该地址段。

```
RMV SECTION:POOLNAME="pool1",SECTIONNUM=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除地址段（RMV-SECTION）_09654197.md`

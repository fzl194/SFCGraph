---
id: UNC@20.15.2@MMLCommand@RMV HTTPSTATUS
type: MMLCommand
name: RMV HTTPSTATUS（删除HTTP状态码判定配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HTTPSTATUS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP状态码管理
status: active
---

# RMV HTTPSTATUS（删除HTTP状态码判定配置）

## 功能

![](删除HTTP状态码判定配置（RMV HTTPSTATUS）_04250405.assets/notice_3.0-zh-cn_2.png)

执行该命令会改变HTTP特定场景下的行为，可能导致业务受损。

该命令用于删除已有的HTTP状态码判定配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTPSTATUS配置的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPSTATUS]] · HTTP状态码判定配置（HTTPSTATUS）

## 使用实例

删除已有的HTTP状态码判定配置，可以用如下命令：

```
RMV HTTPSTATUS: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HTTPSTATUS.md`

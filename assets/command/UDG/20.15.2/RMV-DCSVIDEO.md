---
id: UDG@20.15.2@MMLCommand@RMV DCSVIDEO
type: MMLCommand
name: RMV DCSVIDEO（删除DCS点播视频资源）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: DCSVIDEO
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源管理
status: active
---

# RMV DCSVIDEO（删除DCS点播视频资源）

## 功能

![](删除DCS点播视频资源（RMV DCSVIDEO）_11530325.assets/notice_3.0-zh-cn.png)

该命令用于删除DCS视频资源，资源删除后需要重新拉取，会对业务造成较大影响。

该命令用于删除DCS点播视频资源，作应急逃生手段。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OTTNAME | OTT名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示OTT名称，OTT名称可通过DSP DCSSTATS命令查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| URL | URL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示视频文件的URL名称。URL名称可以通过DSP DCSSTATS命令查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DCSVIDEO]] · DCS点播视频资源（DCSVIDEO）

## 使用实例

删除OTT名称为“douyin”，URL为“aaa.douyincdn.com/fantasy/stream-404357031821050550.mp4”的点播视频资源。

```
RMV DCSVIDEO: OTTNAME="douyin", URL="aaa.douyincdn.com/fantasy/stream-404357031821050550.mp4";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-DCSVIDEO.md`

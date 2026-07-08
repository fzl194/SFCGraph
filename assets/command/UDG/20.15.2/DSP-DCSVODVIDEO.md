---
id: UDG@20.15.2@MMLCommand@DSP DCSVODVIDEO
type: MMLCommand
name: DSP DCSVODVIDEO（显示指定点播视频信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DCSVODVIDEO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源管理
status: active
---

# DSP DCSVODVIDEO（显示指定点播视频信息）

## 功能

该命令用于显示指定点播视频信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OTTNAME | OTT名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示OTT名称，OTT名称可通过DSP DCSSTATS命令查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| URL | URL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示视频文件的URL名称。URL名称可以通过DSP DCSSTATS命令查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DCSVODVIDEO]] · 指定点播视频信息（DCSVODVIDEO）

## 使用实例

显示OTT名称为“douyin”，URL为“aaa.douyincdn.com/fantasy/stream-404357031821050550.mp4”的点播视频信息。

```
%%DSP DCSVODVIDEO: OTTNAME="douyin", URL="aaa.douyincdn.com/fantasy/stream-404357031821050550.mp4";%%
RETCODE = 0  操作成功

结果如下
------------------------
实例ID                 文件状态    视频创建时间         视频大小（KB） 最后访问时间         最后核查时间         最后修改时间         热度  

18378575044281397419   文件存在    2025-02-27 21:02:02  3200          2025-02-27 21:02:02  2025-02-27 21:02:02  2025-02-27 21:02:02  5        
18378575044281401515   文件不存在  NULL                 0             NULL                 NULL                 NULL                 0       
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DCSVODVIDEO.md`

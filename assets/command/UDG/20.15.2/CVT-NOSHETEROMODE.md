---
id: UDG@20.15.2@MMLCommand@CVT NOSHETEROMODE
type: MMLCommand
name: CVT NOSHETEROMODE（转换NOS异构模式）
nf: UDG
version: 20.15.2
verb: CVT
object_keyword: NOSHETEROMODE
command_category: 调测类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- EOX管理
status: active
---

# CVT NOSHETEROMODE（转换NOS异构模式）

## 功能

![](转换NOS异构模式(CVT NOSHETEROMODE)_77109417.assets/notice_3.0-zh-cn.png)

该命令属于高危命令，执行该命令会影响主备OMU的同步等功能，导致主备OMU的关键文件、软件包等存在差异，会对系统造成一定的影响，请谨慎使用。

该命令用来转换NOS异构模式。

该命令仅在 Full-stack 虚机场景下支持。

## 注意事项

只有主备板CPU类型一致时，才能执行该命令。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OMUHETEROSWITCH | OMU异构开关 | 可选必选说明：必选参数<br>参数含义：该参数表示OMU是否打开OMU异构开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- On(打开)：OMU异构开关状态为打开。<br>- Off(关闭)：OMU异构开关状态为关闭。<br>默认值：无<br>配置原则：该参数系统初始值为<br>“Off(关闭)”<br>。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NOSHETEROMODE]] · NOS异构模式（NOSHETEROMODE）

## 使用实例

转换NOS异构模式：

```
CVT NOSHETEROMODE:OMUHETEROSWITCH=On,SERVICEINSTANCE="vnfc";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/CVT-NOSHETEROMODE.md`

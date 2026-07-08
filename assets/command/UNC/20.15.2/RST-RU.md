---
id: UNC@20.15.2@MMLCommand@RST RU
type: MMLCommand
name: RST RU（重启资源单元）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: RU
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# RST RU（重启资源单元）

## 功能

![](重启资源单元（RST RU）_59103467.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，会重启资源单元，请谨慎使用并联系华为技术支持协助操作。

该命令用于复位VNFC上的资源块。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令，一次只能复位一个资源单元，复位后的指定资源单元会重新启动处于正常运行状态。
- 复位重新启动后，资源单元配置数据不会丢失，复位操作期间业务会中断。
- 复位前，需确认该RU是否为IP控制面的RU；需保证不能同时复位该类型的主和备RU，如果同时复位了该类型主和备的RU，则会导致IP业务中断。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RU]] · 解闭CSDB RU（RU）

## 使用实例

复位指定VNFC上的指定资源块，RUNAME为CSDB_SD_RU_0067：

```
RST RU:RUNAME="CSDB_SD_RU_0067"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/重启资源单元（RST-RU）_59103467.md`

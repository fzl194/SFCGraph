---
id: UDG@20.15.2@MMLCommand@DSP FESVERIFICATION
type: MMLCommand
name: DSP FESVERIFICATION（显示FES对账信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FESVERIFICATION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎服务
- 显示FES对账信息
status: active
---

# DSP FESVERIFICATION（显示FES对账信息）

## 功能

该命令用于显示FES对账信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDENTITYFLAG | 身份标志位 | 可选必选说明：可选参数<br>参数含义：该参数用于表示身份标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RUNAME：表示输入资源单元名称。<br>- COMPID：表示输入组件ID。<br>默认值：无 |
| COMPONENTID | 组件ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAG”配置为“COMPID”时为必选参数。<br>参数含义：该参数用来表示组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAG”配置为“RUNAME”时为必选参数。<br>参数含义：该参数用来表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：区分大小写，不支持空格，下发本MML命令前可使用DSP RU查看资源单元信息。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FESVERIFICATION]] · FES对账信息（FESVERIFICATION）

## 使用实例

显示FES对账信息：

```
DSP FESVERIFICATION:;
```

```

RETCODE = 0 操作成功

结果如下
-------------------------
对账时间间隔（s） =  3600
上一次慢对账时间  =  2017-09-30 05:33:02
下一次慢对账时间  =  2017-09-30 06:33:02
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FESVERIFICATION.md`

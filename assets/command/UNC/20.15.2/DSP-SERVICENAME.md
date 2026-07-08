---
id: UNC@20.15.2@MMLCommand@DSP SERVICENAME
type: MMLCommand
name: DSP SERVICENAME（显示注册的服务名称）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SERVICENAME
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP SERVICENAME（显示注册的服务名称）

## 功能

该命令用于查询在CMF上注册的服务名称。

若要查询所有网元在CMF上注册的服务名称，请不要输入任何参数。

若要查询某个网元在CMF上注册的服务名称，请输入“网元ID”参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询在CMF上注册的服务名称，可通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：<br>该参数若不输入，则表示查询所有网元在CMF上注册的服务名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERVICENAME]] · 注册的服务名称（SERVICENAME）

## 使用实例

用户查询在CMF上注册且网元ID为0的服务名称。

```
%%DSP SERVICENAME: MEID="0";%%
RETCODE = 0  操作成功

结果如下
--------
服务名称        网元ID
CellWall        0
SDRS            0
SCFM            0
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SERVICENAME.md`

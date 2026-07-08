---
id: UDG@20.15.2@MMLCommand@ADD PODHEALCPUTHR
type: MMLCommand
name: ADD PODHEALCPUTHR（增加对应PODTYPE下CPU的阈值配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: PODHEALCPUTHR
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# ADD PODHEALCPUTHR（增加对应PODTYPE下CPU的阈值配置）

## 功能

当前版本此命令可正常下发，但配置不生效。

该命令用于增加对应PODTYPE下CPU的阈值配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 不允许配置hafetcd-pod。可通过LST PODHEALCPUTHR查询已配置的Pod类型，避免配置冲突，只要输入的以“#”分隔的Pod类型在已有记录中就不允许配置。
>
> - 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | POD类型 | 可选必选说明：必选参数<br>参数含义：用于设置POD类型。可通过<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NOLOADTHR | 空载阈值（%） | 可选必选说明：可选参数<br>参数含义：用于配置某种类型的POD实例的CPU使用率在空载时的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：无<br>配置原则：无 |
| OVERLOADTHR | 过载阈值（%） | 可选必选说明：可选参数<br>参数含义：用于配置某种类型的POD实例的CPU使用率过载的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODHEALCPUTHR]] · 对应PODTYPE下的阈值配置（PODHEALCPUTHR）

## 使用实例

增加对应PODTYPE下CPU的阈值配置。

```
%%ADD PODHEALCPUTHR: PODTYPE="haf-pod", NOLOADTHR=10, OVERLOADTHR=20;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加对应PODTYPE下CPU的阈值配置（ADD-PODHEALCPUTHR）_60073345.md`

---
id: UNC@20.15.2@MMLCommand@SET APNRATECTRL
type: MMLCommand
name: SET APNRATECTRL（设置APN速率控制配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNRATECTRL
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 速率控制
- APN速率控制
- APN速率控制配置
status: active
---

# SET APNRATECTRL（设置APN速率控制配置）

## 功能

**适用NF：PGW-C**

该命令用于配置基于APN的APN速率控制功能。当网络部署了APN速率控制功能，且规划设置全局默认速率时，使用此命令。

## 注意事项

- 该命令执行后立即生效。

- 配置参数修改后，PGW-C通过发送Update Bearer Request更新上行速率控制参数。配置修改影响整个APN下的用户，所以推送更新会有延迟。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：APNRATECTRLSW：DISABLE，ULTIMEUNIT：UNRESTRICTED，MAXULRATE：0，DLTIMEUNIT：UNRESTRICTED，MAXDLRATE：0。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用<br>[**ADD APN**](../../../APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令配置生成。 |
| APNRATECTRLSW | APN速率控制开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制开启和关闭APN速率控制功能。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：使能<br>- “DISABLE（不使能）”：不使能<br>- “INHERIT（继承全局）”：继承全局<br>默认值：无。<br>配置原则：无 |
| ULTIMEUNIT | 上行时间单位 | 可选必选说明：该参数在"APNRATECTRLSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于表示APN速率控制的上行时间单位。<br>数据来源：本端规划<br>取值范围：<br>- “UNRESTRICTED（不限制）”：表示不进行APN速率控制。<br>- “MINUTE（分钟）”：表示APN速率控制的时间单位为分钟。<br>- “HOUR（小时）”：表示APN速率控制的时间单位为小时。<br>- “DAY（天）”：表示APN速率控制的时间单位是天。<br>- “WEEK（星期）”：表示APN速率控制的时间单位是星期。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNRATECTRL查询当前参数配置值。<br>配置原则：无 |
| MAXULRATE | 最大上行速率 | 可选必选说明：该参数在"APNRATECTRLSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于表示单位时间内可发送的最大上行数据包数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~50000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNRATECTRL查询当前参数配置值。<br>配置原则：<br>0表示不进行APN速率控制。 |
| DLTIMEUNIT | 下行时间单位 | 可选必选说明：该参数在"APNRATECTRLSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于表示APN速率控制的下行时间单位。<br>数据来源：本端规划<br>取值范围：<br>- “UNRESTRICTED（不限制）”：表示不进行APN速率控制。<br>- “MINUTE（分钟）”：表示APN速率控制的时间单位为分钟。<br>- “HOUR（小时）”：表示APN速率控制的时间单位为小时。<br>- “DAY（天）”：表示APN速率控制的时间单位是天。<br>- “WEEK（星期）”：表示APN速率控制的时间单位是星期。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNRATECTRL查询当前参数配置值。<br>配置原则：无 |
| MAXDLRATE | 最大下行速率 | 可选必选说明：该参数在"APNRATECTRLSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于表示单位时间内可发送的最大下行数据包数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~50000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNRATECTRL查询当前参数配置值。<br>配置原则：<br>0表示不进行APN速率控制。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNRATECTRL]] · APN速率控制配置（APNRATECTRL）

## 使用实例

配置APN名称为test，APN速率控制功能使能，上行时间单位为小时，最大上行速率为100，下行时间单位为小时，最大下行速率为100：

```
SET APNRATECTRL: APN="test", APNRATECTRLSW=ENABLE, ULTIMEUNIT=HOUR, MAXULRATE=100, DLTIMEUNIT=HOUR, MAXDLRATE=100;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-APNRATECTRL.md`

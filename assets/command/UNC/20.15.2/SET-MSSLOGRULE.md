---
id: UNC@20.15.2@MMLCommand@SET MSSLOGRULE
type: MMLCommand
name: SET MSSLOGRULE（设置Log过滤或非抑制开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MSSLOGRULE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 日志信息查询
status: active
---

# SET MSSLOGRULE（设置Log过滤或非抑制开关）

## 功能

![](设置Log过滤或非抑制开关（SET MSSLOGRULE）_00841605.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致性能下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置日志过滤和抑制功能，是诊断开关命令；通过开关设置日志过滤和抑制来记录日志信息，协助问题定位；2小时后会自动关闭。

## 注意事项

- 该命令执行后立即生效。
- 本命令用于使能日志过滤或日志非抑制开关，日志非抑制开启会降低性能，关闭后会恢复性能。开关状态将在2小时后自动恢复。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示的RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| RULE | 规则 | 可选必选说明：必选参数<br>参数含义：该参数用于表示要进行过滤或非抑制功能的设置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- filter：过滤。<br>- unsuppress：非抑制。<br>默认值：无 |
| ENABLE | 开关使能 | 可选必选说明：必选参数<br>参数含义：该参数用于表示开关使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| MODULEID | 模块ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示模块的ID号。如果不输入该参数，则表示匹配向MSS注册日志的所有模块。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| LEVELID | 日志级别 | 可选必选说明：可选参数<br>参数含义：该参数用于表示日志级别。如果不输入该参数，则表示匹配所有日志级别。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| LOGLEVELTYPE | 某日志级别以上或以下的所有级别 | 可选必选说明：可选参数<br>参数含义：该参数用于表示某日志级别以上或以下。如果不输入该参数，则表示只匹配指定的日志级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- above：某日志级别及以上。<br>- below：某日志级别以下。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSLOGRULE]] · Log过滤或非抑制开关（MSSLOGRULE）

## 使用实例

设置日志规则：

```
SET MSSLOGRULE: RULE=filter,MODULEID=2,LEVELID=1,LOGLEVELTYPE=above,ENABLE=TRUE,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MSSLOGRULE.md`

---
id: UNC@20.15.2@MMLCommand@SET SFEFEIDEBUG
type: MMLCommand
name: SET SFEFEIDEBUG（FEI报文、进程日志开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SFEFEIDEBUG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FEI消息统计
status: active
---

# SET SFEFEIDEBUG（FEI报文、进程日志开关）

## 功能

该命令用来开关fei报文日志或进程日志功能。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| DBGVALUE | 日志类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定日志类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PACKET_LOG：报文日志。<br>- PROCESS_LOG：进程日志。<br>默认值：无 |
| DBGOPTION | 使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于开关日志调试功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：如果不设置该参数，则不指定使能开关。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFEFEIDEBUG]] · FEI报文、进程日志开关（SFEFEIDEBUG）

## 使用实例

开关指定可用RU的fei报文日志或进程日志功能：

```
SET SFEFEIDEBUG:RUNAME="VNODE_VNRS_VNFC_IPU_0067", DBGVALUE=PACKET_LOG, DBGOPTION=TRUE; 操作成功。
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SFEFEIDEBUG.md`

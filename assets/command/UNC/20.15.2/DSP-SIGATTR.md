---
id: UNC@20.15.2@MMLCommand@DSP SIGATTR
type: MMLCommand
name: DSP SIGATTR（显示信令网属性状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SIGATTR
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- 信令网属性管理
status: active
---

# DSP SIGATTR（显示信令网属性状态）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于查询信令网属性配置数据。系统初始化时会加载数据库中的信令网属性配置数据，当使用 [**SET SIGATTR**](设置信令网属性(SET SIGATTR)_72226021.md) 修改数据库中的配置后，新修改的数据并不会即时生效，所以此时数据库中的配置与当前节点使用的配置不一致，需要重启所有SPP进程、所有SGP进程使之生效。此命令的功能为查询所有SPP进程、所有SGP进程当前使用的配置。关于数据库中的配置数据，请使用 [**LST SIGATTR**](查询信令网属性(LST SIGATTR)_26306154.md) 命令查询。

## 注意事项

查询方式包括：

- 无参数，表示查询SGSN系统内所有SPP进程、所有SGP进程的SIGATTR状态信息。
- 输入参数RUNAME，表示查询指定RU上所有SPP进程、所有SGP进程的SIGATTR状态信息。
- 只能对SPP或者SGP进行查询。并且只有主用进程能返回查询结果，如果指定RU上进程为备进程，则显示备进程对应主进程的参数。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划。<br>取值范围：0~63 位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SIGATTR]] · 信令网属性状态（SIGATTR）

## 使用实例

查询已经设置的信令网属性：

DSP SIGATTR: RUNAME="LINK_SP_RU_0066";

```
%%DSP SIGATTR: RUNAME="LINK_SP_RU_0066";%%
RETCODE = 0  操作成功。

查询信令网属性
--------------

RU名称           进程类型       进程号          国际网标志           国际备用网标志          国内网标志     国内备用网标志             M3UA STP功能                 是否支持BSSAP+     BSSAP+子系统号           BSSAP+所在信令网             MAP所在信令网        信令网协议类型 

LINK_SP_RU_0066    SGP             1              24 位               14 位                        24 位          14 位                   是                            NULL              255                        NULL                        NULL                  ANSI_SS7                  
LINK_SP_RU_0066    SGP             2              24 位               14 位                        24 位          14 位                   是                            NULL              255                        NULL                        NULL                  ANSI_SS7                  
LINK_SP_RU_0066    SGP             4              24 位               14 位                        24 位          14 位                   是                            NULL              255                        NULL                        NULL                  ANSI_SS7                  
LINK_SP_RU_0066    SGP             0              24 位               14 位                        24 位          14 位                   是                            NULL              255                        NULL                        NULL                  ANSI_SS7                  
LINK_SP_RU_0066    SGP             3              24 位               14 位                        24 位          14 位                   是                            NULL              255                        NULL                        NULL                  ANSI_SS7                  
(结果个数 = 5)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SIGATTR.md`

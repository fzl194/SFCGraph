---
id: UNC@20.15.2@MMLCommand@DSP S1LOAD
type: MMLCommand
name: DSP S1LOAD（显示S1模式负载信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: S1LOAD
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1连接信息
status: active
---

# DSP S1LOAD（显示S1模式负载信息）

## 功能

**适用网元：MME**

此命令用于查询S1用户连接信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：待查询的类型。<br>取值范围：<br>- “BYSGP(基于SGP查询)”<br>默认值：无<br>说明：当前版本只支持基于SGP查询，其他查询类型暂不支持。 |
| RUNAME | RU名称 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：该参数在<br>“QUERYTYPE”<br>参数配置为<br>“BYSGP(基于SGP查询)”<br>时生效。<br>取值范围：0~63 位字符串<br>默认值：无 |

## 操作的配置对象

- [S1模式负载信息（S1LOAD）](configobject/UNC/20.15.2/S1LOAD.md)

## 使用实例

查看S1连接信息：

DSP S1LOAD: QUERYTYPE=BYSGP, RUNAME="USN_VSU1";

```
%%DSP S1LOAD: QUERYTYPE=BYSGP, RUNAME="USN_VSU1";%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
RU名称      SGP模块号         S1用户连接数                 记录有效标志 
USN_VSU1    1016              0                            1                 
USN_VSU1    1017              0                            1                 
USN_VSU1    1018              0                            1                 
USN_VSU1    1019              0                            1                 
仍有后续报告输出
---    END
```

```
%%DSP S1LOAD: QUERYTYPE=BYSGP, RUNAME="USN_VSU1";%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
S1用户总连接数 = 0
(结果个数 = 5)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示S1模式负载信息(DSP-S1LOAD)_72345843.md`

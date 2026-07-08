---
id: UNC@20.15.2@MMLCommand@LST GBPDPRESTBL
type: MMLCommand
name: LST GBPDPRESTBL（查询GBP进程PDP用户上下文资源使用状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBPDPRESTBL
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- GBP资源使用状态表
status: active
---

# LST GBPDPRESTBL（查询GBP进程PDP用户上下文资源使用状态）

## 功能

**适用网元：SGSN**

该命令用于查询GBP进程PDP用户上下文资源使用状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划。<br>取值范围：0~63 位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBPDPRESTBL]] · GBP进程PDP用户上下文资源使用状态（GBPDPRESTBL）

## 使用实例

查询GBP资源使用状态表:

LST GBPDPRESTBL: RUNAME="USN_VSU1";

```
%%LST GBPDPRESTBL:RUNAME="USN_VSU1";%%
RETCODE = 0 操作成功。

输出结果如下
--------------
RU名称      进程号   PDP资源拥塞标志 
USN_VSU1    1        0 
USN_VSU1    0        0 
 
(结果个数 = 2) 

---END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GBPDPRESTBL.md`

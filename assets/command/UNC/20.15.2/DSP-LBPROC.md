---
id: UNC@20.15.2@MMLCommand@DSP LBPROC
type: MMLCommand
name: DSP LBPROC（查询CSLB进程）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LBPROC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 系统管理
- 进程状态
- 进程信息
status: active
---

# DSP LBPROC（查询CSLB进程）

## 功能

查询CSLB的进程信息。

## 注意事项

- 需要在CSLB RU拉起后才能使用这个命令。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：RU名称<br>默认值：无<br>取值范围：0 ~ 63个字符串 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>默认值：无<br>取值范围：<br>- “PROC_TYPE_MOMP(PROC_MOMP) ”<br>- “PROC_TYPE_MNCP(PROC_MNCP) ”<br>- “PROC_TYPE_MLBP(PROC_MLBP) ”<br>- “PROC_TYPE_MPEP(PROC_MPEP) ”<br>- “PROC_TYPE_MPCP(PROC_MPCP) ” |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LBPROC]] · CSLB进程（LBPROC）

## 使用实例

查询CSLB的进程信息

%%DSP LBPROC: PROCTYPE=PROC_TYPE_MOMP;%%

```
RETCODE = 0  操作成功

结果如下:

-------------------------
      RU名称  =  CSLB_OM_RU_0001
    进程类型  =  PROC_MOMP
      进程号  =  1
    进程角色  =  主
进程业务状态  =  正常
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LBPROC.md`

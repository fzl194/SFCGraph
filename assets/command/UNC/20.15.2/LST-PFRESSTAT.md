---
id: UNC@20.15.2@MMLCommand@LST PFRESSTAT
type: MMLCommand
name: LST PFRESSTAT（查询资源状态表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PFRESSTAT
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- 资源状态管理
status: active
---

# LST PFRESSTAT（查询资源状态表）

## 功能

**适用网元：SGSN、MME**

该命令用于查询资源状态表，这些资源包括PDP数状态、QoS带宽状态、静态带宽状态、动态带宽状态。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>**DSP RU**<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| PN | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPP进程的序号。<br>取值范围：0~20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PFRESSTAT]] · 资源状态表（PFRESSTAT）

## 使用实例

查询资源单元为USN_SP_RU_0064上0号UPP进程的资源状态：

LST PFRESSTAT: RUNAME="USN_SP_RU_0064", PN=0;

```
%%LST PFRESSTAT: RUNAME="USN_SP_RU_0064", PN=0;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                 RU名称  =  USN_SP_RU_0064
                 进程号  =  0
        转发面PDP数状态  =  正常
  CONV(QoS)带宽使用状态  =  正常
STREAM(QoS)带宽使用状态  =  正常
INTACT(QoS)带宽使用状态  =  正常
    BG(QoS)带宽使用状态  =  正常
           动态带宽状态  =  正常
           静态带宽状态  =  正常
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询资源状态表(LST-PFRESSTAT)_72225533.md`

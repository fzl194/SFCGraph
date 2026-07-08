---
id: UNC@20.15.2@MMLCommand@DSP GTPUPATHNUM
type: MMLCommand
name: DSP GTPUPATHNUM（显示GTP-U路径个数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPUPATHNUM
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- GTP-U
- GTP-U路径管理
status: active
---

# DSP GTPUPATHNUM（显示GTP-U路径个数）

## 功能

**适用网元：SGSN**

该参数用于查询系统内的GTP-U路径数目。

## 注意事项

该命令只用于查询SPU节点上的UPP进程。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>**DSP RU**<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PROCTP | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>取值范围：<br>- “UPP”<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的序号。<br>取值范围：0~20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPUPATHNUM]] · GTP-U路径个数（GTPUPATHNUM）

## 使用实例

1. 查询资源单元为USN_SP_RU_0064上的GTP-U路径数：
  DSP GTPUPATHNUM: RUNAME="USN_SP_RU_0064";
  ```
  %%DSP GTPUPATHNUM: RUNAME="USN_SP_RU_0064";%%
  RETCODE = 0  操作成功。

  输出结果如下
  -------------------------
      RU名称 = USN_SP_RU_0064
    进程类型 = UPP
      进程号 = 0
  GTPU路径数 = 6
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GTPUPATHNUM.md`

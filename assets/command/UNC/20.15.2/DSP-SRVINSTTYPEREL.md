---
id: UNC@20.15.2@MMLCommand@DSP SRVINSTTYPEREL
type: MMLCommand
name: DSP SRVINSTTYPEREL（查询服务实例与业务类型关系）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SRVINSTTYPEREL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务实例管理
- 服务实例与业务类型关系
status: active
---

# DSP SRVINSTTYPEREL（查询服务实例与业务类型关系）

## 功能

用于查询业务VNFC的业务类型对应的服务实例ID。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVVNFCID | 业务VNFCID | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在窗口下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_59103764.md)**<br>获得，所得NODE ID即为服务VNFC ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| SRVTYPE | 业务类型 | 可选必选说明：可选参数<br>参数含义：服务实例的业务类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVINSTTYPEREL]] · 服务实例与业务类型关系（SRVINSTTYPEREL）

## 使用实例

- 查询指定业务VNFC的所有业务类型对应的服务实例ID。
  DSP SRVINSTTYPEREL: SRVVNFCID=4;

  ```
  %%DSP SRVINSTTYPEREL: SRVVNFCID=4;%%
  RETCODE = 0  操作成功。

  操作结果如下：
  -------------------------
  业务VNFCID    服务实例ID    业务类型
  4             0              0
  4             1              1
  (结果个数 = 2)
  --- END
  ```
- 查询指定业务VNFC的指定业务类型对应的服务实例ID。
  DSP SRVINSTTYPEREL: SRVVNFCID=4, SRVTYPE=1;

  ```
  %%DSP SRVINSTTYPEREL: SRVVNFCID=4, SRVTYPE=1;%%
  RETCODE = 0  操作成功。

  操作结果如下：
  -------------------------
  业务VNFCID = 4
  服务实例ID = 1
  业务类型 = 1
  (结果个数 = 1)
  --- END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SRVINSTTYPEREL.md`

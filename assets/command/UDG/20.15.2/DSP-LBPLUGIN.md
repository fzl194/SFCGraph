---
id: UDG@20.15.2@MMLCommand@DSP LBPLUGIN
type: MMLCommand
name: DSP LBPLUGIN（查询CSLB的插件信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LBPLUGIN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 系统管理
- 插件管理
- 插件状态信息
status: active
---

# DSP LBPLUGIN（查询CSLB的插件信息）

## 功能

查询业务VNFC注册CSLB插件的信息。CSLB插件信息包括注册CSLB的业务VNFCID、插件ID、RU信息以及插件所在的进程

## 注意事项

- 该命令仅限于开发和测试使用。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVVNFCID | 业务VNFCID | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在窗口下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODE ID（节点ID）即为业务VNFC ID<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295<br>默认值：无 |
| PLUGINID | 插件ID | 可选必选说明：可选参数<br>参数含义：业务VNFC注册CSLB插件的ID号<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LBPLUGIN]] · CSLB的插件信息（LBPLUGIN）

## 使用实例

- 查询所有业务VNFC注册CSLB的插件信息
  DSP LBPLUGIN:;

  ```
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
  业务VNFCID    		RU名称           	 插件ID    			插件所在进程ID

  4                 GSC_OM_RU_0001     143392885     1007       
  4                 GSC_OM_RU_0002     143392879     1005       
  (结果个数 = 2)
  ---    END
  ```
- 查询指定业务VNFC注册CSLB的插件信息
  DSP LBPLUGIN: SRVVNFCID=4, PLUGINID=143392885;

  ```
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
      业务VNFCID  =  4
          RU名称  =  GSC_OM_RU_0001
          插件ID  =  143392885
  插件所在进程ID  =  1007
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CSLB的插件信息（DSP-LBPLUGIN）_29627105.md`

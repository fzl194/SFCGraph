---
id: UNC@20.15.2@MMLCommand@DSP RUGROUP
type: MMLCommand
name: DSP RUGROUP（显示资源单元组成员信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RUGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 倒换主备资源单元
status: active
---

# DSP RUGROUP（显示资源单元组成员信息）

## 功能

该命令用于显示资源单元组的信息，包括资源单元组名称、资源单元组RU名称及该RU的HA角色。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | RU组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RUGROUP]] · 资源单元组成员信息（RUGROUP）

## 使用实例

- 显示所有资源单元组的成员信息：
  ```
  DSP RUGROUP:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -----------------------------------
  RU组名称        RU名称                        HA角色
  MMB-BG1         VNODE_VNRS_VNFC_OMU_0001      主
  MMB-BG1         VNODE_VNRS_VNFC_OMU_0002      备
  BG_IPCTRL       VNODE_VNRS_VNFC_IPCTR_0071    主
  BG_IPCTRL       VNODE_VNRS_VNFC_IPCTR_0072    备
  BG_IPCTRL       VNODE_VNRS_VNFC_IPCTR_0073    冷备
  BG_IPCTRL       VNODE_VNRS_VNFC_IPCTR_0074    无效角色
  (结果个数 = 6)
  ---    END
  ```
- 显示指定资源单元组的成员信息，资源单元组的名称为MMB-BG1：
  ```
  DSP RUGROUP:GROUPNAME="MMB-BG1"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -----------------------------------
  RU组名称        RU名称                        HA角色
  MMB-BG1         VNODE_VNRS_VNFC_OMU_0001      主
  MMB-BG1         VNODE_VNRS_VNFC_OMU_0002      备
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RUGROUP.md`

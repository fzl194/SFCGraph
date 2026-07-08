---
id: UNC@20.15.2@MMLCommand@DSP RUGROUPSWP
type: MMLCommand
name: DSP RUGROUPSWP（显示资源单元组主备倒换状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RUGROUPSWP
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

# DSP RUGROUPSWP（显示资源单元组主备倒换状态信息）

## 功能

该命令用于显示资源单元组的主备倒换状态信息，包括资源单元组的主用RU、备用RU及倒换状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | RU组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元组名称。可使用<br>[**DSP RUGROUP**](显示资源单元组成员信息（DSP RUGROUP）_59103970.md)<br>命令查询对应的资源单元组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RUGROUPSWP]] · 资源单元组主备倒换状态信息（RUGROUPSWP）

## 使用实例

- 显示所有资源单元组的主备倒换状态信息：
  ```
  DSP RUGROUPSWP:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -----------------------------------
  RU组名称        主用RU                       备用RU                       倒换状态
  MMB-BG1         VNODE_VNRS_VNFC_OMU_0001     VNODE_VNRS_VNFC_OMU_0002     就绪 
  BG_IPCTRL       VNODE_VNRS_VNFC_IPCTR_0071   VNODE_VNRS_VNFC_IPCTR_0072   未就绪         
  (结果个数 = 2)
  ---    END
  ```
- 显示指定资源单元组的主备倒换状态信息，资源单元组的名称为MMB-BG1：
  ```
  DSP RUGROUPSWP:GROUPNAME="MMB-BG1"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -----------------------------------
  资源单元组名称 = MMB-BG1
          主用RU = VNODE_VNRS_VNFC_OMU_0001
          备用RU = VNODE_VNRS_VNFC_OMU_0002
        倒换状态 = 批备中
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RUGROUPSWP.md`

# 显示资源单元组成员信息（DSP RUGROUP）

- [命令功能](#ZH-CN_CONCEPT_0259103970__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259103970__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259103970__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259103970__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259103970__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0259103970__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0259103970)

该命令用于显示资源单元组的信息，包括资源单元组名称、资源单元组RU名称及该RU的HA角色。

#### [注意事项](#ZH-CN_CONCEPT_0259103970)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0259103970)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259103970)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | RU组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0259103970)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0259103970)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RU组名称 | 用于表示资源单元组名称。 |
| RU名称 | 用于表示资源单元名称。 |
| HA角色 | 该参数表示HA角色。<br>- 主：资源单元HA角色为主；。<br>- 备：资源单元HA角色为备；。<br>- 冷备：资源单元HA角色为冷备；。<br>- 无效角色：资源单元无HA角色。 |

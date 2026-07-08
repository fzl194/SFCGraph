---
id: UNC@20.15.2@MMLCommand@DSP COMPONENT
type: MMLCommand
name: DSP COMPONENT（显示组件信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMPONENT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP COMPONENT（显示组件信息）

## 功能

该命令用于显示组件信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- QUERYBYPROCID：根据进程ID查询组件信息。<br>- QUERYBYCOMPCID：根据组件ID查询组件信息。<br>默认值：QUERYBYPROCID |
| PROCID | 进程ID | 可选必选说明：条件必选参数，该参数在<br>“QUERYTYPE”<br>配置为<br>“QUERYBYPROCID”<br>时为必选参数。<br>参数含义：该参数用于指定要查询组件所属进程的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| COMPNAME | 组件名 | 可选必选说明：条件可选参数，该参数在<br>“QUERYTYPE”<br>配置为<br>“QUERYBYPROCID”<br>时为可选参数。<br>参数含义：该参数用于指定要查询的组件名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无 |
| COMPSTATE | 状态 | 可选必选说明：条件可选参数，该参数在<br>“QUERYTYPE”<br>配置为<br>“QUERYBYPROCID”<br>时为可选参数。<br>参数含义：组件的主备状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PRIMARY：主用组件。<br>- BACKUP：备用组件。<br>- FAILURE：组件运行失败。<br>- NOTBACKUP：批备未完成状态。<br>- NULL：组件不存在。<br>- INVALID：角色未定。<br>- COLDBACKUP：冷备组件。<br>默认值：无 |
| COMPCID | 组件ID | 可选必选说明：条件必选参数，该参数在<br>“QUERYTYPE”<br>配置为<br>“QUERYBYCOMPCID”<br>时为必选参数。<br>参数含义：该参数用于指定要查询的组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMPONENT]] · 组件信息（COMPONENT）

## 使用实例

- 在VNFC侧查询进程1000的组件信息：
  ```
  DSP COMPONENT:QUERYTYPE=QUERYBYPROCID,PROCID=1000
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  组件名      组件ID        逻辑ID       RU名称                      进程ID    组件类型    版本号     状态    CPU使用率（%）    内存使用大小（KB）

  EXP_MML     0x84040018    0x4040012    VNODE_CSLB_VNFC_OMU_0001    1000      0x404       1.2.103    主      0                 4793              
  HTTPS       0x82D8001E    0x2D80018    VNODE_CSLB_VNFC_OMU_0001    1000      0x2D8       1.2.103    主      0                 6120              
  HTTPC       0x82D7001D    0x2D70017    VNODE_CSLB_VNFC_OMU_0001    1000      0x2D7       1.2.103    主      0                 6096              
  NPS_MML     0x82080019    0x2080013    VNODE_CSLB_VNFC_OMU_0001    1000      0x208       1.2.103    主      0                 4909              
  NETCONFC    0x8197001C    0x1970016    VNODE_CSLB_VNFC_OMU_0001    1000      0x197       1.2.103    主      0                 112               
  APPCFG      0x80CF0004    0xCF0002     VNODE_CSLB_VNFC_OMU_0001    1000      0xCF        1.2.103    主      0                 56                
  NETCONF     0x8097001A    0x970014     VNODE_CSLB_VNFC_OMU_0001    1000      0x97        1.2.103    主      0                 4997              
  SSHS        0x80930028    0x93001F     VNODE_CSLB_VNFC_OMU_0001    1000      0x93        1.2.103    主      0                 1428              
  SSHC        0x80920026    0x92001D     VNODE_CSLB_VNFC_OMU_0001    1000      0x92        1.2.103    主      0                 331               
  (结果个数 = 9)

  ---    END
  ```
- 在VNFC侧查询组件0x84040018的信息：
  ```
  DSP COMPONENT:QUERYTYPE=QUERYBYCOMPCID,COMPCID="0x84040018"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
              组件名  =  EXP_MML
              组件ID  =  0x84040018
              逻辑ID  =  0x4040012
              RU名称  =  VNODE_CSLB_VNFC_OMU_0001
              进程ID  =  1000
            组件类型  =  0x404
              版本号  =  1.2.103
                状态  =  主
      CPU使用率（%）  =  0
  内存使用大小（KB）  =  4793
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-COMPONENT.md`

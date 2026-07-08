---
id: UDG@20.15.2@MMLCommand@DSP PORT
type: MMLCommand
name: DSP PORT（显示端口信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PORT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- 端口管理
status: active
---

# DSP PORT（显示端口信息）

## 功能

该命令用于显示VNFC上的端口信息，包括端口的配置，部署情况以及运行状态。

## 注意事项

该命令只能显示VNFC上的端口信息，不显示VNFC上的子端口信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PORTNAME | 端口名称 | 可选必选说明：可选参数<br>参数含义：该参数表示端口名称，例如Ethernet64/0/3，其中64代表资源单元编号，0为默认值，3代表端口编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](../RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PORT]] · 端口信息（PORT）

## 使用实例

- 显示VNFC上所有端口的信息：
  ```
  DSP PORT:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  端口名称         RU名称                     是否绑定PAE    是否对外端口    网络平面        带宽类型        MAC地址           运行状态    上次连接时间           上次断开时间    端口在位状态 

  Ethernet1/0/0    CSDB_OM_RU_0001            FALSE          FALSE           基础业务端口    吉比特以太网    00E0-FCXX-XXXX    运行        2015-12-24 11:28:12    NULL            在位         
  Ethernet1/0/1    CSDB_OM_RU_0001            FALSE          FALSE           外部管理端口    吉比特以太网    00E0-FCXX-XXXX    运行        2015-12-24 11:28:12    NULL            在位         
  Ethernet2/0/0    CSDB_OM_RU_0002            FALSE          FALSE           基础业务端口    吉比特以太网    00E0-FCXX-XXXX    运行        2015-12-24 11:28:13    NULL            在位       
  Ethernet2/0/1    CSDB_OM_RU_0002            FALSE          FALSE           外部管理端口    吉比特以太网    00E0-FCXX-XXXX    运行        2015-12-24 11:28:13    NULL            在位       
  (结果个数 = 4)
  ---    END
  ```
- 显示VNFC上指定资源块上所有端口的信息，输入参数RUNAME="CSDB_OM_RU_0001"：
  ```
  DSP PORT:RUNAME="CSDB_OM_RU_0001"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  端口名称         RU名称                     是否绑定PAE    是否对外端口    网络平面        带宽类型        MAC地址           运行状态    上次连接时间           上次断开时间    端口在位状态 

  Ethernet1/0/0    CSDB_OM_RU_0001            FALSE          FALSE           基础业务端口    吉比特以太网    00E0-FCXX-XXXX    运行        2015-12-24 11:28:12    NULL            在位         
  Ethernet1/0/1    CSDB_OM_RU_0001            FALSE          FALSE           外部管理端口    吉比特以太网    00E0-FCXX-XXXX    运行        2015-12-24 11:28:12    NULL            在位         
  (结果个数 = 2)
  ---    END
  ```
- 显示VNFC上指定端口的信息，输入参数PORTNAME="Ethernet1/0/0"：
  ```
  DSP PORT:PORTNAME="Ethernet1/0/0"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
      端口名称  =  Ethernet1/0/0
        RU名称  =  CSDB_OM_RU_0001
   是否绑定PAE  =  FALSE
  是否对外端口  =  FALSE
      网络平面  =  基础业务端口
      带宽类型  =  吉比特以太网
       MAC地址  =  00E0-FCXX-XXXX
      运行状态  =  运行
  上次连接时间  =  2015-12-24 11:28:12
  上次断开时间  =  NULL
  端口在位状态  =  在位
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PORT.md`

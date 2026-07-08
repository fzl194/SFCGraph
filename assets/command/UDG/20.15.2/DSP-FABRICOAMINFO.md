---
id: UDG@20.15.2@MMLCommand@DSP FABRICOAMINFO
type: MMLCommand
name: DSP FABRICOAMINFO（显示PAE OAM链路信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FABRICOAMINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- Fabric
status: active
---

# DSP FABRICOAMINFO（显示PAE OAM链路信息）

## 功能

该命令用于显示Fabric OAM链路状态信息。

## 注意事项

- 该命令执行后立即生效。
- 在sriov bonding模式下链路级探测不再可信，链路探测状态显示为init，此状态无效不代表探测结果。可执行MML命令**[DSP PAEPORTINFO](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)**查询绑定模式是否为是。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| REMOTERETB | 远端节点TB | 可选必选说明：可选参数<br>参数含义：该参数用于指定远端节点的资源ID。<br>数据来源：本端规划<br>取值范围：整数类型，0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FABRICOAMINFO]] · PAE OAM链路信息（FABRICOAMINFO）

## 使用实例

- 显示微服务类型“CCellCpcSrv”微服务类型实例 "2491301"到所有远端资源的Fabric OAM链路状态信息：
  ```
  DSP FABRICOAMINFO:CELLTYPE="CCellCpcSrv", CELLINSTANCE="2491301";
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
  微服务类型   微服务实例号   本端节点TB      远端节点TB  本端端口名称  远端端口名称   链路状态  链路所在平面ID  

  CCellCpcSrv  2491301        1035            1034        uio0          uio1           正常      0         
  CCellCpcSrv  2491301        1035            1034        uio6          uio7           正常      1    
  (结果个数 = 2)

  ---    END
  ```
- 查询微服务类型“CCellCpcSrv”微服务类型实例 "2491301"到远端资源“1034”的Fabric OAM链路状态信息：
  ```
  DSP FABRICOAMINFO:CELLTYPE="CCellCpcSrv", CELLINSTANCE="2491301", REMOTERETB=1034;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
  微服务类型   微服务实例号   本端节点TB      远端节点TB  本端端口名称  远端端口名称   链路状态  链路所在平面ID  

  CCellCpcSrv  2491301        1035            1034        uio0          uio1           正常      0         
  CCellCpcSrv  2491301        1035            1034        uio6          uio7           正常      1    
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PAE-OAM链路信息（DSP-FABRICOAMINFO）_92520043.md`

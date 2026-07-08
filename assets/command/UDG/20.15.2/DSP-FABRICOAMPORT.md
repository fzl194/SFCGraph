---
id: UDG@20.15.2@MMLCommand@DSP FABRICOAMPORT
type: MMLCommand
name: DSP FABRICOAMPORT（显示PAE各链路OAM报文统计结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FABRICOAMPORT
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

# DSP FABRICOAMPORT（显示PAE各链路OAM报文统计结果）

## 功能

该命令用于显示Fabric OAM报文统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| REMOTERETB | 远端节点TB | 可选必选说明：可选参数<br>参数含义：该参数用于指定远端节点的资源ID。<br>数据来源：本端规划<br>取值范围：整数类型，0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FABRICOAMPORT]] · PAE各链路OAM报文统计结果（FABRICOAMPORT）

## 使用实例

- 显示微服务类型为“CCellCpcSrv”微服务实例为“2491301”到所有远端资源Fabric OAM报文统计信息：
  ```
  DSP FABRICOAMPORT:CELLTYPE="CCellCpcSrv", CELLINSTANCE="2491301";
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
  微服务类型   微服务实例号   本端节点TB      远端节点TB      本端端口名称      远端端口名称      发送报文总数   发送报文错误数  接收报文总数    链路中断次数    首次链路中断时间  最近链路中断时间  最近链路中断持续时间  链路中断原因 

  CCellCpcSrv  2491301        1035            1034            uio0              uio1              14860           0               14857           0               NULL              NULL                  NULL               NULL         
  CCellCpcSrv  2491301        1035            1034            uio6              uio7              14860           0               14857           0               NULL              NULL                  NULL               NULL 
  (结果个数 = 2)
  ---    END
  ```
- 查询微服务类型为“CCellCpcSrv”微服务实例为“2491301”到远端资源“1034” 的Fabric OAM报文统计信息：
  ```
  DSP FABRICOAMPORT:CELLTYPE="CCellCpcSrv", CELLINSTANCE="2491301", REMOTERETB=1034;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
  微服务类型   微服务实例号   本端节点TB      远端节点TB      本端端口名称      远端端口名称      发送报文总数   发送报文错误数  接收报文总数    链路中断次数    首次链路中断时间  最近链路中断时间  最近链路中断持续时间  链路中断原因 

  CCellCpcSrv  2491301        1035            1034            uio0              uio1              14860           0               14857           0               NULL              NULL                  NULL               NULL         
  CCellCpcSrv  2491301        1035            1034            uio6              uio7              14860           0               14857           0               NULL              NULL                  NULL               NULL 
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PAE各链路OAM报文统计结果（DSP-FABRICOAMPORT）_92520009.md`

---
id: UDG@20.15.2@MMLCommand@LST FEILOGSWITCH
type: MMLCommand
name: LST FEILOGSWITCH（查询调测日志开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FEILOGSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 设置调测日志开关
status: active
---

# LST FEILOGSWITCH（查询调测日志开关）

## 功能

该命令用来查询调测日志开关配置。

## 注意事项

- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODULENAME | 模块名 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定模块名称。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- BFD：BFD。<br>- BFDEVENT：BFD-EVENT。<br>- CPUDEFEND：CPU-DEFEND。<br>- FEIIPSEC：FEI-IPSEC。<br>- FIM：FIM。<br>- FIMSTAT：FIM-STAT。<br>- FRAME：FRAME。<br>- FRAMEERROR：FRAME-ERROR。<br>- FRAMEMESSAGE：FRAME-MESSAGE。<br>- FRAMEPERFORMANCE：FRAME-PERFORMANCE。<br>- FWDSMOOTH：FWD-SMOOTH。<br>- GRE：GRE。<br>- IPTRACE：IP-TRACE。<br>- IPV4：IPV4。<br>- IPV4ARP：IPV4-ARP。<br>- IPV4NEXTHOP：IPV4-NEXTHOP。<br>- IPV6ND：IPV6-ND。<br>- IPV6NEXTHOP：IPV6-NEXTHOP。<br>- IPV6ROUTE：IPV6-ROUTE。<br>- MC：MC。<br>- MCBRIEF：MC-BRIEF。<br>- QOS：QOS。<br>- FFM：FFM。<br>- TBLMCST：TBLM-CST。<br>- TBLMFRM：TBLM-FRM。<br>- TBLMTPI：TBLM-TPI。<br>- PKT：PKT。<br>- TBLMAPI：TBLM-API。<br>- IPV4AT：IPV4-AT。<br>- IPV6NDH：IPV6-NDH。<br>- MPLS：MPLS。<br>- IPEOP：IPEOP。<br>- FEMP：FEMP。<br>- FEMPFABRIC：FEMP-FABRIC。<br>默认值：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FEILOGSWITCH]] · 调测日志开关（FEILOGSWITCH）

## 使用实例

- 查询调测日志开关配置：
  ```
  LST FEILOGSWITCH:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
  模块名  开关  

  BFD     ON       
  QOS     OFF   
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FEILOGSWITCH.md`

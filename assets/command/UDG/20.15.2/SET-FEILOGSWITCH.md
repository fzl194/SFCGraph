---
id: UDG@20.15.2@MMLCommand@SET FEILOGSWITCH
type: MMLCommand
name: SET FEILOGSWITCH（设置调测日志开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FEILOGSWITCH
command_category: 配置类
effect_mode: 立即生效
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

# SET FEILOGSWITCH（设置调测日志开关）

## 功能

该命令用来打开和关闭调测日志的功能。

调测日志开关默认是关闭的。

在需要定位转发异常时，打开该开关可以辅助定位，但打开开关后，对性能有一定的影响。

建议保持该开关为默认的关闭状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令不支持配置导出。
- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODULENAME | 模块名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定模块名称。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BFD：BFD。<br>- BFDEVENT：BFD-EVENT。<br>- CPUDEFEND：CPU-DEFEND。<br>- FEIIPSEC：FEI-IPSEC。<br>- FIM：FIM。<br>- FIMSTAT：FIM-STAT。<br>- FRAME：FRAME。<br>- FRAMEERROR：FRAME-ERROR。<br>- FRAMEMESSAGE：FRAME-MESSAGE。<br>- FRAMEPERFORMANCE：FRAME-PERFORMANCE。<br>- FWDSMOOTH：FWD-SMOOTH。<br>- GRE：GRE。<br>- IPTRACE：IP-TRACE。<br>- IPV4：IPV4。<br>- IPV4ARP：IPV4-ARP。<br>- IPV4NEXTHOP：IPV4-NEXTHOP。<br>- IPV6ND：IPV6-ND。<br>- IPV6NEXTHOP：IPV6-NEXTHOP。<br>- IPV6ROUTE：IPV6-ROUTE。<br>- MC：MC。<br>- MCBRIEF：MC-BRIEF。<br>- QOS：QOS。<br>- FFM：FFM。<br>- TBLMCST：TBLM-CST。<br>- TBLMFRM：TBLM-FRM。<br>- TBLMTPI：TBLM-TPI。<br>- PKT：PKT。<br>- TBLMAPI：TBLM-API。<br>- IPV4AT：IPV4-AT。<br>- IPV6NDH：IPV6-NDH。<br>- MPLS：MPLS。<br>- IPEOP：IPEOP。<br>- FEMP：FEMP。<br>- FEMPFABRIC：FEMP-FABRIC。<br>默认值：无 |
| SWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定使能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ON：使能。<br>- OFF：去使能。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEILOGSWITCH]] · 调测日志开关（FEILOGSWITCH）

## 使用实例

- 设置BFD模块的调测日志开关打开：
  ```
  SET FEILOGSWITCH: MODULENAME=BFD, SWITCH=ON;
  ```
- 设置TBLMTPI模块的调测日志开关关闭：
  ```
  SET FEILOGSWITCH: MODULENAME=TBLMTPI, SWITCH=OFF;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置调测日志开关（SET-FEILOGSWITCH）_44651703.md`

---
id: UNC@20.15.2@MMLCommand@MOD DMRTPRI
type: MMLCommand
name: MOD DMRTPRI（修改Diameter域路由优先级权重）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMRTPRI
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter路由优先级
status: active
---

# MOD DMRTPRI（修改Diameter域路由优先级权重）

## 功能

**适用网元：SGSN、MME**

该命令用于修改Diameter域路由优先级和权重，当Diameter域路由配置中 “选路模式” 是 “SELMODE_MASTER_SLAVE(主从)” 、 “SELMODE_PRIORITY_WEIGHT(优先级权重)” 或者 “SELMODE_IMSI_PRIORITY(IMSI指定优选)” 时，修改域路由中的对端优先级。当Diameter域路由配置中 “选路模式” 是 “SELMODE_PRIORITY_WEIGHT(优先级权重)” 时，修改域路由中的对端权重。

## 注意事项

- 该命令执行后立即生效。
- 修改的记录必须要在[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)中添加。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备修改的Diameter路由索引。<br>数据来源：本端规划<br>取值范围：0～2047<br>默认值：无<br>说明：可以通过<br>[**LST DMRT**](../Diameter路由/查询Diameter域路由配置(LST DMRT)_72225969.md)<br>命令查看已有配置，确认所要修改的Diameter路由的索引。 |
| PEERIDX | 对端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对等端索引，用于标识目的对等端。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMPE**](../Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)<br>设置此参数。<br>数据来源：本端规划<br>取值范围：0～639<br>默认值：无<br>说明：一个域路由下最多配置16个对端。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域中对端的优先级。<br>前提条件：该参数只在<br>[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)<br>命令中的<br>“选路模式”<br>设置为<br>“SELMODE_MASTER_SLAVE(主从)”<br>、<br>“SELMODE_PRIORITY_WEIGHT(优先级权重)”<br>或者<br>“SELMODE_IMSI_PRIORITY(IMSI指定优选)”<br>时有效。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>说明：- “SELMODE_MASTER_SLAVE(主从)”模式下，同一个域路由中不同对端的优先级不允许相同。<br>- 数值越小，优先级越高。 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域路由中对端的权重。<br>前提条件：该参数只在<br>[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)<br>命令中的<br>“选路模式”<br>设置为<br>“SELMODE_PRIORITY_WEIGHT(优先级权重)”<br>时有效。<br>数据来源：全网规划<br>取值范围：1~255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMRTPRI]] · Diameter域路由优先级权重（DMRTPRI）

## 使用实例

修改Diameter域路由配置中路由索引为“0”，对端实体索引为“1”的优先级为“255”：

MOD DMRTPRI: ROUTEIDX=0, PEERIDX=1, PRIORITY=255;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DMRTPRI.md`

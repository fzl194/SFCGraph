---
id: UNC@20.15.2@MMLCommand@ADD M3RT
type: MMLCommand
name: ADD M3RT（增加M3UA信令路由）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: M3RT
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
max_records: 1280
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA路由
status: active
---

# ADD M3RT（增加M3UA信令路由）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于增加M3UA信令路由。

## 注意事项

- 该命令执行后立即生效。
- 此命令的最大记录数为1280。
- 目的实体对应的本地实体和链路集对应的本地实体必须一致。
- 每个M3UA目的实体最多只能配置16条路由。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RTX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定唯一标识一个路由的索引。<br>数据来源：本端规划<br>取值范围：0~1279<br>默认值：无 |
| DEX | 目的实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该M3UA路由的目的实体。<br>数据来源：本端规划<br>取值范围：0~1279<br>默认值：无 |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定到达该的目的实体的M3UA链路集。<br>数据来源：本端规划<br>取值范围：0~1279<br>默认值：无 |
| PRI | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M3UA路由的选路优先级。<br>数据来源：整网规划<br>取值范围：0~254<br>默认值：0<br>说明：0是最高优先级，254是最低优先级 |
| RTN | 信令路由名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M3UA路由名称，标识M3UA路由。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3RT]] · M3UA信令路由（M3RT）

## 使用实例

增加路由索引为1，目的实体索引为1，链路集索引为1，优先级为0（默认值），路由名为“TEST”的M3UA路由：

ADD M3RT: RTX=1, DEX=1, LSX=1, RTN="TEST";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-M3RT.md`

---
id: UNC@20.15.2@MMLCommand@MOD M3RT
type: MMLCommand
name: MOD M3RT（修改M3UA信令路由）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: M3RT
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA路由
status: active
---

# MOD M3RT（修改M3UA信令路由）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用来修改M3UA信令路由配置数据。

## 注意事项

- 该命令执行后立即生效。
- 只能修改优先级和信令路由名。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RTX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示准备修改的路由的索引。<br>数据来源：本端规划<br>取值范围：0~1279<br>默认值：无 |
| PRI | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示M3UA路由的选路优先级。<br>数据来源：整网规划<br>取值范围：0~254<br>默认值：无 |
| RTN | 信令路由名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示M3UA路由名称，标识M3UA路由。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [M3UA信令路由（M3RT）](configobject/UNC/20.15.2/M3RT.md)

## 使用实例

将路由索引为1的M3UA路由的优先级改为1，路由名改为“R6_M3RT1”：

MOD M3RT: RTX=1, PRI=1, RTN="R6_M3RT1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改M3UA信令路由(MOD-M3RT)_72225995.md`

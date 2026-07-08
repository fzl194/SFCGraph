---
id: UDG@20.15.2@MMLCommand@RTR TETHERDETGLBPARA
type: MMLCommand
name: RTR TETHERDETGLBPARA（恢复Tethering用户终端数量检测全局配置）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: TETHERDETGLBPARA
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering用户终端数量检测全局配置
status: active
---

# RTR TETHERDETGLBPARA（恢复Tethering用户终端数量检测全局配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来恢复Tethering用户终端数量检测全局配置为初始值。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTYPE | 需要删除的Tethering用户终端数量检测全局配置参数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要删除的Tethering用户终端数量检测全局配置参数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AGE_TIME：恢复 AGE_TIME的初始值。<br>- HOTSPOT_AGE_TIME_PARA：恢复HOTSPOT_AGE_TIME_PARA的初始值。<br>- TTL_ANTI_FRAUD：恢复TTL_ANTI_FRAUD的初始值。<br>- PCC_MAX_NUM_CHOICE：恢复PCC_MAX_NUM_CHOICE的初始值。<br>- BWM_SUBSCRIBE_CONTROLLER：恢复BWM_SUBSCRIBE_CONTROLLER的初始值。<br>- STATISTIC_METHOD：恢复STATISTIC_METHOD的初始值。<br>- UDP_CONTROL_MODE：恢复UDP_CONTROL_MODE的初始值。<br>默认值：无<br>配置原则：如果未指定RMVTYPE，则恢复所有Tethering用户终端数量检测全局配置参数的初始值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TETHERDETGLBPARA]] · Tethering用户终端数量检测全局配置（TETHERDETGLBPARA）

## 使用实例

恢复Tethering用户终端数量检测全局配置，使用此命令：

```
RTR TETHERDETGLBPARA:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复Tethering用户终端数量检测全局配置（RTR-TETHERDETGLBPARA）_82837445.md`
